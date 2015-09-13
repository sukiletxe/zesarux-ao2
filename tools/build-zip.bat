pushd ..\src
set /p version= <version.txt
python setup.py py2exe
rd /s /q build
ren dist zesarux-ao2
7z a zesarux-ao2-%version%-win.zip zesarux-ao2\ -r -tzip
rd /s /q zesarux-ao2
popd
