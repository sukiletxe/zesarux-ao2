import cmd, os, sys
import tts, time
import fix_win32com
    if hasattr(sys, "frozen"):
        fix_win32com.fix()
def main():
    tts.set_output(cmd.args.sapi)
    with open(cmd.args.file) as f1:
        for line in f1:
            tts.speak(line, False)
                while True:
                    if tts.get_output().name == "sapi5" and tts.is_speaking:
                        time.sleep(0.05)
                    else:
                        break
main()
