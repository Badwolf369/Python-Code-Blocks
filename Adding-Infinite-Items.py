#place this directly after imports

data = []
prompt = '-->:'
confirmCommand = 'CONFIRM'

#----------------------------------------------------------------------------------------#
#place this near the beginning

def request(inp):
    if(inp!=confirmCommand):
        try:
            i = int(inp)
        except:
            print('Please input numbers or "'+confirmCommand+'" to calculate.')
            return 0
        else:
            data.append(i)
            return 1
    else:
        return confirmCommand

#------------------------------------------------------------------------------------------#
#place this where you want the promts to begin

print('Please input numbers to be added together.') 
print('Use the command '+confirmCommand+'to add items together.')

while True:
    x = request(input(prompt))
    if x == confirmCommand:
        print('You ran the "'+confirmCommand+'" command, enter again to continue.') 
        y = input(prompt)
        if y==confirmCommand:
            break

#------------------------------------------------------------------------------------------#
#place where you would like the given prompts to be added
    
n=0  
for a in data:
    n += a
    
#n equals the sum of the items added
