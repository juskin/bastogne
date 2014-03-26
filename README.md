# Bastogne

高清电影下载站
---


所有数据采集自imax.im和互联网，仅供学习研究之用。



## 数据获取：

测试数据可用 `mongoimport` 从data目录 导入 MongoDB。



## 项目依赖：

* MongoDB
* tornado
* pymongo



## 演示站点: [bastogne](http://bastogne.chinacloudapp.cn)

目前部署在windows azure的小型虚拟机上

* 架构：Linux(ubuntu) + nginx + MongoDB + Python3


## api

通过title参数获取电影信息

http://bastogne.chinacloudapp.cn/api/movie?title=阿甘正传


## 已知问题

由于没有合适的地方存放图片，只是直接贴豆瓣的图片，部分图片由于访问限制无法正常显示。
可以参考tool/image_download.py 将图片下载到本地存储



## TODO

* 直接根据豆瓣id添加新的电影条目
* 同步豆瓣电影评论