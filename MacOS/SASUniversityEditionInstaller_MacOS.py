#!/usr/bin/env python

from Tkinter import *
import subprocess
import webbrowser
import os
import glob
import tkMessageBox
import tkFileDialog

class Installer(Frame, object):
    def __init__(self):
        super(Installer, self).__init__()   
        self.initUI()      
    def initUI(self):
        self.master.update_idletasks()
        self.master.update()
        self.master.title(u"SAS University Edition Install Tool")
        self.pack(fill=BOTH, expand=True)
        
        self.grid_columnconfigure(0,weight=1,uniform='x')
        self.grid_columnconfigure(1, weight=1,uniform='y')
        self.grid_columnconfigure(2,weight=1,uniform='x')
        self.grid_rowconfigure(0, weight=0,uniform='z')
        self.rowconfigure(3, weight=1,uniform='w')
        self.rowconfigure(5, weight=0,uniform='z')

        ### Loading the image ###
        base64_image = b'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'.decode('base64')
        self.analyticsphoto = PhotoImage(data=base64_image)
        self.analytics_u_photo = Label(self, image=self.analyticsphoto, justify=CENTER)
        self.analytics_u_photo.grid(row=0, column=1, sticky=N)
        
        self.messagelabel = Label(self, text=u' Welcome to the SAS University Edition Install Tool!\n\n'+
                                        u' Verify that you have Oracle VirtualBox installed and that you downloaded the\n'+
                                        u' SAS University Edition vApp before running the installer.\n\n', borderwidth=5, relief=u"ridge")
        self.messagelabel.grid(row=1, column=0, columnspan=3, rowspan=4, 
            padx=7, sticky=N+W+E+S)

        self.quit_button = Button(self, text=u"Quit", command=self.exit)
        self.quit_button.grid(row=5, column=0, padx=5, pady=5)

        self.action_button = Button(self, text=u"Next", command=self.first_action_button_clicked)
        self.action_button.grid(row=5, column=2, padx=5, pady=5)        

        self.user = os.getlogin()
        self.home = "/Users/{}".format(self.user)
        self.downloads = self.home+ "/Downloads" 
        self.desktop = self.home+ "/Desktop" 
        self.documents = self.home+ "/Documents"

        self.shared_folder = self.home + "/Documents/SASUniversityEdition/myfolders"
        self.vbox_installation_path = "/Applications/VirtualBox.app/Contents/MacOS/"
        self.vbox_manage_path = "/Applications/VirtualBox.app/Contents/MacOS/VBoxManage"
        self.ova_filename = u''
        self.checklist = [u'SAS',u'University',u'"SAS ',u'"SAS University Edition"',u'SAS University Edition',
                          u'SAS University Edition_1', u'SAS University Edition_2', u'SAS University Edition_3']
        self.master.update_idletasks()
        self.master.update()
    def exit(self):
        u'''
        Quits the program
        '''
        self.destroy()
        exit()
#----- Step 1: Check if VirtualBox is installed -----#
    def open_virtualbox_link(self, button_clicked):
        webbrowser.open_new(ur"https://www.virtualbox.org/wiki/Downloads")
    def check_vbox_installation(self):
        if os.path.isfile(self.vbox_manage_path):
            return True
        else:
            return False
    def first_action_button_clicked(self):
        if self.check_vbox_installation() == True:
            self.action_button.config(text=u"Continue", command=self.second_action_button_clicked)
            self.messagelabel.config(text=u" Click the 'Continue' button to set up your Shared Folders.\n\n")
            self.master.update_idletasks()
            self.master.update()
        else:
            self.action_button.config(state=DISABLED)
            tkMessageBox.showerror(u"Oracle VirtualBox Not Installed",u"Install Oracle VirtualBox into the default directory"+
                                                                   u" (Program Files) before continuing. There will be a link to"+
                                                                   u" download and install Oracle VirtualBox on the next screen.")                                     
            self.messagelabel.config(text=u"\t\t\tDownload Oracle VirtualBox", foreground=u"blue", cursor=u"hand2")
            self.messagelabel.bind(u"<Button-1>", self.open_virtualbox_link)                                              
