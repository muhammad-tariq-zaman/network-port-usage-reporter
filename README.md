# network-port-usage-reporter

Turn raw netstat-style output into a clean listening-port summary: protocol, port and socket count, lowest port first.

## How to run

```sh
python3 main.py netstat.txt
```

## Example output

```
TCP 80: 2 socket(s)
TCP 443: 1 socket(s)
UDP 53: 1 socket(s)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
