import random
import unittest

from url_shortener import UrlShortener


class UrlShortenerTests(unittest.TestCase):
    def setUp(self):
        self.rng = random.Random(0)
        self.shortener = UrlShortener(rng=self.rng)

    def test_shorten_creates_short_url(self):
        long_url = "https://example.com/learn"
        short_url = self.shortener.shorten(long_url)
        self.assertTrue(short_url.startswith("http://short.ly/"))
        self.assertEqual(len(short_url.rsplit("/", 1)[1]), 7)

    def test_shorten_records_link_count(self):
        self.shortener.shorten("http://example.com/abc")
        self.shortener.shorten("https://example.com/def")
        self.assertEqual(self.shortener.stats(), {"total_links": 2})

    def test_invalid_url_rejected(self):
        with self.assertRaises(ValueError):
            self.shortener.shorten("")
        with self.assertRaises(ValueError):
            self.shortener.shorten("example.com/no-scheme")

    def test_deterministic_code_generation(self):
        long_url = "https://example.com/deterministic"
        short_url = self.shortener.shorten(long_url)
        expected_rng = random.Random(0)
        expected_code = "".join(expected_rng.choice(self.shortener._alphabet) for _ in range(7))
        self.assertEqual(short_url, f"http://short.ly/{expected_code}")


if __name__ == "__main__":
    unittest.main()
