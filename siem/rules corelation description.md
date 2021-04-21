AD
- Mimikatz скопирован в административную сетевую папку
- Выгрузка активных пользовательских сеансов на узле
- Неавторизованная репликация DC
- Запущен процесс, обычно используемый для выгрузки активных пользовательских сеансов (типа sysmon)
- Попытка выгрузки локальных групп или членов группы локальных администраторов на контроллере домена или узле
- Попытка выгрузки списка групп домена на узле или контроллере домена
- Session_enumeration_smb


«Выполнение» и «Предотвращение обнаружения»
- Обнаружение попыток обойти контроль учетных записей или запрет на запуск приложения при помощи встроенной утилиты Windows "cmstp"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "control"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "csc"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "InstallUtil"
 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows .NET "MSBuild.exe"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "RegAsm"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "regsvr32"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "rundll32"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенных утилит Windows "cscript" и "wscript"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "dnscmd"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "mavinject"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "msiexec"
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "msxsl"
- Обнаружение попыток обойти запрет на запуск приложений при помощи утилиты Windows "odbcconf", позволяющей настраивать Open Database Connectivity (ODBC)
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "pcalua"
- Обнаружение попыток загрузить или запустить приложения при помощи встроенной утилиты Windows "bitsadmin"
- Пользователь попытался выполнить скрипт (bat|ps1|cmd|vbs|js|psd1|psm1|ps1xml|wsf|vbe|wsc)
- Открыт потенциально опасный файл справки hh.exe 
- Попытка выполнить потенциально опасную команду ("shellcode|-lhost|reverse_|bind_|remove-|psexec|base64|iconv|webclient|webreguest|winhttp|url=|encodedcommand|powerview|powerup|recon|scrnsavebackdoor|regbackdoor|dns_txt|pwnage|backdoor|adsbackdoor|remotepsremoting|remotewmi|amsibypass|lsasecret|listener|passhashes|mimikatz|wdigestdowngrade|adsbackdoor|remotepsremoting|remotewmi|amsibypass|interceptor|nisnag|powerpreter|bruteforce|portscan|psgcat|persistence|remotewmi|amsibypass|antivirusbypass|avsignature|codeexecution|dllinjection|powersploit|gpppassword|minidump|shadowcopy|privesc|llmnresponse|nbnsresponse|inveigh|internetexplorer|serverxmlhttp|mshta.*?http|mshta.*?ftp|dcsync|keystrokes|timedscreenshot|vaultcredential|credentialinjection|ninjacopy|tokenmanipulation|volumeshadowcopy|reflectivepeinjection|userhunter|gpolocation|aclscanner|downgradeaccount|serviceunquoted|servicefilepermission|servicepermission|serviceabuse|servicebinary|regautologon|vulnautorun|vulnschtask|unattendedinstallfile|duplicatetoken|psuacme|targetscreen|poshrathttp|powershellwmi|exfiltration|captureserver|chromedump|foxdump|indexeditem|screenshot|netripper|egresscheck|postexfil|psinject|runas|powerdump|sshcommand|backdoorlnk|bypassuac|wscriptbypassuac|paranoia|winenum|arpscan|reversednslookup|smbscanner|mimikittenz|volumeshadowcopytools|regalwaysinstallelevated|port-scan|powershelltcp|clipboardcontents|install-ssp|powerbreach|invoke-tater|phant0m|-noni|-noninteractive|-enc|-nol\s+|non\s+|invoke-|bypass|hidden|downloadfile|downloadstring|nop\s+|-noprofile|executionpolicy|iex\s+|reflectedpeinjection|new-object|paexec|xcopy|sdelete|plink|nping|nmap|ncat\.exe|ncat\s+|-p\s+22|:3389|vssadmin|ftp\s+|ftp\.exe|taskkill|robocopy|copy-item|schtask\s+|^at\s+|at\.exe|mofcomp|wevtutil|vnc|cpassword|pskill|winscp|wmic|psexesvc|-ma\s+lsass\.exe|wmic.*?http|wmic.*?ftp|cmdkey\s+/list|cmd.*?/k.*?<.*?\.txt|ntds\.dit|copy.*?ntds\.dit|copy.*?config\\sam|reg\s+save.*?system|snapshot")
- powershell|-noni|-noninteractive|-enc|-nol|non|invoke-|exec|bypass|hidden|downloadfile|downloadstring|payload|shellcode|-lhost|reverse_|bind_|remove-|psexec|psexesvc|winexesvc|base64|iconv|webclient|nop|-noprofile|executionpolicy|iex\s|reflectedpeinjection|new-object|webreguest|winhttp|url=|encodedcommand
- Попытка управления задачами по расписанию через командную строку или PowerShell "schtasks.*?/(create|delete|run|query|change)"  "schtasks\s+/(create|delete|run|query|change)|register-scheduled|registertaskdefinition"
- Detect_Sysmon_driver_unload "fltmc.exe", "unload.*?sysmondrv"
- Обнаружение попыток загрузить или запустить приложение при помощи встроенной утилиты Windows "mshta" (".*(http|ftp|\.sct|getobject|\.txt.*\.hta|\.hta).*") 
- Обнаружение попыток запустить потенциально опасный сценарий при помощи утилит, встроенных в Windows ["cmd.exe","powershell.exe","wscript.exe", "mshta.exe", "script.exe"]
- Обнаружение попыток использовать утилиту "wmic" для совершения подозрительных действий (потенциальная атака путем бокового смещения (lateral movement attack)) "\s+/node|\s+/node:|process\s+call\s+create|\s+-w\s+>\s+"
- Обнаружение попыток запустить сценарии XSL (eXtensible Stylesheet Language) при помощи утилиты "wmic" "wmic.*/format:.*\.xsl"
- Обнаружение попытки запустить утилиту "cmd", встроенную в Windows, с потенциально опасными аргументами
- Обнаружение попыток запусить утилиту администрирования PSEXEC и ее аналогов         "psexec*" "winexec*" "csexec*" "paexec*"
- Подозрительная последовательность запуска процесса приложением Microsoft Office   and in_list(["winword.exe", "excel.exe", "powerpnt.exe", "visio.exe", "mspub.exe", "eqnedt32.exe", "mshta.exe", "outlook.exe"], lower(datafield4))  and in_list(["powershell.exe", "cmd.exe", "wmic.exe", "wscript.exe", "script.exe", "wmiprvse.exe", "sh.exe", "bash.exe", "scrcons.exe", "schtasks.exe", "regsvr32.exe", "hh.exe", "rundll32.exe", "msiexec.exe", "forfiles.exe", "scriptrunner.exe", "mftrace.exe", "appvlp.exe", "msbuild.exe", "mshta.exe"], lower(object name))
- Обнаружение попыток установить новую службу не из системных каталогов Windows  "(c:\\\\programdata\\\\|c:\\\\program\s+files|\\\\systemroot\\\\system32\\\\|c:\\\\windows\\\\system32\\\\).*"


