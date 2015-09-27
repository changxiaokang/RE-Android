::set /p saveapk=please save apk:
::java -jar apktool.jar b -f %saveapk% -o %saveapk%\ok.apk
::Ô´Âë±àÒë
java -jar apktool.jar b -d %1 -o "%~dp1%~n1.apk"
::±àÒësmali
::java -jar apktool.jar b -f %1 -o "%~dp1%~n1.apk"

pause