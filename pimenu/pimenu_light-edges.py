#!/usr/bin/python3
# -*- coding: utf-8 -*-
#import Tkconstants as TkC #for python2
import os
import subprocess
import sys
from tkinter import *
from math import sqrt, floor, ceil
#from tkinterhtml import HtmlFrame as HTMLLabel #import the HTML browser #HtmlLabel as
import json
import webbrowser

from tkinter import (
        constants as TkC,
)
def pi_apps_mainpage():
    os.system("x-www-browser https://github.com/botspot/pi-apps >/dev/null &")
    quit()
class SimpleFlatButton(Button):
    def __init__(self, master=None, cnf=None, **kw):
        Button.__init__(self, master, cnf, **kw)

        self.config(
            compound=TkC.TOP,
            relief=TkC.FLAT,
            bd=0,
            bg="#b91d47",  # dark-red
            fg="white",
            activebackground="#b91d47",  # dark-red
            activeforeground="white",
            highlightthickness=0
        )

    def set_color(self, color):
        self.configure(
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white"
        )
        
def colorscale(self, hexstr, scalefactor):
    #pylint: disable=unused-argument
    hexstr = hexstr.strip('#')

    if scalefactor < 0 or len(hexstr) != 6:
        return hexstr

    r, g, b = int(hexstr[:2], 16), int(hexstr[2:4], 16), int(hexstr[4:], 16)

    r = clamp(r + scalefactor)
    g = clamp(g + scalefactor)
    b = clamp(b + scalefactor)

    return "#%02x%02x%02x" % (r, g, b)

def clamp(val, minimum=0, maximum=255):
    if val < minimum:
        return minimum
    if val > maximum:
        return maximum
    return val

class FlatButton(Button):
    def __init__(self, master=None, cnf=None, **kw):
        Button.__init__(self, master, cnf, **kw)

        self.config(
            compound=TkC.TOP,
            relief=TkC.FLAT,
            bd=0,
            bg="#b91d47",  # dark-red
            fg="white",
            activebackground=colorscale(self, "#b91d47", 30),  # dark-red
            activeforeground="white",
            highlightthickness=2,
            highlightbackground=colorscale(self, "#b91d47", 60)
        )

    def set_color(self, color):
        self.configure(
            bg=color,
            fg="white",
            activebackground=colorscale(self, color, 30),
            activeforeground="white",
            highlightbackground=colorscale(self, color, 60)
        )

