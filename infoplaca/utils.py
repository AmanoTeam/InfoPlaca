import re

import httpx

hc = httpx.AsyncClient()

PLATE_REGEX = re.compile(
    r"(?:^| |\n)(([a-z]{3})-?([0-9][a-z0-9][0-9]{2}))(?: |\n|$)", re.IGNORECASE
)


def format_plate(plate: str) -> str:
    groups = re.search(PLATE_REGEX, plate).groups()
    if groups[2].isnumeric():
        return f"{groups[1]}-{groups[2]}"
    return f"{groups[1]}{groups[2]}"
