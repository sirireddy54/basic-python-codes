
started= False

while True:  
    #command= str(input()).lower()
    command= str(input(">")).casefold()
    if(command=="help"):
        print("start to start the car \n Stop to stop the car \n quit to quit the program")
    elif(command=="start"):
        if(started):
            print("Car is already started!")
        else:
            started= True
            print("Car Strated....Ready to go")
    elif(command=="stop"):
        if(not started):
            print("Car is already stopped")
        else:
            started= False
            print("Car Stopped")
    elif(command=="quit"):
        break
    else:
        print("I dont understand that")


