# SAS-University-Edition-Installer
Imports SAS University Edition into Oracle VirtualBox Automatically

This is a Graphical User Interface Application written in Python 3.6.5, using Python's included tkinter package.

Dependencies: 
- All Python packages used in the ueinstaller.py file are included with Python 3.6.5.
- The analytics_u.gif photo must be in the same directory as the ueinstaller.py file upon runtime.
- **Pyinstaller version 3.4.dev0+bbede2ea3 . This is only necessary if you would like to create a single-file executable.

The SAS University Edition Installer is a GUI program that does the following:
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

********************************************************************************************************************************
If you would like to turn the application into a stand-alone EXE file for windows, download Pyinstaller and use the included spec file. With everything in the same directory, open up a command prompt window, CD to the directory containing the files, and run the following command:

Pyinstaller ueinstaller.spec

(don't forget to modify the file paths in the ueinstaller.spec file, making sure each '\' has two '\\' in the folder paths. Example: 'C:\Windows\System32' should be 'C:\\Windows\\System32')
********************************************************************************************************************************

This program was written entirely by me, and is not affiliated with SAS or SAS University Edition at this time.

If you have any questions/concerns, feel free to shoot me an email at dduval6@outlook.com
