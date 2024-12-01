# Advent of Code 2024

My solutions to AoC 2024.

## Usage

Input files are automatically loaded. Save with same filename as the script, but change extension to `.input`. For example, `five.py` will load `five.input`.

And if you want to run the script using the much shorter test data provided in the problem description, save it to `five.test.input`, and pass the `--test` flag.

To enable debug logging output, use `-d` or `--debug` flag. Otherwise, log level is `logging.INFO`.

Run only one test by passing the `-p1`/`--part-1` or `-p2`/`--part-2` flags. 

Save log to a file with `-l` or `--log` e.g. `--log ten.log`

```
$ python3.11 ten.py --help
usage: ten.py [-h] [-d] [-t] [-p1] [-p2] [-l LOGFILE]

2023 Advent of Code, Day 10

options:
  -h, --help            show this help message and exit
  -d, --debug           Show debug output
  -t, --test            Use test input file
  -p1, --part-1         Only run part 1
  -p2, --part-2         Only run part 2, overrides -p1
  -l LOGFILE, --log LOGFILE
                        Filename for writing log file

https://adventofcode.com/2024
```

## Scores

```
      --------Part 1---------   --------Part 2---------
Day       Time    Rank  Score       Time    Rank  Score
  1   00:50:19    9562      0   01:00:33    9311      0
```

### Day 1
```
$ python3 one.py
2024-12-01 02:09:08,268 [INFO] [Part 1] Solution: XXXXXXX in 0.0005 seconds
2024-12-01 02:09:08,270 [INFO] [Part 2] Solution: XXXXXXXX in 0.0012 seconds
```

