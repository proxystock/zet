# Bash exec vs source

> 20250625

> #bash #exec #source #env #code

Examining the difference of `exec` vs `source` in bash scripting. 

Both of these will execute the script line by line as if commands were typed by hand. The primary difference is that sourcing a file can alter the current running environment and execute will not. 


## Exec

While exec and execute technically fall into the same category, it is worth noting a heavy difference in behavior. 

> [!NOTE] 
> Using `exec` will terminate the current shell and then execute the script in place of the terminated shell. Meaning that when `myscript` is done, there is no shell to return to. 

Syntax:
```bash
exec myscript
```

## Execute

When executing a script you are essentially opening a new shell, typing the commands into the new shell, copying the output back to your current shell, then closing the new shell. 

Any changes to environment will take effect only in the new shell and will be lost once the new shell is closed.

Syntax:
```bash
# Must be executable and valid shell script.
./path/to/myscript
```

Alt. syntax:
```bash
# Must be executable, valid shell script, and located somewhere in $PATH
myscript
```

## Source

When you `source` the script you are essentially typing the commands into your current shell. Any changes to the environment will take effect and stay in your current shell, which includes common tasks such as defining or altering variables.

Syntax:
```bash
# The file does not need to be executable, but it does need to be a valid shell script
source /path/to/myscript
```

Alt. syntax:
```bash
# Official POSIX usage. Bash defined "source" as an alias to the dot. 
. /path/to/myscript
```

## Related

- [https://superuser.com/questions/176783/what-is-the-difference-between-executing-a-bash-script-vs-sourcing-it#176788](https://superuser.com/questions/176783/what-is-the-difference-between-executing-a-bash-script-vs-sourcing-it#176788)
