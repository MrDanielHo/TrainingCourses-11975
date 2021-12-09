'''
Python scripts should start with a shebang:
Windows:    #! python3
OSX:        #! /usr/bin/env python3
Linux       #! /usr/bin/python3

To run a python script in cmd.exe execute the following:
    py.exe <directoryInFolder\python_script.py>

To run a python script from Win+R execute the following:
    py <directoryInFolder\python_script.py>
Window will close as soon as it ends.

To prevent this, create a batch file (.bat):
    @py <directoryInFolder\python_script.py> %*
    @pause
Save this file in <directoryInFolder\>
Then execute the batch file.

Use @pyw to make the script windowless.

Using the PATH Environment Variable
Control Panel ==> System ==> Advanced System Settings ==> Advanced ==> Environment Variables
    ==> <directoryInFolder\>;  

We can then use cmd.exe to launch without the *.py and include arguements (arg1, arg2, etc.) when launching.
Insert arguements in the python script using:
import sys
sys.argv
'''

