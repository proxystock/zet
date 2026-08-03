# User Troubleshooting in Kubernetes
#k8s #troubleshooting #kubectl

Collection of troubleshooting tools for users in K8s.

## kubectl auth can-i

Check whether an action is allowed with `kubectl auth can-i` ([doc](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/)):

```bash
k auth can-i VERB [TYPE | TYPE/NAME | NONRESOURCEURL]
```

```console
# Checking for a specific user
k auth can-i create secret -n somenamespace --as userid --as-group userGroupName
yes
```
