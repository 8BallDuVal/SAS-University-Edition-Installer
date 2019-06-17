# SAS-University-Edition-Installer
Imports SAS University Edition into Oracle VirtualBox Automatically

This is a Graphical User Interface Application. There are several versions written in Python, using Python's included tkinter package, there is also a GUI application written for Microsoft's Powershell.

Dependencies: 
- All Python packages used are included with Python (no additional downloads required).
- **SASUniversityEditionInstaller_MacOS.py is written in Python 2.7.1**
- **SASUniversityEditionInstaller_Windows.py and SASUniversityEditionInstaller_Windows_Simple.py are both written in Python 3.6.5**
- Powershell running on a Windows Machine


There are five (very similar) versions of the program: 
- SASUniversityEditionInstaller_MacOS.py is identical to SASUniversityEditionInstaller_Windows.py
- SASUniversityEditionInstaller_Windows_Simple.py has one static GUI window that does not change other than the buttons which are grayed out at first and become clickable as you pass the system checks.
- SAS University Edition Installer.ps1 and SAS University Edition Installer.exe are the same program.


The SASUniversityEditionInstaller_Windows_Simple.py program does the following:
1. Checks that your system has 64-bit Hardware Virtualization enabled. If so, it moves on to the next step.
2. Checks that Oracle VirtualBox is installed. If so, it continues.
3. If Oracle VirtualBox is not installed, there is a link at the top of the GUI application to the Oracle VirtualBox download page.
4. Checks that Oracle VirtualBox's VBoxManage.exe CLI is installed. If so, it continues.
5. Checks for duplicate "SAS University Edition" Virtual Machines imported into Oracle VirtualBox. If none are imported, it continues.
6. Checks for duplicate "SAS University Edition" folders in the 'C:\Users\<windows-username>\VirtualBox VMs\' folder. If there are no duplicate SAS University Edition folders, it continues
7. Checks the 'Downloads' folder for the location of the *newest* SAS University Edition vApp file (.ova file) to import into Oracle VirtualBox. If it finds the vApp file in the 'Downloads folder, it continues.
8. If the program does not find the SAS University Edition vApp file in the Downloads folder, the program prompts you to search for the vApp file in your system files using a typical Windows file search box. You must select a file ending with '.ova', or you will get a warning.
9. If you have not yet downloaded the SAS University Edition vApp file (.ova file), there is a link to the download page at the top of the GUI application.
10. Once the vApp has been selected, a batch file called Install_SAS_University_Edition.bat is written. Using Oracle VirtualBox's included VBoxManage CLI, the batch file imports the latest vApp, creates a directory for the shared folder (C:\Users\<windows-username>\Documents\SASUniversityEdition\myfolders), and imports the shared folder to the SAS University Edition Virtual Machine in VirtualBox, making sure to auto-mount it.
11. The batch file is then run in the background. The GUI window may say "not responding", but if you look in the console you will see the progress bar gradually increasing in percentage.
12. After SAS University Edition has finished importing, you can click the "run" button to open Oracle VirtualBox and quit the GUI application.
13. If you have any issues importing SAS University Edition or setting it up beyond importing the vApp, there is a link to SAS Technical support at the bottom of the GUI application.

The SASUniversityEditionInstaller_Windows.py/SASUniversityEditionInstaller_MacOS.py file does the following:
1. Checks that Oracle VirtualBox is installed.
2. If Oracle VirtualBox is not installed, a warning message and link to the Oracle VirtualBox download page is displayed.
3. If Oracle VirtualBox is installed, the next step checks that your system has 64-bit Hardware Virtualization enabled.
4. If Virtualization is not enabled, a warning is displayed telling the user that they need this to be enabled and to contact their PC manufacturer for assistance.
5. If Virtualization is enabled, the next step allows you to set up your shared folder. You can either allow the program to create a shared folder for you at a default location (displayed on the screen for you), or you can select another 'myfolders' folder on your hard drive using a typical Windows file search box by clicking the 'choose folder' button. You must select a folder spelled 'myfolders' with no spaces or capital letters, or you will get a warning.
6. Checks the 'Downloads' folder for the location of the *newest* SAS University Edition vApp file (.ova file) to import into Oracle VirtualBox. If it finds the vApp file in the 'Downloads folder, it continues.
7. If the program does not find the SAS University Edition vApp file in the Downloads folder, the program prompts you to search for the vApp file in your system files using a typical Windows file search box. You must select a file ending with '.ova', or you will get a warning.
8. Checks for duplicate "SAS University Edition" Virtual Machines imported into Oracle VirtualBox. Then, it checks for duplicate "SAS University Edition" folders in the 'C:\Users\<windows-username>\VirtualBox VMs\' folder. If there are no duplicate SAS University Edition folders, it continues on to the next step. 
9. If there are duplicates for either of the duplicate VM/VirtualBox VMs Folder checks, you will get a warning message with specific instructions on what to do.
10. The next step is the import step, where a batch file called Install_SAS_University_Edition.bat is written. Using Oracle VirtualBox's included VBoxManage CLI, the batch file imports the latest vApp, creates a directory for the shared folder directory you chose or the default directory (C:\Users\<windows-username>\Documents\SASUniversityEdition\myfolders), and adds the shared folder to the SAS University Edition Virtual Machine in VirtualBox, auto-mounting it as well.
11. The batch file then runs in the background. The GUI window may say "not responding", but if you run the batch file in a command prompt console you will see the progress bar increasing in percentage.
12. After SAS University Edition has finished importing, you can click the "run" button to open Oracle VirtualBox and quit the GUI application.

Using the SAS® University Edition Install Tool.ps1
1. To start the install tool, right-click the SAS® University Edition Install Tool.ps1 file and hit Run with PowerShell.
2. Right-Click and Run with Powershell
3. PowerShell does not allow files downloaded from the internet to be run as a security measure. If the tool does not start, you may need to bypass your Powershell Execution Policy by using the following command**:
    
    PowerShell.exe -ExecutionPolicy Bypass -File .\'GUI SAS University Edition Installer'.ps1

    **Before running the command above, verify that you are in the same directory as the SAS University Edition Install Tool.ps1 file. To do this, open up a file explorer and open up the folder containing the SAS University Edition Install Tool.ps1 file. In the Explorer window's address bar, type "Powershell". A powershell window will open up at the same directory. You should then be able to run the command above successfully and start the tool**.

4. Once the SAS® University Edition Install Tool starts up, follow the on-screen prompts to import SAS University Edition into Oracle VirtualBox. If there are errors, follow the instructions in the window to determine how to resolve these.

********************************************************************************************************************************
********************************************************************************************************************************

These programs were written entirely by me, and are not affiliated with SAS or SAS University Edition at this time.

If you have any questions/concerns, feel free to shoot me an email at dduval6@outlook.com
