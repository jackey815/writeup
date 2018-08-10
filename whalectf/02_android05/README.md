#### writeup
##### 使用JEB打开。查看MainActivity类，发现一个逻辑关系。
```
 PackageInfo v2 = MainActivity.this.getPackageManager().getPackageInfo("com.example.yaphetshan.tencentgreat", 16384);
                    String v3 = v2.versionName;
                    int v4 = v2.versionCode;
                    int v0 = 0;
                    while(v0 < v1.length()) {
                        if(v0 >= v3.length()) {
                            break;
                        }

                        if(v1.charAt(v0) != (v3.charAt(v0) ^ v4)) {
                            Toast.makeText(MainActivity.this, "再接再厉，加油~", 1).show();
                            return;
                        }
                        else {
                            ++v0;
                            continue;
                        }
                    }

                    if(v1.length() != v3.length()) {
                        goto label_39;
                    }

                    Toast.makeText(MainActivity.this, "恭喜开启闯关之门！", 1).show();
                    return;
```
##### 逻辑很简单，使用v2.versionName与v2.versionCode相异或即可得到答案。在BuildConfig中可以找到字符串。
```
   public static final int VERSION_CODE = 15;
   public static final String VERSION_NAME = "X<cP[?PHNB<P?aj";

```
##### 使用python异或下字符串得到答案：flag{W3l_T0_GAM3_0ne}
```
#coding:utf-8
code="X<cP[?PHNB<P?aj"
num=15
anw=''
for i in code:
    anw += chr(ord(i)^num)
print anw
```