#coding:utf-8
code="X<cP[?PHNB<P?aj"
num=15
anw=''
for i in code:
    anw += chr(ord(i)^num)
print anw