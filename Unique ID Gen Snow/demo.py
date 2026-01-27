"""demo.py
Runnable demo for the SnowflakeLite generator.
"""
from snowflake_lite import SnowflakeLite, decode, format_timestamp


def main() -> None:
    gen = SnowflakeLite()

    ids = [gen.next_id() for _ in range(10_000)]

    is_unique = len(set(ids)) == 10_000
    is_non_decreasing = all(ids[i] <= ids[i + 1] for i in range(len(ids) - 1))

    print("Generated: 10000")
    print(f"Unique: {is_unique}")
    print(f"Non-decreasing order: {is_non_decreasing}")

    print("First 5 IDs:")
    for value in ids[:5]:
        ts_ms, seq = decode(value)
        ts_str = format_timestamp(ts_ms)
        print(f"  {value} -> {ts_str} (seq={seq})")

    last_value = ids[-1]
    last_ts_ms, last_seq = decode(last_value)
    last_ts_str = format_timestamp(last_ts_ms)
    print("Last ID:")
    print(f"  {last_value} -> {last_ts_str} (seq={last_seq})")


if __name__ == "__main__":
    main()
