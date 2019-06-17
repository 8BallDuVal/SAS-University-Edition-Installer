# SAS-University-Edition-Installer
Imports SAS University Edition into Oracle VirtualBox Automatically

This is a Graphical User Interface Application. There are several versions written in Python, using Python's included tkinter package, there is also a GUI application written for Microsoft's Powershell.

Dependencies: 
- All Python packages used are included with Python (no additional downloads required).
- **SASUniversityEditionInstaller_MacOS.py is written in Python 2.7.1**. Python 2.7.1 is pre-installed on every MacOS computer, so no need to download Python on your Mac.
- **SASUniversityEditionInstaller_Windows.py and SASUniversityEditionInstaller_Windows_Simple.py are both written in Python 3.6.5** (link to download: https://www.python.org/downloads/)
- Powershell running on a Windows Machine

________________________________________________________________________________________________________________________________

There are five (very similar) versions of the program: 
- SASUniversityEditionInstaller_MacOS.py is identical to SASUniversityEditionInstaller_Windows.py
- SASUniversityEditionInstaller_Windows_Simple.py has one static GUI window that does not change other than the buttons which are grayed out at first and become clickable as you pass the system checks.
- SAS University Edition Installer.ps1 and SAS University Edition Installer.exe are the same program.

________________________________________________________________________________________________________________________________

To start SASUniversityEditionInstaller_Windows_Simple.py, SASUniversityEditionInstaller_Windows.py, or SASUniversityEditionInstaller_MacOS.py:
- Windows:  
    1. Open up a command prompt window and verify that you are in the same directory as the file you are trying to run.
    2. Type one of the following command on Windows: **python SASUniversityEditionInstaller_Windows.py**, **python3 SASUniversityEditionInstaller_Windows.py**, or **python -m SASUniversityEditionInstaller_Windows.py**
    3. Make sure that you have installed Python 3 before trying to run the file, and that you have added python to your environment variables. 
- MacOS:
    1. Type the following command on MacOS: **python SASUniversityEditionInstaller_MacOS.py**
________________________________________________________________________________________________________________________________

To start the SAS University Edition Install Tool.ps1
1. To start the install tool, right-click the **SAS University Edition Install Tool.ps1** file and hit Run with PowerShell.
2. PowerShell does not allow files downloaded from the internet to be run as a security measure. If the tool does not start, you may need to bypass your Powershell Execution Policy by using the following command**:
    
    PowerShell.exe -ExecutionPolicy Bypass -File .\'GUI SAS University Edition Installer'.ps1

    **Before running the command above, verify that you are in the same directory as the SAS University Edition Install Tool.ps1 file. To do this, open up a file explorer and open up the folder containing the SAS University Edition Install Tool.ps1 file. In the Explorer window's address bar, type "Powershell". A powershell window will open up at the same directory. You should then be able to run the command above successfully and start the tool**.

3. Once the SAS® University Edition Install Tool starts up, follow the on-screen prompts to import SAS University Edition into Oracle VirtualBox. If there are errors, follow the instructions in the window to determine how to resolve these.

********************************************************************************************************************************
********************************************************************************************************************************

These programs were written entirely by me, and are not affiliated with SAS or SAS University Edition at this time.

If you have any questions/concerns, feel free to shoot me an email at dduval6@outlook.com