class PiMenu(Frame):
    framestack = []
    icons = {}
    path = ''
    lastinit = 0

    def __init__(self, parent,pabc):
        Frame.__init__(self, parent, bg=pabc)
        self.parent = parent
        self.pack(fill=TkC.BOTH, expand=1)
        self.bg=pabc

        self.path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.initialize()

    def initialize(self):
        """
        (re)load the the items from the json configuration and (re)init
        the whole menu system

        :return: None
        """
        with open(self.path + '/../tmp.json', 'r') as f:
            file=f.readline()
            doc = json.loads(file)


        if len(self.framestack):
            self.destroy_all()
            self.destroy_top()
        item1=doc[0]
        if item1['label'] == 'App Details':
           self.load_app(doc[1])
        else:
            self.show_items(doc)
    def load_app(self,item):
        app_details_frame = Frame(self,bg=self.bg)
        #functions
        def gotowebsite(*args): #open website and close pimenu
            os.system("x-www-browser " + item['website'] + " >/dev/null &")
            quit()
            
        def back():#go back to app menu using pimenu.sh script
            os.system(self.path + '/pimenu.sh' + ' ' + '.reload')# bash instance
            app_details_frame.destroy()#----destroy details
            self.initialize()          #----reload script
        
        #App label, status and icon + back button
        #get the icon for app label
        icon = self.get_icon(item['icon'])
        print('Status Message:App Details\n')
        print("Status Message:" + item['name'])# + "\n" + item['status'] + "\n")
        app_label_frame=Frame(app_details_frame, bg=self.bg)
        
        #back button
        back_button=SimpleFlatButton(app_label_frame, image=self.get_icon('xzxzxzxzxzxzxzxzxzx'))
        back_button.set_color(self.bg)
        back_button.configure(command=back)
        back_button.pack(side='left')
        
        #display label
        app_label = Label(app_label_frame, text= item['name'] + "\n" + item['status'] + "\n" + item['website'], font="Helvetica 12", anchor='nw', justify='left', image=icon,compound='left', bg=self.bg)
        app_label.pack(side='left')#grid(column=1,row=0)
        app_label_frame.pack(anchor='nw',fill='x')
        app_label.bind('<1>', gotowebsite)
        print("Status Message:" + item['website'] + "\n")
        
        # app managing buttons
        def install():
            print("install " + item['name'])
        def uninstall():
            print("uninstall " + item['name'])
        manage_buttons_frame=Frame(app_label_frame)
        manage_buttons_frame.config(width=100)
        if item['status'] == '(uninstalled)':
            install_btn=FlatButton(manage_buttons_frame, image=self.get_icon(self.path + '/../icons/install.png'), text=" Install... ",command=install)
            install_btn.set_color('green')
            install_btn.pack(side='right',fill='both',expand=1)
            btn_place=self.winfo_width()
        if item['status'] == '(installed)':
            uninstall_btn=FlatButton(manage_buttons_frame, image=self.get_icon(self.path + '/../icons/uninstall.png'), text="Uninstall...",command=uninstall)
            uninstall_btn.set_color('red')
            uninstall_btn.pack(side='right',fill='both',expand=1)
            btn_place=self.winfo_width()
        if item['status'] == '(corrupted)':
            manage_buttons_frame.config(width=200)
            uninstall_btn=FlatButton(manage_buttons_frame, image=self.get_icon(self.path + '/../icons/uninstall.png'), text="Uninstall...",command=uninstall)
            uninstall_btn.set_color('red')
            uninstall_btn.pack(side='right',fill='both',expand=1)
            btn_place=self.winfo_width()
            install_btn=FlatButton(manage_buttons_frame, image=self.get_icon(self.path + '/../icons/install.png'), text=" Install... ",command=uninstall)
            install_btn.set_color('green')
            install_btn.pack(side='right',fill='both',expand=1)
            btn_place=self.winfo_width()
        manage_buttons_frame.pack(side='right', fill='y')
        
        #Description
        with open(item['description'], 'r') as f:
            description=f.readlines()
        textframe=Frame(app_details_frame)
        textframe.pack(side="left", fill=TkC.BOTH,expand=1)
        text=""
        for i in description:
            print("Description Message: " + i)
            text=text + "\n" + i
        description=Text(textframe, wrap = WORD)
        description.pack(fill=TkC.BOTH,expand=1)
        description.insert('1.0', text)
        description['state'] = 'disabled'
        
        #End of description script
        app_details_frame.pack(fill=TkC.BOTH,expand=1) # affichage
        
    def has_config_changed(self):
        """
        Checks if the configuration has been changed since last loading

        :return: Boolean
        """
        return self.lastinit != os.path.getmtime(self.path + '/pimenu.yaml')

    def show_items(self, items, upper=None):
        """
        Creates a new page on the stack,

        :param items: list the items to display
        :param upper: list previous levels' ids
        :return: None
        """
        if upper is None:
            upper = []
        num = 0
        
        # create a new frame
        wrap = Frame(self, bg=self.bg)

        if len(self.framestack):
            # when there were previous frames, hide the top one and add a back button for the new one
            self.hide_top()
            back = FlatButton(
                wrap,
                text='back',
                image=self.get_icon("arrow.left"),
                command=self.go_back,
            )
            back.set_color("#00a300")  # green
            back.grid(row=0, column=0, padx=0, pady=0, sticky=TkC.W + TkC.E + TkC.N + TkC.S)
            num += 1

        # add the new frame to the stack and display it
        self.framestack.append(wrap)
        self.show_top()

        # calculate tile distribution
        allitems = len(items) + num
        rows = floor(sqrt(allitems))
        cols = ceil(allitems / rows)

        # make cells autoscale
        for x in range(int(cols)):
            wrap.columnconfigure(x, weight=1)
        for y in range(int(rows)):
            wrap.rowconfigure(y, weight=1)

        # display all given buttons
        for item in items:
            act = upper + [item['name']]

            if 'icon' in item:
                image = self.get_icon(item['icon'])
            else:
                image = self.get_icon('scrabble.' + item['label'][0:1].lower())

            btn = FlatButton(
                wrap,
                text=item['label'] + "\n" + item['status'],
                image=image
            )

            if 'items' in item:
                # this is a deeper level
                btn.configure(command=lambda act=act, item=item: self.show_items(item['items'], act),
                              text=item['label'])
                btn.set_color("#2b5797")  # dark-blue
            else:
                # this is an action
                btn.configure(command=lambda act=act: self.go_action(act), )

            if 'color' in item:
                btn.set_color(item['color'])

            # add buton to the grid
            btn.grid(
                row=int(floor(num / cols)),
                column=int(num % cols),
                padx=0,
                pady=0,
                sticky=TkC.W + TkC.E + TkC.N + TkC.S
            )
            num += 1

    def get_icon(self, name):
        """
        Loads the given icon and keeps a reference

        :param name: string
        :return:
        """
        if name in self.icons:
            return self.icons[name]

        ico = name
        if not os.path.isfile(ico):
            ico = self.path + '/ico/' + name + '.gif'
            if not os.path.isfile(ico):
                ico = self.path + '/ico/cancel.gif'

        self.icons[name] = PhotoImage(file=ico)
        return self.icons[name]

    def hide_top(self):
        """
        hide the top page
        :return:
        """
        self.framestack[len(self.framestack) - 1].pack_forget()

    def show_top(self):
        """
        show the top page
        :return:
        """
        self.framestack[len(self.framestack) - 1].pack(fill=TkC.BOTH, expand=1)

    def destroy_top(self):
        """
        destroy the top page
        :return:
        """
        self.framestack[len(self.framestack) - 1].destroy()
        self.framestack.pop()

    def destroy_all(self):
        """
        destroy all pages except the first aka. go back to start
        :return:
        """
        while len(self.framestack) > 1:
            self.destroy_top()

    def go_action(self, actions):
        """
        execute the action script
        :param actions:
        :return:
        """
        # hide the menu and show a delay screen
        self.hide_top()
        #delay = Frame(self, bg="#2d89ef")
        #delay.pack(fill=TkC.BOTH, expand=1)
        #label = Label(delay, text="Executing...", fg="white", bg="#2d89ef", font="Sans 30")
        #label.pack(fill=TkC.BOTH, expand=1)
        self.parent.update()

        # excute shell script
        subprocess.call([self.path + '/pimenu.sh'] + actions)

        # remove delay screen and show menu again
        #delay.destroy()
        self.destroy_all()
        #quit
        self.initialize()

    def go_back(self):
        """
        destroy the current frame and reshow the one below, except when the config has changed
        then reinitialize everything
        :return:
        """
        if self.has_config_changed():
            self.initialize()
        else:
            self.destroy_top()
            self.show_top()

