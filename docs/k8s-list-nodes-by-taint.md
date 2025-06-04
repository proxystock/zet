# List Kubernetes nodes by taint

The taints and labels added to nodes entirely depends on the environment, administration team, and applications/workloads that are hosted. Therefore, the examples below are simply just generic for reference.


```txt
# Find cpu-only nodes
k get nodes -l kubernetes.io/node-type=cpu

# Find gpu-only nodes, regardless of type (H100, A100, T4, etc)
k get nodes -l kubernetes.io/node-type=gpu
k get nodes -l kubernetes.io/node-type!=cpu

# Find H100 gpu nodes
k get nodes -l kubernetes.io/gpu-type=H100

# Multiple filters (repeat -l)
k get nodes -l kubernetes.io/gpu-type!=H100 -l hpc.ford.com/gpu-type!=A100
```
