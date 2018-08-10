#### writeup
#####　打开数据包后发现全是802.11协议的数据包，需要对其包进行解码。
![image](https://github.com/jackey815/writeup/blob/master/whalectf/A记录/1.PNG)
##### 使用kali里的aircrack-ng进行解密。
```
aircrack-ng -w top1500.txt shipin.cap
```
##### 得到密码 8888888 ESID为0719
![image](https://github.com/jackey815/writeup/blob/master/whalectf/A记录/2.PNG)
##### 解密数据包
```
airdecap-ng shipin.cap -e 0719 -p 88888888
```
##### 得到shipin-dec.cap，打开后发现网址。
![image](https://github.com/jackey815/writeup/blob/master/whalectf/A记录/3.PNG)

##### key为ctf{push.m.youku.com}