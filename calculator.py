# A Python Calculator
from tkinter import *

# the main class
class Calc():
    def _init_(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq_flag = False

    def num_press(self,num):
        temp = text_box.get()
        self.eq_flag = False
        temp2 = str(num)
        if self.new_num == True:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return self.current = temp + temp2
        text_box.delete(0,END)
        text_box.insert(0,self.current)
