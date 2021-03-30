AD
1 Mimikatz скопирован в административную сетевую папку
2 Выгрузка активных пользовательских сеансов на узле
3 Неавторизованная репликация DC
4 Запущен процесс, обычно используемый для выгрузки активных пользовательских сеансов (типа sysmon)
5 Попытка выгрузки локальных групп или членов группы локальных администраторов на контроллере домена или узле
6 Попытка выгрузки списка групп домена на узле или контроллере домена
7 Session_enumeration_smb


«Выполнение» и «Предотвращение обнаружения»
8 Обнаружение попыток обойти контроль учетных записей или запрет на запуск приложения при помощи встроенной утилиты Windows "cmstp"
9 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "control"
10 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "csc"
11 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "InstallUtil"
12 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows .NET "MSBuild.exe"
13 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "RegAsm"
14 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "regsvr32"
15 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "rundll32"
16 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенных утилит Windows "cscript" и "wscript"
17 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "dnscmd"
18 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "mavinject"
19 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "msiexec"
20 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "msxsl"
21 Обнаружение попыток обойти запрет на запуск приложений при помощи утилиты Windows "odbcconf", позволяющей настраивать Open Database Connectivity (ODBC)
22 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "pcalua"
23 Обнаружение попыток загрузить или запустить приложения при помощи встроенной утилиты Windows "bitsadmin"
24 Пользователь попытался выполнить скрипт (bat|ps1|cmd|vbs|js|psd1|psm1|ps1xml|wsf|vbe|wsc)
25 Открыт потенциально опасный файл справки hh.exe 
26 Попытка выполнить потенциально опасную команду ("shellcode|-lhost|reverse_|bind_|remove-|psexec|base64|iconv|webclient|webreguest|winhttp|url=|encodedcommand|powerview|powerup|recon|scrnsavebackdoor|regbackdoor|dns_txt|pwnage|backdoor|adsbackdoor|remotepsremoting|remotewmi|amsibypass|lsasecret|listener|passhashes|mimikatz|wdigestdowngrade|adsbackdoor|remotepsremoting|remotewmi|amsibypass|interceptor|nisnag|powerpreter|bruteforce|portscan|psgcat|persistence|remotewmi|amsibypass|antivirusbypass|avsignature|codeexecution|dllinjection|powersploit|gpppassword|minidump|shadowcopy|privesc|llmnresponse|nbnsresponse|inveigh|internetexplorer|serverxmlhttp|mshta.*?http|mshta.*?ftp|dcsync|keystrokes|timedscreenshot|vaultcredential|credentialinjection|ninjacopy|tokenmanipulation|volumeshadowcopy|reflectivepeinjection|userhunter|gpolocation|aclscanner|downgradeaccount|serviceunquoted|servicefilepermission|servicepermission|serviceabuse|servicebinary|regautologon|vulnautorun|vulnschtask|unattendedinstallfile|duplicatetoken|psuacme|targetscreen|poshrathttp|powershellwmi|exfiltration|captureserver|chromedump|foxdump|indexeditem|screenshot|netripper|egresscheck|postexfil|psinject|runas|powerdump|sshcommand|backdoorlnk|bypassuac|wscriptbypassuac|paranoia|winenum|arpscan|reversednslookup|smbscanner|mimikittenz|volumeshadowcopytools|regalwaysinstallelevated|port-scan|powershelltcp|clipboardcontents|install-ssp|powerbreach|invoke-tater|phant0m|-noni|-noninteractive|-enc|-nol\s+|non\s+|invoke-|bypass|hidden|downloadfile|downloadstring|nop\s+|-noprofile|executionpolicy|iex\s+|reflectedpeinjection|new-object|paexec|xcopy|sdelete|plink|nping|nmap|ncat\.exe|ncat\s+|-p\s+22|:3389|vssadmin|ftp\s+|ftp\.exe|taskkill|robocopy|copy-item|schtask\s+|^at\s+|at\.exe|mofcomp|wevtutil|vnc|cpassword|pskill|winscp|wmic|psexesvc|-ma\s+lsass\.exe|wmic.*?http|wmic.*?ftp|cmdkey\s+/list|cmd.*?/k.*?<.*?\.txt|ntds\.dit|copy.*?ntds\.dit|copy.*?config\\sam|reg\s+save.*?system|snapshot")
27 powershell|-noni|-noninteractive|-enc|-nol|non|invoke-|exec|bypass|hidden|downloadfile|downloadstring|payload|shellcode|-lhost|reverse_|bind_|remove-|psexec|psexesvc|winexesvc|base64|iconv|webclient|nop|-noprofile|executionpolicy|iex\s|reflectedpeinjection|new-object|webreguest|winhttp|url=|encodedcommand
28 Попытка управления задачами по расписанию через командную строку или PowerShell "schtasks.*?/(create|delete|run|query|change)"  "schtasks\s+/(create|delete|run|query|change)|register-scheduled|registertaskdefinition"
29 Detect_Sysmon_driver_unload "fltmc.exe", "unload.*?sysmondrv"
30 Обнаружение попыток загрузить или запустить приложение при помощи встроенной утилиты Windows "mshta" (".*(http|ftp|\.sct|getobject|\.txt.*\.hta|\.hta).*") 
31 Обнаружение попыток запустить потенциально опасный сценарий при помощи утилит, встроенных в Windows ["cmd.exe","powershell.exe","wscript.exe", "mshta.exe", "script.exe"]
32 Обнаружение попыток использовать утилиту "wmic" для совершения подозрительных действий (потенциальная атака путем бокового смещения (lateral movement attack)) "\s+/node|\s+/node:|process\s+call\s+create|\s+-w\s+>\s+"
33 Обнаружение попыток запустить сценарии XSL (eXtensible Stylesheet Language) при помощи утилиты "wmic" "wmic.*/format:.*\.xsl"
34 Обнаружение попытки запустить утилиту "cmd", встроенную в Windows, с потенциально опасными аргументами
35 Обнаружение попыток запусить утилиту администрирования PSEXEC и ее аналогов         "psexec*" "winexec*" "csexec*" "paexec*"
36 Подозрительная последовательность запуска процесса приложением Microsoft Office   and in_list(["winword.exe", "excel.exe", "powerpnt.exe", "visio.exe", "mspub.exe", "eqnedt32.exe", "mshta.exe", "outlook.exe"], lower(datafield4))  and in_list(["powershell.exe", "cmd.exe", "wmic.exe", "wscript.exe", "script.exe", "wmiprvse.exe", "sh.exe", "bash.exe", "scrcons.exe", "schtasks.exe", "regsvr32.exe", "hh.exe", "rundll32.exe", "msiexec.exe", "forfiles.exe", "scriptrunner.exe", "mftrace.exe", "appvlp.exe", "msbuild.exe", "mshta.exe"], lower(object name))
37 Обнаружение попыток установить новую службу не из системных каталогов Windows  "(c:\\\\programdata\\\\|c:\\\\program\s+files|\\\\systemroot\\\\system32\\\\|c:\\\\windows\\\\system32\\\\).*"


