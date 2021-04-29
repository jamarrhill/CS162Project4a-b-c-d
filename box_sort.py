# Name: Jamar Hill
# Date: 4/25/2021
# Description: CS 162 Project 4.b


class Box():
    def __init__(self, length, width, height):
        self.__length= length
        self.__width = width
        self.__height = height

    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def volume(self):
        return self.__length * self.__width * self.__height

    def get_volume(self):
        return self.__volume
def box_sort(box_list):
    for i in range(1,len(box_list)):
        current_box = box_list[1]
        j = i - 1
        while j >= 0 and current_box.get_volume() < box_list[j].get_volume():
            box_list[j + 1] = box_list[j]
            j -= 1
            box_list[j + 1] = current_box

