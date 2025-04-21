# Query running binary in k8s pod without an interactive shell
> #k8s #pod #kubectl #noshell

A lot of images in k8s don't actually contain shells, so you can't exec in with `bash` or `sh`.   

However, you can call the binary directly. The example below uses mongodb as reference. 

```shell
kubectl exec -it --namespace=tools mongo-pod -- /path/to/mongo --version
```
