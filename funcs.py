from random import choice, shuffle
from tkinter import *


class Generator:


    empty_list = []
    my_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    my_list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    my_num_list = [0,1,2,3,4,5,6,7,8,9]
    symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',':',';']


    def random_generating(self):
        char_list = [choice(self.my_list) for _ in range(3)]
        char_list2 = [choice(self.my_list_lower) for _ in range(4)]
        num_list = [choice(self.my_num_list) for _ in range(3)]
        symb_list = [choice(self.symbols) for _ in range(2)]
        result = char_list + num_list + symb_list + char_list2
        shuffle(result)
        new_new = "".join([str(element) for element in result])
        return new_new

