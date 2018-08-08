#### 图片隐写题
##### 使用binwalk将图片分解。
```
PS F:\Desktop\CTF做题记录\5.32> binwalk .\1.png
* suggest: you'd better to input the parameters enclosed in double quotes.
* made by pcat

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 296 x 300, 8-bit/color RGBA, non-interlaced
2861          0xB2D           Zlib compressed data, compressed
44378         0xAD5A          Zip archive data, encrypted at least v2.0 to extract, compressed size: 58, uncompressed size: 47, name: flag.txt
44564         0xAE14          End of Zip archive, footer length: 22
```

##### 可以发现有zip压缩包，分解后发现zip压缩包需要密码。
##### 想到图片中出现字符串“oNFlag”,尝试用这个做密码，得到答案
```
zjctf{4ddc4ca5af8ac2aebd1a44d152eec5aec19a8f44}
```