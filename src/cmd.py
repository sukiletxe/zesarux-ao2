import argparse
parser = argparse.ArgumentParser(prog = "Screen reader filter for ZEsarUX")
parser.add_argument("file",  help ="Specifies the input file")
parser.add_argument("--sapi", nargs = '?', type = int, const = -1, default = 0, help = "If present and blank, a menu will be displayed to choose the SAPI5 voice used by the emulator; if present with a number, the emulator will use the voice corresponding to that number; and if absent, the program will try to detect your screen reader.")
args = parser.parse_args()
