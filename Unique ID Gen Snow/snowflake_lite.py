"""Minimal Snowflake-style ID generator (single machine, no worker bits)."""
from datetime import datetime, timezone
import time

EPOCH_MS = 1704067200000  # Jan 1, 2024 UTC
SEQUENCE_MASK = 0xFFF  # 12 bits (0-4095)


class SnowflakeLite:

    def __init__(self) -> None:
        # last millisecond timestamp we used
        self.last_ts = -1
        # per-millisecond sequence counter
        self.seq = 0

    def _wait_until_next_ms(self, last_ts: int) -> int:
        # busy-wait until the clock moves forward
        now_ms = int(time.time() * 1000)
        while now_ms <= last_ts:
            now_ms = int(time.time() * 1000)
        return now_ms

    def next_id(self) -> int:
        # current time in milliseconds
        now_ms = int(time.time() * 1000)

        # if clock moved backwards, wait until it catches up
        if now_ms < self.last_ts:
            now_ms = self._wait_until_next_ms(self.last_ts)

        if now_ms == self.last_ts:
            # same millisecond: increment sequence
            self.seq = (self.seq + 1) & SEQUENCE_MASK
            if self.seq == 0:
                # overflowed 4095 -> wait for next millisecond
                now_ms = self._wait_until_next_ms(self.last_ts)
        else:
            # new millisecond: reset sequence
            self.seq = 0

        # update state and pack timestamp + sequence
        self.last_ts = now_ms
        return ((now_ms - EPOCH_MS) << 12) | self.seq


def decode(id_value: int) -> tuple[int, int]:
    """Decode an ID into (timestamp_ms_utc, sequence)."""
    # high bits are timestamp offset from EPOCH_MS
    timestamp_ms = (id_value >> 12) + EPOCH_MS
    # low 12 bits are the sequence
    sequence = id_value & SEQUENCE_MASK
    return timestamp_ms, sequence


def format_timestamp(timestamp_ms: int) -> str:
    """Format a millisecond UTC timestamp for display."""
    dt = datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc)
    return dt.isoformat()
