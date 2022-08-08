#!/usr/bin/env bash

# Copy this file to /etc/profile.d/polybg.sh to run it on login.

gsettings set org.gnome.desktop.background picture-uri-dark file://$(python ~/Polybg/main.py)
gsettings set org.gnome.desktop.background picture-uri file://$(python ~/Polybg/main.py)

