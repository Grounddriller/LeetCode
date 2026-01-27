import threading
import unittest

from rate_limiter import RateLimiter


class RateLimiterTests(unittest.TestCase):
    def test_single_user_basic(self) -> None:
        limiter = RateLimiter(3, 10_000)
        self.assertTrue(limiter.allowRequest("A", 0))
        self.assertTrue(limiter.allowRequest("A", 2000))
        self.assertTrue(limiter.allowRequest("A", 4000))
        self.assertFalse(limiter.allowRequest("A", 6000))
        self.assertTrue(limiter.allowRequest("A", 11000))

    def test_multiple_users_independent(self) -> None:
        limiter = RateLimiter(2, 5000)
        self.assertTrue(limiter.allowRequest("A", 0))
        self.assertTrue(limiter.allowRequest("B", 0))
        self.assertTrue(limiter.allowRequest("A", 1000))
        self.assertFalse(limiter.allowRequest("A", 2000))
        self.assertTrue(limiter.allowRequest("B", 2000))

    def test_concurrent_same_user(self) -> None:
        limiter = RateLimiter(5, 10_000)
        results = []
        results_lock = threading.Lock()

        def worker() -> None:
            allowed = limiter.allowRequest("A", 1000)
            with results_lock:
                results.append(allowed)

        threads = [threading.Thread(target=worker) for _ in range(10)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        self.assertEqual(results.count(True), 5)
        self.assertEqual(results.count(False), 5)

    def test_concurrent_multiple_users(self) -> None:
        limiter = RateLimiter(3, 10_000)
        results = []
        results_lock = threading.Lock()

        def worker(user_id: str) -> None:
            allowed = limiter.allowRequest(user_id, 1000)
            with results_lock:
                results.append(allowed)

        threads = [
            threading.Thread(target=worker, args=("A",)),
            threading.Thread(target=worker, args=("A",)),
            threading.Thread(target=worker, args=("A",)),
            threading.Thread(target=worker, args=("B",)),
            threading.Thread(target=worker, args=("B",)),
            threading.Thread(target=worker, args=("B",)),
            threading.Thread(target=worker, args=("C",)),
            threading.Thread(target=worker, args=("C",)),
            threading.Thread(target=worker, args=("C",)),
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        self.assertEqual(len(results), 9)
        self.assertTrue(all(results))


if __name__ == "__main__":
    unittest.main()