"Закрепление"
- Обнаружение попыток создать локальную учетную запись
- Обнаружение попыток создать и удалить учетную запись в течение короткого промежутка времени
- Обнаружение попыток измененить ключ реестра "Image File Execution Options", чтобы встроить стороннее ПО в цепочку запуска
- Обнаружение попыток изменить стандартный шаблон документов Microsoft Office (normal\.dotm)
- Обнаружение попыток изменить параметры надстроек Excel в реестре ОС Windows
- Обнаружение потенциальных попыток создать учетную запись при помощи командной строки или PowerShell (net user add) ".*(add-netuser|new-localuser|new-aduser).*"
- Попытка обойти вход в систему, используя особенности ОС Windows
- Обнаружение потенциальных попыток разместить Web Shell на веб-сервере Windows
- Обнаружение попыток изменить ключи реестра Windows, связанные с утилитой Windows "winlogon.exe"
- Обнаружение попыток изменить ветки реестра, отвечающие за запуск приложений специальных возможностей
- Обнаружение попыток изменить состав автозапуска ОС Windows
- Обнаружение попыток изменить заставку рабочего стола Windows
- Обнаружение попыток выполнить операции со службами Windows через командную строку или PowerShell
- Обнаружение попыток изменить состав подписок WMI 

«Перемещение внутри периметра»
- Обнаружение попыток создать и удалить запланированную задачу в течение короткого промежутка времени
- Обнаружение попыток удаленного доступа к административным ресурсам компьютера от имени учетных записей пользователей
- Обнаружение попыток доступа к сетевым ресурсам компьютера от имени учетных записей пользователей сразу после входа в систему
- Обнаружение попытки администратора безопасности удаленно войти на узел, не являющийся контроллером домена
- Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "certutil"
- Обнаружение использования DCOM
- Обнаружение попыток скопировать файлы через утилиту "expand"
- Обнаружение попыток скопировать файлы через утилиту "extrac32"
- Обнаружение попыток загрузить файлы через инструментарий Java
- Обнаружение попыток скопировать потенциально вредоносные файлы
- Обнаружение попыток создать потенциально вредоносные файлы
- Обнаружение попыток использовать Powershell remoting (WinRM) при удаленном выполнении команд
- Обнаружение попыток доступа к удаленным файловым ресурсам через PSEXEC
- Обнаружение попыток запустить утилиту "tscon" с повышенными привилегиями
- Обнаружение попыток удаленного создания запланированной задачи Windows при помощи встроенной утилиты Windows "atsvc"
- Обнаружение попыток удаленного создания запланированной задачи Windows при помощи встроенной утилиты Windows "schtasks"
- Обнаружение попытки удаленного входа на контроллер домена пользователя, не являющегося администратором безопасности
- Обнаружение попыток использовать Windows Remote Shell (WinRS) при удаленном выполнении команд
- Обнаружение попыток использовать утилиту администрирования Windows "WinExec" при удаленном выполнении команд
- Обнаружение попыток использовать WMI Remoting

