#A python script that determines wether an IPV4 is private or public based on user input.
#Made by Adam Pacek II


#Starts off by asking user for the IPV4.
INP = input("Please input the IPV4 in the format of (0.0.0.0) : ")


#Check if the user used the valid format.
if "." in INP:

    #Split the input by . & turn the input into usable variables.
    splitINP = INP.split(".")

    #Test if there are 4 octets in the input.
    if len(splitINP) == 4:   

        #Define the values that determine wether an IP is public or private.
        private = [10, 172, 192]

        #Turn each value in private into usable, or testable Strings. Then test the values to determine if the input is a public or private IP in a loop.
        for values in private:

            #Create a variable to check the first octet.
            testval = splitINP[0]
            values = str(values)

            if values == testval:
                print(" : The octet "+ values +" has been detected in the first octet. \n")
                print(" : The IP is Private! \n")
                input()
                break

        #If all tests fail, inform the user that the IP is public.
        else:
            print(" : The IP is Public! \n")
            input()

    #Inform the user their missing 4 octets.
    else:
        print(" : Please use a valid format! \n")
        input()

#Inform the user they arent using the proper format.
else:
    print("Please use a valid format! \n")
    input()