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
import base64

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
        base64_image = b'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'
        analyticsphoto = PhotoImage(data=base64.b64decode(base64_image))
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
