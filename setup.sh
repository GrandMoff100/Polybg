cat polybg.desktop | sed s/1234567890/$(echo $PWD/polybg.sh | sed 's/\//\\\//g')/g polybg.desktop > ~/Desktop/polybg.desktop
sudo cp polybg.sh /etc/profile.d/polybg.sh
mkdir -p ~/Pictures/backgrounds