"Закрепление"
38 Обнаружение попыток создать локальную учетную запись
39 Обнаружение попыток создать и удалить учетную запись в течение короткого промежутка времени
40 Обнаружение попыток измененить ключ реестра "Image File Execution Options", чтобы встроить стороннее ПО в цепочку запуска
41 Обнаружение попыток изменить стандартный шаблон документов Microsoft Office (normal\.dotm)
42 Обнаружение попыток изменить параметры надстроек Excel в реестре ОС Windows
43 Обнаружение потенциальных попыток создать учетную запись при помощи командной строки или PowerShell (net user add) ".*(add-netuser|new-localuser|new-aduser).*"
44 Попытка обойти вход в систему, используя особенности ОС Windows
45 Обнаружение потенциальных попыток разместить Web Shell на веб-сервере Windows
46 Обнаружение попыток изменить ключи реестра Windows, связанные с утилитой Windows "winlogon.exe"
47 Обнаружение попыток изменить ветки реестра, отвечающие за запуск приложений специальных возможностей
48 Обнаружение попыток изменить состав автозапуска ОС Windows
49 Обнаружение попыток изменить заставку рабочего стола Windows
50 Обнаружение попыток выполнить операции со службами Windows через командную строку или PowerShell
51 Обнаружение попыток изменить состав подписок WMI 

«Перемещение внутри периметра»
52 Обнаружение попыток создать и удалить запланированную задачу в течение короткого промежутка времени
53 Обнаружение попыток удаленного доступа к административным ресурсам компьютера от имени учетных записей пользователей
54 Обнаружение попыток доступа к сетевым ресурсам компьютера от имени учетных записей пользователей сразу после входа в систему
55 Обнаружение попытки администратора безопасности удаленно войти на узел, не являющийся контроллером домена
56 Обнаружение попыток обойти запрет на запуск приложений при помощи встроенной утилиты Windows "certutil"
57 Обнаружение использования DCOM
58 Обнаружение попыток скопировать файлы через утилиту "expand"
59 Обнаружение попыток скопировать файлы через утилиту "extrac32"
60 Обнаружение попыток загрузить файлы через инструментарий Java
61 Обнаружение попыток скопировать потенциально вредоносные файлы
62 Обнаружение попыток создать потенциально вредоносные файлы
63 Обнаружение попыток использовать Powershell remoting (WinRM) при удаленном выполнении команд
64 Обнаружение попыток доступа к удаленным файловым ресурсам через PSEXEC
65 Обнаружение попыток запустить утилиту "tscon" с повышенными привилегиями
66 Обнаружение попыток удаленного создания запланированной задачи Windows при помощи встроенной утилиты Windows "atsvc"
67 Обнаружение попыток удаленного создания запланированной задачи Windows при помощи встроенной утилиты Windows "schtasks"
68 Обнаружение попытки удаленного входа на контроллер домена пользователя, не являющегося администратором безопасности
69 Обнаружение попыток использовать Windows Remote Shell (WinRS) при удаленном выполнении команд
70 Обнаружение попыток использовать утилиту администрирования Windows "WinExec" при удаленном выполнении команд
71 Обнаружение попыток использовать WMI Remoting

