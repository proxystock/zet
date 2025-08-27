# Multi-function debug 

Useful to print a message if `debug=true`, or print whatever body of information if executed without a parameter.

```bash
function debug() {
	local debug_message="$1"
	if [[ "$debug" != true ]]; then
		return 1
	fi

	if [[ -z "$debug_message" ]]; then
		cat <<-EOF
		***********
		*  DEBUG  *
		***********
		URL: $elasticsearch_url
		Index name: $index_name
		Doc type: $doc_type
		Configuration file: $config
		Submit: $submit


		Imported: $api_key

		Plugin script: $plugin_script
		Output: $output
		Exit code: $exit_code
		Extracted metric: $metric_value

		*************
		* END DEBUG *
		*************
		EOF

		return 0
	fi

	echo "$debub_message" && return 0
}
```
