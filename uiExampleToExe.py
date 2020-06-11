from cx_Freeze import setup, Executable
setup(name='uitest',
      version = '1',
      description = 'ui',
      executables = [Executable("uiExample.py")])
