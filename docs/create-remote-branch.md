# Create a remote git branch
> #git #remote #branch

```bash
# Create and switch to a new branch
git checkout -b <branch-name>

# Push the new branch upstream to remote
git push <remote-name> <branch-name>

# Side note: the long-form format is below. When one is ommitted, it will assume both branch names are the same.
#git push <remote-name> <local-branch-name>:<remote-branch-name>

# The new branch is not currently being tracked. To set tracking, you can configure the remote. 
# So that subsequent git pulls will know what to do, you can write the upstream into its local config with:
git push --set-upstream <remote-name> <local-branch-name>
```

Example
```
# Create the new branch
git checkout -b mybranch

# Add new or modified files to the new branch
git add file1 file2

# Commit
git commit -m "commit message"

# Push
git push origin mybranch

# Which I believe the long-form would be
git push origin mybranch:mybranch
```


Cheat sheet:
```txt
To delete a local branch, whether tracking or non-tracking, safely:
  git branch -d <branchname>

To delete a local branch, whether tracking or non-tracking, forcefully:
  git branch -D <branchname>

To delete a remote-tracking branch:
  git branch -rd <remote>/<branchname>

To create a new local non-tracking branch:
  git branch <branchname> [<start-point>]

To create a new local tracking branch: (Note that if <start-point> is specified and is a remote-tracking branch like origin/foobar, then the --track flag is automatically included)
  git branch --track <branchname> [<start-point]

  Example:
  git branch --track hello-kitty origin/hello-kitty

To delete a branch on a remote machine:
  git push --delete <remote> <branchname>

To delete all remote-tracking branches that are stale, that is, where the corresponding branches on the remote machine no longer exist:
  git remote prune <remote>
```

A good note to keep track of when to use `remote/branch` vs `remote branch` is that the former refers to a remote tracking branch on your local machine, whereas the latter refers to a remote-tracking branch across a network. 
