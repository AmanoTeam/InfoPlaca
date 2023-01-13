import re

import httpx

hc = httpx.AsyncClient()

PLATE_REGEX = re.compile(
    r"(?:^| |\n)([a-z]{3}-?[0-9][a-z0-9][0-9]{2})(?: |\n|$)", re.IGNORECASE
)
