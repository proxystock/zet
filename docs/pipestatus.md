# PIPESTATUS

> 20250625

> #bash #builtin #variables #array #pipe #pipestatus

Per the Bash manual:

> PIPESTATUS is an array variable (see Arrays below) containing a list of exit status values from the processes in the most-recently-executed foreground pipeline (which may contain only a single command).

Working example:

```console
$ cat x| sed 's///'
cat: x: No such file or directory

$ echo $?
0

$ cat x| sed 's///'
cat: x: No such file or directory

$ echo ${PIPESTATUS[*]}
1 0

$ touch x

$ cat x| sed 's'
sed: 1: "s": substitute pattern can not be delimited by newline or backslash

$ echo ${PIPESTATUS[*]}
0 1
```


## Pipefail

Pipefail (ksh, zsh, bash) sets the exit status to the exit code of the last program to exit non-zero (or zero if all exited successfully).

```console
$ false | true; echo $?
0
$ set -o pipefail
$ false | true; echo $?
1
```
