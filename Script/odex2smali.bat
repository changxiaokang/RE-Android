::set /p apkpath=please input apk path:
::java -jar apktool.jar d -f %apkpath%
::cd /d %~dp1
::set outdir=%~n1
::md %outdir%
::cd /d %~dp0
java -jar baksmali.jar -a 16 -x  %1 -d %~dp1 -o %~dp1De_%~n1
pause