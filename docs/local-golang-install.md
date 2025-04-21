# Local golang install
> 202502--

> #go #golang #compiler #build

Local GoLang Compiler

1. Download the appropriate tar from the [releases page](https://go.dev/doc/install), taking note of the version.

2. Create dirs

```shell
mkdir -p /s/$USER/go/$VERSION
```

3. Install 

```shell
tar -C /s/$USER/go/$VERSION -xzvf thedownloaded.tar.gz
```

4. Set in your env:

```shell
export GOPATH=/s/$USER/go GOROOT=/s/$USER/go/$VERSION/go
```

5. For safety: 

```shell
ln -s /s/$USER/go /u/$USER/go
```

6. Add `/s/$USER/go/$VERSION/go/bin` to path (consider defining this in your bash profile).

```shell
export PATH="$PATH:/$GOROOT/bin"
```
