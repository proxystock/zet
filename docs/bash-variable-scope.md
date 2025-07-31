# Bash variable scope

It's time to write a reminder on how bash variables are scoped. When variables are exported natively to sub-shells, when they are not. 

Starting with this [stackoverflow post](https://stackoverflow.com/questions/51903718/when-are-bash-variables-exported-to-subshells-and-or-accessible-by-scripts), hopefully my attempt to break the accepted answer down will help my brain retain the logic. 

---

## Subshell

`( )` runs the enclosed content in a subshell (otherwise separate environment). A subshell is a **child process** created by `fork()`ing the the old or existing shell, but **not calling any `execv`-family` function**. This means that the entire in-memory state of the parent is duplicated, which includes non-exported shell variables. 

Reference: See [grouping commands](https://www.gnu.org/software/bash/manual/bash.html#Command-Grouping).

While non-exported variables are copied into the subshell, any variables set within the subshell are not inherited by the parent environment. 

### Command substitution

`$()` is specifically used for [command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html), which also executes in a subshell environment. 

> [!NOTE] 
> It's documented that *"non-exported variables **are not** available in command substitution"*, but this seems to disagree.  
> ```console
> $ x=5
> $ y=$(echo $x)
> $ echo $y
> 5
> ```  
> 
> See the following example:  
>  
> ```console
> $ bash -c 'f() { echo "$a $b"; }; a=1; b=1; (b=2; f); f'
> 1 2
> 1 1
> ``` 

See the following...

- [3.7.3 Command Execution Environment](https://www.gnu.org/software/bash/manual/html_node/Command-Execution-Environment.html#Command-Execution-Environment)
- [3.2.2 Pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html#index-pipeline)

> When a simple command other than a builtin or shell function is to be executed, it is invoked in a separate execution environment that consists of the following.  
> * shell variables and functions marked for export, along with variables exported for the command, passed in the environment

## The execve boundary

The `execve` [function](https://www.man7.org/linux/man-pages/man2/execve.2.html) in Bash is used to execute a program, replacing the current process with a new one. It requires the program's pathname, an array of arguments, and an array of environment variables. 

Common scenarios that leverage `execve` are:

1. Replacing the Current Process, or Process Replacement
    - `execve` replaces the current process image with a new process image. This is useful when you want to run a new program without creating a new process.
2. Script Execution
    - When a script is executed, `execve` is often used to run the script's commands in the current shell environment. This allows the script to inherit the environment variables and settings of the calling process.
3. Command Execution in Shells
    - In interactive shells, `execve` is used to execute commands entered by the user. This allows for seamless command execution without spawning a new shell.
4. Handling File Descriptors
    - `execve` can be used to manipulate file descriptors, allowing for redirection of input and output streams when executing commands.
5. Running Background Processes
    - When running processes in the background, `execve` can be used to execute commands without blocking the terminal, allowing users to continue using the shell.


## Knowing when variables need to be exported

1. During `$()` *command substitution* if you are not running a builtin or a shell function.
2. When executing a secondary script using `exec`, `source`, or `.`
3. Terminal multiplexers
4. Exporting functions into bash environment allows them to be accessible across scripts.
    - `export -f function_name`
5. Build environments
