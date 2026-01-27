from __future__ import annotations

from dataclasses import dataclass
from threading import RLock
from typing import Dict, Generic, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


@dataclass
class _Node(Generic[K, V]):
    key: Optional[K]
    value: Optional[V]
    prev: Optional["_Node[K, V]"] = None
    next: Optional["_Node[K, V]"] = None


class LRUCache(Generic[K, V]):
    """Simple LRU cache using a dict + doubly linked list with dummy ends.

    Thread safety: a single RLock guards all map/list mutations so that the
    LRU order remains consistent under concurrent access. An RLock is a
    re-entrant lock, meaning the same thread can acquire it multiple times
    without deadlocking, which helps when helper methods also use the lock.
    """

    def __init__(self, capacity: int) -> None:
        if capacity < 0:
            raise ValueError("capacity must be non-negative")
        self._capacity = capacity
        # Single global lock for correctness under concurrency.
        self._lock = RLock()
        # Dummy sentinels avoid edge cases when adding/removing nodes.
        self._head: _Node[K, V] = _Node(None, None)
        self._tail: _Node[K, V] = _Node(None, None)
        self._head.next = self._tail
        self._tail.prev = self._head
        # Map keys to nodes for O(1) lookup.
        self._map: Dict[K, _Node[K, V]] = {}

    def get(self, key: K) -> Optional[V]:
        # Capacity 0 cache is always empty.
        if self._capacity == 0:
            return None
        # Thread safety: hold the lock while reading/updating map and list.
        with self._lock:
            node = self._map.get(key)
            if node is None:
                return None
            # Move accessed node to the front (MRU position).
            self._remove(node)
            self._add_to_front(node)
            return node.value

    def put(self, key: K, value: V) -> None:
        if value is None:
            raise ValueError("None values are not supported")
        # Capacity 0 cache ignores inserts.
        if self._capacity == 0:
            return
        # Thread safety: hold the lock during all mutations.
        with self._lock:
            node = self._map.get(key)
            if node is not None:
                # Update existing node and promote to MRU.
                node.value = value
                self._remove(node)
                self._add_to_front(node)
            else:
                # Insert new node at MRU position.
                node = _Node(key, value)
                self._map[key] = node
                self._add_to_front(node)
                if len(self._map) > self._capacity:
                    # Evict LRU node when over capacity.
                    self._pop_lru()

    def _add_to_front(self, node: _Node[K, V]) -> None:
        # Insert right after head sentinel.
        first = self._head.next
        node.prev = self._head
        node.next = first
        self._head.next = node
        if first is not None:
            first.prev = node

    def _remove(self, node: _Node[K, V]) -> None:
        # Splice out node from the list.
        prev_node = node.prev
        next_node = node.next
        if prev_node is not None:
            prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node
        node.prev = None
        node.next = None

    def _pop_lru(self) -> None:
        # LRU is the node right before the tail sentinel.
        lru = self._tail.prev
        if lru is None or lru is self._head:
            return
        self._remove(lru)
        if lru.key is not None:
            self._map.pop(lru.key, None)

    def _check_invariants(self) -> bool:
        # Thread safety: lock while traversing internal structures.
        with self._lock:
            # Validate sentinel pointers.
            if self._head.prev is not None:
                raise AssertionError("head.prev must be None")
            if self._tail.next is not None:
                raise AssertionError("tail.next must be None")
            if self._head.next is None or self._tail.prev is None:
                raise AssertionError("head/tail must be connected")
            seen_keys = set()
            count = 0
            node = self._head
            while node is not None:
                next_node = node.next
                if next_node is not None and next_node.prev is not node:
                    raise AssertionError("broken prev/next linkage")
                if node is not self._head and node is not self._tail:
                    # Internal nodes must have real keys/values.
                    if node.key is None:
                        raise AssertionError("node.key must not be None")
                    if node.value is None:
                        raise AssertionError("node.value must not be None")
                    seen_keys.add(node.key)
                    count += 1
                if node is self._tail:
                    break
                node = next_node
            if count != len(self._map):
                raise AssertionError("map size mismatch")
            if seen_keys != set(self._map.keys()):
                raise AssertionError("map keys mismatch")
            if len(self._map) > self._capacity:
                raise AssertionError("capacity exceeded")
            return True
