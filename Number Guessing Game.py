import random # importing random module

#creatimg custom Execptions 
class BigValueError(Exception) : 
    pass 
    
class SmallValueError(Exception) : 
    pass 

class EmptyInputError(Exception) : 
    pass
      
# initiating value range     
small_value = 1 
big_value = 1000    
number = random.randint(small_value, big_value)


def play() :
    print ("********New Game********")
    print()
    print (f"Enter a Value between {small_value} and {big_value}")   
    print('Enter \'exit\' to exit the game')
    print ()
    
    #Here we will count how many times user have guessed
    count = 0
    
    while True  : 
        try : 
            # taking input 
            guess = input("Enter an Integer Number : ")
            
            # if user enter exit then exit the game
            if guess.lower() == 'exit' : 
                break 
            # if it'a Empty input then raise EmptyInputError
            if guess.strip() == '' : 
                raise EmptyInputError

            # convert to integer
            guess = int(guess) 
            
            # if input is bigger than constraints then raise BigValueError              
            if guess > big_value : 
                raise BigValueError
            
            # if input is smaller than constraints then raise SmallValueError
            if guess < small_value : 
                raise SmallValueError 
            
            # if guess is correct then congrat User  
            if guess == number :
                count += 1 
                print ()
                print ("Congratulations! You Guessed it") 
                print (f"You took {count} Chances")
                print ()
                
            # ask him/her to play again
                play_again = input("Do you want to play again?\nPress \'Y/y\' to play again : ")
                
                if play_again.lower() == 'y' : 
                    play() 
                else : 
                      break
             
            elif small_value <= guess < number : 
                count += 1
                print ("Enter a Bigger Number") 
                print () 
            
            elif big_value >= guess > number : 
                count += 1
                print ('Enter a Smaller Number') 
                print ()
            
        # Handling Error s    
        except EmptyInputError as e : 
            print (f"You Didn't Enter anything. Enter valid Integer between {small_value} and {big_value}")  
            print ()
          
        except BigValueError : 
            print ("Your guess is bigger than original contraints. Enter a lower number") 
            print () 
        
        except SmallValueError: 
            print ("Your guess is smaller than original contraints. Enter a bigger number") 
            print ()
        
        except ValueError : 
            print ("Enter a Integer")
            print()
        
        except Exception as e : 
            print (e) 

if __name__ == "__main__" :            
    play()

