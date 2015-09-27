#[ApkTool + Eclipse 调试 APK]
##1、反编译apk为java代码(加-d参数反编译后为java)
   java -jar apktool.jar d -d LINE.apk -o out_

##2、在AndroidManifest.xml中设置调试标记
   在application节点设置属性android:debuggable=”true”

##3、在Activity的入口OnCreate方法前插入调试点
   a=0;//     invoke-static {}, Landroid/os/Debug;->waitForDebugger()V

##4、对反编译后的java代码重新打包
   java -jar apktool.jar b -d out_ -o outdebug.apk

##5、通过signapk签名
   java -jar signapk.jar PubKey.pem PriKey.pk8 outdebug.apk outnew.apk

##6、通过adb shell 启动程序进入等待调试状态
   adb shell am start -D -W -n jp.naver.line.android/.activity.SplashActivity

##7、添加反编译后的java工程到Eclipse中并下好断点
   del build/apktool.yml -> create java project -> 
   load out_文件 -> next -> 修改smali为src

##8、模拟器安装签名后apk在DDMS中查看调试端口

##9、配置远程调试关联反编译后的JAVA代码和调试程序
