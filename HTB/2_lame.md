# Lame

# Scan

```bash
    nmap -A -T4 -p- 10.10.10.3
```

Open port:
- 21 with anonym login vsftpd 2.3.4
- 22 openssh 4.7p1
- 139 smb
- 445 smb
- 3632 distccd

# Expoilt

```bash
    smbclient -L \\\\10.10.10.3\\
```

https://www.rapid7.com/db/modules/exploit/multi/samba/usermap_script

Look for flags home directories

use updatedb and locate

For prepare file for decrypt passwords from shadow use unshadow

Decrypt with hashcat