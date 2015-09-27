::set /p apkpath=please input apk path:
::java -jar apktool.jar d -f %apkpath%
::cd /d %~dp1
::set outdir=%~n1
::md %outdir%
::cd /d %~dp0
java -jar smali.jar -a 16 -o %~dp1%~n1.dex %~dp1%~n1
pause