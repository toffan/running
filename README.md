# Running

A small script to automate the scheduling of a training plan on Garmin Connect.

## Usage

Update the code at the end of `garmin.py` to
1. Choose your training plan
2. Choose your starting date

Then connect legitimately on connect.garmin.com, inspect the requests and copy your Authorization and Cookies headers in two files `./token` and `./cookies`.

Finally run:
```console
$ poetry run python garmin.py -t ./token -c ./cookies
```

Eventually add the LOG_LEVEL=debug env var.

## Installation

Git clone the repository and run
```console
$ poetry install
```

