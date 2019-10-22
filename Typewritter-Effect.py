import sys

def write(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.15)
    print('')
   
write('Hello World!')
