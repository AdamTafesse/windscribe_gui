import subprocess

#------------------------------------------------------------
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# When the application is launched…
def on_activate(app):
    # … create a new window…
    win = Gtk.ApplicationWindow(application=app)
    # … with a button in it…
    btn = Gtk.Button(label='Hello, World!')
    # … which closes the window when clicked
    btn.connect('clicked', lambda x: win.destroy())
    win.add(btn)
    win.show_all()

# Create a new application
app = Gtk.Application(application_id='com.example.GtkApplication')
app.connect('activate', on_activate)

# Run the application
app.run(None)

#-------------------------------------------------------------

##def main():
        
   # get = subprocess.run(['grep', 'Ct', 'output.txt'], capture_output=True, text = True)
   # print(get.stdout)
    #out = subprocess.run(['ls','-l'],capture_output=True);  Captures outputs

    #Add text = True as argument to get the output as a string(without newline chars) 
    #with open('output.txt','w') as f:   -->Then "add stdout = f" as an argument to capture to a textfile


    #print(out.stdout)
