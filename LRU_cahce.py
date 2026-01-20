from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Generic, Optional, TypeVar


Key = TypeVar("Key")
Value = TypeVar("Value")


@dataclass
class _Node(Generic[Key, Value]):
    key: Key
    value: Value
    prev: Optional["_Node[Key, Value]"] = None
    next: Optional["_Node[Key, Value]"] = None


class LRUCache(Generic[Key, Value]):

    def __init__(self, capacity: int) -> None:
        if capacity < 0:
            raise ValueError("capacity must be non-negative")
        self._capacity = capacity
        self._nodes: Dict[Key, _Node[Key, Value]] = {}
        self._head: Optional[_Node[Key, Value]] = None
        self._tail: Optional[_Node[Key, Value]] = None

    def get(self, key: Key) -> Optional[Value]:
        node = self._nodes.get(key)
        if node is None:
            return None
        self._move_to_front(node)
        return node.value

    def put(self, key: Key, value: Value) -> None:
        if self._capacity == 0:
            return
        node = self._nodes.get(key)
        if node is not None:
            node.value = value
            self._move_to_front(node)
            return
        new_node = _Node(key=key, value=value)
        self._nodes[key] = new_node
        self._add_to_front(new_node)
        if len(self._nodes) > self._capacity:
            self._evict_lru()

    def _add_to_front(self, node: _Node[Key, Value]) -> None:
        node.prev = None
        node.next = self._head
        if self._head is not None:
            self._head.prev = node
        self._head = node
        if self._tail is None:
            self._tail = node

    def _move_to_front(self, node: _Node[Key, Value]) -> None:
        if node is self._head:
            return
        self._unlink(node)
        self._add_to_front(node)

    def _unlink(self, node: _Node[Key, Value]) -> None:
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node is self._head:
            self._head = node.next
        if node is self._tail:
            self._tail = node.prev
        node.prev = None
        node.next = None

    def _evict_lru(self) -> None:
        if self._tail is None:
            return
        lru = self._tail
        self._unlink(lru)
        self._nodes.pop(lru.key, None)


def _demo() -> None:
    cache = LRUCache[int, str](capacity=2)
    cache.put(1, "A")
    cache.put(2, "B")
    print(f"get(1) -> {cache.get(1)!r}")
    cache.put(3, "C")
    print(f"get(2) -> {cache.get(2)!r}")
    cache.put(4, "D")
    print(f"get(1) -> {cache.get(1)!r}")
    print(f"get(3) -> {cache.get(3)!r}")
    print(f"get(4) -> {cache.get(4)!r}")


if __name__ == "__main__":
    _demo()
