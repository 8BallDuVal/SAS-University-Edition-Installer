***THIS NEEDS TO BE UPDATED FOR THE FILES I HAVE ADDED. PLEASE BE PATIENT WHILE I WORK ON THE DOCUMENTATION. THE FILES I HAVE ADDED RECENTLY ARE HOWEVER WORKING AND WILL IMPORT SAS UNIVERSITY EDITION INTO ORACLE VIRTUALBOX.***


# SAS-University-Edition-Installer
Imports SAS University Edition into Oracle VirtualBox Automatically

This is a Graphical User Interface Application written in Python 3.6.5, using Python's included tkinter package.

Dependencies: 
- All Python packages used in the ueinstaller.py file are included with Python 3.6.5.
- The analytics_u.gif photo must be in the same directory as the ueinstaller.py file upon runtime.
- **Pyinstaller version 3.4.dev0+bbede2ea3 . This is only necessary if you would like to create a single-file executable.

I have included two versions of the program: 

-ueinstaller.py

-ueinstaller_ALTERNATE.py

Both of these versions perform essentially the same exact functions, however the "Alternate" version is attempting to be more like a windows installer, with separate 'pages' for each step of the install process.

The ueinstaller.py program does the following:
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

The ueinstaller_ALTERNATE.py does the following:
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


********************************************************************************************************************************
If you would like to turn the application into a stand-alone EXE file for windows, download Pyinstaller and use the included spec file. With everything in the same directory, open up a command prompt window, CD to the directory containing the files, and run the following command:

Pyinstaller ueinstaller.spec

(don't forget to modify the file paths in the ueinstaller.spec file, making sure each '\' has two '\\' in the folder paths. Example: 'C:\Windows\System32' should be 'C:\\\\Windows\\\\System32')
********************************************************************************************************************************

This program was written entirely by me, and is not affiliated with SAS or SAS University Edition at this time.

If you have any questions/concerns, feel free to shoot me an email at dduval6@outlook.com
