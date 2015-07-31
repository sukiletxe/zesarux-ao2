from  setuptools import setup, find_packages
import py2exe
import platform
from glob import glob
import accessible_output2
def get_data():
  if platform.architecture()[0][:2] == "32":
   return [
   ("Microsoft.VC90.CRT", glob("windows_vc++/msvc32/Microsoft.VC90.CRT/*")),
   ("Microsoft.VC90.MFC", glob("windows_vc++/msvc32/Microsoft.VC90.MFC/*")),]
  elif platform.architecture()[0][:2] == "64":
   return [
   ("Microsoft.VC90.CRT", glob("windows_vc++/msvc64/Microsoft.VC90.CRT/*")),
   ("Microsoft.VC90.MFC", glob("windows_vc++/msvc64/Microsoft.VC90.MFC/*")),]

setup(
    name = "ZEsarUX Ao2",
    author = "Sukil Etxenike",
    author_email = "sukiletxe@yahoo.es",
    version = "1.1",
    data_files= get_data() + [("", ['../readme.html'])] + accessible_output2.find_datafiles(),
    packages = find_packages(),
    options = {
        "py2exe":{
            "optimize": 2,
            "dll_excludes": ["CRYPT32.dll"],
            "compressed": True,
        }
    },  
    console=[{
        'script': 'main.py',
        'dest_base': 'zesarux-ao2'}],
)