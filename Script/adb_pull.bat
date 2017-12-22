adb pull /data/local/tmp/log.txt %1
::adb shell chmod 777 /data/local/tmp/%~nx1
::adb shell /data/local/tmp/android_server
pause