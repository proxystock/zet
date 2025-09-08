# Running commands as a user without shell access

Pertaining mainly to system users that are prohibited from opening a shell. 

Which (this should go without saying), if you are reading this as a new user - don't ever modify the users `passwd` file. As someone who has done this before in days starting out, it's worth mentioning, 

Example showing opening a temporary shell under the user to check the limits they inherit.

```console
root@server # su - icinga 
Last login: Mon Sep  8 14:28:40 EDT 2025 on pts/1
This account is currently not available.

root@server # sudo -u icinga -s

icinga@server:/root $ whoami
icinga
```

Alternatively, you can invoke the shell without `-s`. 

> [!NOTE]
> The `-s` (or `--shell`) flag does not accept positional parameters.  
> A common mistake is to invoke `-s /bin/bash`, which (while it does work) spawns two shells. 

```console
root@server:~ # sudo -u icinga bash

icinga@host:/root $ whoami
icinga

icinga@server:/root $ ulimit -a
core file size          (blocks, -c) unlimited
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 3092605
max locked memory       (kbytes, -l) unlimited
max memory size         (kbytes, -m) unlimited
open files                      (-n) 65535
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) unlimited
cpu time               (seconds, -t) unlimited
max user processes              (-u) 3092605
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```

## Ansible

> [!NOTE]
> This belongs in its own note object with a link to this one, but until I get my zets working, it will be here. 

If you are attempting to run a task in Ansible as a user with `/bin/nologin` defined (or a `false` shell), you can just use the `become_user` directive without any arguments. 

```ansible
- hosts: localhost
  tasks:
    - command: whoami
      become_user: mail
```

```console
ec2-user@pandora ansible $ grep mail /etc/passwd
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin

ec2-user@pandora ansible $ ansible-playbook ~/test.yml -v

PLAY [localhost] ***************************************************************

TASK [command] ***************************************************************

changed: [localhost] =>
    changed: true
    cmd:
    - whoami
    delta: '0:00:00.004282'
    end: '2023-12-07 11:57:37.151609'
    msg: ''
    rc: 0
    start: '2023-12-07 11:57:37.147327'
    stderr: ''
    stderr_lines: <omitted>
    stdout: mail
    stdout_lines: <omitted>
```

