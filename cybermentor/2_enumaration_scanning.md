# Scanning, enumaration

Common ports and protocols

TCP:
- FTP (21)
- SSH(22)
- Telnet(23)
- SNMTP (25)
- DNS (53)
- HTTP (80) / HTTPS (443)
- POP3 (110)
- SMB (139 + 445)
- IMAP (143)

UDP:
- DNS (53)
- DHCP (67, 68)
- TFTP (69)
- SNMP (161)

## nmap

Note all services. Check each service

```bash
    # TCP scan all ports
    nmap -T4 -p- -A address

    # UDP scan all porst
    nmap -sU -T4 -p- -A address
```

## nikto

```bash
   nikto -h adress
```

## Burp suit
    Check sitemap, headers.

## DirBuster
    Check directories.

## Wappalyzer
    check build with...

## Metasploit

```bash
    # search exploits or portscan
    msfconsole
    search (smb)
    use (number position)
    info #get all information
    options #get options
    set NAME_OPTION VALUE
    run
```


## SMB
    ```bash
        # Kali
        smbclient -L \\\\192.168.57.134\\ ##
    ```

## Google exloits for enumarated services

```
    searchsploit Samba 2.
```

## masscan 

```bash
    masscan -p1-65535 --rate 1000 ip_adress
```

## Nessus