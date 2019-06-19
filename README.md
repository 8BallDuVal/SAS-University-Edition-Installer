# SAS-University-Edition-Installer
Imports SAS University Edition into Oracle VirtualBox Automatically

This is a Graphical User Interface Application. There are several versions written in Python, using Python's included tkinter package, there is also a GUI application written for Microsoft's Powershell.

Dependencies: 
- Windows:
    - Powershell, which is pre-installed
    - Oracle VirtualBox (link: https://www.virtualbox.org/wiki/Downloads)
    - SAS University Edition vApp (.ova file) (link to download: https://www.sas.com/en_us/software/university-edition/download-software.html#windows-download)

- MacOS:
    - Python 2.7.1, which is pre-installed
    - Oracle VirtualBox (link: https://www.virtualbox.org/wiki/Downloads)
    - SAS University Edition vApp (.ova file) (link to download: https://www.sas.com/en_us/software/university-edition/download-software.html#osx-download)
________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________

# Usage:

- Windows:
    - Download the **SAS University Edition Installer.exe** file on to your computer and follow the on-screen prompts. 
    - You may need to run the file as an administrator for it to start successfully.
    - If you are unable to download an executable, download the **SAS University Edition Installer.ps1** source file
    - right-click the **SAS University Edition Install Tool.ps1** file and hit Run with PowerShell.
    - PowerShell does not allow files downloaded from the internet to be run as a security measure. If the tool does not start,  you may need to bypass your Powershell Execution Policy by using the following command:
    
    **PowerShell.exe -ExecutionPolicy Bypass -File .\'GUI SAS University Edition Installer'.ps1**

    - Before running the command above, verify that you are in the same directory as the SAS University Edition Install Tool.ps1 file. To do this, open up a file explorer and open up the folder containing the SAS University Edition Install Tool.ps1 file. In the Explorer window's address bar, type "Powershell". A powershell window will open up at the same directory. You should then be able to run the command above successfully and start the tool.

- MacOS:
    - Download the **SAS University Edition Install Tool.app.zip** file on to your MacOS computer.
    - Right-click the **SAS University Edition Install Tool.app** file and click **Open**. A prompt will appear asking you if you're sure you'd like to open this file. Click **Open** and the Install tool window will open.
    - If you are unable to download or run the executable file for any reason, download the **SASUniversityEditionInstaller_MacOS.py** file
    - Open up a terminal window and change directories to the same directory as the **SASUniversityEditionInstaller_MacOS.py** file (For example, if the **SASUniversityEditionInstaller_MacOS.py** file is in the 'Downloads' folder, enter the following terminal command to change directories to the 'Downloads' folder: **cd /Users/your-mac-username/Downloads**)
    - Then, enter the following command in the terminal window on MacOS: **python SASUniversityEditionInstaller_MacOS.py**
    

********************************************************************************************************************************
********************************************************************************************************************************

These programs were written entirely by me, and are not affiliated with SAS or SAS University Edition at this time.

If you have any questions/concerns, feel free to shoot me an email at dduval6@outlook.com
