#place this directly after imports

data = []
prompt = '-->:'
confirmCommand = 'done'

#----------------------------------------------------------------------------------------#
#place this near the beginning

#this makes sure you get the correct inputs
def request(inp):
    if(inp!=confirmCommand):
        try:
            #test for correct input
        except:
            print('Please input correct inputs or "'+confirmCommand+'" to calculate.')
            return 0
        else:
            data.append(i)
            return 1
    else:
        return confirmCommand

#------------------------------------------------------------------------------------------#
#place this where you want the promts to begin

#place beginning dialogue here

#this runs the prompts and tests to see if you said to finish
while True:
    x = request(input(prompt))
    if x == confirmCommand:
        print('You ran the "'+confirmCommand+'" command, enter again to continue.') 
        y = input(prompt)
        if y==confirmCommand:
            break

#data[] now holds all the prompts
#run this block of code every time you wish to enter more inputs
