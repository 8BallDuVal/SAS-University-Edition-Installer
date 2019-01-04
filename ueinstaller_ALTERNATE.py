from tkinter import Tk, WORD, Frame, PhotoImage, Label, Button, RIGHT, LEFT, N, S, W, E, END, Text, SUNKEN, messagebox, DISABLED, filedialog, BOTH
import subprocess
import webbrowser
from tkinter.ttk import *
import os
import glob

class Example(Frame):
    def __init__(self):
        super().__init__()   
        self.initUI()      
    def initUI(self):
        self.master.title("SAS University Edition Install Tool")
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        ### Loading the image ###
        filelocation = __file__
        filepath = filelocation.replace('ueinstaller_ALTERNATE.py','analytics_u.gif')
        analyticsphoto = PhotoImage(file=filepath)
        self.analytics_u_photo = Label(self, image=analyticsphoto, justify=RIGHT)
        self.analytics_u_photo.image = analyticsphoto
        self.analytics_u_photo.grid(row=0, column=2, pady=4, padx=5, sticky=N)
        
        self.messagelabel = Label(self, text='   Welcome to the SAS University Edition Install Tool!\n\n'+
                                        '   Verify that you have Oracle VirtualBox installed and\n'+
                                        '   that you have downloaded the SAS University Edition\n'+
                                        '   vApp and Oracle VirtualBox before running the installer.\n\n', borderwidth=5, relief="ridge")
        self.messagelabel.grid(row=1, column=0, columnspan=4, rowspan=4, 
            padx=7, sticky=E+W+S+N)

        self.quit_button = Button(self, text="Quit", command=self.exit)
        self.quit_button.grid(row=5, column=0, padx=5)

        self.action_button = Button(self, text="Next", command=self.first_action_button_clicked)
        self.action_button.grid(row=5, column=3)        

        self.user = os.getlogin()
        self.downloads = r"C:\Users\{}\Downloads".format(self.user)
        self.shared_folder = r"C:\Users\{}\Documents\SASUniversityEdition\myfolders".format(self.user)
        self.ova_filename = ''
        
        self.checklist = ['SAS','University','"SAS ','"SAS University Edition"','SAS University Edition',
                          'SAS University Edition_1', 'SAS University Edition_2', 'SAS University Edition_3']
    def exit(self):
        '''
        Quits the program
        '''
        self.destroy()
        exit()
    def open_virtualbox_link(self, button_clicked):
        webbrowser.open_new(r"https://www.virtualbox.org/wiki/Downloads")
    def check_vbox_installation(self):
        if os.path.isfile('C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe'):
            return True
        else:
            return False
    def first_action_button_clicked(self):
        if self.check_vbox_installation() == True:
            self.action_button.config(text="Continue", command=self.second_action_button_clicked)
            self.messagelabel.config(text="   Click the 'Continue' button to check to see \n"+
                                          "   if 64-bit Hardware Virtualization is enabled on \n"+
                                          "   your system. If not, you will need to contact \n"+
                                          "   your PC's manufacturer for instructions on how to\n"+
                                          "   enable 64-bit Hardware Virtualization.\n\n", borderwidth=5)
        else:
            self.action_button.config(state=DISABLED)
            messagebox.showerror("Oracle VirtualBox Not Installed","Install Oracle VirtualBox into the default directory"+
                                                                   " (Program Files) before continuing. There will be a link to"+
                                                                   " download and install Oracle VirtualBox on the next screen.")
            self.messagelabel.config(text="Download Oracle VirtualBox", fg="blue", cursor="hand2")
            self.messagelabel.bind("<Button-1>", self.open_virtualbox_link)
    def confirm_vtx_enabled(self):
        '''
        Returns: virtualization status
        Object type: string
        About: Provides the status of the VT-X bios setting in the Windows BIOS Menu
        Notes: N/A
        '''
        try:
            input = subprocess.Popen('systeminfo', shell=False, stdout=subprocess.PIPE)
        except:
            messagebox.showerror("Error","You may need administrator privelages to run this software. "+
                                "Try exiting the program and running as an administrator to resolve this issue.")
        output = input.stdout.read().decode("utf-8")
        if 'Virtualization Enabled In Firmware: Yes' in output:
            return True
        else:
            messagebox.showerror( "Virtualization Check","Virtualization is disabled in Firmware. To resolve this issue, \n"+
                                                        "you need to contact your PC manufacturer for instructions on how\n"+
                                                        "to enter the BIOS menu and enable Virtualization on your device.")
            return False
    def second_action_button_clicked(self):
        self.messagelabel.config(text="Checking system for status of 64-bit Hardware Virtualization...")
        if self.confirm_vtx_enabled() == True:
            self.action_button.config(command=self.third_action_button_clicked)
            self.messagelabel.config(text=" Virtualization was enabled on your system! \n"+
                                          " Click the 'Continue' button to set up your \n"+
                                          " Shared Folders.\n\n")
        else:
            self.messagelabel.config(text=" Virtualization is disabled on your system. You will need\n"+
                                          " to contact your PC manufacturer (Dell, Acer, Lenovo) for\n"+
                                          " instructions on how to enable 64-bit Hardware Virtualization.\n\n")   
    def openfile(self):
        '''
        Allows the user to search their filesystem for another .OVA file 
        (SAS University Edition vApp) using a gui windows file window.
        '''
        self.ova_filename = filedialog.askopenfilename()
        if self.ova_filename.endswith('.ova'):
            print('SAS University Edition vApp File Location: '+self.ova_filename)
        else:
            messagebox.showerror('Wrong Filetype', 'Please select the SAS University Edition vApp file only.'+
                                                    ' The file should end with the following three-letter extension: ".ova".'+
                                                    '\n\n(Example: unvbasicvapp.ova)')
            self.ova_filename = ''
    def choose_shared_folder(self):
        self.shared_folder = filedialog.askdirectory()
        if os.path.isdir(self.shared_folder):
            if self.shared_folder.endswith('myfolders'):
                self.locate_vapp()
            else:
                messagebox.showerror('Misspelled Directory', 'Please select the "myfolders" folder only.'+
                                                    ' The folder must be spelled with all lowercase letters and no spaces. '+
                                                    'Please try again.')
        else:
            messagebox.showerror('Select a directory', 'Please try again, and select the "myfolders" folder only.'+
                                                       'The folder must be spelled with all lowercase letters and no spaces. ')
            self.shared_folder = r"C:\Users\{}\Documents\SASUniversityEdition\myfolders".format(self.user)    
    def third_action_button_clicked(self):
        self.messagelabel.config(text=    " Either choose an existing 'myfolders' folder on \n"+
                                          " your hard drive, or a 'myfolders' folder will be \n"+
                                          " created for you, at the following location:\n"+
                                          self.shared_folder+'\n\n')

        self.action_button.config(command=self.locate_vapp)
        self.choose_sharedfolder = Button(self, text="Choose Folder", command=self.choose_shared_folder)
        self.choose_sharedfolder.grid(row=5, column=2, pady=1)  
    def locate_vapp(self):
        self.action_button.config(command=self.fourth_action_button_clicked)
        self.choose_sharedfolder.grid_remove()
        self.messagelabel.config(text=    " Click the 'Continue' button to scan your hard drive\n"+
                                          " for the SAS University Edition vApp. If it is found,\n"+
                                          " you will move on to the next step. If not, a file \n"+
                                          " explorer window will pop up, allow you to search for\n"+
                                          " it.\n\n")
    def download_UE_ova(self, button_clicked):
        webbrowser.open_new(r"https://login.sas.com/opensso/UI/Login?realm=/extweb&goto=https%3A%2F%2Fwww.sas.com%2Fstore%2Fexpresscheckout.ep%3FstoreCode%3DSAS_US%26storeCode%3DSAS_US%26item%3DDPUNVE001_VirtualBox&req=ph&locale=")
    def fourth_action_button_clicked(self):
        list_of_files = glob.glob(self.downloads+'\\*.ova')
        if list_of_files != []:
            latest_file = max(list_of_files, key=os.path.getctime)
            self.ova_filename = latest_file
        else:
            messagebox.showinfo("Error", "The SAS University Edition vApp was not found in your system's "+
                                         "'Downloads' Folder. Please search"+
                                         " your system files for the location of the SAS University Edition"+
                                         " vApp. \n\nIf you do not yet have the SAS University Edition vApp, you"+
                                         " can download it by clicking on the link on the next screen.")
            self.messagelabel.config(text="Download SAS University Edition vApp", fg="blue", cursor="hand2")
            self.messagelabel.bind("<Button-1>", self.download_UE_ova)
            self.choose_sharedfolder = Button(self, text="Find vApp", command=self.openfile)
            self.choose_sharedfolder.grid(row=5, column=2, pady=1)
        if self.ova_filename !='' and self.ova_filename.endswith('.ova'):
            self.fifth_action_button_clicked()

    def fifth_action_button_clicked(self):
        self.choose_sharedfolder.grid_remove()
        self.action_button.config(command=self.check_duplicates)
        self.messagelabel.config(text=    " Click the 'Continue' button to verify that you do\n "+
                                          " not have any duplicate SAS University Edition VMs\n "+
                                          " imported into Oracle VirtualBox. \n\n")
    def run_command(self, command):
        p = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        return iter(p.stdout.readline, b'')
    def check_duplicate_vms(self):
        command = '"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe" list vms'
        for line in self.run_command(command):
                        output = line.decode('utf-8').split()
                        for word in output:
                            if word in self.checklist:
                                messagebox.showerror('Already imported', 'You have already imported SAS University Edition into Oracle VirtualBox.'+
                                                                    ' Please remove all SAS University Edition Virtual Machines from Oracle '+
                                                                    'VirtualBox before proceeding. To remove them, open Oracle VirtualBox and'+
                                                                    ' right-click on the "SAS University Edition - Powered Off"'+
                                                                    ' tab, then hit remove --> Delete All Files. Do this for all existing SAS '+
                                                                    'University Edition Virtual Machines in VirtualBox.')
                                notimported = False
                                return notimported
        noduplicates = True
        return noduplicates    
    def check_vbox_vms_folder(self):
        vboxvmsfolder = 'C:\\Users\\'+os.getlogin()+'\\VirtualBox VMs'
        vboxvms = os.listdir(vboxvmsfolder)
        
        if vboxvms != []:
            for item in self.checklist:
                if item in vboxvms:
                    messagebox.showerror('Already imported','The virtual machine "'+ item+'" was removed from Oracle VirtualBox incorrectly. '+
                                                            'Please delete all SAS University Edition folder(s) from the '+
                                                            'following location: \n\n'+vboxvmsfolder)
                    return False
        
        test = True
        return test
    def check_duplicates(self):
        if self.check_duplicate_vms() == True:
            if self.check_vbox_vms_folder() == True:
                self.sixth_action_button_clicked()
    def sixth_action_button_clicked(self):
        self.write_batchfile()
        self.action_button.config(text='Import')
        self.action_button.config(command=self.seventh_action_button_clicked)
        self.messagelabel.config(text=    " Click the 'Import' button to import the SAS University\n "+
                                          " Edition vApp into Oracle VirtualBox. This may take a few\n "+
                                          " moments. \n\n")
    def write_batchfile(self):
        batchfile = open("Install_SAS_University_Edition.bat", 'w')
        batchfile.write(r'set PATH=%PATH%;"C:\Program Files\Oracle\VirtualBox"')
        batchfile.write('\n')
        batchfile.write('VBoxManage import '+self.ova_filename)
        batchfile.write('\n')
        if os.path.isdir(self.shared_folder):
            batchfile.write('VBoxManage sharedfolder add "SAS University Edition" --name myfolders --hostpath '+self.shared_folder+' --automount')
        else:
            batchfile.write('MKDIR '+self.shared_folder)
            batchfile.write('\n')
            batchfile.write('VBoxManage sharedfolder add "SAS University Edition" --name myfolders --hostpath '+self.shared_folder+' --automount')                   
        batchfile.close()
    def import_ova_file(self):
        try:
            subprocess.call("Install_SAS_University_Edition.bat")
            messagebox.showinfo("Successfully Installed","SAS University Edition has now been imported into Oracle VirtualBox.\n\n"+
                                "A shared folder was created at the following location:\n"+
                                self.shared_folder+'\n\n')
            self.successful_import()
        except:
            messagebox.showerror("Error","There was an issue installing SAS University Edition. "+
                                         "Try running the 'Install_SAS_University_Edition.bat' file "+
                                         "with administrator privelages.")       
    def seventh_action_button_clicked(self):
        self.import_ova_file()
    def successful_import(self):
        self.action_button.config(text='Run')
        self.action_button.config(command=self.run_button_clicked)
        self.messagelabel.config(text=    " You are now finished setting up SAS University Edition. \n "+
                                          " Click the 'Run' button to run Oracle VirtualBox \n "+
                                          " and quit the Installer. \n\n")
    def run_button_clicked(self):
        '''
        Allows users to run Oracle VirtualBox after a successful import and quit the installer.
        '''
        try:
            subprocess.Popen(['C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe'])
            messagebox.showinfo("Successfully Installed","The SAS University Edition Install Tool will quit "+
                                "after clicking OK. You can now begin using SAS University Edition in Oracle VirtualBox "+
                                "by right-clicking 'SAS University Edition' and hitting 'Start'.")
            self.quit()
        except:
            messagebox.showerror("Error","You may need administrator privelages to open Oracle VirtualBox. "+
                                 "Try opening Oracle VirtualBox manually by searching for 'Oracle VirtualBox' "+
                                 "in the Windows Search Bar (bottom left hand corner of the screen).")

def main():
    root = Tk()
    root.geometry("350x300+300+300")
    app = Example()
    root.mainloop()  

if __name__ == '__main__':
    main()  
