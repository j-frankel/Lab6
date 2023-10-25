'''
Lab 6
Jacob F & Alex F

'''

def main():
    print("Menu")
    print("------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    user_choice = int(input("\nPlease enter an option: "))

    while user_choice != 3:
        try:
            if user_choice == 1:
                list_pass = input("Please enter your password to encode: ")
                list_pass = list_pass.split()
                for i in list_pass:
                    i = int(i)
                    i += 3
                    return i
                encoded = ''.join(list_pass)
                print("Your password has been encoded and stored!")
                print(encoded)
        except:
            print("Error")


if __name__ == '__main__':
    main()