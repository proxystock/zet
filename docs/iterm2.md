# iTerm2 Settings

> #zet #custom #shell #iterm #terminal 

With how customizable iTerm2 is, the below are confirmed recommended settings from testing. 

## GENERAL

| Description | Value | Notes |
|-------------|-------|-------|
| Quit when all windows are closed	| Disabled | To accomodate hotkey for snap-in terminal |
| Window > Smart Window Placement | Disabled | Noting because of random misplacement of settings window when moving across desktops |

## Session

| Description | Value |
|-----------------------------|
| Password manager | Enabled |


## Profiles 

| Description                                                           | Value   | Notes                                                   |
|-----------------------------------------------------------------------|---------|---------------------------------------------------------|
| Window > Transparency                                                 | 20      |                                                         |
| Terminal > Terminal may enable alt mouse scroll                       | Enabled |                                                         |
| Session > Undo can revive a session thats been closed up to X seconds	| 30      |                                                         |
| Key Bindings                                                          | -       | Defined in sub-section below                            |
| Shell Integration                                                     | -       | https://iterm2.com/documentation-shell-integration.html |
|-----------------------------------------------------------------------|---------|---------------------------------------------------------|
		


### Profiles Cont. Key Bindings
```txt
# Profiles > $profile > Keys > Key Bindings Tab 

# word jump backwards (b)
Option + Left = Action(send escape) = “b”

# word jump forward (f)
Option + Right = Action(send escape) = “f”


# Mapping scroll to move cursor in vim. 
#  Note the 'Terminal may enable alt mouse scroll' setting resolves this.
#  Having mouse enabled in .vimrc changes the behavior of the alt mouse scroll setting. 
#  So this is another workaround if the above .vimrc config is needed.

map <ScrollWheelDown> j
map <ScrollWheelUp> k
```

### Profiles Cont. Automatic Profile Switching

A setting available under Profiles > Advanced labeled as “Automatic profile switching” allows any session to switch profiles based on criteria defined. 

```txt
#Any session will switch to this profile automatically when your hostname, username, and current path match one of the rules specified in the adjacent table.

#A rule may specify a username, hostname, path, or job. It can also specify combinations of them.

#For example:

#・	user@host:/path
#・	user@
#・	host
#・	/path
#・	&job

#Hostnames, paths, and jobs may use * wildcards. When a rule that had matched no longer matches (e.g., because the hostname changes), the profile switches back. You can prevent that by adding ! at the end of the rule. For example, user@example.com!.
```


### Profiles Cont. Shell Integration

[iTerm2 shell integration](https://iterm2.com/documentation-shell-integration.html)

Considerations and features

- Configures shell on each host that is logged into to send special escape codes that convey specific information.
- Assign profile to remote ssh hosts
- Assign profile to local root
- Assign profile to remote ssh root
- Drag/drop scp features
- Download files from remote hosts with right click (such as a file shown in ls output)
- View information about commands (


## Integrations and add-ons

- Pastel color theme - catppuccin/iterm
- Special glyphs (Powerline) - 

