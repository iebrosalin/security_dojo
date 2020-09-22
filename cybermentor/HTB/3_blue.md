# Blue

# Scan 

```bash
    nmap -A -T4 -p- 10.10.10.40
```

Saw Windows 7 7601 SP1. May be  eternal blue will work.


# Exploit

First check vulnurability and after ask permission for exploit it. 

```
    msfconsole
    search MS17-010
```

https://github.com/3ndG4me/AutoBlue-MS17-010