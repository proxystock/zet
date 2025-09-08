# Python Data Types Pocket Ref
> #python #code

## Data types and Collections

| Data type | Example | Mutable |
|-----------|---------|---------|
| integer | 10 | No |
| float | 3.14 | No |
| boolean | True/False | No |
| string | abcde | No |
| list | [1, 2, 3, 4 ] | Yes |
| tuple | (1, 2, 'a', 'b') | No |
| set | {'a', 'b', 'c'} | Yes |
| dictionary | {'a': 1, 'b': 2} | Yes |

## List Methods

```
# Append x to end of list
l.append(x) 

# Insert x at position y
l.insert(y, x)

# Remove first occurrence of x
l.remove(x)

# Reverse list in place
l.reverse()
```

## Dictionary Methods

```
# Return list of keys
d.keys()

# Return list of values
d.values()

# return list of (key, value)
d.items()

# Update dictionary, add new values or replace existing values if the key matches
d.update()


```

## String Methods

```
# Remove trailing whitespace
s.strip()

# Return list, delimiter x
s.split(x)

# Return string, delimiter s
s.join(listname)

# Return True of s starts with x
s.startswith(x)

# Return True if s ends with x
s.endswith(x)

# Return copy, upppercase only
s.upper()

# Return copy, lowercase only
s.lower()
```


