#!/usr/bin/env bash

# Copy this file to /etc/profile.d/polybg.sh to run it on login. (On ubuntu)
# cp polybg.sh /etc/profile.d/polybg.sh

gsettings set org.gnome.desktop.background picture-uri-dark file://$(python $HOME/Polybg/main.py)
gsettings set org.gnome.desktop.background picture-uri file://$(python $HOME/Polybg/main.py)

 