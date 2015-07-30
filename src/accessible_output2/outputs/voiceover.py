from __future__ import absolute_import
from __builtin__ import str
import subprocess, os
from .base import Output

class VoiceOver(Output):
 """Speech output supporting the Apple VoiceOver screen reader."""
 def runAppleScript(self, command, process = 'voiceover'):
  return subprocess.Popen(['osascript', '-e', 'tell application "' + process + '"\n' + command + '\nend tell'], stdout = subprocess.PIPE).communicate()[0]
 name = 'VoiceOver'
 def speak(self, text, interrupt=0):
  if interrupt:
   self.silence()
  os.system('osascript -e \"tell application \\\"voiceover\\\" to output \\\"%s\\\"\" &' % text)
 def silence (self):
  self.runAppleScript('output ""')
 def is_active(self):
  return self.runAppleScript('return (name of processes) contains "VoiceOver"', 'system events').startswith('true') and not self.runAppleScript('try\nreturn bounds of vo cursor\non error\nreturn false\nend try').startswith('false')

output_class = VoiceOver
