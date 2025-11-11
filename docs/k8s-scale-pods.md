# Scaling pods in K8s
#hpcml #badnodes #k8sapp #zet #kubectl #scale 

## Reference

Declarative scaling 

```bash
# Scaling against the yaml
kubectl scale --replicas=1 -f nginx.yaml 
```

Imperative scaling

```bash
# Scaling against a live deployment
kubectl scale --replicas=2 deployment/nginx -n scaling-demo
```

Scaling pods based on condition

```bash
# This example sets the replica count of NGINX deployment to 2 ONLY if the current replica count is 1.
kubectl scale --current-replicas=1 --replicas=2 deployment/nginx -n scaling-demo
```

Scale multiple pods

```bash
kubectl scale --replicas=3 deployment/nginx deployment/redis -n scaling-demo
```

Scale all pods

```bash
kubectl scale --replicas=1 --all deployment -n scaling-demo
```

