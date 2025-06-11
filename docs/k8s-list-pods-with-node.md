# List pods with their assigned hostname
> #k8s #kubernetes #kubectl #pod #node

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
