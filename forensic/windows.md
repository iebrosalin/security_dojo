## User enumeration

**PowerShell**
### Просмотр списка домашних дирректорий пользоватлей

```ps
    Get-ChildItem C:\Users -Force
```

### Список локальных пользователей вместе с их SID

```ps
    get-wmiobject -Class Win32_UserAccount
```

### Список локальных пользователей с описанием (помогает сразу увидеть, где системные пользователи)

```ps
    Get-LocalUser
```


**CMD**

Список локальных пользователей

```cmd 
    net user
```
Детальная информаци об пользователе

```
    net user $username
```
**Собиытия в журналах**

Событие 4722 S: учетная запись пользователя включена.
Событие 4723 S, F: попытка изменить пароль учетной записи.
Событие 4724 S, F: попытка сбросить пароль учетной записи.
Событие 4725 S: учетная запись пользователя отключена.
Событие 4726 A: учетная запись пользователя удалена.
Событие 4738 S: учетная запись пользователя изменена.
Событие 4740 S: учетная запись пользователя была заблокирована.
Событие 4765 S: журнал SID был добавлен в учетную запись.
Событие 4766 F: ошибка добавления журнала SID в учетную запись.
Событие 4767 S: учетная запись пользователя разблокирована.
Событие 4780 S: список ACL настроен для учетных записей, входящих в группы администраторов.
Событие 4781 S: имя учетной записи было изменено.
Событие 4794 S, F: осуществлена попытка установить пароль администратора режима восстановления служб каталогов.
Событие 4798 S: перечислено участие пользователя в локальных группах.
Событие 5376 S: создана резервная копия учетных данных диспетчера учетных данных.
Событие 5377 S: учетные данные диспетчеры учетных данных были восстановлены из резервной копии.

## RDP Информаци о подключениях

https://winitpro.ru/index.php/2018/09/25/analizing-rdp-logs-windows-terminal-rds/

```ps
    Get-EventLog -LogName Security -after (Get-date -hour 0 -minute 0 -second 0)| ?{(4624,4778) -contains $_.EventID -and $_.Message -match 'logon type:\s+(10)\s'}| %{
(new-object -Type PSObject -Property @{
TimeGenerated = $_.TimeGenerated
ClientIP = $_.Message -replace '(?smi).*Source Network Address:\s+([^\s]+)\s+.*','$1'
UserName = $_.Message -replace '(?smi).*Account Name:\s+([^\s]+)\s+.*','$1'
UserDomain = $_.Message -replace '(?smi).*Account Domain:\s+([^\s]+)\s+.*','$1'
LogonType = $_.Message -replace '(?smi).*Logon Type:\s+([^\s]+)\s+.*','$1'
})
} | sort TimeGenerated -Descending | Select TimeGenerated, ClientIP `
, @{N='Username';E={'{0}\{1}' -f $_.UserDomain,$_.UserName}} `
, @{N='LogType';E={
switch ($_.LogonType) {
2 {'Interactive - local logon'}
3 {'Network conection to shared folder)'}
4 {'Batch'}
5 {'Service'}
7 {'Unlock (after screensaver)'}
8 {'NetworkCleartext'}
9 {'NewCredentials (local impersonation process under existing connection)'}
10 {'RDP'}
11 {'CachedInteractive'}
default {"LogType Not Recognised: $($_.LogonType)"}
}
}}
```

Инструменты 
                             
- FTK               
- RamCapturer             
- Sysmon
- Autoruns 
- mftdump.zip       
- RegistryExplorer
- avz4                                     
- ProcessExplorer   
- RegRipper3.0-master
- ProcessMonitor    
- Sigcheck                
- Zoomlt
- PsTools           
- sleuthkit-4.8.0-win32

Информацию о пользователях на локальной машине можно получить
из SAM-файла \Windows\System32\config (там хранятся файлы реестра )

Инфа о профилях находится 
в реестре по пути HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList