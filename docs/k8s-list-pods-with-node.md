# List pods with their assigned hostname
> #k8s #kubernetes #kubectl #pod #node


If you just want to show where pods in a specific namespace are running, you can adjust the output flag:

```console
$ k get pods -n $namespace -owide
NAME                        READY   STATUS    RESTARTS   AGE     IP             NODE           NOMINATED NODE   READINESS GATES
somepodname                 1/1     Running   0          5h43m   10.233.92.15   hpca14r00n01   <none>           <none>

```console
$ kubectl get pod -o=custom-columns=NODE:.spec.nodeName,NAME:.metadata.name -n elastic-agent |grep somehostname
somehostname   elastic-agent-standalone-6ztkv
```

A short executable
```bash
#!/bin/bash

# No args will show all namespaces
# Provide namespace to isolate query

if [[ $1 = "-h" ]] || [[ $1 = "?" ]]; then
	echo "Query specific namespace:"
	echo "$0 <namespace>"
	echo
	echo "Query all namespaces:"
	echo "$0"
	exit
fi

if [[ $# -ne 0 ]]; then
	kubectl get pod -o=custom-columns=NODE:.spec.nodeName,NAME:.metadata.name -n $1
	exit
fi

kubectl get pod -o=custom-columns=NODE:.spec.nodeName,NAME:.metadata.name --all-namespaces
```
