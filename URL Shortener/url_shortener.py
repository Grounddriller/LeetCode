import random
import string
from typing import Optional


class UrlShortener:
    def __init__(
        self,
        base_url: str = "http://short.ly",
        code_length: int = 7,
        rng: Optional[random.Random] = None,
    ):
        # Public settings for the shortener.
        self.base_url = base_url
        self.code_length = code_length
        # Allow a seeded RNG for deterministic behavior in demo.
        self.rng = rng or random.Random()
        # Base62 alphabet: letters + digits.
        self._alphabet = string.ascii_letters + string.digits
        # In-memory mapping of short code -> original URL.
        self._code_to_url = {}

    def _validate_url(self, long_url: str) -> None:
        # Enforces a minimal URL format.
        if not isinstance(long_url, str) or not long_url:
            raise ValueError("URL must be a non-empty string")
        if not (long_url.startswith("http://") or long_url.startswith("https://")):
            raise ValueError("URL must start with http:// or https://")

    def _make_code(self) -> str:
        # Generate a unique random code of fixed length.
        while True:
            code = "".join(self.rng.choice(self._alphabet) for _ in range(self.code_length))
            if code not in self._code_to_url:
                return code

    def shorten(self, long_url: str) -> str:
        # Validate input, generate a code, store it, and return the full short URL.
        self._validate_url(long_url)
        code = self._make_code()
        self._code_to_url[code] = long_url
        return f"{self.base_url.rstrip('/')}/{code}"

    def stats(self) -> dict:
        # Return a simple count of stored links.
        return {"total_links": len(self._code_to_url)}