#!/bin/bash
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