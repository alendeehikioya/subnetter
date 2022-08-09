__author__ = 'Alende'
import tkinter as tk
from random import *

class Randomize_classes:

    def class_a_randomize(self):
        random_a_first = randint (1,127)
        self.f_s.set(random_a_first if self.count>0 else random_a_first)
        random_a_sec = randint(1,255)
        self.s_s.set(random_a_sec if self.count>0 else random_a_sec)

        random_a_th = randint(1,255)
        self.t_s.set(random_a_th if self.count>0 else random_a_th)

        random_a_fo = randint(1,255)
        self.fo_s.set(random_a_fo if self.count>0 else random_a_fo)
        self.count+=1


    count_a = 0
    count_b = 0
    count_c = 0

    f_s = tk.StringVar()
    f_s.set('')
    s_s = tk.StringVar()
    s_s.set('')
    t_s = tk.StringVar()
    t_s.set('')
    fo_s = tk.StringVar()
    fo_s.set('')


    def class_b_randomize(self):
        random_b_f = randint(128,191)
        self.f_s.set(random_b_f if self.count >0 else random_b_f )
        random_b_sec = randint(1,255)
        self.s_s.set(random_b_sec if self.count>0 else random_b_sec)
        self.count+=1
        random_b_th = randint(1,255)
        self.t_s.set(random_b_th if self.count>0 else random_b_th)
        self.count+=1
        random_b_fo = randint(1,255)
        self.fo_s.set(random_b_fo if self.count>0 else random_b_fo)
        self.count+=1

    count = 0
    f_s = tk.StringVar()
    f_s.set('')
    s_s = tk.StringVar()
    s_s.set('')
    t_s = tk.StringVar()
    t_s.set('')
    fo_s = tk.StringVar()
    fo_s.set('')


    def class_c_randomize(self):
        random_c_f = randint(192,223)
        self.f_s.set(random_c_f if self.count >0 else random_c_f )
        random_c_sec = randint(1,255)
        self.s_s.set(random_c_sec if self.count>0 else random_c_sec)
        self.count+=1
        random_c_th = randint(1,255)
        self.t_s.set(random_c_th if self.count>0 else random_c_th)
        self.count+=1
        random_c_fo = randint(1,255)
        self.fo_s.set(random_c_fo if self.count>0 else random_c_fo)
        self.count+=1



    count = 0
    f_s = tk.StringVar()
    f_s.set('')
    s_s = tk.StringVar()
    s_s.set('')
    t_s = tk.StringVar()
    t_s.set('')
    fo_s = tk.StringVar()
    fo_s.set('')


    def clear(self):

        self.f_s.set('' if self.count >0 else '' )
        self.s_s.set('' if self.count>0 else '')
        self.count+=1
        self.t_s.set('' if self.count>0 else '')
        self.count+=1
        self.fo_s.set('' if self.count>0 else '')
        self.count+=1



    count = 0
    f_s = tk.StringVar()
    f_s.set('')
    s_s = tk.StringVar()
    s_s.set('')
    t_s = tk.StringVar()
    t_s.set('')
    fo_s = tk.StringVar()
    fo_s.set('')
