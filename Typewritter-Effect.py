from time import sleep
import random

#--------------------------------------------------------------#

def write(text):
    for c in text:
        print(c, end='', flush=True)
        sleep(uniform(0.2, 0.1))
    print('')
  
#--------------------------------------------------------------#

write('Hello World!')
