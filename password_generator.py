import string
import random
import sys



def password(length):
    
    small_letters= string.ascii_lowercase
    capital_letters= string.ascii_uppercase
    symbols= "~!@#$%^&*()-_+=/|\\><?\"\':"
    numbers= "0123456789"
    
    all_characters= small_letters + capital_letters + symbols + numbers
    
    if(length<=86):
        word= "".join(random.sample(all_characters,length))
        return word
    else:
        print("\ncan't generate a password larger than 86 digits.")
    
    
def main():
    while True:
        while True:
            print("choose your option:\n\t1)generate password\n\t2)Exit")
            
            try:
                choice= int(input("\nyour choice: "))
                break
            except:
                print("please enter 1 or 2.")
        
        if choice == 1:
            while True:
                print("\nplease enter the length of your password: ")
                
                try:
                    length= int(input("\nyour password length: "))
                    break
                except:
                    print("please enter a valid integer number.")
                
            print(f"\nyour password is : {password(length)}")
                    
        elif choice== 2:
            sys.exit("\ngoodbye!!")
            
        else:
            print("please enter 1 or 2.")            
                        

main()    
    
            
