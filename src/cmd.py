import argparse, platform
parser = argparse.ArgumentParser(prog = "Screen reader filter for ZEsarUX")
if platform.system() == 'Windows':
    parser.add_argument("file",  help ="Specifies the input file.")
    parser.add_argument("--sapi", nargs = '?', type = int, const = -1, default = 0, help = "If present and blank, a menu will be displayed to choose the SAPI5 voice used by the emulator; if present with a number, the emulator will use the voice corresponding to that number; and if absent, the program will try to detect your screen reader.")
else:
    parser.add_argument("text", help = "Specifies the text to be spoken.")
    parser.add_argument("--wait", help="Specifies the time to wait between program cycles. Decrease it if messages are interrupted, increase it if the delay is too long between messages. Default is 0.2.", type=float, default=0.2)
args = parser.parse_args()
