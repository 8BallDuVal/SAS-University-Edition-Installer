# -*- mode: python -*-

block_cipher = None


a = Analysis(['ueinstaller.py'],
             pathex=['path-to-folder-containing-ueinstaller.py'],
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
			 
a.datas += [('analytics_u.gif','path-to-folder-containing-analytics_u.gif-and-ueinstaller.py\\analytics_u.gif', "DATA")]		 
	
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
