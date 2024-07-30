import time
from os import system
import sys

def timer(hour,minute,second):
    
    total_time= hour * 3600 + minute * 60 + second
    
    while total_time > 0:
        print(f"{hour} : {minute} : {second}")
        
        total_time -= 1
        
        if second > 0:
            second -= 1
        else:
            if minute > 0:
                minute -= 1
                second = 59
            else:
                if hour > 0:
                    hour -= 1
                    minute = 59
                                    
        time.sleep(1)
        
        system("cls")
    else:
        main()    
   
         

def main():
    while True:
        while True:
            print("please choose your option:\n\t1)enter time\n\t2)exit")
            
            try:
                choice=int(input("\nyour choice is : "))
                break        
            except:
                print("\nplease enter 1 or 2.\n")
                
        if choice == 1:
            while True:
                
                try:
                    hour= int(input("\nenter hour: "))
                    minute= int(input("\nenter minute: "))
                    second= int(input("\nenter second: "))
                    break
                except:
                    print("\nplease enter valid integer numbers.\n")
            
            timer(hour,minute,second)
                
        
        elif choice == 2:
            sys.exit("\ngoodbye!\n")
        
        else:
            print("\ninvalid input. please enter 1 or 2.\n")
        

main()                                 
        
        
        
        
    