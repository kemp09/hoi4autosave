import os
import shutil
import time

try:
    print('Note: Recommended to keep hoi4 autosave interval on monthly.')
    print('Files to keep?')
    keep = int(input())
    print('Savefile name? (eg. A country tag)')
    svfile = str(input())
    print('Destination? (eg. D:\\Hoi4 saves):')
    inputdest = input()
    print('Waiting for an autosave...')
    x = 1
    i = 1
    b = 0
    while x <= keep:
        dest = inputdest+'\\' + svfile + str(i) + '.hoi4'
        rm = inputdest + '\\' + svfile + str(x) + '.hoi4'
        path = 'C:\\Users\\'+os.getlogin()+'\\Documents\\Paradox Interactive\\Hearts of Iron IV\\save games\\autosave.hoi4'
        dateMod = os.path.getmtime(path)
        time.sleep(1)
        if dateMod < os.path.getmtime(path):
            shutil.copy(path, dest)
            if b == 1:
                os.remove(rm)
            print('Save',i,'successful')
            x += 1
            i += 1
            if keep == x - 1:
                x = 1
                b = 1
except Exception as e:
    print(e)





