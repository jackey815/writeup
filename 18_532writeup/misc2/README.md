#### 流量分析题
##### 使用wireshark打开流量包
##### 大致浏览后发现是FTP爆破的过程。找到爆破成功的数据包。选择ftp的包数据，并找到爆破成功的ftp包。
![image](https://github.com/jackey815/writeup/blob/master/18_532writeup/misc2/1.PNG)
##### 浏览前后可以发现下载了football.rar，提取出文件后发现需要密码。
![image](https://github.com/jackey815/writeup/blob/master/18_532writeup/misc2/2.PNG)
##### 发现了后面又下载了tmp.txt，想到里面是不是会有密码。找到对应的数据包，发现密码在后面。
![image](https://github.com/jackey815/writeup/blob/master/18_532writeup/misc2/3.PNG)
