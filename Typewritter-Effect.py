from time import sleep

def write(text):
    for c in text:
        print(c, end='', flush=True)
        sleep(0.15)
    print('')
   
write('Hello World!')
