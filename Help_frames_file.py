import tkinter as tk
from random import randint
class HelpFrames:
    def gen_help(self):
        main_help_win = tk.Tk()
        main_help_win.title ('About this Application')
        gen_label = tk.Label(main_help_win,text = '''This application will be useful to anyone learning about networks.
This application will also provide ease to anyone creating a network.
It does not matter if the network being created is a small one or a big one.
It will no doubt be useful in either case.
There were only three prefix lengths before 'subnetting' was a thing.
Subnetting is dividing a network into smaller networks.
This was done to make assigning IP addresses more flexible as IP addresses were nearing depletion.
For information on any of the concepts or topics, please click the  "?" icon beside it.''',font = ('Bradley Hand Itc',20),bg = 'black',fg = 'white')
        gen_label.pack(side = 'top')
        main_help_win.resizable(False,False)
        main_help_win.mainloop()

    def IP_add_help(self):
        main_IP_add_help_win = tk.Tk()
        main_IP_add_help_win.title('IP Addresses')
        main_ip_label = tk.Label(main_IP_add_help_win, text = '''An IP addresses is a logical address that must be present on a device for that device to communicate over a network.
As long as your device is communicating with another device, be it locally or over the internet, it has an IP address.
IP addresses are written as numbers in four sections (also known as four octets) separated by three dots.
An Example is (125.45.34.3).
The second, third and fourth sections can not be over 255 while the first section can not be over 223.''',font = ('Bradley Hand Itc',20),bg = 'black',fg = 'white')
        main_ip_label.pack(side = 'top')
        main_IP_add_help_win.resizable(False,False)
        main_IP_add_help_win.mainloop()

    def pref_help(self):
        main_pref_help_win = tk.Tk()
        main_pref_help_win.title ('Prefix-Length')
        main_pref_label = tk.Label(main_pref_help_win,text = ''' A prefix length is used to identify different characteristics of an IP address.
These characteristics include number of hosts (also known as IP addresses), class of IP addresses etc.
All usable prefix lengths begin with a slash('/') notation and range from 8 to 30.
Default prefix lengths are /8 for class A, /16 for class B, and /24 for class C.
All other prefix lengths are subnetted.''', font = ('Bradley Hand Itc',20),bg = 'black',fg = 'white')
        main_pref_label.pack(side = 'top')
        main_pref_help_win.resizable(False,False)
        main_pref_help_win.mainloop()

    def class_add_help(self):
        main_class_add_help_win = tk.Tk()
        main_class_add_help_win.title ('Class of IP Addresses')
        main_class_add_label = tk.Label(main_class_add_help_win,text = '''IP addresses are defined into three main classes:(A, B, and C).
IP address classes are based on the number of network addresses and IP addresses each of them provide.
Concerning the number of network addresses, they increase per class from class A to class C.
On the other hand, the number of IP addresses decrease per class from class A to class C.''', font = ('Bradley Hand Itc',20),bg = 'black',fg = 'white')
        main_class_add_label.pack(side = 'top')
        main_class_add_help_win.resizable(False,False)
        main_class_add_help_win.mainloop()


    def net_add_help(self):
        main_net_add_help_win = tk.Tk()
        main_net_add_help_win.title ('Network Addresses')
        main_net_add_label = tk.Label(main_net_add_help_win,text = '''The network address uniquely identifies each network.
Every device on the same network shares that network address as part of its IP address.
The portion(s)in the IP address for the network address depends on the prefix length.
This column gives you the network address of the IP address you specified.''', font = ('Bradley Hand Itc',20),bg = 'black',fg = 'white')
        main_net_add_label.pack(side = 'top')
        main_net_add_help_win.resizable(False,False)
        main_net_add_help_win.mainloop()

    def sub_mask_help(self):
        main_sub_mask_help_win = tk.Tk()
        main_sub_mask_help_win.title ('Subnet Masks')
        main_sub_mask_label = tk.Label(main_sub_mask_help_win,text = '''A subnet mask is a prefix length written in an IP address format.
It is used to identify different characteristics of an IP address.''',font = ('Bradley Hand Itc',20),bg = 'black',fg = 'white')
        main_sub_mask_label.pack(side = 'top')
        main_sub_mask_help_win.resizable(False,False)
        main_sub_mask_help_win.mainloop()

    def no_hosts_help(self):
        main_no_hosts_help_win = tk.Tk()
        main_no_hosts_help_win.title ('Number of Hosts')
        main_no_hosts_Label = tk.Label(main_no_hosts_help_win,text = '''Number of hosts  means the number of assignable IP addresses in that particular network.
'Hosts' refer to the devices that use IP addresses.''',font = ('Bradley Hand Itc',20),bg = 'black',fg = 'white')
        main_no_hosts_Label.pack(side = 'top')
        main_no_hosts_help_win.resizable(False,False)
        main_no_hosts_help_win.mainloop()


    def no_netw_help(self):
        main_no_netw_help_win = tk.Tk()
        main_no_netw_help_win.title ('Number of Networks')
        main_no_netw_Label = tk.Label(main_no_netw_help_win,text = '''Number of networks refer to the number of networks available for the prefix length specified.
The number of networks means the number of network addresses that are available in that prefix length.''',font = ('Bradley Hand Itc',20),bg = 'black',fg = 'white')
        main_no_netw_Label.pack(side = 'top')
        main_no_netw_help_win.resizable(False,False)
        main_no_netw_help_win.mainloop()

    def block_size_help(self):
        main_block_size_help_win = tk.Tk()
        main_block_size_help_win.title ('Block Sizes')
        main_block_size_Label = tk.Label(main_block_size_help_win,text = '''When a network address is subnetted,
it uses a block size to determine what networks are available in that particular subnetted network.
The block size also aids in determining the number of networks in the subnetted network. ''', font = ('Bradley Hand Itc',20),bg = 'black',fg = 'white')
        main_block_size_Label.pack(side = 'top')
        main_block_size_help_win.resizable (False,False)
        main_block_size_help_win.mainloop()

    def rand_help(self):
        main_rand_help_win = tk.Tk()
        main_rand_help_win.title('Random IP Address')
        main_rand_help_Label = tk.Label(main_rand_help_win,text = '''You can generate a random IP address by clicking on either of the 'class' buttons below.
The IP address generated is based on the class of IP address selected.''', font = ('Bradley Hand Itc',20),bg = 'black',fg = 'white')
        main_rand_help_Label.pack(side = 'top')
        main_rand_help_win.resizable(False,False)
        main_rand_help_win.mainloop()


















