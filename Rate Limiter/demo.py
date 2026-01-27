from rate_limiter import RateLimiter


def main() -> None:
    limiter = RateLimiter(3, 10_000)
    calls = [
        ("A", 0),
        ("A", 2000),
        ("A", 4000),
        ("A", 6000),
        ("A", 11000),
        ("B", 1000),
        ("B", 2000),
        ("B", 7000),
    ]
    for user_id, timestamp in calls:
        limiter.allowRequest(user_id, timestamp)


if __name__ == "__main__":
    main()
