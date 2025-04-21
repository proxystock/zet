# Show blocked IP addresses or IP ranges
> #linux #iptables #firewall #ip #address #network #shell

```shell
iptables -L INPUT -v -n
```

Eventually, and if working properly, you should see non-zero packet and byte counts for the country blocking rules.  

Example:

```shell
Chain INPUT (policy DROP 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
   ...
   60848  3326067 DROP       all  --  enp4s0 *       0.0.0.0/0            0.0.0.0/0            match-set china src
    1265    57566 DROP       all  --  enp4s0 *       0.0.0.0/0            0.0.0.0/0            match-set hongkong src
   26865  1085462 DROP       all  --  enp4s0 *       0.0.0.0/0            0.0.0.0/0            match-set romania src
  193511  7816920 DROP       all  --  enp4s0 *       0.0.0.0/0            0.0.0.0/0            match-set russia src
   33149  1358726 DROP       all  --  enp4s0 *       0.0.0.0/0            0.0.0.0/0            match-set ukraine src
```

To list the contents of any set, do `ipset list SETNAME`:

```console
$ sudo ipset list romania | head -15
Name: romania
Type: hash:net
Revision: 6
Header: family inet hashsize 1024 maxelem 65536
Size in memory: 65600
References: 1
Members:
193.104.73.0/24
45.131.104.0/22
89.45.66.0/24
91.240.94.0/24
176.223.66.0/24
185.248.136.0/22
46.175.152.0/22
176.116.32.0/20
```
