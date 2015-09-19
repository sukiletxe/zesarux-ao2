import shutil, compileall, os, os.path
compileall.compile_dir(os.path.curdir, quiet = 1)
shutil.copytree(os.path.curdir, 'mac', ignore = shutil.ignore_patterns('*.py', 'windows_vc++', 'fix_win*', 'setup*'))
os.chdir('mac')
os.rename('main.pyc', 'zesarux-ao2.pyc')
os.chdir('../..')
files = ['license.txt', 'readme.html']
for file in files:
    shutil.copy2(file, 'src/mac')
scripts = []
shutil.copytree('scripts', 'src/mac/scripts')
