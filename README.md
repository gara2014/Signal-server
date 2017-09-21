# 基于WebRtc实现多人视频会议的信令服务器
## 背景说明
* WebRTC，名称源自网页实时通信（Web Real-Time Communication）的缩写，是一个支持网页浏览器进行实时语音对话或视频对话的技术，是谷歌2010年以6820万美元收购Global IP Solutions公司而获得的一项技术。2011年5月开放了工程的源代码，在行业内得到了广泛的支持和应用，成为下一代视频通话的标准。<br><br>
* WebRTC提供了视频会议的核心技术，包括音视频的采集、编解码、网络传输、显示等功能，并且还支持跨平台：windows，linux，mac，android。<br><br>
* Native方面，GitHub上只看到使用WebRTC实现P2P视频通话的Demo，本项目是利用WebRTC实现了多人视频会议的Demo<br>

## 部署步骤
1、安装Python 2.7， Django<br>
2、安装mysql<br>
3、新建数据库signal1(最好能支持中文字符)<br>
4、在settings.py中ALLOWED_HOSTS字段添加本机IP<br>
5、在settings.py中DATABASES字段中配置数据库用户名，密码等信息<br>
6、启动服务，命令行中输入：python manage.py runserver 0.0.0.0:8080<br>
7、修改Client端代码中的RoomSignalClient.SignalUrl的IP和端口<br>

## 相关项目地址
iOS：https://github.com/gara2014/Multiplayer-video-using-webrtc<br>
Android：https://github.com/gara2014/Multiplayer-video-using-webrtc-android

## 开发环境
Python 2.7, Django部署

## WebRTC官方地址
https://webrtc.org
