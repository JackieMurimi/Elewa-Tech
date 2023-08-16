#area, perimeter and volume of a rectangle

#we prompt the use to give the measurements
print("Kindly fill the information")
print("Length")
len = int(input())
print("Width")
wid = int(input())
print("Height")
Hgt = int(input())

#perimeter
per = 2 * (len + wid)
print(per)

area = len * wid
print(area)

volume = len * wid * Hgt
print(volume)
