#!C:\Users\natha\anaconda3\envs\Generator\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pymclevel==0.1','console_scripts','mce.py'
__requires__ = 'pymclevel==0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pymclevel==0.1', 'console_scripts', 'mce.py')()
    )
