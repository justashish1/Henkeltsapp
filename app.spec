# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all, copy_metadata

# List of packages to include
packages = [
    'streamlit',
    'pandas',
    'numpy',
    'scikit-learn',
    'statsmodels',
    'prophet',
    'plotly',
    'seaborn',
    'streamlit_aggrid'
]

datas, binaries, hiddenimports = [], [], []

# Collect all necessary dependencies
for pkg in packages:
    pkg_datas, pkg_binaries, pkg_hiddenimports = collect_all(pkg)
    datas += pkg_datas
    binaries += pkg_binaries
    # Filter out any invalid hidden imports
    valid_hiddenimports = [
        imp for imp in pkg_hiddenimports
        if not any(
            invalid in imp for invalid in [
                'pyinstaller', '_pss_critical_values'
            ]
        )
    ]
    hiddenimports += valid_hiddenimports

# Add metadata for each package
for package in packages:
    datas += copy_metadata(package)

# Ensure the __version__.py file for prophet is included
datas += [
    ('venv\\Lib\\site-packages\\prophet\\__version__.py', 'prophet')
]

# Exclude problematic modules
excludedimports = ['pytest', 'langchain', 'plotly.plotly']

# Add the missing scipy modules
hiddenimports += [
    'scipy._lib.array_api_compat.numpy.fft',
    'scipy.special._ufuncs',
    'scipy.special._ufuncs_cxx',
    'scipy.special._specfun',
    'scipy.special._comb',
    'scipy.special._ellip_harm',
    'scipy.special._gamma',
    'scipy.special._loggamma',
    'scipy.special._zeta',
    'scipy.special._basic',
    'scipy.special._round',
    'scipy.special._loggamma'
]

# Analysis section
a = Analysis(
    ['app.py'],  # Replace with your main application script
    pathex=['C:\\MyElectronApp2_1.0.6'],  # Adjust the path as necessary
    binaries=binaries,
    datas=[('logo.ico', '.')] + datas,  # Include any additional files you need
    hiddenimports=hiddenimports,
    hookspath=['./hooks'],  # Add the custom hooks directory
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludedimports,
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
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
    icon='logo.ico',
)
