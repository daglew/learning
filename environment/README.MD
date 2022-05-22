# Environment
It is a file about how to prepare environment.

## Table of contents
* [Download python](#download-python)
* [Download pycharm](#download-pycharm)
* [Download git](#download-git)
* [Install Notepad](#install-notepad)
* [Create repository on github](#create-repository-on-github)
* [Clone repository](#clone-repository-using-git-bash)
* [Create a new branch](#create-a-new-branch)
* [Create prepare_environment file](#create-prepare_environment-file)
* [Sprint1](#sprint1)


## Download python

 Go to [python](https://www.python.org/downloads/)
```
1. Download python 3.10.4
2. Install it.
3. Click windows button+r on your keyboard.
4. Provide "cmd" command
5. Use command "python3 --version" in cmd
6. Check version of installed python.
```

## Download pycharm
Go to [pycharm](https://www.jetbrains.com/pycharm/)
```
1. Take community version.
2. Install it.
```

## Download git

Go to [git](https://git-scm.com/download/win)
```
1. Download 32-bits version.
2. Install it.
```

## Install Notepad
Go to [notepad++](https://notepad-plus-plus.org/downloads/v8.4.1/)
```
1. Go to Download Notepad++ v8.4.1.
2. Download 32-bit x86 installer.
3. Install it.
``` 

## Create repository on Github

```
1. Go to GitHub: Where the world builds software
2. Log in/Sign in
3. Click New repository button.
4. Repository name - "learning"
5. Description:
 "It is my first repository, there will be all information about my learning"
6. Select Public
7. Select Add a README file.
8. Change "main" branch to "develop".
9. Create repository.
``` 
## Clone repository using Git Bash

```
1. Create folder "repositories" in your DISK D
2. Go to this folder
3. Click right mouse button
4. Run Git Bash
5. Go to github.com
6. Choose "learning" repository
7. Click "code" button
8. Copy HTTPS link.
9. Back to Git Bash
10. Clone repository to your local machine use command "git clone <copied link>"
11. Check if folder "learning" is visible in folder "repositories"
``` 
## Create a new branch

```
1. Open Pycharm
2. Go to terminal
3. Use command "git status"
4. Check on what branch are you ( there should be information that you are on develop branch)
5. Create a new branch use command "git checkout -b task_1-first branch"
6. Use command "git status"
7. Check on what branch are you
8. Use command "git checkout develop"
9. Check on what branch are you
10. Use command "git checkout task_1-first branch"
11. Check on what branch are you
12. Go to develop branch
13. Delete the branch "git branch -d <task_1-first branch>
``` 
## Create prepare_environment file

```
1. Go to the Notepad ++
2. Create file prepare_environment.sh
```

```bash
#!/bin/bash
#instalacja paczki virtualvenv
echo 'Execute command: python3 -m pip install virtualenv, Installing virtualenv package'
python3 -m pip install virtualenv

#instalacja wirtualnego środowiska do pliku virtual_environment(to moge sobie zmienić i podstawić, 
#stworzy się w pliku gdzie to egzekwujemy
echo "Execute command: python3 -m virtualenv virtual_environment, installing environament into the virtual_environment folder"
python3 -m virtualenv virtual_environment

#aktywacja środowiska
echo 'Execute command: source virtual_environment/Scripts/activate, ACTIVATE PYTHON'
source virtual_environment/Scripts/activate

#instalujemy zewewnętrzne paczki z lokalizacji gdzie wywołujemy z pliku requirements.txt (musi być w tej samej ścieżce)
echo "Execute command: pip install -r requirements.txt, installing all aditional packages"
pip install -r requirements.txt 
```
```
3. Save file in Desktop/create_environment folder.
4. Go to this folder.
5. Execute a script.
```

## Sprint1

* ![image1](https://ibb.co/tBTs5Hn)
* ![image2](https://ibb.co/n89zbvG)
* ![image3](https://ibb.co/183GWSK)
