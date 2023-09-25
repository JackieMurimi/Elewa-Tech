#try exception handliing file
#works in error handling

var_a = 34
var_b = "daisy"

try:
    calc = var_a + var_b
    print(calc)
except:
    print("An error has occured")


#second demo
#perimeter, area and volume of a rectangle
length = 14
height = 13
width = 8

try:
    per = 2 * (length * width)
    print(per)
except:
    print("There's an error")

# demo 3
situation = "Home alone"
try:
     if(situation == "Home alone"):
        dec_1 = print("Go out and have fun")
        dec_2 = print("Stay home and wear flip flops")
        final = dec_1 or dec_2
        print(final)
except:
        print("There is an error")

#second demo(logical control structure)

sugar = 1
milk = 1
teaBags = 0
heat = 1
sufuria = 1
water = 1
sieve = 1

#control structure starts here
try:
     if(sieve == 1 and sufuria == 1 and heat == 1):
          try:
               if(water == 1 and milk == 1):
                    try:
                         if(sugar == 1 or teaBags == 1):
                              print("You can cook tea")
                    except:
                         print("An error has occured")
                    else:
                         try:
                              print("You can go buy some necessities")
                         except:
                              print("There is an error")
          except:
               print("an error")
except:
     print( "error error")




