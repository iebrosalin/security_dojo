# Windows RDP

https://winitpro.ru/index.php/2018/09/25/analizing-rdp-logs-windows-terminal-rds/

```
  Актуально для Windows Server 2008 R2, 2012/R2, 2016, так и в соответствующих десктопных версиях Windows (Windows 7, 8.1, 10).
```

1. Network Connection - 1149 (Remote Desktop Services: User authentication succeeded)
2. Authentication  – успешная или неуспешная аутентификация пользователя на сервере  – 4624 (успешная аутентификация — An account was successfully logged on) или 4625 (ошибка аутентификации — An account failed to log on)
3. Logon
4. Session Disconnect/Reconnect
5. Logoff

## Network Connection - 1149 (Remote Desktop Services: User authentication succeeded)

```
  Applications and Services Logs -> Microsoft -> Windows -> Terminal-Services-RemoteConnectionManager -> Operational
```
Содержимое зависит от ключения NLA аутентификации]()
```
  User
  Domain
  Source Network Address
```

## Authentication  – успешная или неуспешная аутентификация пользователя на сервере  4624 (успешная аутентификация — An account was successfully logged on) или 4625 (ошибка аутентификации — An account failed to log on)

```
  Windows -> Security
```
 При входе через терминальную службу RDP — LogonType = 10 или 3. Если LogonType = 7, значит выполнено переподключение к уже имеющейся RDP сессии.
```
Account Name
имя компьютера в Workstation Name, а имя пользователя в Source Network Address.
```
