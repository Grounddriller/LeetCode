"""Thread-safe sliding window log rate limiter."""

from __future__ import annotations

from collections import deque
from threading import Lock
from typing import Deque, Dict


class RateLimiter:
    """Rate limiter using a sliding window log per user.

    Attributes:
        max_requests: Maximum number of requests allowed per window.
        window_ms: Window size in milliseconds.
    """

    def __init__(self, max_requests: int, window_ms: int) -> None:
        if max_requests <= 0:
            raise ValueError("max_requests must be positive")
        if window_ms <= 0:
            raise ValueError("window_ms must be positive")

        self.max_requests = max_requests
        self.window_ms = window_ms
        # Per-user data (timestamps + lock) stored in two dicts.
        self._timestamps: Dict[str, Deque[int]] = {}
        self._locks: Dict[str, Lock] = {}
        # Global lock only for safely creating per-user entries.
        self._init_lock = Lock()

    def allowRequest(self, userId: str, timestamp: int) -> bool:  # noqa: N802
        """Return True if a request for userId at timestamp is allowed."""
        # Thread-safe initialization of per-user structures.
        with self._init_lock:
            if userId not in self._timestamps:
                self._timestamps[userId] = deque()
                self._locks[userId] = Lock()

        # Per-user lock protects that user's deque from concurrent access.
        with self._locks[userId]:
            timestamps = self._timestamps[userId]
            cutoff = timestamp - self.window_ms
            # Evict requests outside the sliding window.
            while timestamps and timestamps[0] <= cutoff:
                timestamps.popleft()

            # Decide if we can accept this request.
            if len(timestamps) >= self.max_requests:
                decision = False
            else:
                timestamps.append(timestamp)
                decision = True

        # Print after releasing the per-user lock to avoid blocking other calls.
        status = "Approved" if decision else "Rejected"
        print(f"{userId}@{timestamp}ms -> {status}")
        return decision
