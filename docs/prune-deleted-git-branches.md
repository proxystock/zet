# Prune deleted branches
> #git

Is `git branch -a` showing deleted branches?


Prune all deleted branches from origin:

```shell
git remote prune origin
```

Prune just one deleted branch from origin

```shell
git branch -d -r origin/branch/name
```

> [!TIP]  
> Alternatively, docs also reference `git fetch -p` and/or `git pull -p` to prune.


To overcomplicate a simple solution, sometimes the following work-around may work in certain scenarios. 

- I'm only including this because it gives working examples of `git branch -vv` with `xargs`, and I haven't utilized `xargs` enough to know it well. 

    ```shell
    git branch -vv | grep 'gone]' | awk '{print $1}' | xargs git branch -D
    ```


Furthermore, `git branch -vv` provides context for each branch such as the last commit and commit message along with `origin/path` (which will note if the branch was deleted from orgin).

```console
$ git branch -vv 
  add-hostpath-k8s 05cc2616 [origin/add-hostpath-k8s] adding updated ldapsearch query for confirming record add
  main             cf12de95 [origin/main: behind 18] Updated and relocated appropriate documents with screenshots (#291)
  metrics          1b1746b1 [origin/metrics] Add batch links
* mon-triage-doc   f77eaba0 [origin/mon-triage-doc] Update oncall-triage.md
```
