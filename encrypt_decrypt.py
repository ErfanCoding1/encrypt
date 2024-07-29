import sys


def encrypt(text):
    
    encrypt_text= ""
    
    for i in text:
        tmp = ord(i) * 3 + 6
        encrypt_text += chr(tmp)
        
    return encrypt_text

def decrypt(text):
    
    plain_text=""
    
    for i in text:
        tmp = (ord(i)-6)//3
        plain_text += chr(tmp)
        
    return plain_text        

def main():
    
    while True:
        print("\nplease choose an option.\n\t1)encrypt a text\n\t2)decrypt a text\n\t3)exit the program!")
        
        while True:
            try:
                choise= int(input("\nyour choise is : "))
                break
            except:
                print("\nplease enter 1 , 2 or 3.")
                
        if(choise==1):
            plain_text = input("\nenter your plain text : ")
            print(f"\nencrypted text : {encrypt(plain_text)}")
        elif(choise==2):
            encrypted_text = input("\nenter your encrypted text : ")   
            print(f"\nyour plain text : {decrypt(encrypted_text)}")
        elif(choise==3):
            sys.exit("\ngoodbye!")
        else:
            print("please enter 1 , 2 or 3.")
            

if __name__=="__main__":
    main()                    
                  
    
            
    
    