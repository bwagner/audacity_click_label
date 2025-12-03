# audacity_click_label – Audacity Click Labels

`audacity_click_label.py` generates evenly spaced timestamps for use with **Audacity** label tracks.

By default it prints **regions** (`start<TAB>end`), suitable for importing directly
as a label track. With an option it can also print **instants** (single timestamps)
instead.

The script is designed to be run via [`uv`](https://github.com/astral-sh/uv), but
it is just regular Python and can be run with any Python 3 interpreter.

```bash
./audacity_click_label.py ...
```

(or whatever filename you give it).

---

## Features

- Generate **regions** over a time range:
  - Each line: `start<TAB>end`
  - Perfect for Audacity label tracks as regions.
- Optionally generate **instants**:
  - Each line: a single timestamp.
- Configurable:
  - `end`: upper limit (or `0` for infinity)
  - `interval`: step between timestamps
  - `start`: starting timestamp

---

## Usage

Basic syntax:

```bash
./audacity_click_label.py [--instants|-i] <end> [<interval>] [<start>]
```

- `end` (required): upper bound in seconds; use `0` for infinity.
- `interval` (optional): step between timestamps (default: `1`).
- `start` (optional): starting time (default: `0`).
- `--instants` / `-i`: output instants instead of regions.

### Output format

By default, output is **regions**:

```text
start<TAB>end
start<TAB>end
...
```

With `--instants`, output is:

```text
time
time
...
```

---

## Examples

### 1. Regions every second from 0 to 10 seconds

```bash
./audacity_click_label.py 10 > regions.txt
```

Example output:

```text
0.0     1.0
1.0     2.0
2.0     3.0
...
9.0     10.0
```

Import `regions.txt` in Audacity:

- `File → Import → Labels…`

You now have regions `[0–1]`, `[1–2]`, …, `[9–10]` seconds.

---

### 2. Instants every 0.5 seconds, from 0 to 5 seconds

```bash
./audacity_click_label.py --instants 5 0.5 > instants.txt
```

Example output:

```text
0.0
0.5
1.0
1.5
...
5.0
```

You can post-process this further (e.g. with `awk`) to add label text.

---

### 3. Regions starting at 2 seconds, stepping by 0.25 seconds

```bash
./audacity_click_label.py 5 0.25 2 > regions_2_to_5.txt
```

This produces regions `[2.0–2.25]`, `[2.25–2.5]`, … up to `5.0`.

---

## Audacity Workflow

1. Generate a label file with `audacity_click_label.py`, e.g.:

   ```bash
   ./audacity_click_label.py 120 0.5 > beat_regions.txt
   ```

2. In Audacity, choose:

   - `File → Import → Labels…`
   - Select the generated file.

3. Audacity will create a new label track with your regions (or instants).

This is useful for:

- Regular cue points,
- Quick region slicing,
- Beat/bar markers,
- Segmenting long recordings.

---

## See Also

- [shift_labels](https://github.com/bwagner/shift_labels)
- [quantize_labels](https://github.com/bwagner/quantize_labels)
- [beats2bars](https://github.com/bwagner/beats2bars)
- [audacity_legatize](https://github.com/bwagner/audacity_legatize)
- [pyaudacity](https://github.com/bwagner/pyaudacity)
