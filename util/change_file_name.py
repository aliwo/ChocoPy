import os
from glob import glob

for number, filename in enumerate(glob(r'C:\Users\aliwo\Downloads\logo\*.png')):
    print(number, filename)
    os.rename(filename, '{0:02d}.png'.format(number))
