'''
Lab 6
Jacob F & Alex F

'''
#encodes the password
def encode(input_string_pass):
            
    try:
        
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

        return input_string_pass, encoded
    
    except:

        print("Error")

#decodes the password
def decode(input_string_pass, encoded):
    try:
        print(f'The encoded password is {encoded}, and the original password is {input_string_pass}.')
    except:
        print("There was an error...")
        
#executes the program
def main():

    user_choice = None
    
    while user_choice != 3:
        
        print("Menu",
        "------------",
        "1. Encode",
        "2. Decode",
        "3. Quit", sep='\n')
        user_choice = int(input("\nPlease enter an option: "))

        if user_choice == 1:
           input_string_pass, encoded =  encode(input("Please enter your password to encode: "))

        elif user_choice == 2:
           decode(input_string_pass, encoded) 
            
        elif user_choice == 3:
            break


if __name__ == '__main__':
    main()