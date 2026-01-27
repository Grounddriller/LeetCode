from lru_cache import LRUCache


def main() -> None:
    cache: LRUCache[int, str] = LRUCache(2)
    print("Capacity = 2\n")

    print("put(1, 'A') -> cache holds: {1:A}")
    cache.put(1, "A")
    print("put(2, 'B') -> cache holds: {1:A, 2:B}")
    cache.put(2, "B")

    print("\nget(1) -> returns 'A' and makes key=1 most-recently-used (MRU)")
    print("get(1):", cache.get(1))

    print("\nput(3, 'C') -> cache exceeds capacity, evict least-recently-used key=2")
    cache.put(3, "C")
    print("get(2) after eviction (should be None):", cache.get(2))

    print("\nput(4, 'D') -> cache exceeds capacity, evict least-recently-used key=1")
    cache.put(4, "D")
    print("get(1) after eviction (should be None):", cache.get(1))
    print("get(3) (should be 'C'):", cache.get(3))
    print("get(4) (should be 'D'):", cache.get(4))


if __name__ == "__main__":
    main()
