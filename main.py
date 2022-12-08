import os
from wget import download
from subprocess import call, Popen, DEVNULL, STDOUT

tools = os.path.isfile('BrowserAddonsView.exe')

if tools:
    print('Tools sudah terinstall')
else:
    print('Mendownload tools yang dibutuhkan')
    download('https://github.com/evanvyz/sipd-chrome-extension-autoinstall/raw/main/BrowserAddonsView.exe')
os.system('BrowserAddonsView.exe /sjson list.json')

try: # Mengecek git sudah terinstall
    call(['git'], stdout=DEVNULL, stderr=STDOUT)
    print('Git sudah terinstall')
except:
    print('Mendownload & menginstall git')
    try:
        Popen('winget install --id Git.Git -e --source winget')
        print('Git berhasil terinstall')
    except:
        print('Mendownload git')
        download('https://github.com/git-for-windows/git/releases/download/v2.38.1.windows.1/Git-2.38.1-32-bit.exe')
        print('Sedang menginstall git')
        os.system('Git-2.38.1-32-bit.exe /VERYSILENT')
        print('Git berhasil terinstall')