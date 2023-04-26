# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# pyinstaller main script
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('Icons/*', 'Icons'),
        ('keys.json', '.'),
        ('UI/dialog.ui','UI')
    ],
    hiddenimports=[
        'serial',
        'serial.tools.list_ports',
        'google.oauth2.credentials',
        'googleapiclient.discovery',
        'googleapiclient.errors',
        'google.oauth2.service_account',
        'google_auth_oauthlib.flow',
        'PyQt5.QtWidgets',
        

    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# pyinstaller binary archive
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# pyinstaller executable
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AIoT_Dashboard',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
