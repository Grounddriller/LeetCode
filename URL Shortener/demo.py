import random

from url_shortener import UrlShortener


def main() -> None:
    rng = random.Random(42)
    shortener = UrlShortener(rng=rng)
    long_urls = [
        "https://docs.python.org/3/library/random.html",
        "https://www.example.com/tutorials/url-shortener",
        "http://short.ly/learning/resources",
    ]

    print("Long URLs:")
    for url in long_urls:
        print(f"- {url}")

    print("\nShortened URLs:")
    short_urls = []
    for url in long_urls:
        short_url = shortener.shorten(url)
        short_urls.append(short_url)
        print(f"- {short_url}")

    print("\nStats:")
    print(shortener.stats())


if __name__ == "__main__":
    main()