def quit_pi_apps():
    print("exit")
    quit()
    

def main():
    root = Tk()
    root.geometry("640x480")
    root.wm_title('PiMenu')
    root.attributes('-alpha',0.0)
    pabcf = open(os.path.dirname(os.path.realpath(sys.argv[0])) + "/settings/Pi_apps_button_color")
    pabc = pabcf.read()

    if len(sys.argv) > 2 and sys.argv[2] == 'fs':
        root.wm_attributes('-fullscreen', True)
    btn_frame = Frame(root, bg=pabc)
    img = PhotoImage(file=os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0]))) + "/icons/proglogo.png")
    pi_apps_btn = SimpleFlatButton(btn_frame, image=img, command=pi_apps_mainpage, text=sys.argv[1])#
    pi_apps_btn.set_color(pabc)
    pi_apps_btn.pack()
    close_btn_image=PhotoImage(file=os.path.dirname(os.path.realpath(sys.argv[0])) + "/ico/close.png")
    close_btn=SimpleFlatButton(btn_frame,text="Close", image=close_btn_image, command=quit_pi_apps )
    close_btn.set_color(pabc)
    btn_frame.update()
    #When tkhtml will work 
    #Tips = HTMLLabel(btn_frame, text=sys.argv[1])
    #Tips.pack()
    piframe = Frame(root, bg=pabc)
    btn_frame.pack(padx=1,pady=1, fill=TkC.BOTH)
    btn_frame.update()
    
    os.system(os.path.dirname(os.path.realpath(sys.argv[0])) + '/updateyaml reset')
    close_btn.place(x = btn_frame.winfo_width() - 96 , y = 0)
    piframe.pack(fill=TkC.BOTH, expand=1)
    PiMenu(piframe,pabc)
    root.mainloop()
    #btn_frame.winfo_width()

if __name__ == '__main__':
    main()
