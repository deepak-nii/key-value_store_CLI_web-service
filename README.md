# key-value_store_CLI_web-service

A CLI client which consumes the web service supporting following commands:
- get <key>: displays the value of an existing key over HTTP.
- set <key> <value>: sets the value of the given key.
- watch <key>: when executed this displays any new changes happening on the KV store in real time to the given key.

## Installation

This script supports only Python 3.x

```bash
$ git clone https://github.com/deepak-nii/key-value_store_CLI_web-service.git
$ cd key-value_store_CLI_web-service
$ pip install -r requirements.txt
```
## Usage

For Client

```bash
$ client.py key [-h] [--set SET] [--watch] [--root http://localhost:8080/]
```
For Server

```bash
$ server.py
```

## Example
For server

```bash
$ server.py
======== Running on http://0.0.0.0:8080 ========
(Press CTRL+C to quit)
```
<key> watch: When executed this displays any new changes happening on the KV store in real time to the given key.

```bash
$ client.py random-key --watch
{"random-key": "12345"}
```
<key> set: Sets the value of the given key.

```bash
$ client.py random-key --set 12345
```
<key> root (i.e. get) : Displays the value of an existing key over HTTP.

```bash
$ client.py random-key --root http://0.0.0.0:8080
{'random-key': '12345'}
```
