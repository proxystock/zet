# Checking for an exact match in bash array

The below example checks user input against a controlled array and will exit if a match does not exist. 
The tricky part about this is most methods will pass on a partial match. 

```bash
if ! grep -Fw "$user_input" <<<"${control_array[*]}" >/dev/null; then
	echo "Acceptable options for this are: ${control_array[*]}"
    exit 1
fi
```
