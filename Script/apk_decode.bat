::set /p apkpath=please input apk path:
::java -jar apktool.jar d -f %apkpath%
::cd /d %~dp1
::set outdir=%~n1
::md %outdir%
::cd /d %~dp0

::Դ�뷴��������java�ļ�
java -jar apktool.jar d -d %1 -o "%~dp1De_%~n1"

::�������smali�ļ�
::java -jar apktool.jar d -f %1 -o "%~dp1De_%~n1"
pause