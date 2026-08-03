# Resolving detached head with changes

So, somehow you ended up in a detached state and appear pinned to a specific commit instead of a branch?

```
# Create a temporary branch, checkout the target branch and merge the two.
git branch tmp-branch
git checkout target-branch
git merge tmp-branch

# Now push your changes
```

Or maybe you just need to re-attach the origin/main because tracking is broken:

```bash
git fetch
git merge origin/main
```
