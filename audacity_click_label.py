#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
# ]
# ///
from typing import Iterator

DEFAULT_END = 0
DEFAULT_INTERVAL = 1
DEFAULT_START = 0


def acl(end: float = DEFAULT_END, interval: float = DEFAULT_INTERVAL, start: float = DEFAULT_START) -> Iterator[float]:
    if end < 0:
        raise ValueError(f"end ({end}) < 0")
    if interval < 0:
        raise ValueError(f"interval ({interval}) < 0")
    if start < 0:
        raise ValueError(f"start ({start}) < 0")
    while end == 0 or start <= end:
        yield start
        start += interval


if __name__ == '__main__':
    import sys
    from pathlib import Path as p

    def main():
        if len(sys.argv) in (2, 3, 4):
            acl1 = acl(*(float(x) for x in sys.argv[1:]))
        else:
            raise ValueError(f"""
            Usage: {p(__file__).name} [<end>={DEFAULT_END}] [<interval>={DEFAULT_INTERVAL}] [<start>={DEFAULT_START}]
            - end == 0 : infinity
            """)
        for x in acl1:
            print(x)


    main()
