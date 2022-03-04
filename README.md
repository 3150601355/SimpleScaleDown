# 图像缩放攻击：图片缩小后变成另一张图
这是我一个视频的配套代码，视频链接：
https://www.bilibili.com/video/BV1Lf4y1r7dZ

配套代码中，**仅generate.py是核心文件**，其余的图片神马的，都是赠品。
这个核心文件利用了近邻法缩放的弱点，可以将图a的像素按顺序嵌入到图b中，然后生成图c。图c看起来和图b是基本一样的。不过，在PS软件或者python的PIL模块中使用近邻法把图c缩小到图a的尺寸时，图a就显示出来了。算是一种形式的“幻影坦克”吧。

# 使用方法：
假设generate.py、图a、b都在同一目录下，且均为png格式。

```python generate.py a.png b.png out.png```

回车后即可生成out.png
