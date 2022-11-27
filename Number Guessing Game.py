import random

'''
creating custom 
Error below...
'''

class TooBigValueError(Exception):
    pass 
class TooSmallValueError(Exception):
    pass

low_value = 1
high_value = 1000
number = random.randint(low_value, high_value)

count = 0

while True :
    try :
        guess = int (input("Enter Guess : "))
        print ()
        count += 1
        
        if guess > high_value :
            raise TooBigValueError
        
        elif guess < low_value : 
            raise TooSmallValueError
        break 
           
    except ValueError :
        print ('Please Enter a Number : ')
        print ()  
    
    except Exception : # this bolck of code is unnecessary 
        print (Exception)
        print ()
        
    except TooBigValueError :
        print ('Value is too Big, try again! ', end = '')
        print (f"Enter Value Between {low_value} & {high_value}.")
        print ()
        
    except TooSmallValueError:
        print ("Value is too small, try again! ", end ="")
        print (f'Enter Value Between {low_value} & {high_value}.')
        print ()
        
    if guess > number : 
        print ("Enter a lower Value")
        print ()
        
    elif guess < number : 
        print ("Enter a Higher Value")
        print ()
        
print ("You nailed it! ", end = "")
print (f'You took {count} chances.')
        
    