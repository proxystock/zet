# Multiple variables from bash function

While it would be nice to just global every variable, here's a decent strategy to setting multiple variables from a function. 

```bash
function runx() {
	local var1 var2 etc...
	# run code, assign var1, var2, etc...
	echo "$var1 $var2 $var3"
}

function_results=$(runx)
read -r var1 var2 var3 <<<"${function_results}"

# Now you have all the vars set 
```

> [!NOTE]
> The difference between a global variable and a scripts global variable are whether or not it persists outside of execution.  
> Defining a variable within the main body of a script does technically make it global (to the script). But not global to the shell. 

