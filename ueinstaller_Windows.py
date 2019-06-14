'''
Created on Nov 16, 2018

@author: daduva
'''
#import time
#start_time = time.time()
from tkinter import Tk, WORD, Frame, PhotoImage, Label, Button, RIGHT, LEFT, N, S, W, E, END, Text, SUNKEN, messagebox, DISABLED, filedialog
import os
import glob
import subprocess
import webbrowser


class UniversityEditionInstaller:
    def __init__(self, window):
        '''
        Initializes the following objects:
        self.window
        self.top_frame
        self.bottom_frame
        self.center_frame
        self.lowest_frame
        self.analytics_u_photo 
        self.virtualbox_link 
        self.OVA_link
        self.welcome_label
        self.exit_button
        self.run_button
        self.install_button
        self.vtx_check_btn
        self.user
        self.downloads
        self.shared_folder
        self.contact_support
        self.checklist
        self.ova_filename
        self.latest_file
        '''
        ### Build the GUI window ###
        self.window = window
        self.window.title("SAS University Edition Install Tool")
        self.window.geometry("430x540")
    
        ### Build Frames ###
        # "flat", "raised", "sunken", "ridge", "solid", and "groove"
        self.top_frame = Frame(self.window, width=200, height=100, padx=5,pady=5)
        self.bottom_frame= Frame(self.window, width=600, height=247, padx=5, pady=5, borderwidth=10, relief="raised")
        self.center_frame = Frame(self.window, width=747, height=300, padx=5, pady=5, borderwidth=10, relief="flat")
        self.lowest_frame = Frame(self.window, width=747, height=300, padx=5,pady=5, borderwidth=10, relief="ridge")
        ### Layout frames ###
        self.top_frame.grid(row=0, sticky='n')
        self.center_frame.grid(row=1,sticky='nsew')
        self.bottom_frame.grid(row=2, sticky='s')
        self.lowest_frame.grid(row=3, sticky='s')
        
        ### add logo photo ###
        filelocation = __file__
        filepath = filelocation.replace('ueinstaller.py','analytics_u.gif')
        analyticsphoto = PhotoImage(file=filepath)
        self.analytics_u_photo = Label(self.top_frame, image=analyticsphoto, justify=RIGHT)
        self.analytics_u_photo.image = analyticsphoto
        self.analytics_u_photo.pack()
        
        ### add a link to download Oracle VirtualBox ###
        self.virtualbox_link = Label(self.center_frame, text="Download Oracle VirtualBox", fg="blue", cursor="hand2")
        self.virtualbox_link.grid(row=0,column=0,sticky=N)
        self.virtualbox_link.bind("<Button-1>", self.open_virtualbox_link)
        
        ### add a link to download the SAS University Edition OVA file ###
        self.OVA_link = Label(self.center_frame, text="Download SAS University Edition vApp", fg="blue", cursor="hand2")
        self.OVA_link.grid(row=1,column=0,sticky=N)
        self.OVA_link.bind("<Button-1>", self.download_UE_ova)

        ### Add welcome label ###    
        self.welcome_label = Label(self.center_frame,
                                   text='\nWelcome to the SAS University Edition Install Tool!\n\n'+
                                        'Verify that you have Oracle VirtualBox installed and that you have \n'+
                                        'downloaded the SAS University Edition vApp before running the installer.\n\n'+
                                        'Complete steps 1-3 below to configure SAS University Edition:\n\n'+
                                        "1. Click on 'Virtualization Check' to check if virtualization has been Enabled.\n"+
                                        "2. Click 'Install' to import SAS University Edition into Oracle VirtualBox.\n"+
                                        "3. Click 'Open VirtualBox' to open Oracle VirtualBox after a successful \nimport.")
        self.welcome_label.grid(row=2, column=0, sticky=W)
        ### Add "Exit" Button ###
        self.exit_button = Button(self.bottom_frame, text="Quit", width=10, height=2, command=self.quit, cursor="hand2")
        self.exit_button.grid(row=3, column=0, sticky=W)

        ### Add "Run" Button ###
        self.run_button = Button(self.bottom_frame, text="Open \nVirtualBox", state=DISABLED, width=10, height=2, command=self.run_button_clicked, cursor="hand2")
        self.run_button.grid(row=3, column=3, sticky=W)

        ### Add "Install" Button ###
        self.install_button = Button(self.bottom_frame, text="Install", state=DISABLED, width=10, height=2, command=self.install_button_clicked, cursor="hand2")
        self.install_button.grid(row=3, column=6, sticky=E)

        ### Add "Virtualization Check" Button ###
        self.vtx_check_btn = Button(self.bottom_frame, text="Virtualization Check", width=15, height=2, command=self.confirm_vtx_enabled, cursor="hand2")
        self.vtx_check_btn.grid(row=3, column=9, sticky=W)

        self.user = os.getlogin()

        self.downloads = r"C:\Users\{}\Downloads".format(self.user)
        self.shared_folder = r"C:\Users\{}\Documents\SASUniversityEdition\myfolders".format(self.user)

        ### add a "Contact Technical Support" textbox and links
        self.contact_support = Label(self.lowest_frame, text="Contact SAS Technical Support", fg="blue", cursor="hand2")
        self.contact_support.grid(row=2, column=0, sticky=W)
        self.contact_support.bind("<Button-1>", self.contact_ts)
    
        self.checklist = ['SAS','University','"SAS ','"SAS University Edition"','SAS University Edition',
                          'SAS University Edition_1', 'SAS University Edition_2', 'SAS University Edition_3']

        self.ova_filename = ''
        self.latest_file = ''

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

    def contact_ts(self, button_clicked):
        webbrowser.open_new(r"https://www.sas.com/en_us/contact.html")
    
    def open_virtualbox_link(self, button_clicked):
        webbrowser.open_new(r"https://www.virtualbox.org/wiki/Downloads")

    def download_UE_ova(self, button_clicked):
        webbrowser.open_new(r"https://login.sas.com/opensso/UI/Login?realm=/extweb&goto=https%3A%2F%2Fwww.sas.com%2Fstore%2Fexpresscheckout.ep%3FstoreCode%3DSAS_US%26storeCode%3DSAS_US%26item%3DDPUNVE001_VirtualBox&req=ph&locale=")

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
        

    def quit(self):
        '''
        Quits the program
        '''
        self.window.destroy()

    def install_button_clicked(self):
        r'''
        Obtains user data (OS Login for accurate filepaths) and then writes a batch file using user data.
        It only writes this batch file if Oracle VirtualBox was successfully installed into the following directory:

        C:\Program Files\Oracle\VirtualBox

        Then, it runs the batch file, which will import SAS University Edition into
        Oracle VirtualBox.

        Batch File contents:
        "
        set PATH=%PATH%;"C:\Program Files\Oracle\VirtualBox"
        VBoxManage import "C:\Users\%USERNAME%\Downloads\<Most_recently_downloaded_SAS_University_Edition_vApp.ova>"
        MKDIR "C:\Users\%USERNAME%\Documents\SASUniversityEdition\myfolders"
        VBoxManage sharedfolder add "SAS University Edition" --name myfolders --hostpath "C:\Users\%USERNAME%\Documents\SASUniversityEdition\myfolders" --automount
        "
        '''
        if os.path.isdir('C:\\Program Files\\Oracle\\VirtualBox'):
            if os.path.isfile('C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe'):
                if self.check_duplicate_vms() == True and self.check_vbox_vms_folder() == True:
                    if glob.glob(self.downloads+'\\*.ova') == [] and self.ova_filename == '':
                        messagebox.showinfo("Error", "The SAS University Edition vApp was not found in your system's "+
                                                    "'Downloads' Folder. Please search"+
                                                    " your system files for the location of the SAS University Edition"+
                                                    " vApp. \n\nIf you do not yet have the SAS University Edition vApp, you"+
                                                    " can download it by clicking on the link at the top of the application.")
                                ### choose another file location###
                        self.openfile()        

                    else:
                        if self.latest_file == '' and self.ova_filename != '':
                            self.latest_file = self.ova_filename
                            self.write_batchfile()
                        else:
                            list_of_files = glob.glob(self.downloads+'\\*.ova')
                            self.latest_file = max(list_of_files, key=os.path.getctime)
                            self.write_batchfile()

        else:
            messagebox.showerror("Error","Oracle VirtualBox was not installed successfully, or the default settings were modified. "+
                                "Please install Oracle VirtualBox with the default settings and do not modify the installation "+
                                "path (C:\\Program Files\\Oracle\\VirtualBox\\)")

    def write_batchfile(self):
        batchfile = open("Install_SAS_University_Edition.bat", 'w')
        batchfile.write(r'set PATH=%PATH%;"C:\Program Files\Oracle\VirtualBox"')
        batchfile.write('\n')
        batchfile.write('VBoxManage import '+self.latest_file)
        batchfile.write('\n')
        batchfile.write('MKDIR '+self.shared_folder)
        batchfile.write('\n')
        batchfile.write('VBoxManage sharedfolder add "SAS University Edition" --name myfolders --hostpath '+self.shared_folder+' --automount')                   
        batchfile.close()
        self.import_ova_file()

    def import_ova_file(self):
        try:
            subprocess.call("Install_SAS_University_Edition.bat")
            self.window.update()

            messagebox.showinfo("Successfully Installed","SAS University Edition has now been imported into Oracle VirtualBox.\n\n"+
                                "A shared folder was created for you at the following location:\n"+
                                self.shared_folder+'\n\n')
            self.run_button.config(state="normal")
        except:
            messagebox.showerror("Error","There was an issue installing SAS University Edition. "+
                                         "Try running the 'Install_SAS_University_Edition.bat' file "+
                                         "with administrator privelages.")        

            
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
                messagebox.showinfo( "Virtualization Check", "Virtualization is Enabled in Firmware.")
                self.install_button.config(state="normal")
            else:
                messagebox.showerror( "Virtualization Check", "Virtualization is disabled in Firmware. To resolve this issue, \n"+
                                                            "you need to contact your PC manufacturer for instructions on how\n"+
                                                            "to enter the BIOS menu and enable Virtualization on your device.")

    def run_button_clicked(self):
        '''
        Allows users to run Oracle VirtualBox after a successful import and quit the installer.
        '''
        try:
            subprocess.Popen(['C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe'])
            messagebox.showinfo("Successfully Installed","The SAS University Edition Install Tool will quit "+
                                "after clicking OK. You can now begin using SAS University Edition in Oracle VirtualBox "+
                                "by right-clicking 'SAS University Edition' and hitting 'Start'.")
            self.window.destroy()
        except:
            messagebox.showerror("Error","You may need administrator privelages to open Oracle VirtualBox. "+
                                 "Try opening Oracle VirtualBox manually by searching for 'Oracle VirtualBox' "+
                                 "in the Windows Search Bar (bottom left hand corner of the screen).")

if __name__ == "__main__":
    root = Tk()
    UEInstallerGUI = UniversityEditionInstaller(root)
    root.update()
    root.mainloop()
