# Using a variable in awk search

Use double quotes and escape awks positional parameter:

```console
$ fqmgr -S hpcq2adas -a all | awk "/$pattern/ {print \$1}"
pattern1
pattern2
pattern3
pattern4
pattern5
```
