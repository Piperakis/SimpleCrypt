from pswd_encoder import checkpswd, translatepswd
keys = []


def ProcessFile(filename, key, selection):
    file = open(filename, 'rb')
    data = file.read()  # Reading file 
    file.close()

    keys = translatepswd(key)  # Translating the key to list of nuumeric values

    for val in keys:
        data = bytearray(data) # Translating data to proccess to byte array
        for intex, value in enumerate(data):  
            data[intex] = value ^ int(val) # Passing each byte array through the XOR operator

    if selection == "1":
        file = open("CC-" + filename, "wb") # Setting the filename according to user's selection
    else:
        file = open(filename, "wb")

    file.write(data) # Saving file
    file.close


choice = ""
while choice != "3": # Displayed menu 
    print("Please select you option. \n 1. Encrypt File \n 2. Decrypt File \n 3. Quit")
    choice = input()
    if choice == "1" or choice == "2":
        key = input("Enter a password!\n")
        filename = input("Enter filename with extension:\n")
        ProcessFile(filename, key, choice)
