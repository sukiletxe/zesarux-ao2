import cmd, platform, sys
import tts, time
import fix_win32com
if hasattr(sys, "frozen"):
    fix_win32com.fix()
tts.set_output()
if platform.system() == 'Windows':
    with open(cmd.args.file) as f1:
        for line in f1:
            tts.speak(line, False)
            while True:
                if cmd.args.sapi != 0 and tts.is_speaking() == True:
                    time.sleep(0.05)
                else:
                    break
else:
    tts.speak(cmd.args.text, False)
