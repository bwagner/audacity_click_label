#!/usr/bin/env -S uv run --script
"""
Generate evenly spaced timestamps for Audacity label tracks.

By default, this script prints *regions* as 'start<TAB>end' pairs,
covering consecutive intervals over the given time range. With the
--instants option, it prints single time instants instead (one per line).
"""

# /// script
# dependencies = [
# ]
# ///
from typing import Iterator


DEFAULT_END = 0
DEFAULT_INTERVAL = 1
DEFAULT_START = 0


def acl(
    end: float = DEFAULT_END,
    interval: float = DEFAULT_INTERVAL,
    start: float = DEFAULT_START,
) -> Iterator[float]:
    """
    Yield an arithmetic sequence of timestamps.

    The sequence is:
        start, start + interval, start + 2 * interval, ...

    and continues while `start <= end`, unless `end == 0`, in which
    case the sequence is infinite.

    Parameters
    ----------
    end : float, default 0
        Upper bound for the sequence. If 0, the sequence is unbounded
        above (infinite).
    interval : float, default 1
        Step size between consecutive values. Must be non-negative.
        Note that `interval == 0` will result in an infinite loop if
        the while-condition is satisfied.
    start : float, default 0
        First value to yield. Must be non-negative.

    Yields
    ------
    float
        The next value in the arithmetic sequence.

    Raises
    ------
    ValueError
        If `end`, `interval`, or `start` is negative.
    """
    if end < 0:
        raise ValueError(f"end ({end}) < 0")
    if interval < 0:
        raise ValueError(f"interval ({interval}) < 0")
    if start < 0:
        raise ValueError(f"start ({start}) < 0")

    while end == 0 or start <= end:
        yield start
        start += interval


def _print_regions(times: Iterator[float]) -> None:
    """
    Print consecutive regions as 'start<TAB>end' from an iterator of times.

    Each line corresponds to a region spanning from one timestamp to the next.
    """
    iterator = iter(times)
    try:
        prev = next(iterator)
    except StopIteration:
        return  # No timestamps, nothing to print.

    for current in iterator:
        print(f"{prev}\t{current}")
        prev = current


def _print_instants(times: Iterator[float]) -> None:
    """
    Print each timestamp from an iterator on its own line.
    """
    for t in times:
        print(t)


if __name__ == "__main__":
    import sys
    from pathlib import Path as p

    def main() -> None:
        """
        Command-line interface.

        Usage
        -----
        {script_name} [--instants|-i] <end> [<interval>] [<start>]

        - By default, prints regions as 'start<TAB>end' lines suitable
          for Audacity label tracks.
        - With --instants / -i, prints single instants instead.

        Parameters
        ----------
        end : float
            Upper bound; use 0 for infinity.
        interval : float, optional
            Step size between timestamps (default: {default_interval}).
        start : float, optional
            Starting timestamp (default: {default_start}).
        """
        args = sys.argv[1:]
        instants = False

        # Allow either --instants or -i anywhere in the arguments.
        for flag in ("--instants", "-i"):
            if flag in args:
                instants = True
                args.remove(flag)
                break

        if len(args) not in (1, 2, 3):
            raise ValueError(
                f"""
Usage: {p(sys.argv[0]).name} [--instants|-i] <end> [<interval>={DEFAULT_INTERVAL}] [<start>={DEFAULT_START}]
- end == 0 : infinity
- default output: regions as 'start<TAB>end'
- with --instants / -i: single instants (one per line)
"""
            )

        # Parse positional arguments as floats: end [interval] [start]
        numeric_args = [float(x) for x in args]
        if len(numeric_args) == 1:
            end = numeric_args[0]
            interval = DEFAULT_INTERVAL
            start = DEFAULT_START
        elif len(numeric_args) == 2:
            end, interval = numeric_args
            start = DEFAULT_START
        else:
            end, interval, start = numeric_args

        times = acl(end=end, interval=interval, start=start)

        if instants:
            _print_instants(times)
        else:
            _print_regions(times)

    main()
