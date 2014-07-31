# add faceburn directory to path
currentDirectory=$(pwd)

if [ ! -e "~/.bash_profile" ]; then
    touch ~/.bash_profile
fi

echo "export PATH=\"$currentDirectory:\$PATH\"" >> ~/.bash_profile
source ~/.bash_profile

# change file permissions
chmod 744 faceburn.py
chmod 700 config.py