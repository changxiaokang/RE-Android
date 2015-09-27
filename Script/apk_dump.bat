@echo off
::aapt dump badging %1 | find "launchable-activity"
aapt dump badging %1 | find "package"
aapt dump badging %1 | find "launchable-activity"
pause