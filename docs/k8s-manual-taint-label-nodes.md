# Manually label and taint nodes in Kubernetes

In this example, we are labeling H100 GPU nodes in a production cluster. The taints and labels referenced **are not** universal to all K8s clusters, and are only being used as reference info for a generalized Kubernetes knowledge base.

> [!NOTE]
> Using `somedomain.com` as a generic domain. In a running environment, this domain can reflect anything. 

1. Identify the nodes you need to update

    ```bash
    k get nodes -l somedomain.com/gpu-type=H100
    ```

2. Confirm that any existing workloads on the nodes already have the correct tolerations. If they do not match, the workloads will be removed from the nodes and unable to reschedule. 
 
    ```bash
    # The general process here is to identify any pods on the target nodes, and check that they have the matching tolerations to the labels or taints you are adding
    k get pods -A -oyaml
    ```

    ```bash
    # An example that uses two custom programs: k-multidoc, and yamlgrep 
    $ k get po -A -oyaml | k multidoc | yamlgrep H100 | yq '"\(.metadata.namespace) \(.metadata.name) \(.spec.tolerations[].key)"' | column -t
    ```

3. Add the new node **label**.

    ```bash
    k label node $x somedomain.com/prod-gpu=true
    ```

4. Add the new node **taint**.

    ```bash
    k taint node $x node.kubernetes.io/prod-gpu:NoSchedule
    ```

5. Confirm that the pre-existing workloads are still running. 

