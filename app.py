from random import randint
import tkinter as tk
from Help_frames_file import HelpFrames
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as font


window = tk.Tk()
from Randomize_file import Randomize_classes
var3 = Randomize_classes()

window['bg'] = 'black'

var2 = HelpFrames()

first_portion = tk.Entry(window,textvariable = (var3.f_s),width=3 ,font= 'times 20',bd=2)
first_portion.place(x=20, y=100)

second_portion = tk.Entry(window,textvariable = (var3.s_s),width=3,font= 'times 20',bd=2)
second_portion.place (x=80,y=100)

third_portion = tk.Entry(window,textvariable = var3.t_s ,width=3,font= 'times 20',bd=2)
third_portion.place(x=140, y=100)

fourth_portion = tk.Entry(window,textvariable = var3.fo_s ,width=3,font= 'times 20',bd=2)
fourth_portion.place(x=200, y=100)

n = tk.StringVar()

prefix_length_input = ttk.Combobox(window,width=2,font='times 17',textvariable = n,state = 'readonly')

prefix_length_input['values'] = (8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
prefix_length_input.place (x=405,y=280)

class first_frame:
    subnet_mask = [128,192,224,240,248,252,254]
    no_of_hosts = [16777214,8388606,4194302,2097150,1048574,524286,262142,131070,65534,32766,16382,8190,4094,2046,1022,510,254,126,62,30,14,6,2]
    no_of_networks = [2,4,8,16,32,64,128]
    block_size = [128,64,32,16,8,4,2]

    def output_window(self):
        try:
            self.first = int(first_portion.get())
            self.second = int(second_portion.get())
            self.third = int(third_portion.get())
            self.fourth =int(fourth_portion.get())
            self.pref = int(prefix_length_input.get())

        except ValueError:
            messagebox.showerror('Error','''Please Fill in All Entry Boxes.
All Boxes can only contain numbers.''')
            return

        sec_win = tk.Tk()

        sec_win.geometry('700x400')
        sec_win.resizable(False,False)


##########SUBNETTER##############


        if self.first not in range (1,224) and self.second not in range (1,256)  and self.pref not in range (8,31):
            error_mess3 = tk.Label(sec_win, text = '''Invalid  IP Address Format. Usable IP addresses first octet start at 1 and end at 223
Invalid Prefix Length Format. Usable Prefix Length Range from 8 to 30
Invalid Prefix Length Format. The Maximum number that can be in each octet start at 1 and end at 255''',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess3.pack(side='bottom')

        elif self.first not in range (1,224) and self.third not in range (1,256)  and self.pref not in range (8,31):
            error_mess3 = tk.Label(sec_win, text = '''Invalid  IP Address Format. Usable IP addresses first octet start at 1 and end at 223
Invalid Prefix Length Format. Usable Prefix Length Range from 8 to 30
Invalid Prefix Length Format. The Maximum number that can be in each octet start at 1 and end at 255''',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess3.pack(side='bottom')

        elif self.first not in range (1,224) and self.fourth not in range (1,256)  and self.pref not in range (8,31):
            error_mess4 = tk.Label(sec_win, text = '''Invalid  IP Address Format. Usable IP addresses first octet start at 1 and end at 223
Invalid Prefix Length Format. Usable Prefix Length Range from 8 to 30
Invalid Prefix Length Format. The Maximum number that can be in each octet start at 1 and end at 255''',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess4.pack(side='bottom')

        elif self.first not in range (1,224) and self.pref not in range (8,31):
            error_mess5 = tk.Label(sec_win, text = '''Invalid  IP Address Format. Usable IP addresses first octet start at 1 and end at 223
Invalid Prefix Length Format. Usable Prefix Length Range from 8 to 30''',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess5.pack(side='bottom')

        elif self.second not in range (1,224) and self.pref not in range (8,31):
            error_mess6 = tk.Label(sec_win, text = '''Invalid IP Address Format. The Maximum number that can be in each octet start at 1 and end at 255
Invalid Prefix Length Format. Usable Prefix Length Range from 8 to 30''',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess6.pack(side='bottom')

        elif self.third not in range (1,224) and self.pref not in range (8,31):
            error_mess7 = tk.Label(sec_win, text = '''Invalid IP Address Format. The Maximum number that can be in each octet start at 1 and end at 255
Invalid Prefix Length Format. Usable Prefix Length Range from 8 to 30''',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess7.pack(side='bottom')

        elif self.fourth not in range (1,224) and self.pref not in range (8,31):
            error_mess8 = tk.Label(sec_win, text = '''Invalid IP Address Format. The Maximum number that can be in each octet start at 1 and end at 255
Invalid Prefix Length Format. Usable Prefix Length Range from 8 to 30''',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess8.pack(side='bottom')

        elif self.first not in range (1,224) and self.second not in range (1,256):
            error_mess9 = tk.Label(sec_win, text = '''Invalid  IP Address Format. Usable IP addresses first octet start at 1 and end at 223
Invalid IP Address Format. The Maximum number that can be in each octet start at 1 and end at 255''',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess9.pack(side='bottom')

        elif self.first not in range (1,224) and self.third not in range (1,256):
            error_mess10 = tk.Label(sec_win, text = '''Invalid  IP Address Format. Usable IP addresses first octet start at 1 and end at 223
Invalid IP Address Format. The Maximum number that can be in each octet start at 1 and end at 255''',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess10.pack(side='bottom')

        elif self.first not in range (1,224) and self.fourth not in range (1,256):
            error_mess11= tk.Label(sec_win, text = '''Invalid  IP Address Format. Usable IP addresses first octet start at 1 and end at 223
Invalid IP Address Format. The Maximum number that can be in each octet start at 1 and end at 255''',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess11.pack(side='bottom')
        elif self.second not in range (1,256) or self.third not in range (1,256) or self.fourth not in range (1,256) :
            error_mess12 = tk.Label (sec_win,text = 'Invalid IP Address Format. The Maximum number that can be in each octet start at 1 and end at 255',font = ('Imprint MT Shadow',10),fg = 'red')
            error_mess12.pack(side = 'bottom')


        elif self.first not in range (1,224):
            error_mess13 = tk.Label(sec_win, text = 'Invalid IP Address Format. Usable IP addresses first octet start at 1 and end at 224',font = ('Imprint MT Shadow',15),fg = 'red')
            error_mess13.pack(side='bottom')


        elif self.second not in range (1,256):
            error_mess13 = tk.Label(sec_win, text = 'Invalid IP Address Format. The Maximum number that can be in each octet start at 1 and end at 255',font = ('Imprint MT Shadow',20),fg = 'red')
            error_mess13.pack(side='bottom')

        elif self.third not in range (1,256):
            error_mess13 = tk.Label(sec_win, text = 'Invalid IP Address Format. The Maximum number that can be in each octet start at 1 and end at 255',font = ('Imprint MT Shadow',20),fg = 'red')
            error_mess13.pack(side='bottom')
        elif self.fourth not in range (1,256):
            error_mess13 = tk.Label(sec_win, text = 'Invalid IP Address Format. The Maximum number that can be in each octet start at 1 and end at 255',font = ('Imprint MT Shadow',20),fg = 'red')
            error_mess13.pack(side='bottom')
        elif self.pref == 8:
                if self.first in range (1,128):
                    class_add_l2 = tk.Label(sec_win, text = 'A',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    net_add_l2 = tk.Label(sec_win, text = '{}.0.0.0'.format(self.first),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    sub_mask_l2= tk.Label(sec_win,text = '255.0.0.0',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    no_network_l2 = tk.Label(sec_win, text = '256',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    block_size_l2 = tk.Label(sec_win,text = '''Not Subnetted
Default prefix length''',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    class_add_l2.place(x = 290,y = 20)
                    net_add_l2.place(x = 290,y = 60)
                    sub_mask_l2.place(x = 290,y =100)
                    no_hosts_l2.place(x = 290,y = 140)
                    no_network_l2.place(x = 290,y = 180)
                    block_size_l2.place(x = 290,y = 220)

                else:
                    error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                    error_mess1.pack(side='bottom')



        elif self.pref == 16:
                if self.first in range (128,192):
                    class_add_l2 = tk.Label(sec_win, text = 'B',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    sub_mask_l2= tk.Label(sec_win,text = '255.255.0.0',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[8]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    no_network_l2 = tk.Label(sec_win, text = '65536',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    block_size_l2 = tk.Label(sec_win,text = '''Not Subnetted
Default prefix length''',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                    class_add_l2.place(x = 290,y = 20)
                    net_add_l2.place(x = 290,y = 60)
                    sub_mask_l2.place(x = 290,y =100)
                    no_hosts_l2.place(x = 290,y = 140)
                    no_network_l2.place(x = 290,y = 180)
                    block_size_l2.place(x = 290,y = 220)

                else:
                    error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                    error_mess1.pack(side='bottom')

        elif self.pref == 24:
            if self.first in range (192,224):
                class_add_l2 = tk.Label(sec_win, text = 'C',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.255.0:',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[16]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '16777216',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = '''Not Subnetted
Default prefix length''',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)
            else:
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')

#################Class A Addresses###########
        elif self.pref == 9 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            if self.first >= 128:
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')

            else:
                class_add_l2 = tk.Label(sec_win, text = 'A',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.0.0.0'.format(self.first),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.{}.0.0'.format(first_frame.subnet_mask[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[0],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)

        elif self.pref == 10 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            if self.first >= 128:
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')
            else:
                class_add_l2 = tk.Label(sec_win, text = 'A',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.0.0.0'.format(self.first),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.{}.0.0'.format(first_frame.subnet_mask[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[1],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)
        elif self.pref == 11 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            if self.first >= 128:
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')
            else:
                class_add_l2 = tk.Label(sec_win, text = 'A',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.0.0.0'.format(self.first),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.{}.0.0'.format(first_frame.subnet_mask[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[2],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)

        elif self.pref == 12 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            if self.first >= 128:
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')
            else:
                class_add_l2 = tk.Label(sec_win, text = 'A',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.0.0.0'.format(self.first),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.{}.0.0'.format(first_frame.subnet_mask[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[3],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)
        elif self.pref == 13 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            if self.first >= 128:
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')
            else:
                class_add_l2 = tk.Label(sec_win, text = 'A',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.0.0.0'.format(self.first),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.{}.0.0'.format(first_frame.subnet_mask[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[4],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)

        elif self.pref == 14 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            if self.first >= 128:
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')
            else:
                class_add_l2 = tk.Label(sec_win, text = 'A',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.0.0.0'.format(self.first),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.{}.0.0'.format(first_frame.subnet_mask[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[6]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[5],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)

        elif self.pref == 15 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            if self.first >= 128:
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')
            else:
                class_add_l2 = tk.Label(sec_win, text = 'A',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.0.0.0'.format(self.first),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.{}.0.0'.format(first_frame.subnet_mask[6]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[7]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[6]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[6],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)

#################Class B Prefix Length  ###########
        elif self.pref == 17 and  self.first >= 192 and  self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
               error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
               error_mess1.pack(side='bottom')




        elif self.pref ==17 and self.first in range (1,128) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'A with Class B Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[9]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '512',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)

        elif self.pref ==17 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'B',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[9]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[0],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)


        elif self.pref == 18 and  self.first >= 192 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')

        elif self.pref ==18 and self.first in range (1,128) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'A with Class B Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[10]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '1024',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)

        elif self.pref ==18  and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'B',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[10]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[1],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)


        elif self.pref == 19 and self.first >= 192 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')

        elif self.pref ==19 and self.first in range (1,128) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'A with Class B Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[11]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '2048',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)
        elif self.pref == 19 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'B',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[11]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[2],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)



        elif self.pref == 20 and self.first >= 192  and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')

        elif self.pref ==20 and self.first in range (1,128) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'A with Class B Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[12]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '4096',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)
        elif self.pref ==20 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'B',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[12]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[3],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)



        elif self.pref == 21 and  self.first >= 192  and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')

        elif self.pref == 21 and self.first in range (1,128) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'A with Class B Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[13]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '8192',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)

        elif self.pref == 21 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'B',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[13]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[4],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)


        elif self.pref == 22 and self.first >= 192 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')

        elif self.pref == 22 and self.first in range (1,128) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'A with Class B Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[14]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '16384',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)
        elif  self.pref == 22 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'B',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[14]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[5],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)



        elif self.pref == 23 and self.first >= 192  and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :

                error_mess1 = tk.Label(sec_win, text = 'Invalid Class of IP with Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'red')
                error_mess1.pack(side='bottom')


        elif self.pref == 23 and self.first in range(1,128) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'A with Class B Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[6]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[15]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '32768',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[6]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)

        elif self.pref == 23  and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
                class_add_l2 = tk.Label(sec_win, text = 'B',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                net_add_l2 = tk.Label(sec_win, text = '{}.{}.0.0'.format(self.first,self.second),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                sub_mask_l2= tk.Label(sec_win,text = '255.255.{}.0'.format(first_frame.subnet_mask[6]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[15]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[6]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                block_size_l2 = tk.Label(sec_win,text = first_frame.block_size[6],font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
                class_add_l2.place(x = 290,y = 20)
                net_add_l2.place(x = 290,y = 60)
                sub_mask_l2.place(x = 290,y =100)
                no_hosts_l2.place(x = 290,y = 140)
                no_network_l2.place(x = 290,y = 180)
                block_size_l2.place(x = 290,y = 220)


#########Class C Prefix Length ###################


        elif self.pref == 25 and self.first in range (192,224) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            class_add_l2 = tk.Label(sec_win, text = 'C',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[17]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 25 and self.first <=192 and self.first >=128 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
            class_add_l2 = tk.Label(sec_win, text = 'B with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[17]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '512',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 25 and self.first <=127 and self.first >=1 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
             class_add_l2 = tk.Label(sec_win, text = 'A with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[17]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_network_l2 = tk.Label(sec_win, text = '131072',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[0]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             class_add_l2.place(x = 290,y = 20)
             net_add_l2.place(x = 290,y = 60)
             sub_mask_l2.place(x = 290,y =100)
             no_hosts_l2.place(x = 290,y = 140)
             no_network_l2.place(x = 290,y = 180)
             block_size_l2.place(x = 290,y = 220)

        elif self.pref == 26 and self.first in range (192,224) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            class_add_l2 = tk.Label(sec_win, text = 'C',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[18]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 26 and self.first <=192 and self.first >=128 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
            class_add_l2 = tk.Label(sec_win, text = 'B with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[18]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '1024',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 26 and self.first <=127 and self.first >=1 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
             class_add_l2 = tk.Label(sec_win, text = 'A with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[18]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_network_l2 = tk.Label(sec_win, text = '262144',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[1]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             class_add_l2.place(x = 290,y = 20)
             net_add_l2.place(x = 290,y = 60)
             sub_mask_l2.place(x = 290,y =100)
             no_hosts_l2.place(x = 290,y = 140)
             no_network_l2.place(x = 290,y = 180)
             block_size_l2.place(x = 290,y = 220)

        elif self.pref == 27 and self.first in range (192,224) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            class_add_l2 = tk.Label(sec_win, text = 'C',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[19]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 27 and self.first <=192 and self.first >=128 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
            class_add_l2 = tk.Label(sec_win, text = 'B with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[19]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '2048',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 27 and self.first <=127 and self.first >=1 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
             class_add_l2 = tk.Label(sec_win, text = 'A with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[19]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_network_l2 = tk.Label(sec_win, text = '524288',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[2]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             class_add_l2.place(x = 290,y = 20)
             net_add_l2.place(x = 290,y = 60)
             sub_mask_l2.place(x = 290,y =100)
             no_hosts_l2.place(x = 290,y = 140)
             no_network_l2.place(x = 290,y = 180)
             block_size_l2.place(x = 290,y = 220)

        elif self.pref == 28 and self.first in range (192,224) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            class_add_l2 = tk.Label(sec_win, text = 'C',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[20]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 28 and self.first <=192 and self.first >=128 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            class_add_l2 = tk.Label(sec_win, text = 'B with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[20]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '4096',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 28 and self.first <=127 and self.first >=1 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
             class_add_l2 = tk.Label(sec_win, text = 'A with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[20]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_network_l2 = tk.Label(sec_win, text = '1048576',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[3]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             class_add_l2.place(x = 290,y = 20)
             net_add_l2.place(x = 290,y = 60)
             sub_mask_l2.place(x = 290,y =100)
             no_hosts_l2.place(x = 290,y = 140)
             no_network_l2.place(x = 290,y = 180)
             block_size_l2.place(x = 290,y = 220)

        elif self.pref == 29 and self.first in range (192,224) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            class_add_l2 = tk.Label(sec_win, text = 'C',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[21]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 29 and self.first <=192 and self.first >=128 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
            class_add_l2 = tk.Label(sec_win, text = 'B with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[21]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '8192',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 29 and self.first <=127 and self.first >=1 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
             class_add_l2 = tk.Label(sec_win, text = 'A with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[21]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_network_l2 = tk.Label(sec_win, text = '2097152',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[4]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             class_add_l2.place(x = 290,y = 20)
             net_add_l2.place(x = 290,y = 60)
             sub_mask_l2.place(x = 290,y =100)
             no_hosts_l2.place(x = 290,y = 140)
             no_network_l2.place(x = 290,y = 180)
             block_size_l2.place(x = 290,y = 220)

        elif self.pref == 30 and self.first in range (192,224) and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256):
            class_add_l2 = tk.Label(sec_win, text = 'C',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[22]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '{}'.format(first_frame.no_of_networks[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 30 and self.first <=192 and self.first >=128 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
            class_add_l2 = tk.Label(sec_win, text = 'B with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[22]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            no_network_l2 = tk.Label(sec_win, text = '16384',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
            class_add_l2.place(x = 290,y = 20)
            net_add_l2.place(x = 290,y = 60)
            sub_mask_l2.place(x = 290,y =100)
            no_hosts_l2.place(x = 290,y = 140)
            no_network_l2.place(x = 290,y = 180)
            block_size_l2.place(x = 290,y = 220)

        elif self.pref == 30 and self.first <=127 and self.first >=1 and self.second in range (1,256) and self.third in range (1,256) and self.fourth in range (1,256) :
             class_add_l2 = tk.Label(sec_win, text = 'A with Class C Prefix Length',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             net_add_l2 = tk.Label(sec_win, text = '{}.{}.{}.0'.format(self.first,self.second,self.third),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             sub_mask_l2= tk.Label(sec_win,text = '255.255.255.{}'.format(first_frame.subnet_mask[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_hosts_l2 = tk.Label(sec_win, text='{}'.format(first_frame.no_of_hosts[22]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             no_network_l2 = tk.Label(sec_win, text = '4194304',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             block_size_l2 = tk.Label(sec_win,text = '{}'.format(first_frame.block_size[5]),font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
             class_add_l2.place(x = 290,y = 20)
             net_add_l2.place(x = 290,y = 60)
             sub_mask_l2.place(x = 290,y =100)
             no_hosts_l2.place(x = 290,y = 140)
             no_network_l2.place(x = 290,y = 180)
             block_size_l2.place(x = 290,y = 220)

        else:
            return






###########help buttons########
        self.obj_d = first_frame()
        class_add_help_b = tk.Button (sec_win,text = '?',bg = 'gold',width=1,command = var2.class_add_help,font = ('GOUDY STOUT',10))
        class_add_help_b.place(x=500,y=0)

        net_add_help_b = tk.Button (sec_win,text = '?',bg = 'gold',width=1,command = var2.net_add_help,font = ('GOUDY STOUT',10))
        net_add_help_b.place (x=500,y =60)

        sub_mask_help_b = tk.Button (sec_win,text = '?',bg = 'gold',width=1, command = var2.sub_mask_help,font = ('GOUDY STOUT',10))
        sub_mask_help_b.place(x=500,y=100)

        no_host_help_b = tk.Button (sec_win,text = '?',bg = 'gold',width=1,command = var2.no_hosts_help,font = ('GOUDY STOUT',10))
        no_host_help_b.place(x=500,y=140)

        no_network_help_b = tk.Button (sec_win,text = '?',bg = 'gold',width=1,command = var2.no_netw_help,font = ('GOUDY STOUT',10))
        no_network_help_b.place(x=500,y=180)

        block_size_help_b = tk.Button(sec_win,text = '?',bg = 'gold' ,width=1,command = var2.block_size_help,font = ('GOUDY STOUT',10))
        block_size_help_b .place (x=500 ,y=220)
        ######'constant' labels######

        class_add_l = tk.Label(sec_win, text = 'Class of Address :',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
        net_add_l = tk.Label(sec_win, text = 'Network Address :',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
        sub_mask_l= tk.Label(sec_win,text = 'Subnet Mask:',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
        no_hosts_l = tk.Label(sec_win, text='Number of Hosts :',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
        no_network_l = tk.Label(sec_win, text = 'Number of Networks :',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
        block_size_l = tk.Label(sec_win,text = 'Block Size :',font = ('Imprint MT Shadow',20),bg = 'black',fg = 'silver')
        class_add_l.place(x = 10,y = 20)
        net_add_l.place(x = 10,y = 60)
        sub_mask_l.place(x = 10,y =100)
        no_hosts_l.place(x = 10,y = 140)
        no_network_l.place(x = 10,y = 180)
        block_size_l.place(x = 10,y = 220)



        sec_win['bg'] = 'black'
        sec_win.title ('Information on IP address {} . {} . {}. {} with prefix length /{}'.format(self.first,self.second,self.third,self.fourth,self.pref))






















#############DOTS############
first_dot = tk.Label(window,text = '.',font = 'times 20',bg = 'black',fg = 'white')
first_dot.place(x=67,y=94)

second_dot = tk.Label(window,text = '.',font = 'times 20',bg = 'black',fg = 'white')
second_dot.place(x=127,y=94)

third_dot = tk.Label(window,text = '.',font = 'times 20',bg = 'black',fg = 'white')
third_dot.place(x=187,y=94)

####### Labels##########

ip_add_label = tk.Label(window,text = 'IP Address' ,bg = 'black',fg = 'silver',font = ('Imprint MT Shadow',20))
ip_add_label.place(x = 70, y =60)
pref_label = tk.Label(window,text = 'Prefix Length /',bg = 'black',fg = 'silver',font = ('Imprint MT Shadow',20))
pref_label.place (x = 217,y=280)
randomize_label = tk.Label(window,text = 'Get a random IP address :',bg = 'black', fg = 'silver',font = ('Imprint MT Shadow',20))
randomize_label.place (x = 20,y = 170)


var1 = first_frame()
###############Buttons###############
ip_add_help = tk.Button (window,text = '?',width = 1,bg = 'gold',command = var2.IP_add_help,font = ('GOUDY STOUT',10))
ip_add_help.place(x = 250,y=100)
pref_help_b = tk.Button (window,text = '?',width = 1,bg = 'gold',command = var2.pref_help, font = ('GOUDY STOUT',10))
pref_help_b.place(x = 452,y=280)
rand_help = tk.Button (window,text = '?',width = 1,bg = 'gold',command = var2.rand_help, font = ('GOUDY STOUT',10))
rand_help.place(x = 330,y=180)
gen_help_b = tk.Button (window, text = 'Help',width = 4,bg = 'gold',command = var2.gen_help,font = ('ALGERIAN',15),bd = 3)
gen_help_b.place (x=20,y=400)

sub_button = tk.Button(window, text = 'Subnet',bg = 'gold',command = var1.output_window,font = ('ALGERIAN',15),bd = 3)
sub_button.place(x = 389,y =400)

class_a = tk.Button(window,text = 'Class A Address',bg = 'gold',command = var3.class_a_randomize, font = ('ALGERIAN',10),bd = 4)
class_a.place(x = 20,y = 220)


class_b = tk.Button(window,text = 'Class B Address',bg = 'gold', font = ('ALGERIAN',10),bd = 4,command = var3.class_b_randomize)
class_b.place(x = 180,y = 220)


class_c = tk.Button(window,text = 'Class C Address',bg = 'gold',command = var3.class_c_randomize, font = ('ALGERIAN',10),bd = 4)
class_c.place(x = 330,y = 220)

clear_ip_add = tk.Button(window,text = 'Clear IP Address',bg = 'gold',command = var3.clear,font = ('ALGERIAN',10),bd = 4)
clear_ip_add.place(x = 330,y = 100)




window.title('Subnetter')
window.geometry('500x500')
window.resizable(False,False)


window.mainloop()


