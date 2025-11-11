# User Resource Usage on Memory and CPU
#ps #resource #cpu #top #memory #query #linix #system #troubleshooting #watch #top

Just some of the system queries I've collected over the years, because some of these I can't recall what the flags were. 

## Static

To list top 10 CPU usage processes with user
```bash
ps -e -o pcpu,pid,user,args|sort -k1 -nr|head -10
```

Find out top 10 CPU consuming process
```bash
ps -auxf|sort -nr -k3|head -10
```

To list top 10 Memory consuming processes with user
```bash
ps -e -o pmem,pid,user,args|sort -k1 -nr|head -10
```

Find out the top 10 memory consuming process
```bash
ps -auxf|sort -nr -k4|head -10
```

Find out every process running under a user
```bash
ps -U user-name -u user-name u

# or
ps -e -o pid,user,args|grep $username
```
## Dynamic

To show the process usage of a user with ‘top’
```bash
top -u $username
```

To list top 10 CPU usage processes with user
```bash
watch "ps -e -o pcpu,pid,user,args|sort -k1 -nr|head -10"
```

To list top 10 Memory consuming processes with user
```bash
watch "ps -e -o pmem,pid,user,args|sort -k1 -nr|head -10"
```

