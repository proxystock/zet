# Identify Container Overlay 

Identifying which containers own which overlays.

```bash
docker inspect $(docker ps -qa) |  jq -r 'map([.Name, .GraphDriver.Data.MergedDir]) | .[] | "\(.[0])\t\(.[1])"'
```

```console
# docker inspect $(docker ps -qa) |  jq -r 'map([.Name, .GraphDriver.Data.MergedDir]) | .[] | "\(.[0])\t\(.[1])"'
kdc2	/var/lib/containers/storage/overlay/3bd8fb2b401da1bcd09266663dc3f50fbafb825194b74437a567ffc38d61b934/merged
ntp2	/var/lib/containers/storage/overlay/2ba16d952fd2e60e9655b9134f032c0665d7fff7a71b4150010fba7115ef6670/merged
hpcdns2	null
git2	/var/lib/containers/storage/overlay/12d6bfeb5ab192b5e836221f2fd9c2c4db9eba050e9d59a32f620720a777ecb7/merged
build0	/var/lib/containers/storage/overlay/39eb9a8ca9729746672ad994bb065a9ac8182f532ca4b033935b8bb3640652f0/merged
webhook1	null
nice_remoteviz_enginframe	/var/lib/containers/storage/overlay/bac3a1a5c78ad04552a2b60f4ff424df29c244fe74d120d56118572d294760c5/merged
graphitetest	null
graphite	/var/lib/containers/storage/overlay/b61295308d48e2b79549dac15e9cdf8f1a025c10778d6cee383d9d227ab8406b/merged
ldap3	/var/lib/containers/storage/overlay/3ee306cf48c4f2d09e6fc827643c4deb608a011e7d86468823569afc4d3c08c6/merged
ldap1	/var/lib/containers/storage/overlay/3bb17492557ed6c76b9a8fbb102c5ef01c6bc2764826116c05c7aff26a050252/merged
```
