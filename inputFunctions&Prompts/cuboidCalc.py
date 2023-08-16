#surface area (SA)=2lw+2lh+2hw
#Volume of a cuboid = l × w × h

print("Kindly fill the following information")
print("Length")
len = int(input())
print("Width")
wid = int(input())
print("Height")
Hgt = int(input())

#area calculation
surfaceArea = 2 * (len * wid) + 2 * (len * Hgt) + 2 * (Hgt * wid)
print("The surface area of your cuboid is ", surfaceArea)

#volume calc
vol = len * wid * Hgt
print("The volume of your cuboid is ", vol)

