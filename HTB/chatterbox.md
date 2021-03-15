
```
    sudo nmap -Pn -p 1-65355 -T4 10.129.113.159
Starting Nmap 7.80 ( https://nmap.org ) at 2021-03-15 05:33 UTC
Nmap scan report for 10.129.113.159
Host is up (0.13s latency).
All 65355 scanned ports on 10.129.113.159 are filtered

    Nmap done: 1 IP address (1 host up) scanned in 536.55 seconds
    ─[eu-dedivip-2]─[10.10.14.13]─[htb-iebrosalin@htb-sja9vqvd0h]─[~]
    └──╼ [★]$ sudo nmap -sU -p- -T4 10.129.113.159
    Starting Nmap 7.80 ( https://nmap.org ) at 2021-03-15 05:43 UTC
    Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
    Nmap done: 1 IP address (0 hosts up) scanned in 2.10 seconds
    ─[eu-dedivip-2]─[10.10.14.13]─[htb-iebrosalin@htb-sja9vqvd0h]─[~]
    └──╼ [★]$ sudo nmap -A -p- -T4 10.129.113.162
    Starting Nmap 7.80 ( https://nmap.org ) at 2021-03-15 05:47 UTC
    Nmap scan report for 10.129.113.162
    Host is up (0.023s latency).
    Not shown: 65533 filtered ports
    PORT     STATE SERVICE VERSION
    9255/tcp open  http    AChat chat system httpd
    |_http-server-header: AChat
    |_http-title: Site doesn't have a title.
    9256/tcp open  achat   AChat chat system
    Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
    Device type: general purpose|phone|specialized
    Running (JUST GUESSING): Microsoft Windows 8|Phone|2008|7|8.1|Vista|2012 (92%)
    OS CPE: cpe:/o:microsoft:windows_8 cpe:/o:microsoft:windows cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_7 cpe:/o:microsoft:windows_8.1 cpe:/o:microsoft:windows_vista::- cpe:/o:microsoft:windows_vista::sp1 cpe:/o:microsoft:windows_server_2012
    Aggressive OS guesses: Microsoft Windows 8.1 Update 1 (92%), Microsoft Windows Phone 7.5 or 8.0 (92%), Microsoft Windows 7 or Windows Server 2008 R2 (91%), Microsoft Windows Server 2008 R2 (91%), Microsoft Windows Server 2008 R2 or Windows 8.1 (91%), Microsoft Windows Server 2008 R2 SP1 or Windows 8 (91%), Microsoft Windows 7 (91%), Microsoft Windows 7 Professional or Windows 8 (91%), Microsoft Windows 7 SP1 or Windows Server 2008 R2 (91%), Microsoft Windows Vista SP0 or SP1, Windows Server 2008 SP1, or Windows 7 (91%)
    No exact OS matches for host (test conditions non-ideal).
    Network Distance: 2 hops

    TRACEROUTE (using port 9256/tcp)
    HOP RTT      ADDRESS
    1   22.75 ms 10.10.14.1
    2   22.83 ms 10.129.113.162

    OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 434.32 seconds

```