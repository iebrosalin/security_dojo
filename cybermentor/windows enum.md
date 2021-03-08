# Windows enum

## Manual

### System info

```
    systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
```

### Installed updates

```
    wmic qfe
```

### Logical disk

```
    wmic logicaldisk get caption
```

### User/group info

```
    whoami
    whoami /priv
    whoami /groups
    net user $userName
    net localgroup $group
```

### List of users/groups

```
    net user 
    net localgroup
```

### Network

```
    ipconfig
    arp -a
    route print
    netstat -ano
```

### Service, firewall

```
    sc query windefend
    sc queryex type= service
    netsh advfirewall firewall dump
    netsh firewall show state
    netsh firewall show config
```

## Automated tools

### Executables

- winPEAS.exe
- Searbeit.exe (compile)
- Watson.exe (compile)
- SarpUp.exe (compile)

### PowerShell
- Sherlock.ps1
- PowerUp.ps1
- jaws-enum.ps1

### Other
- windows-exploit-suggester.py (local)
- Exploit Suggester(Metasploit)