#----- Step 2: Set up Shared folder (either the default directory or user-selected) -----#
    def openfile(self):
        u'''
        Allows the user to search their filesystem for another .OVA file 
        (SAS University Edition vApp) using a gui windows file window.
        '''
        self.ova_filename = tkFileDialog.askopenfilename()
        if self.ova_filename.endswith(u'.ova'):
            self.fourth_action_button_clicked()
        else:
            tkMessageBox.showerror(u'Wrong Filetype', u'Please select the SAS University Edition vApp file only.'+
                                                    u' The file should end with the following three-letter extension: ".ova".'+
                                                    u'\n\n(E.g.: unvbasicvapp.ova)')
            self.ova_filename = u''
    def choose_shared_folder(self):
        self.shared_folder = tkFileDialog.askdirectory()
        if os.path.isdir(self.shared_folder):
            if self.shared_folder.endswith(u'myfolders'):
                self.locate_vapp()
            else:
                tkMessageBox.showerror(u'Misspelled Directory', u'Please select the "myfolders" folder only.'+
                                                    u' The folder must be spelled with all lowercase letters and no spaces. '+
                                                    u'Please try again.')
        else:
            tkMessageBox.showerror(u'Select a directory', u'Please try again, and select the "myfolders" folder only.'+
                                                       u'The folder must be spelled with all lowercase letters and no spaces. ')  
    def second_action_button_clicked(self):
        self.messagelabel.config(text=    u" Either choose an existing 'myfolders' folder on your hard drive, or a 'myfolders' \n"+
                                          u" folder will be created for you, at the following location:\n\n"+
                                          u' ' + self.shared_folder+u'\n\n')
        self.action_button.config(command=self.locate_vapp)
        self.choose_sharedfolder = Button(self, text=u"Choose Folder", command=self.choose_shared_folder)
        self.choose_sharedfolder.grid(row=5, column=1,  padx=5, pady=5)  
        self.master.update_idletasks()
        self.master.update()
#----- Step 3: Locate vApp (auto-searches the Downloads folder. If not found, user must search for it) -----#    
    def locate_vapp(self):
        self.action_button.config(command=self.third_action_button_clicked)
        self.choose_sharedfolder.destroy()
        self.messagelabel.config(text=    u" Click the 'Continue' button to scan your hard drive for the SAS University Edition \n"+
                                          u" vApp. If it is found, you will move on to the next step. If not, click the 'Find vApp'\n"+
                                          u" button on the next screen, which will allow you to search for it manually.\n\n")
    def download_UE_ova(self, button_clicked):
        webbrowser.open_new(ur"https://login.sas.com/opensso/UI/Login?realm=/extweb&goto=https%3A%2F%2Fwww.sas.com%2Fstore%2Fexpresscheckout.ep%3FstoreCode%3DSAS_US%26storeCode%3DSAS_US%26item%3DDPUNVE001_VirtualBox&req=ph&locale=")
    def third_action_button_clicked(self): 
        downloads_files = glob.glob(self.downloads+'/*.ova')
        desktop_files = (glob.glob(self.desktop+'/*.ova'))
        documents_files = (glob.glob(self.documents+'/*.ova'))
        if downloads_files or desktop_files or documents_files:
            latest_file = max(downloads_files+desktop_files+documents_files, key=os.path.getctime)
            self.ova_filename = latest_file
        else:
            tkMessageBox.showinfo(u"Error", u"The SAS University Edition vApp was not found in your system's "+
                                         u"'Downloads' Folder. \n\nPlease search your system files for the location "+
                                         u"of the SAS University Edition vApp by clicking on the 'Find vApp' button on the"+
                                         u" next page. \n\nIf you do not yet have the SAS University Edition vApp,"+
                                         u" you can download it by clicking on the link on the next screen.")
            
            self.messagelabel.config(text=u"\t\t\tDownload SAS University Edition vApp", foreground=u"blue", cursor=u"hand2")
            self.messagelabel.bind(u"<Button-1>", self.download_UE_ova)
            self.action_button.config(text=u"Find vApp", command=self.openfile) 
            self.master.update_idletasks()
            self.master.update()
        if self.ova_filename.endswith(u'.ova'):
            self.fourth_action_button_clicked()
