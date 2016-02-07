adb push %1 /data/local/tmp
::adb shell chmod 777 /data/local/tmp/%~nx1
::adb shell /data/local/tmp/android_server
pause