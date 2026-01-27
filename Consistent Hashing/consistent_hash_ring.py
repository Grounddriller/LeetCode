"""Thread-safe consistent hash ring with virtual nodes."""

from __future__ import annotations

#fast lookup O(log N). Using bisectleft to find the insert position.
##We are looking for first position >= key hash.
import bisect 
import hashlib
import struct
import threading
from typing import Dict, List, Optional


class ConsistentHashRing:
    """Consistent hash ring with virtual nodes."""

    def __init__(self, replicas: int = 100) -> None:
        if not isinstance(replicas, int) or replicas <= 0:
            raise ValueError("replicas must be a positive integer")
        self._replicas = replicas
        # Sorted list of virtual node positions for O(log N) lookups.
        self._positions: List[int] = []
        # Maps virtual node position -> physical node id.
        self._position_to_node: Dict[int, str] = {}
        # Maps physical node id -> list of its virtual positions.
        self._node_to_positions: Dict[str, List[int]] = {}
        # Single lock protects all shared state for thread safety.
        self._lock = threading.Lock()

    @staticmethod
    def _hash(value: str) -> int:
        # Hash to a 32-bit position using MD5 and the first 4 bytes.
        digest = hashlib.md5(value.encode("utf-8")).digest()
        return struct.unpack(">I", digest[:4])[0]

    def addNode(self, nodeId: str) -> None:
        """Add a physical node with its virtual replicas to the ring."""
        if not isinstance(nodeId, str) or nodeId == "":
            raise ValueError("nodeId must be a non-empty string")
        # Thread safety: lock guards shared ring state during mutation.
        with self._lock:
            # Idempotent add: ignore if already present.
            if nodeId in self._node_to_positions:
                return
            positions: List[int] = []
            for replica_index in range(self._replicas):
                # Each replica uses a unique virtual id for hashing.
                virtual_node_id = f"{nodeId}#{replica_index}"
                position = self._hash(virtual_node_id)
                # Collision: skip if another replica already occupies this position.
                if position in self._position_to_node:
                    continue
                # Insert into sorted list to keep O(log N) lookup behavior.
                bisect.insort(self._positions, position)
                self._position_to_node[position] = nodeId
                positions.append(position)
            self._node_to_positions[nodeId] = positions

    def removeNode(self, nodeId: str) -> None:
        """Remove a physical node and all its virtual replicas from the ring."""
        if not isinstance(nodeId, str) or nodeId == "":
            raise ValueError("nodeId must be a non-empty string")
        # Thread safety: lock guards shared ring state during mutation.
        with self._lock:
            positions = self._node_to_positions.pop(nodeId, None)
            # Idempotent remove: nothing to do if missing.
            if not positions:
                return
            for position in positions:
                # Remove mappings and delete the position from the sorted list.
                self._position_to_node.pop(position, None)
                index = bisect.bisect_left(self._positions, position)
                if index < len(self._positions) and self._positions[index] == position:
                    self._positions.pop(index)

    def getNode(self, key: str) -> Optional[str]:
        """Get the node responsible for the given key."""
        if not isinstance(key, str) or key == "":
            raise ValueError("key must be a non-empty string")
        # Thread safety: lock guards shared ring state during lookup.
        with self._lock:
            if not self._positions:
                return None
            # Hash the key to a position on the ring.
            position = self._hash(key)
            # Find the first position >= key's position.
            index = bisect.bisect_left(self._positions, position)
            # Wrap around to the start if we run off the end.
            if index == len(self._positions):
                index = 0
            # Return the physical node at that virtual position.
            return self._position_to_node[self._positions[index]]
