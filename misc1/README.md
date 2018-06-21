# writeup
#### 1、加解密1 

```
=E4=B8=89=E5=B8=9D=E4=BA=94=E5=B8=81=E4=B8=83=E6=98=93=E6=81=A9=E5=85=AD
=E5=93=A6=E8=BE=9F=E6=9B=BF=E4=BC=98=E5=85=AB=E5=BE=AE=E5=A4=96=E4=B9=9D
```
Quoted-printable 编码

```
#-*- encoding: utf-8 -*-
import quopri
print quopri.decodestring("=E4=B8=89=E5=B8=9D=E4=BA=94=E5=B8=81=E4=B8=83=E6=98=93=E6=81=A9=E5=85=AD=E5=93=A6=E8=BE=9F=E6=9B=BF=E4=BC=98=E5=85=AB=E5=BE=AE=E5=A4=96=E4=B9=9D")
```
结果为：

```
三帝五币七易恩六哦辟替优八微外九
```
翻译为：

```
3d5b7en6optu8vy9
