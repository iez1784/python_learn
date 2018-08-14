#!C:\Python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'athena==2.1.7','console_scripts','athena'
__requires__ = 'athena==2.1.7'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('athena==2.1.7', 'console_scripts', 'athena')()
    )
