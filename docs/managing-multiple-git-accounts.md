# Managing multiple GIT accounts

> 20250416

> #git

## Using the ssh config

You can use custom `Host` definitions within the ssh config to set per-repository ssh keys:

```
Host proxystock
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_mygitkey
  IdentitiesOnly yes

Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_myworkkey
```

Using this method would require replacing "github.com" with "proxystock" as needed. Otherwise, it will default to using the work settings. 

So, if I wanted to clone this repository I would run:

```shell
git clone proxystock:proxystock/zet.git
```

## Defining variables from within repository

You can query and set variables that the remote uses.

```shell
# Query
git config user.email
git config user.name

# Define
git config user.email myemail@email.com
git config user.name "My Name"
```


## Global variables

This is not something I have experimented with personally, but you can set the [global git variables](https://git-scm.com/docs/git#Documentation/git.txt-codeGITSSHCOMMANDcode).

