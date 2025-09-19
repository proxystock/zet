# zet
My personal [zettelkasten](https://zettelkasten.de/introduction/#a-zettelkasten-is-a-personal-tool-for-thinking-and-writing).

## Usage

```console
$ z help

Zettel helper script.

Usage:

    z h|help              : Show this help screen
    z c|create TITLE...   : Create a new zettel
    z e|edit   QUERY...   : Search for a zettel and edit it
    z p|print  QUERY...   : Search for a zettel and print it
    z push                : Push changes to github
    z s|search QUERY...   : Print IDs and titles of zettels matching QUERY
	z u|url    QUERY...   : Search for a zettel and print its github url
    z v|view   QUERY...   : Search for a zettel and view it
    z id       QUERY...   : Search for a zettel and display its ID
```

```bash
# Zettel (bashrc)
if [[ -d "$GITDIR/proxystock/zet" ]]; then
    export ZETDIR="$GITDIR/proxystock/zet"
fi
```
