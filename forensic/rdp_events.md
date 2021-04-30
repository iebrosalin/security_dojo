# Windows RDP события


*Актуально для Windows Server 2008 R2, 2012/R2, 2016, так и в соответствующих десктопных версиях Windows (Windows 7, 8.1, 10).*

1. [Network Connection - 1149 (Remote Desktop Services: User authentication succeeded)](https://github.com/iebrosalin/security_dojo/blob/master/forensic/rdp.md#network-connection---1149-remote-desktop-services-user-authentication-succeeded)
2. [Authentication  – успешная или неуспешная аутентификация пользователя на сервере  – 4624 (успешная аутентификация — An account was successfully logged on) или 4625 (ошибка аутентификации — An account failed to log on)](https://github.com/iebrosalin/security_dojo/blob/master/forensic/rdp.md#authentication---%D1%83%D1%81%D0%BF%D0%B5%D1%88%D0%BD%D0%B0%D1%8F-%D0%B8%D0%BB%D0%B8-%D0%BD%D0%B5%D1%83%D1%81%D0%BF%D0%B5%D1%88%D0%BD%D0%B0%D1%8F-%D0%B0%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F-%D0%BD%D0%B0-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%B5--4624-%D1%83%D1%81%D0%BF%D0%B5%D1%88%D0%BD%D0%B0%D1%8F-%D0%B0%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F--an-account-was-successfully-logged-on-%D0%B8%D0%BB%D0%B8-4625-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B0-%D0%B0%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8--an-account-failed-to-log-on)
3. [Logon](https://github.com/iebrosalin/security_dojo/blob/master/forensic/rdp.md#logon--21--remote-desktop-services-session-logon-succeeded-rdp-%D0%B2%D1%85%D0%BE%D0%B4-%D0%B2-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5-%D0%BF%D0%BE%D1%8F%D0%B2%D0%BB%D1%8F%D1%8E%D1%89%D0%B5%D0%B5%D1%81%D1%8F-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D1%83%D1%81%D0%BF%D0%B5%D1%88%D0%BD%D0%BE%D0%B9-%D0%B0%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F)
4. [Session Disconnect/Reconnect](https://github.com/iebrosalin/security_dojo/blob/master/forensic/rdp.md#session-disconnectreconnect)
5. [Logoff](https://github.com/iebrosalin/security_dojo/blob/master/forensic/rdp.md#logoff-eventid-23-remote-desktop-services-session-logoff-succeeded--%D0%B2%D1%8B%D1%85%D0%BE%D0%B4-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F-%D0%B8%D0%B7-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B)

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
Account Domain
Workstation Name
Source Network Address
```

*Обратите внимание на значение поля TargetLogonID – это уникальный идентификатор сессии пользователя с помощью которого можно отслеживать дальнейшую активность данного пользователя. Однако при отключении от RDP сессии (disconnect) и повторного переподключения в сессию, пользователю будет выдан новый TargetLogonID (хотя RDP сессия осталась той же самой).*

## Logon – 21  (Remote Desktop Services: Session logon succeeded) RDP вход в систему, событие появляющееся после успешной аутентификации пользователя

```
  Applications and Services Logs -> Microsoft -> Windows -> TerminalServices-LocalSessionManager -> Operational
```
Событие с EventID – 21 (Remote Desktop Services: Shell start notification received) означает успешный запуск оболочки Explorer (появление окна рабочего стола в RDP сессии).

## Session Disconnect/Reconnect 

```
  Applications and Services Logs -> Microsoft -> Windows -> TerminalServices-LocalSessionManager -> Operational
```

- EventID – 24 (Remote Desktop Services: Session has been disconnected) – пользователь отключился от RDP сессии.
- EventID – 25 (Remote Desktop Services: Session reconnection succeeded) – пользователь переподключился к своей имеющейся RDP сессии на сервере.
- EventID – 39 (Session <A> has been disconnected by session <B>) – пользователь сам отключился от своей RDP сессии, выбрав соответствующий пункт меню (а не просто закрыл окно RDP клиента). Если идентификаторы сессий разные, значит пользователя отключил другой пользователь (или администратор).
- EventID – 40 (Session <A> has been disconnected, reason code <B>). Здесь нужно смотреть на код причины отключения в событии. Например:
  - reason code 0 (No additional information is available)– обычно говорит о том, что пользователь просто закрыл окно RDP клиента.
  - reason code 5 (The client’s connection was replaced by another connection) – пользователь переподключился к своей старой сессии.
  - reason code 11 (User activity has initiated the disconnect) – пользователь сам нажал на кнопку Disconnect в меню.

Событие с EventID – 4778 в журнале Windows -> Security (A session was reconnected to a Window Station). Пользователь переподключился к RDP сессии (пользователю выдается новый LogonID).

Событие с EventID 4799 в журнале Windows -> Security (A session was disconnected from a Window Station). Отключение от RDP сеанса.

## Logoff EventID 23 (Remote Desktop Services: Session logoff succeeded)  выход пользователя из системы

```
  Applications and Services Logs -> Microsoft -> Windows -> TerminalServices-LocalSessionManager -> Operational
```

При этом в журнале Security нужно смотреть событие EventID 4634 (An account was logged off).

Событие Event 9009 (The Desktop Window Manager has exited with code (<X>) в журнале System говорит о том, что пользователь инициировал завершение RDP сессии, и окно и графический shell пользователя был завершен.

Шпора составлена на основе:

https://winitpro.ru/index.php/2018/09/25/analizing-rdp-logs-windows-terminal-rds/
https://ponderthebits.com/2018/02/windows-rdp-related-event-logs-identification-tracking-and-investigation/
