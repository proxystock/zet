# Regex capture group example
> #regex #bash #shell

I just thought [this](https://grafana.com/docs/grafana/latest/dashboards/variables/add-template-variables/#filter-and-modify-using-named-text-and-value-capture-groups) example was really cool, and should be explored a bit for PD. 

Using regex capture groups, you can print matching data in columns as if it were a table. 


Text sample:

```txt
node_hwmon_chip_names{chip="0000:d7:00_0_0000:d8:00_0",chip_name="enp216s0f0np0"} 1
node_hwmon_chip_names{chip="0000:d7:00_0_0000:d8:00_1",chip_name="enp216s0f0np1"} 1
node_hwmon_chip_names{chip="0000:d7:00_0_0000:d8:00_2",chip_name="enp216s0f0np2"} 1
node_hwmon_chip_names{chip="0000:d7:00_0_0000:d8:00_3",chip_name="enp216s0f0np3"} 1
```


Regex:

```regex
/chip_name="(?<text>[^"]+)|chip="(?<value>[^"]+)/g
```


Output:

```txt
Display Name          Value
------------          -------------------------
enp216s0f0np0         0000:d7:00_0_0000:d8:00_0
enp216s0f0np1         0000:d7:00_0_0000:d8:00_1
enp216s0f0np2         0000:d7:00_0_0000:d8:00_2
enp216s0f0np3         0000:d7:00_0_0000:d8:00_3
```

> [!NOTE]
> Only `text` and `value` capture group names are supported.
