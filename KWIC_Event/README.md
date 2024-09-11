# KWIC - Event

## Usage

```
$ python3 KWIC.py --input test_input.txt --output index.txt --stop_list stop_list.txt --context 2 --help
usage: Attempt the KWIC with event architecture (observer pattern) [-h] --input INPUT --output OUTPUT [--stop_list STOP_LIST] [--context CONTEXT]

options:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        input text file to build the index from
  --output OUTPUT, -o OUTPUT
                        output text file to write the index to
  --stop_list STOP_LIST, -s STOP_LIST
                        a stop list of words to ignore
  --context CONTEXT, -c CONTEXT
                        size of the context round the keyword
```

## Samples

**test_input.txt** - Based on (Wikipedia KWIC Entry)[https://en.wikipedia.org/wiki/Key_Word_in_Context]

**stop_list.txt** - Sample stop listed pulled from (sebleier's Github)[https://gist.github.com/sebleier/554280]
