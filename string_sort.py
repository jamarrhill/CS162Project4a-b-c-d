# Name: Jamar Hill
# Date: 4/25/2021
# Description: CS 162 Project 4c

def string_sort (y):
    for x in range (1, len(y)):
        temp = y[x]
        z = x
        while ( z > 0 and y [z - 1].lower() > temp.lower ()):
            y[z] = y [z - 1]
            z -= 1
            y[z] = temp
    return y

y1 = ["apple", "zebra", "maRker","marble"]
y2 = string_sort(y1)
for x in range (len(y2)):
    temp = y2[x]
    for z in range (len(y1)):
        if (y1[z]. lower() ==temp.lower()):
            print(y1[z])