import cmd, platform, sys
import tts, time
if platform.system() == 'Windows':
    import fix_win32com
    if hasattr(sys, "frozen"):
        fix_win32com.fix()
tts.set_output(cmd.args.sapi)
if platform.system() == 'Windows':
    with open(cmd.args.file) as f1:
        for line in f1:
            tts.speak(line, True)
else:
    tts.speak(cmd.args.text, False)
