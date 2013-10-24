import sys
import os

def answer():
   global a
   print "Do you have XCode installed on your system? y/n/q"
   a = raw_input()

answer()

if a =='y':
   os.system('cd ~/Downloads/kith-master/')
   os.system('wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py')
   os.system('python ez_setup.py --user')
   os.system('cd')
   os.system('sudo easy_install pip')
   os.system('cd')
   os.system('sudo pip install -U selenium')
   os.system('cd')
   os.system('sudo pip install -e git+git://github.com/seatgeek/fuzzywuzzy.git#egg=fuzzywuzzy')

elif a =='n':
  print """Please install XCode from the Mac App Store, it is free.
https://developer.apple.com/support/xcode/"""

elif a=='q':
  pass

else:
   answer()
