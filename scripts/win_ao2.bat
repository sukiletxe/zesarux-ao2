echo off

rem important use %1 and %2 without "". The "" are already sent by the emulator
zesarux-ao2/zesarux-ao2.exe %1 %2
rem Tell speech finished
del %2
