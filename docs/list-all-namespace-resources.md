# Listing ALL resources in a namespace
> #k8s #namespace #resources #query #cluster #kubernetes #admin

Using `k get all -n <namespace>` does not actually show all of the resources for a namespace. 

## Using kubectl 

```bash
kubectl get all,cm,secret,ing -A
```

This may not get **all** resources, but it will query the following:
- pod
- service
- daemonset
- deployment
- replicaset
- statefulset
- job
- configmap
- secret
- ingress

## Iterating with xargs

The supported way to list **all resources** would be to iterate through all of the api versions listed in `kubectl api-resources`, as noted in [this stack post](https://stackoverflow.com/questions/47691479/listing-all-resources-in-a-namespace#53016918). 

A quick query against the existing K8s env shows approximately 140 different resource types for a K8s cluster. 

```bash
$ kubectl api-resources
NAME                               SHORTNAMES         APIVERSION                                NAMESPACED   KIND
bindings                                              v1                                        true         Binding
componentstatuses                  cs                 v1                                        false        ComponentStatus
configmaps                         cm                 v1                                        true         ConfigMap
endpoints                          ep                 v1                                        true         Endpoints
events                             ev                 v1                                        true         Event
limitranges                        limits             v1                                        true         LimitRange
namespaces                         ns                 v1                                        false        Namespace
nodes                              no                 v1                                        false        Node
persistentvolumeclaims             pvc                v1                                        true         PersistentVolumeClaim
persistentvolumes                  pv                 v1                                        false        PersistentVolume
pods                               po                 v1                                        true         Pod
podtemplates                                          v1                                        true         PodTemplate
replicationcontrollers             rc                 v1                                        true         ReplicationController
resourcequotas                     quota              v1                                        true         ResourceQuota
secrets                                               v1                                        true         Secret
serviceaccounts                    sa                 v1                                        true         ServiceAccount
services                           svc                v1                                        true         Service

[... continues...]
```

The following command chain is noted:

```bash
kubectl api-resources --verbs=list --namespaced -o name | xargs -n 1 kubectl get --show-kind --ignore-not-found -n <namespace>
```

Basically, it will first only pull the api-resources that are "namespaced", then proceed to pull any objects within that resource for the namespace you are attempting to query.

> [!NOTE]
> If you use `xargs -t -n ...`, it will show the command `xargs` is running (debug mode) which provides context on which resource name the results were rendered from.  
> Which is helpful when it's not obvious in the output.

### Example

This is an example executed against an existing environment for a namespace that shows no resources available using the standard `k get all` command. 

```console
$ kubectl api-resources --verbs=list --namespaced -o name | xargs -n 1 kubectl get --show-kind --ignore-not-found -n my-namespace
NAME                           DATA   AGE
configmap/istio-ca-root-cert   1      39d
configmap/kube-root-ca.crt     1      39d
NAME                     CREATED AT
limitrange/limit-range   2025-09-04T13:18:41Z
NAME                              AGE   REQUEST                                                                                                                          LIMIT
resourcequota/compute-resources   39d   requests.cpu: 0/8, requests.memory: 0/32Gi, requests.nvidia.com/gpu: 0/2, services.loadbalancers: 0/0, services.nodeports: 0/0   limits.cpu: 0/8, limits.memory: 0/32Gi, limits.nvidia.com/gpu: 0/2
NAME                     SECRETS   AGE
serviceaccount/default   0         39d
NAME                                                 ROLE                       AGE
rolebinding.rbac.authorization.k8s.io/generic-customer   ClusterRole/generic-customer   39d
```

### Integrations

Helpful functions for the bashrc, profile, or a bin command.

```
function kgetall {
	kubectl api-resources --verbs=list --namespaced -o name | xargs -n1 kubectl get --show-kind --ignore-not-found "$@" 
}

# Adding this will also grant kubectl tab completion
complete -F __start_kubectl kgetall
```

## Resources
- [Kubernetes-list-all-resources](https://www.baeldung.com/ops/kubernetes-list-all-resources)
