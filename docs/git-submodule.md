# Nested git repos

TODO: Provide an explanation how sub-modules work in git, how they are configured. 

The quick overview is that these allow you to clone a secondary repository in your current one. The submodules need to be pulled and updated separately, they do not automatically pull in when you perform actions just in case your repository is dependent on specific code or features within the current version. 

```
<inf> jkoss11@hpcloginml /s/jkoss11/git/ford-innersource/hpc.k8s.cicd (main)
$ cat .gitmodules
[submodule "hpc.k8s.kubespray"]
	path = hpc.k8s.kubespray
	url = git@github.com:ford-innersource/hpc.k8s.kubespray
```
