# -*- mode: python -*-

block_cipher = None


a = Analysis(['ueinstaller.py'],
             pathex=['C:\\Users\\daduva\\Desktop\\SAS University Edition Installer\\misc'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
			 
a.datas += [('analytics_u.gif','C:\\Users\\DDuVa\\OneDrive\\Desktop\\SAS University Edition Installer v1.0\\analytics_u.gif', "DATA")]		 
	
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='ueinstaller',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='SAS University Edition Install Tool')
