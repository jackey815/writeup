#### writeup
##### 使用JEB打开是个比较复杂的APK程序。先用模拟器打开看看，是个北极熊打南极企鹅的游戏= =！题目要求最后的提交分数页面要全部是20000。
![image](https://github.com/jackey815/writeup/blob/master/whalectf/android09/1.PNG)
##### 在模拟器中找到关于得分的类。发现一段奇特代码。
```
  public double getScore() {
        double v0;
        if(Score.GET_SCORE_FLAG == 11) {
            v0 = this.getvalue();
        }
        else if(Score.GET_SCORE_FLAG == 31) {
            v0 = this.getScoreReal();
        }
        else {
            v0 = -1;
        }

        return v0;
    }

    public double getScoreReal() {
        return this._score;
    }

    public String getUserName() {
        return this._userName;
    }

    public double getvalue() {
        return 20000;
    }

```
##### 当变量Score.GET_SCORE_FLAG==11时，得到的分数为固定值20000
##### 利用改之理尝试下。改变Score.GET_SCORE_FLAG初始赋值为0xb。
![image](https://github.com/jackey815/writeup/blob/master/whalectf/android09/2.PNG)
##### 运行后得到结果。
![image](https://github.com/jackey815/writeup/blob/master/whalectf/android09/3.PNG)
##### 根据题目描述得到flag{11}