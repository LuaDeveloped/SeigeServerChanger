import os
from configparser import ConfigParser
import tkinter

Window = tkinter.Tk()
Servers = ["australiaeast", "brazilsouth", "centralus", "eastasia", "eastus", "japaneast", "northeurope", "southafricanorth", "southcentralus", "southeastasia", "uaenorth", "westeurope", "westus"]

listbox = tkinter.Listbox(Window, width=50, height = 15)
for i in range(1, len(Servers)):
    listbox.insert(i, Servers[i])
listbox.pack()

def selected_item():
    TargetServer = "centralus"
    for i in listbox.curselection():
        TargetServer = listbox.get(i)
    rootdir = os.path.expanduser("~/Documents/My Games/Rainbow Six - Siege")
    #rootdir = 'C:/Users/Gavin/Documents/My Games/Rainbow Six - Siege'
    SERVER_SELECT = "playfab/"+TargetServer
    for subdir, dirs, file in os.walk(rootdir):
        for name in file:
            if "GameSettings" in name:
                PATH = os.path.join(subdir, name)
                read_config = ConfigParser()
                read_config.read(PATH)
                if "ONLINE" in read_config.sections():
                    read_config.set("ONLINE", "DataCenterHint", SERVER_SELECT)
                    cfgfile = open(PATH,'w')
                    read_config.write(cfgfile)
                    cfgfile.close()

Window.title('Rainbow 6 server selector by LuaDeveloped')
button = tkinter.Button(Window, text='Set Server', width=50, command=selected_item)
button.pack()
Window.mainloop()