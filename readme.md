# ZEsarUX AO2


## Introduction
ZEsarUX AO2 is a program which can interact with many Windows screen readers, Microsoft SAPI 5 and VoiceOver in Mac. As its name suggests, it was thought to be used with [ZEsarUX](http://sourceforge.net/projects/zesarux) although it has more uses.

## Usage
In Windows, it gets a filename as input, and it reads it outloud. In Mac, it gets the text to be read. If you are using Windows and if you specify --sapi, a menu will be opened for you to choose the voice to be used. You can also append a number to the option to use the voice corresponding to that menu item directly.

## License and source code
This program is available under the GNU General Public License version 2, or, at your option, any later version.
The source code of the program is available at <http://github.com/sukiletxe/zesarux-ao2>.

## Running from source and building a binary
To run from source, you will need:
* Python (I use version 2.7.10)
* [Python for Windows Extensions](http://sourceforge.net/projects/pywin32/)
* [Pandoc](http://pandoc.org) to build the readme.

You will need py2exe to make a compiled Windows executable. Also, to make the compiled executable run properly, you will need to delete the gen_py folder of the win32com package, usually found at C:\Python27\Lib\site-packages\win32com.

## Aknowledgements
This program uses accessible_output2 (with an extra function to see if SAPI5 is speaking or not), Libloader and Platform_utils by [Tyler Spivey and Christopher Toth](http://q-continuum.net).
