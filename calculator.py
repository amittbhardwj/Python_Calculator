# A Python Calculator
from Tkinter import *


# the main class
class Calc():
    def _init_(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq_flag = False

    def num_press(self, num):
        temp = text_box.get()
        self.eq_flag = False
        temp2 = str(num)
        if self.new_num is True:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        text_box.delete(0, END)
        text_box.insert(0, self.current)

    def calc_total(self):
        if self.op_pending is True:
            self.do_sum()
            self.op_pending = False

    def do_sum(self):
        self.current = float(self.current)
        if self.op is "add":
            self.total += self.current
        if self.op is "minus":
            self.total -= self.current
        if self.op is "times":
            self.total *= self.current
        if self.op is "divide":
            self.total /= self.current
        text_box.delete(0, END)
        text_box.insert(0, self.total)
        self.new_num = True

    def operation(self, op):
        if self.op_pending is True:
            self.do_sum()
            self.op = op
        else:
            self.op_pending = True
            if self.eq_flag is False:
                self.total = float(text_box.get())
            else:
                self.total = self.current
            self.new_num = True
            self.op = op
            self.eq_flag = False
