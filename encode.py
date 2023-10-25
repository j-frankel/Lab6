'''
Lab 6
Jacob F & Alex F

'''

def menu(): 
    user_choice = None
    print("Menu",
   "------------",
   "1. Encode",
   "2. Decode",
   "3. Quit", sep='\n')
    user_choice = int(input("\nPlease enter an option: "))
    return user_choice

def encode():
            
    try:
        input_string_pass = input("Please enter your password to encode: ")
        list_pass = []

        for i in input_string_pass:
            list_pass.append(i)
        encoded_list = []

        for i in list_pass:
            i = int(i)
            i += 3
            i = str(i)
            encoded_list.append(i)
        encoded = ''.join(encoded_list)
        print("Your password has been encoded and stored!")
        return encoded
    except:
        print("Error")

def main():

    
    while  != 3:
        
        if 


    


if __name__ == '__main__':
    main()