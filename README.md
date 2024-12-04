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

2024 Advent of Code, Day 1

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
      --------Part 1---------   --------Part 2--------
Day       Time    Rank  Score       Time   Rank  Score
  4   00:53:18    9746      0   02:24:26  14821      0
  3   00:19:46    8082      0   00:39:04   7664      0
  2   20:23:22  110374      0          -      -      -
  1   00:50:19    9562      0   01:00:33   9311      0
```

### Day 1
```
$ python3 one.py
2024-12-01 02:09:08,268 [INFO] [Part 1] Solution: XXXXXXX in 0.0005 seconds
2024-12-01 02:09:08,270 [INFO] [Part 2] Solution: XXXXXXXX in 0.0012 seconds
```

### Day 2
```
2024-12-02 21:07:26,887 [INFO] [Part 1] Solution: XXX in 0.0047 seconds
```

### Day 3
```
$ python3.11 three.py
2024-12-03 00:39:35,661 [INFO] [Part 1] Solution: XXXXXXXXX in 0.0009 seconds
2024-12-03 00:39:35,664 [INFO] [Part 2] Solution: XXXXXXXXX in 0.0035 seconds
```

### Day 4
```
$ python3.11 four.py
2024-12-04 02:29:03,920 [INFO] [Part 1] Solution: XXXX in 0.2194 seconds
2024-12-04 02:29:04,079 [INFO] [Part 2] Solution: XXXX in 0.1588 seconds
```

## Problem Notes

### Day 2.2

I can't seem to get the correct answer here, although I'm very close, but I'm missing a way to narrow down the outputs to find a false negative.

After looking through the solutions on Reddit, I'm embarassed at how easily these guys are solving this problem.

Apparently `set()` is a great solution but I have no idea how to use it. Also a lot of folks are using a sliding window of 3, which I am not.

I think we're just going to admit defeat on this one and maybe come back to it another time.

### Day 4.2

This code is indecipherable. The code is as literal as possible, uses nothing but lists and crazy lookup tables. I'm sorry, it's just how my brain works.
