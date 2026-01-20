from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Dict


@dataclass
class RateLimiter:
    max_requests: int
    window_ms: int
    _user_requests: Dict[str, Deque[int]] = field(default_factory=dict, init=False)

    def allowRequest(self, user_id: str, timestamp: int) -> bool:
        if user_id not in self._user_requests:
            self._user_requests[user_id] = deque()

        requests = self._user_requests[user_id]
        window_start = timestamp - self.window_ms

        while requests and requests[0] <= window_start:
            requests.popleft()

        if len(requests) >= self.max_requests:
            return False

        requests.append(timestamp)
        return True


def run_demo() -> None:
    limiter = RateLimiter(max_requests=3, window_ms=10_000)
    tests = [
        ("A", 0),
        ("A", 2000),
        ("A", 4000),
        ("A", 6000),
        ("A", 11_000),
    ]
    expected = [
        True,
        True,
        True,
        False,
        True,
    ]

    print("Rate limiter demo (3 requests per 10 seconds):")
    for (user_id, timestamp), should_allow in zip(tests, expected):
        allowed = limiter.allowRequest(user_id, timestamp)
        verdict = "ALLOWED" if allowed else "REJECTED"
        expected_verdict = "ALLOWED" if should_allow else "REJECTED"
        print(
            f"user={user_id} t={timestamp:>5} -> {verdict} "
            f"(expected {expected_verdict})"
        )


if __name__ == "__main__":
    run_demo()
