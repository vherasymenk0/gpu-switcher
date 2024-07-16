/-Requires nvidia prime already installed -/

sudo apt-get install python3-tk

chmod +x /path/gpu_switcher.sh

changpe path into gpu_switcher.desktop

cp gpu_switcher.desktop ~/.local/share/applications/

sudo update-desktop-database /usr/share/applications
