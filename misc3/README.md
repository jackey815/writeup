# writeup
#### 3、LASS文件解密。
参考[：https://blog.csdn.net/yiyefangzhou24/article/details/11760277?_t_t_t=0.25886626888210196](https://blog.csdn.net/yiyefangzhou24/article/details/11760277?_t_t_t=0.25886626888210196)
##### 使用工具mimikatz
dump文件和mimikatz的版本对应关系，对应关系如图：
![image](https://github.com/jackey815/writeup/blob/master/misc3/对应表.PNG)

将文件拷入到xp x86机子，使用命令
```
mimikatz # sekurlsa::minidump lsass.dmp  
Switch to MINIDUMP  
mimikatz # sekurlsa::logonPasswords full  
```
得到结果：
```
mimikatz # sekurlsa::minidump LSASS.DUMP
Switch to MINIDUMP : 'LSASS.DUMP'

mimikatz # sekurlsa::logonPasswords full
Opening : 'LSASS.DUMP' file for minidump...

Authentication Id : 0 ; 984524 (00000000:000f05cc)
Session           : Interactive from 0
User Name         : Administrator
Domain            : EF3D-A3A4CBDD6
Logon Server      : EF3D-A3A4CBDD6
Logon Time        : 2018-6-15 1:06:50
SID               : S-1-5-21-796489640-1449036476-780432832-500
        msv :
         [00000002] Primary
         * Username : Administrator
         * Domain   : EF3D-A3A4CBDD6
         * NTLM     : 771aad64f9064f2e599db78ce83ee7ea
         * SHA1     : 7cff826bf8d6b80d1fbffb412fabe3d2cc851bd7
        wdigest :
         * Username : Administrator
         * Domain   : EF3D-A3A4CBDD6
         * Password : 60E90BDC0A723F11
```
```
KEY:60E90BDC0A723F11
```