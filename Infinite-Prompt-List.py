#place this directly after imports

data = []
prompt = '-->:'
confirmCommand = 'done'

#----------------------------------------------------------------------------------------#
#place this during function definitions; near the beginning

#this makes sure you get the correct inputs
def request(inp):
    if(inp!=confirmCommand):
        try:
            #test for correct input
            if():
               raise Exception()
        except:
            print('Error message')
        else:
            data.append(inp)
    else:
        return confirmCommand

#------------------------------------------------------------------------------------------#
#place this where you want the promts to begin
#run this block of code every time you wish to enter more inputs

#place beginning dialogue here

#this runs the prompts and tests to see if you said to finish
while True:
    x = request(input(prompt))
    if x == confirmCommand:
        print('You ran the "'+confirmCommand+'" command, enter again to save.') 
        y = input(prompt)
        if y==confirmCommand:
            break

#data[] now holds all the prompts
