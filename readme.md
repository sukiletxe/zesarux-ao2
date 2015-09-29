# ZEsarUX AO2

## Introduction
ZEsarUX AO2 is a program which can interact with many Windows screen readers, Microsoft SAPI 5 and VoiceOver in Mac. As its name suggests, it was thought to be used as a text to speech program with [ZEsarUX](http://sourceforge.net/projects/zesarux) although it  may have more uses.

Note that this was thought to be an added convenience, as ZEsarUX itself includes scripts to be used with eSpeak, Jampal and Balabolka in Windows and Say in Mac.

## License and source code
This program is available under the GNU General Public License version 2, or, at your option, any later version. See the included license.txt file or <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>.
The source code of the program is available at <http://github.com/sukiletxe/zesarux-ao2>.

## Usage with ZEsarUX
In Mac, before using the program, you will need to open the VoiceOver utility by pressing VO+F8, and in the general tab, check the checkbox to allow VoiceOver to be controlled with AppleScript. After enabling this setting, you can proceed following the instructions of the next paragraphs.

Assuming you have the program (compiled in   Windows, in source code form in Mac) in the speech_filters folder of ZEsarUX, you can copy the contents of the folder called `scripts` to that same folder. 
To run it with ZEsarUX, you should specify `--textspeechprogram speech_filters\win_ao2.bat` in  Windows, or `--textspeechprogram macos_ao2.sh` in  Mac.
In Windows, if you are using a screen reader (tested with JAWS and NVDA) you don't need to specify a script to stop speech when a key is pressed. In other cases, you need to specify `--textspeechstopprogram win_ao2.bat`in Windows, and `--textspeechstopprogram macos_ao2.sh`in Mac.

Some parameters you may wish to change:
* Windows: By default, the  program uses your screen reader or SAPI5 if no screen reader is detected. To use SAPI5 even if a screen reader is running, append `--sapi` plus a number (for example `--sapi 1`) to the third non-empty line of the batch file which calls the program. The number represents a SAPI voice, starting from 1 (the default one). To get a list of voices with their numbers, run the program by itself and specify a filename to read and `--sapi` without any number.
* Mac: If you see a significant delay between some messages, or that the messages are being interrupted, you can specify --wait plus a number. Append this parameter to the  last line of the shell script calling the program. This is the number of seconds to wait for each  character in the text to speak. The default value is 0.2. 

## Running from source and building a binary
To run from source, you will need:
* Python (I use version 2.7.10)
* [Python for Windows Extensions](http://sourceforge.net/projects/pywin32/)
* [Pandoc](http://pandoc.org) to build the readme.
* [7-zip](http://www.7-zip.org) to use the build script to zip the Windows executable.

You will need py2exe to make a compiled Windows executable. Also, to make the compiled executable run properly, you will need to delete the gen_py folder of the win32com package, usually found at C:\Python27\Lib\site-packages\win32com.

## Aknowledgements
This program uses accessible_output2 (with an extra function to see if SAPI5 is speaking or not), Libloader and Platform_utils by [Tyler Spivey and Christopher Toth](http://q-continuum.net).
