from time import sleep
from random import *

def write(text):
    for c in text:
        print(c, end='', flush=True)
        sleep(uniform(0.2, 0.1))
    print('')
   
write('Hello World!')