Повышение привелегий
- Возможная попытка повысить привилегии учетной записи, загрузив вредоносную библиотеку
- Попытка пробросить сетевой порт
- Запуск приложения от имени другого пользователя
- Обнаружение подозрительного поведения встроенной утилиты Windows "spoolsv"
- Создан файл с образом ядра операционных систем семейства Windows NT "ntkrnlmp.exe"
- Обнаружение попыток создать интернет-соединение с потенциально опасными аргументами
- Запуск приложения от имени другого пользователя

Получение учётных данных
- Выполняется изменение параметров CredSSP чтобы использовать менее безопасные алгоритмы аутентификации
- Попытка получить учетные данные пользователей ОС
- Сохранение куста реестра, содержащего учетные данные пользователей ОС Windows
- Поиск групп и пользователей AD, у которых есть привилегии управления LAPS, а так же компьютеров-членов домена, на которых используется LAPS
- Поиск паролей с помощью командной строки или PowerShell
- Доступ к приложению и открытие сетевого соединения в течение 12 часов
- Сохранение информации процесса LSASS.exe через библиотеку comsvcs.dll
- Включение возможности просмотра паролей в открытом виде
- Процесс запросил доступ к ячейке 0х1fffff процесса LSASS.exe
- Процесс запросил доступ к процессу LSASS.exe
- Удаленный доступ к процессу LSASS.exe с маской доступа 0х1fffff
- Доступ к процессу LSASS.exe с последующим открытием сетевого соединения
- Удаленный доступ к SAMR, WINREG, SVCCTL и C:\Windows в течение 30 секунд после аутентификации
- Detect_Windows_Disable_LSA_Protection
- Запуск приложения с последующим открытием сетевого соединения в течение 12 часов
- Запуск приложения и открытие сетевого соединения в течение 12 часов 


Разведка
- Попытка получить список учетных записей
- Попытка получить список учетных записей через SAM-R
- Попытка получить список контроллеров домена
- Попытка получить список файлов и папок, существующих в системе
- Попытка получить список общих сетевых ресурсов узла
- Попытка получить политику паролей
- Попытка получить список прав групп пользователей
- Попытка просканировать определенные порты нескольких узлов
- Попытка получить список процессов, запущенных в системе
- Попытка выполнить запрос к реестру
- Попытка получить список установленных приложений
- Попытка получить информацию о конфигурации сети
- Попытка получить список установленных служб
- Попытка получить список доверенных доменов
- Выгрузка объектов типа "компьютер" из Active Directory
- Выгрузка объектов типа "пользователь" из Active Directory
- Выгрузка объектов типа "сервис" из Active Directory
- Удаленный доступ к файлу PST в течение 30 секунд после аутентификации
- Обнаружение попыток сделать теневую копию информации, скопированной в буфер обмена
- Обнаружение попыток сделать теневую копию информации, скопированной в буфер обмена, через PowerShell
- Обнаружение попыток безвозвратно удалить данные или часть данных на жестком диске
- Обнаружение попыток выгрузить файлы PST при помощи консоли Excahnge и удалить данные об этом
- Обнаружение попыток заблокировать доступ к учетной записи, значимой для ИБ
- Обнаружение попыток удалить учетную запись из группы, значимой для ИБ
- Обнаружение попыток удалить теневые копии данных, необходимых для восстановления Windows
- Обнаружение попыток сделать скрытый снимок экрана
- Обнаружение попыток сделать множество скрытых снимков экрана через PowerShell
- Работа с офисными документами через cmd.exe или PowerShell
- Обнаружение попыток остановить важную службу
- Обнаружение попыток получить доступ к объекту удаленной файловой системы с путем по маске "C:\Users\*"

https://docs.microsoft.com/ru-ru/windows/security/threat-protection/auditing/event-4689
https://docs.microsoft.com/ru-ru/windows/security/threat-protection/auditing/event-4688
Нажмите Win+ Rи введите gpedit.msc, чтобы открыть диспетчер групповой политики.
На левой панели перейдите к

Политика локального компьютера \ Конфигурация компьютера \ Параметры Windows \ Параметры безопасности \ Локальные политики \ Политика аудита

На правой панели дважды щелкните «Аудит отслеживания процессов» и установите оба флажка.

https://docs.microsoft.com/ru-ru/windows/security/threat-protection/auditing/event-5024
https://docs.microsoft.com/ru-ru/windows/security/threat-protection/auditing/event-5025
https://docs.microsoft.com/ru-ru/windows/security/threat-protection/auditing/event-5031
https://docs.microsoft.com/ru-ru/windows/security/threat-protection/auditing/event-5032
https://docs.microsoft.com/ru-ru/windows/security/threat-protection/auditing/event-5033
https://docs.microsoft.com/ru-ru/windows/security/threat-protection/auditing/event-5034
