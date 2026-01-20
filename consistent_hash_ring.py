from __future__ import annotations

import bisect
import hashlib
from typing import Callable, Dict, List, Optional

HashFunction = Callable[[str], int]


class ConsistentHashRing:
    def __init__(self, replicas: int = 100, hash_fn: Optional[HashFunction] = None) -> None:
        if replicas <= 0:
            raise ValueError("replicas must be a positive integer")
        self._replicas = replicas
        self._hash_fn = hash_fn or self._default_hash
        self._ring: Dict[int, List[str]] = {}
        self._sorted_hashes: List[int] = []
        self._node_hashes: Dict[str, List[int]] = {}

    @property
    def replicas(self) -> int:
        return self._replicas

    def addNode(self, nodeId: str) -> None:
        if nodeId in self._node_hashes:
            return
        hashes: List[int] = []
        for replica in range(self._replicas):
            vnode_id = f"{nodeId}#{replica}"
            vnode_hash = self._hash_fn(vnode_id)
            hashes.append(vnode_hash)
            if vnode_hash in self._ring:
                self._ring[vnode_hash].append(nodeId)
                continue
            self._ring[vnode_hash] = [nodeId]
            bisect.insort(self._sorted_hashes, vnode_hash)
        self._node_hashes[nodeId] = hashes

    def removeNode(self, nodeId: str) -> None:
        hashes = self._node_hashes.pop(nodeId, None)
        if not hashes:
            return
        for vnode_hash in hashes:
            node_list = self._ring.get(vnode_hash)
            if not node_list:
                continue
            try:
                node_list.remove(nodeId)
            except ValueError:
                continue
            if node_list:
                continue
            del self._ring[vnode_hash]
            index = bisect.bisect_left(self._sorted_hashes, vnode_hash)
            if index < len(self._sorted_hashes) and self._sorted_hashes[index] == vnode_hash:
                self._sorted_hashes.pop(index)

    def getNode(self, key: str) -> Optional[str]:
        if not self._sorted_hashes:
            return None
        key_hash = self._hash_fn(key)
        index = bisect.bisect_right(self._sorted_hashes, key_hash)
        if index == len(self._sorted_hashes):
            index = 0
        vnode_hash = self._sorted_hashes[index]
        return self._ring[vnode_hash][0]

    @staticmethod
    def _default_hash(value: str) -> int:
        digest = hashlib.sha256(value.encode("utf-8")).digest()
        return int.from_bytes(digest[:4], byteorder="big", signed=False)


def _demo() -> None:
    ring = ConsistentHashRing(replicas=100)
    for node_id in ("A", "B", "C"):
        ring.addNode(node_id)

    keys = ("user123", "order456", "image789")

    print("Nodes added: A, B, C")
    for key in keys:
        print(f"getNode({key!r}) -> {ring.getNode(key)}")

    ring.removeNode("B")
    print("Removed node: B")
    for key in keys:
        print(f"getNode({key!r}) -> {ring.getNode(key)}")


if __name__ == "__main__":
    _demo()
