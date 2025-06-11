# Count by prefixed number of characters in bash

> #bash #zet #count #group

Cut out characters 1-6, and give me a count of all repeating items in groups.

```bash
cut -c 1-6 $filename |uniq -c |sort -rn
```

Example:

```console
somehost # cut -c 1-6 hostnames.txt |uniq -c |sort -rn
    109 host1
    103 host2
      5 host3
      3 host4
      2 host5
```

It’s ugly, but the output looks authentic.

```console
somehost # cut -c 1-6 hostnames.txt | uniq -c |sort -rn |column -t; echo "--------------";wc -l hostnames.txt 
109  hpcn09
103  hpcm05
5    hpcm04
3    hpcn10
2    hpcn12
--------------
222 hostnames.txt
```

> [!TIP] 
> Using `colunn -t` isn't necessary, but it quickly lines the counts up with the second commands total.
