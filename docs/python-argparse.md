# Argparse pocket reference 
> #python #argparse #parser #code

There is nothing here yet, because Idk what I should put here. 

```python
>>> parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
>>> parser.add_argument('--foo', nargs='?', help='foo help')
>>> parser.add_argument('bar', nargs='+', help='bar help')
usage: PROG [options]

positional arguments:
 bar          bar help

options:
 -h, --help   show this help message and exit
 --foo [FOO]  foo help
```

- Using options vs positional arguments (shown in usage)
- Overriding the default usage output (line 1)
- Describeehavior of `parse_args()`, `parse_known_args()`, and `parse_intermixed_args()`. If any additional methods or functions exist. 

## Variable scope and functions

This applies to all global variables, but I'm highlighting them here.  

Python allows functions to read global variables without needing them passed in, but it's bad practice not to. 

- Hard to read: You don't know what process_globally() needs without reading its implementation.
- Hard to test: You can't easily call process_globally("some_file", True) from a test. You'd have to set my_script_global.args = Namespace(input_file="some_file", verbose=True) first.
- Less reusable: If your function is imported into another script, it won't work unless that script also defines a global args variable in the exact same way.
