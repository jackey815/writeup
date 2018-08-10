#coding:utf-8
import base64

a=[97, 72, 82, 48, 99, 68, 111, 118, 76, 122, 81, 49, 76, 106, 77, 121, 76, 106, 81, 51, 76, 106, 107, 52]
b=''.join(map(chr,a))
print base64.b64decode(b)
