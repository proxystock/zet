# YQ Reference  
#zet #yq #yaml #kubernetes   
  
[A pretty dope write-up](https://thebottleneckdev.com/blog/processing-yaml-files).  
  
Basic structure

```bash
yq '.key' file.yaml
```
  
Update a value

```bash
yq -i '.key = "new value"' file.yaml
```
  
Convert yaml to json

```bash
yq -o=json '.' file.yaml

```
  
## Common Usage  
```bash
# Get a simple value
yq '.apiVersion' deployment.yaml

# Get a nested value
yq '.metadata.name' deployment.yaml

# Get an array element
yq '.spec.containers[0].image' deployment.yaml

# Get all matching values (extremely useful!)
yq '.spec.containers[].name' deployment.yaml
```
  
Working with multi-docs (K8s)  

```bash
# Process all documents (crucial for Kubernetes manifests)
yq 'all(.metadata.name)' multi-doc.yaml

# Update a field in all documents
yq -i 'all(.metadata.namespace = "production")' multi-doc.yaml
```
  
Output formatting - pretty print  

```bash
# Pretty-print YAML for better readability
yq -P '.' messy.yaml > pretty.yaml
```


```bash
# Pretty print with color
yq -C '.' file.yaml

# Output as single line
yq -j '.' file.yaml

# Control indentation
yq -P '.' file.yaml

# Preserve comments
yq --indent=2 '.' file.yaml
```
  
## Working with complex YAML structures  

Manipulating arrays  
```bash
# Add to an array
yq -i '.spec.containers += {"name":"sidecar", "image":"nginx"}' deployment.yaml

# Filter array elements
yq '.spec.containers[] | select(.name == "app")' deployment.yaml

# Map over array elements
yq '.items[] | .metadata.name' resources.yaml

# Sort an array
yq -i '.spec.containers |= sort_by(.name)' deployment.yaml

```
  
Multi-doc continued  

```bash
# Process all documents
yq 'all(.metadata.name)' multi-doc.yaml

# Process specific document
yq 'select(documentIndex == 0).metadata.name' multi-doc.yaml

# Update all documents
yq -i 'all(select(has("kind")) | .metadata.namespace = "production")' multi-doc.yaml

# Add a new document
yq -i '. as $item ireduce ([]; . + $item) | .[0].metadata.namespace = "new-value"' file.yaml
```
  
Controlling field order  

```bash
# Order specific fields first
yq -i '... | select(has("type")) |= with_entries(select(.key == "type") + select(.key == "id") + select(.key == "problemStatement") + select(.key == "correctAnswer") + select(.key == "answerPrompt") + select(.key == "solutionDetails"))' questions.yaml
```
  
## Common problems   
  
### Working with String Formats  

- Problem: YAML string formatting (quotes vs block style) doesn't match the current needs
- Solution: Use YQ's style modifiers  
	```bash
	# Convert multi-line strings to block literal format (|)
	yq -i '.. | select(has("solutionDetails")).solutionDetails style="literal"' questions.yaml

	# Convert to double-quoted style
	yq -i '.description style="double"' config.yaml
	```
  
### Modifying Nested Arrays  

- Problem: Updating specific elements in arrays can be tricky.  
- Solution: Combine select() with array indexing:  

	```bash
	# Update the container named "app" in a Kubernetes deployment
	yq -i '.spec.containers[] |= select(.name == "app").image = "new-image:v2"' deployment.yaml
	```
  
### Multiple Document Files  

- Problem: Processing files with multiple YAML documents (separated by `---`).  
- Solution: Use the `all` or `select` functions with document awareness:  

	```bash
	# Process only Deployment resources in a multi-document file
	yq -i 'select(.kind == "Deployment").spec.replicas = 3' k8s-manifests.yaml
	```
  
## Real-World Examples  
  
### Extract All Container Images from Kubernetes Manifests  

Finding all container images across multiple Kubernetes manifests is a common task:  

```bash
# List all container images across all deployments
yq '.spec.template.spec.containers[].image' */deployment.yaml

# With better formatting
yq '.spec.template.spec.containers[] | [.name, .image] | join(": ")' */deployment.yaml
```
  
