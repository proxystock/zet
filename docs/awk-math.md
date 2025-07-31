# Math in AWK 

> #awk #math #bash #shell

Just a quick example of implementing math in an `awk` statement.

```bash
# Using the memory usage, grab the 3rd and 2nd fields from the line that matches search. 
# Divide field 3 by field 2 and multiply by 100

free | awk '/Mem:/ {print $3/$2 * 100.0}'
```

```console
$ free
              total        used        free      shared  buff/cache   available
Mem:      527513292    39292300    71867972     4167772   416353020   479742788
Swap:       8388604     1107408     7281196

# ($total / $used) * 100

$ free | awk '/Mem:/ {print $3/$2 * 100.0}'
7.44918
```
