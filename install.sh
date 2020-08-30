#!/bin/bash

echo "Installing dependencies ..............."

echo "Installing requests ......."
pip3 install requests

echo "Intsalling Pyperclip ......"
pip3 install pyperclip

echo "Installing Pywal ......"
pip3 install pywal


echo "Creating directories ........"
mkdir -p ~/.local/share/nautilus/scripts/NaughtyLust/application
mkdir -p ~/.local/share/nautilus/scripts/NaughtyLust/arrange
mkdir -p ~/.local/share/nautilus/scripts/NaughtyLust/copy
mkdir -p ~/.local/share/nautilus/scripts/NaughtyLust/customization
mkdir -p ~/.local/share/nautilus/scripts/NaughtyLust/rename
mkdir -p ~/.local/share/nautilus/scripts/NaughtyLust/git

echo "Copying files ............"
yes | cp -rf $PWD/application/* ~/.local/share/nautilus/scripts/NaughtyLust/application/
yes | cp -rf $PWD/arrange/* ~/.local/share/nautilus/scripts/NaughtyLust/arrange/
yes | cp -rf $PWD/copy/* ~/.local/share/nautilus/scripts/NaughtyLust/copy/
yes | cp -rf $PWD/customization/* ~/.local/share/nautilus/scripts/NaughtyLust/customization/
yes | cp -rf $PWD/rename/* ~/.local/share/nautilus/scripts/NaughtyLust/rename/
yes | cp -rf $PWD/git/* ~/.local/share/nautilus/scripts/NaughtyLust/git/
echo "Adding execute permission ........."
chmod +x ~/.local/share/nautilus/scripts/NaughtyLust/application/*.py
chmod +x ~/.local/share/nautilus/scripts/NaughtyLust/arrange/*.py
chmod +x ~/.local/share/nautilus/scripts/NaughtyLust/copy/*.py
chmod +x ~/.local/share/nautilus/scripts/NaughtyLust/customization/*.py
chmod +x ~/.local/share/nautilus/scripts/NaughtyLust/rename/*.py
chmod +x ~/.local/share/nautilus/scripts/NaughtyLust/git/*.py

echo "NaughtyLust has been Installed successfully :)"