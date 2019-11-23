# key-value_store_CLI_web-service

A CLI client which consumes the web service supporting following commands:
- get <key>: displays the value of an existing key over HTTP.
- put <key> <value>: sets the value of the given key.
- watch <key>: when executed this displays any new changes happening on the KV store in real time to the given key.

## Installation

This script supports both Python 2.x and Python 3.x

```bash
$ pip install pipenv --user
$ git clone git@gitlab.com:theSage21/deepak.git
$ cd deep
```
## Usage

This script supports both Python 2.x and Python 3.x

```bash
$ git_file_disclosure.py [-h] file
```

## Example
The input file should contain domains one per line. The script will output discovered domains.

```bash
$ python3 git_file_disclosure.py domain.txt 
www.connorrealestate.com is vulnerable
codemirror.net is vulnerable
```