Повышение привелегий
72 Возможная попытка повысить привилегии учетной записи, загрузив вредоносную библиотеку
73 Попытка пробросить сетевой порт
74 Запуск приложения от имени другого пользователя
75 Обнаружение подозрительного поведения встроенной утилиты Windows "spoolsv"
76 Создан файл с образом ядра операционных систем семейства Windows NT "ntkrnlmp.exe"
77 Обнаружение попыток создать интернет-соединение с потенциально опасными аргументами
78 Запуск приложения от имени другого пользователя

Получение учётных данных
79 Выполняется изменение параметров CredSSP чтобы использовать менее безопасные алгоритмы аутентификации
80 Попытка получить учетные данные пользователей ОС
81 Сохранение куста реестра, содержащего учетные данные пользователей ОС Windows
82 Поиск групп и пользователей AD, у которых есть привилегии управления LAPS, а так же компьютеров-членов домена, на которых используется LAPS
83 Поиск паролей с помощью командной строки или PowerShell
84 Доступ к приложению и открытие сетевого соединения в течение 12 часов
85 Сохранение информации процесса LSASS.exe через библиотеку comsvcs.dll
86 Включение возможности просмотра паролей в открытом виде
87 Процесс запросил доступ к ячейке 0х1fffff процесса LSASS.exe
88 Процесс запросил доступ к процессу LSASS.exe
89 Удаленный доступ к процессу LSASS.exe с маской доступа 0х1fffff
90 Доступ к процессу LSASS.exe с последующим открытием сетевого соединения
91 Удаленный доступ к SAMR, WINREG, SVCCTL и C:\Windows в течение 30 секунд после аутентификации
92 Detect_Windows_Disable_LSA_Protection
93 Запуск приложения с последующим открытием сетевого соединения в течение 12 часов
94 Запуск приложения и открытие сетевого соединения в течение 12 часов 


Разведка
95 Попытка получить список учетных записей
96 Попытка получить список учетных записей через SAM-R
97 Попытка получить список контроллеров домена
98 Попытка получить список файлов и папок, существующих в системе
99 Попытка получить список общих сетевых ресурсов узла
100 Попытка получить политику паролей
101 Попытка получить список прав групп пользователей
102 Попытка просканировать определенные порты нескольких узлов
103 Попытка получить список процессов, запущенных в системе
104 Попытка выполнить запрос к реестру
105 Попытка получить список установленных приложений
106 Попытка получить информацию о конфигурации сети
107 Попытка получить список установленных служб
108 Попытка получить список доверенных доменов
109 Выгрузка объектов типа "компьютер" из Active Directory
110 Выгрузка объектов типа "пользователь" из Active Directory
111 Выгрузка объектов типа "сервис" из Active Directory
112 Удаленный доступ к файлу PST в течение 30 секунд после аутентификации
113 Обнаружение попыток сделать теневую копию информации, скопированной в буфер обмена
114 Обнаружение попыток сделать теневую копию информации, скопированной в буфер обмена, через PowerShell
115 Обнаружение попыток безвозвратно удалить данные или часть данных на жестком диске
116 Обнаружение попыток выгрузить файлы PST при помощи консоли Excahnge и удалить данные об этом
117 Обнаружение попыток заблокировать доступ к учетной записи, значимой для ИБ
118 Обнаружение попыток удалить учетную запись из группы, значимой для ИБ
119 Обнаружение попыток удалить теневые копии данных, необходимых для восстановления Windows
120 Обнаружение попыток сделать скрытый снимок экрана
121 Обнаружение попыток сделать множество скрытых снимков экрана через PowerShell
122 Работа с офисными документами через cmd.exe или PowerShell
123 Обнаружение попыток остановить важную службу
124 Обнаружение попыток получить доступ к объекту удаленной файловой системы с путем по маске "C:\Users\*"

