# VIM olympics

| #vim #shortcuts

> [!TIP] 
> QUESTION: Does vim read environment variables? I think it can!
>
> Shortlist of what you often forget...
> - <kbd>CTRL R</kbd>: Re-do an accidental undo (`u`)
> - `zz`: Center screen
> - `yy`: Yank line
> - `yE`: Grab word 



## Execute shell commands

- `: ! <cmd>`: Temporarily break away from vim session to show output of command. 
- `:r ! <cmd>`: Paste (*[r]ead*) output from command into vim session.

### Directory list

```
:r ! ls path/
```

> [!NOTE]
> Relative to working directory.

### Double bang will repeat previous bang command

```
:!!
```

### Base64 encode current line

*More explanation needed on this because double bang `!!` is used to recall previous commands.* 

```
:!!base64
```

### Curl

```
:r !curl -s 'https://jsonplaceholder.typicode.com/todos/1'
```

> [!NOTE]
> - Curl needs to be installed
> - Works with POST/PUT/DELETE

## Prefix highlighted lines

Prefix highlighted lines with `:norm I`.

1. First, highlight the lines you intend to prefix.  
2. Execute

    ```
    :norm <SHIFT> I
    ```

3. Whatever you type after `I` will insert at the beginning of any highlighted lines.

> [!TIP]
> You can use `<shift> A` to suffix.


## Quickly re-select last visual selection

Type `gv` while in normal mode (non-insert).

## Center highlighted search match

Type `zz` while in normal mode.

## Tabs vs. spaces

Convert tabs to spaces

```
:set noexpandtab
:retab
```

Convert spaces to tabs

```
:set expandtab
:set tabstop=4
:set shiftwidth=4
:retab
```

## Show diff before saving file

```
:w !diff % -
```

## Spellcheck

```
:set spell
```

## Word count

You can use `:!wc %` or `g C-g` (normal mode).

## Show line numbers

### All lines

```
:set number
```

### Relative lines

```
:set number relativenumber
```

## Open with vim cursor on specific line

```shell
vim +line_num FILE
```

## Delete while using INSERT mode

- <kbd>CTRL + w</kbd>: Delete previous word (equivalent to `db` in normal mode).
- <kbd>CTRL + h</kbd>: Delete previous character.
- <kbd>CTRL + u</kbd>: Delete all previous characters until the start of line (equivalent to `d0` in normal mode).
- <kbd>CTRL + k</kbd>: Delete all leading characters until end of line (equivalent to `d$` in normal mode).

## Search & Replace

- `:s/black/white/`: Replace the first occurrence of the string ‘black’ by ‘white’
- `:s/Ben\( Rogers\)\@!/Ben Rogers/g`: Replace every occurrence of the string ‘Ben’ by ‘Ben Rogers’ except when ‘ Rogers’ was already present
- `:s/.*/<p>\r&\r<\/p>/`: Wrap the line between <p> and </p>
- `:-1s/–/\&mdash;/g`: Replace evert occurrence of `-` with `&mdash` in the preceding line. 


## Resources

- [vimtricks.com](https://vimtricks.com/p/50-useful-vim-commands/)
- [thevaluable.dev/vim-advanced](https://thevaluable.dev/vim-advanced/)
