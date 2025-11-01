# Create github patch file
> #git #patch

Patch files allow an upstream branch to be forked and maintained in a separate repository or location. 

The process is simply pull the upstream code-base and apply any patch files that represent any changes made to your fork. 

```bash
git format-patch
```

Example
```
git format-patch -N 1 HEAD
```
- For the last 1 commit, create a patch file. 

Patch files also allow you to see the changes between a patch and upstream. 
