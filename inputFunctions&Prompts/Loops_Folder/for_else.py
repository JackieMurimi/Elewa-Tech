work = 5
vacation = 2
day = 0

for i in range(work):
    day = day + 1
    if(day > work):
        print("wake up early in the morning")
    else:
        print("You can sleep in")

else:
        day = day + 6
        if(day > work):
             print("You can wake up late")
        else:
             print("You can wake up early")


#case 3,complex
my_list = [1,23,24,15,17,18,37,45,21,2]
patt = "x"

for i in my_list:
        if(i < 45):
             patt = patt * 9
             print(patt)
        elif(i < 37):
             patt = patt * 8
             print(patt)
        elif(i < 34):
             patt = patt * 7
             print(patt)
        elif(i < 23):
             patt = patt * 6
             print(patt)
        elif(i < 21):
             patt = patt * 5
             print(patt)
        elif(i < 18):
             patt = patt * 4
             print(patt)
        elif(i < 17):
             patt = patt * 3
             print(patt)
        elif(i < 15):
             patt = patt * 2
             print(patt)
        elif( i < 2):
             patt = patt * 1
             print(patt)
        else:
             patt = patt * 0
             print(patt)

else:
        if(i <- 45):
             print(my_list)

        
        
        i