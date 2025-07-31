# Using a variable in awk search

> #awk #search #variable #bash #shell

Use double quotes and escape awks positional parameter:

```console
$ pattern='abc'

$ awk "/$pattern/ {print \$1}"
abc1
abc2
abc3
abc4
abc5
```