#----- Step 4: Checks for duplicate VMs in VirtualBox and 'SAS University Edition' folders in the 'VirtualBox VMs' folder. -----#  
    def fourth_action_button_clicked(self):
        self.action_button.config(text= 'Check Duplicates', command=self.check_duplicates)
        self.messagelabel.config(text=u" Click the 'Continue' button to verify that you do not have any duplicate SAS\n"+
                                      u" University Edition VMs imported into Oracle VirtualBox.\n\n")
        self.master.update_idletasks()
        self.master.update()
    def run_command(self, command):
        p = subprocess.Popen(command,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        return iter(p.stdout.readline, '')
    def check_duplicate_vms(self):
        command = self.vbox_manage_path+u' list vms'
        for line in self.run_command(command):
                        output = line.decode(u'utf-8').split()
                        for word in output:
                            if word in self.checklist:
                                tkMessageBox.showerror(u'Already imported', u'You have already imported SAS University Edition into Oracle VirtualBox.'+
                                                                    u' Please remove all SAS University Edition Virtual Machines from Oracle '+
                                                                    u'VirtualBox before proceeding. To remove them, open Oracle VirtualBox and'+
                                                                    u' right-click on the "SAS University Edition - Powered Off"'+
                                                                    u' tab, then hit remove --> Delete All Files. Do this for all existing SAS '+
                                                                    u'University Edition Virtual Machines in VirtualBox.')
                                notimported = False
                                return notimported
        noduplicates = True
        return noduplicates    
    def check_vbox_vms_folder(self):
        vboxvmsfolder = self.home + ur'/VirtualBox VMs'
        vboxvms = os.listdir(vboxvmsfolder)
        
        if vboxvms != []:
            for item in self.checklist:
                if item in vboxvms:
                    tkMessageBox.showerror(u'Already imported',u'The virtual machine "'+ item+u'" was removed from Oracle VirtualBox incorrectly. '+
                                                            u'Please delete all SAS University Edition folder(s) from the '+
                                                            u'following location: \n\n'+vboxvmsfolder)
                    return False
        
        test = True
        return test
    def check_duplicates(self):
        if self.check_duplicate_vms() == True:
            if self.check_vbox_vms_folder() == True:
                self.fifth_action_button_clicked()
#----- Step 5: Write batch file using information collected above & run batch file to import vApp -----#   
    def import_ova_file(self):
        try:
            #Imports the .ova file in the location specified using the VBoxManage CLI module 
            os.system(self.vbox_manage_path+' import '+self.ova_filename)
            if os.path.isdir(self.shared_folder):
                #Adds the shared folder using the location specified
                os.system(self.vbox_manage_path+' sharedfolder add "SAS University Edition" --name myfolders --hostpath '+self.shared_folder+' --automount')
            else:
                os.mkdir(self.shared_folder)
                os.system(self.vbox_manage_path+' sharedfolder add "SAS University Edition" --name myfolders --hostpath '+self.shared_folder+' --automount')
                tkMessageBox.showinfo(u"Successfully Installed",u"SAS University Edition has now been imported into Oracle VirtualBox.\n\n"+
                                    u"A shared folder was created at the following location:\n"+
                                    self.shared_folder+u'\n\n')
            self.successful_import()
        except:
            tkMessageBox.showerror(u"Error",u"There was an issue importing SAS University Edition. You may need to run this file using administrator privelages.")   
    def fifth_action_button_clicked(self):
        self.action_button.config(text=u'Import', command=self.import_ova_file)
        self.messagelabel.config(text=u" Click the 'Import' button to import the SAS University Edition vApp\n "+
                                      u"into Oracle VirtualBox. This may take a few moments. \n\n")
        self.master.update_idletasks()
        self.master.update()
#----- Step 6: Open Oracle VirtualBox and close the installer -----#
    def successful_import(self):
        self.action_button.config(text=u'Finish')
        self.action_button.config(command=self.run_button_clicked)
        self.messagelabel.config(text=u" You are now finished setting up SAS University Edition. \n"+
                                      u" Click the 'Finish' button to run Oracle VirtualBox and quit the Installer. \n\n")
        self.master.update_idletasks()
        self.master.update()
    def run_button_clicked(self):
        u'''
        Allows users to run Oracle VirtualBox after a successful import and quit the installer.
        '''
        try:
            subprocess.Popen([u'VirtualBox'])
            tkMessageBox.showinfo(u"Successfully Installed",u"The SAS University Edition Install Tool will quit "+
                                u"after clicking OK. You can now begin using SAS University Edition in Oracle VirtualBox "+
                                u"by right-clicking 'SAS University Edition' and hitting 'Start'.")
            self.quit()
        except:
            tkMessageBox.showerror(u"Error",u"You may need administrator privelages to open Oracle VirtualBox. "+
                                 u"Try opening Oracle VirtualBox manually by searching for 'Oracle VirtualBox' "+
                                 u"in the Windows Search Bar (bottom left hand corner of the screen).")
def main():
    root = Tk()
    root.geometry(u"700x500")
    app = Installer()
    root.update_idletasks()
    app.update_idletasks()
    app.mainloop()  
if __name__ == u'__main__':
    main()  
