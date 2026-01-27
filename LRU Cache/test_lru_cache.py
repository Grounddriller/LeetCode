import random
import threading
import time
import unittest

from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_example_flow_evictions(self) -> None:
        cache: LRUCache[int, str] = LRUCache(2)
        cache.put(1, "a")
        cache.put(2, "b")
        self.assertEqual(cache.get(1), "a")
        cache.put(3, "c")
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(3), "c")
        cache._check_invariants()

    def test_update_existing_key_makes_mru(self) -> None:
        cache: LRUCache[int, str] = LRUCache(2)
        cache.put(1, "a")
        cache.put(2, "b")
        cache.put(1, "a2")
        cache.put(3, "c")
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(1), "a2")
        cache._check_invariants()

    def test_capacity_zero_behavior(self) -> None:
        cache: LRUCache[int, str] = LRUCache(0)
        cache.put(1, "a")
        self.assertIsNone(cache.get(1))
        cache._check_invariants()

    def test_repeated_access_keeps_mru(self) -> None:
        cache: LRUCache[int, str] = LRUCache(2)
        cache.put(1, "a")
        cache.put(2, "b")
        self.assertEqual(cache.get(1), "a")
        self.assertEqual(cache.get(1), "a")
        cache.put(3, "c")
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(1), "a")
        self.assertEqual(cache.get(3), "c")
        cache._check_invariants()

    def test_none_value_disallowed(self) -> None:
        cache: LRUCache[int, str] = LRUCache(2)
        with self.assertRaises(ValueError):
            cache.put(1, None)

    def test_concurrency_stress(self) -> None:
        cache: LRUCache[int, int] = LRUCache(5)
        stop_event = threading.Event()
        errors = []

        def worker(seed: int) -> None:
            rng = random.Random(seed)
            try:
                while not stop_event.is_set():
                    key = rng.randint(0, 9)
                    if rng.random() < 0.6:
                        cache.put(key, rng.randint(1, 1000))
                    else:
                        cache.get(key)
                    if rng.random() < 0.05:
                        with cache._lock:
                            cache._check_invariants()
            except Exception as exc:  # pragma: no cover - for debugging
                errors.append(exc)
                stop_event.set()

        threads = [threading.Thread(target=worker, args=(i,)) for i in range(8)]
        for thread in threads:
            thread.start()
        time.sleep(0.5)
        stop_event.set()
        for thread in threads:
            thread.join()

        if errors:
            raise errors[0]
        cache._check_invariants()
        self.assertLessEqual(len(cache._map), 5)


if __name__ == "__main__":
    unittest.main()
