#!/bin/sh

mkdir /opt/iconmod > setuplog.txt
cp iconmod.py /opt/iconmod/iconmod.py >> setuplog.txt
cp errors.py /opt/iconmod/errors.py >> setuplog.txt
ln -s /opt/iconmod/iconmod.py /usr/bin/iconmod >> setuplog.txt
mkdir /opt/iconmod/photos >> setuplog.txt
cp icon.png /opt/iconmod/photos/icon.png >> setuplog.txt

echo "
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=IconMod
Comment=Customize your Icons
Exec=sudo iconmod -g
Icon=/opt/iconmod/photos/icon.png
Terminal=true
" > /usr/share/applications/iconmod.desktop 