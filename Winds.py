#!/usr/bin/env python3

import sys
import subprocess
from subprocess import PIPE, Popen
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class main:

    def __init__(self):

        
       
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("WindsGlade.glade")     
        
        #can connect directly to glade signals without having to do
        #do individual buttons like below
        self.builder.connect_signals(self)         
        
        #statusButton = self.builder.get_object("statusBtn")
        #statusButton.connect('clicked', self.getStatus) 

        window = self.builder.get_object("mainWindow")
        
        #Clicking 'Quit' and closing window quits program
        quitButton = self.builder.get_object("quitBtn")
        quitButton.connect('clicked', Gtk.main_quit)
        window.connect('delete-event',Gtk.main_quit)

        window.show()

   
    def getStatus(self, widget):

        status = subprocess.Popen(['windscribe','status'], stdout = PIPE, text = True)
        self.displayStatus(status)
       
    def connect(self, widget):

        status = subprocess.Popen(['windscribe','connect'], stdout = PIPE, text = True)
        self.displayStatus(status)

    def disconnect(self, widget):

        status = subprocess.Popen(['windscribe','disconnect'], stdout = PIPE, text = True)
        self.displayStatus(status)
        #line = status.stdout.readline()
        #print(line)

    def displayStatus(self,status):
       
        tv = self.builder.get_object("statusTV")
        buffer = tv.get_buffer()

        self.box = self.builder.get_object("vbox")
        self.box.pack_end(tv,True,True,0)        
    
        line = status.communicate()
        #textView = Gtk.TextView()            
        #textView = self.builder.get_object("statusTV")

        for l in line:

            print (buffer.set_text(l))

   
if __name__ == '__main__':
    main = main()
    Gtk.main()


