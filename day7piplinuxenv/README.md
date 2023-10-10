fajriillahi@Fajris-MacBook-Pro ~ % which python3.8
/opt/homebrew/bin/python3.8

pip install virtualenv

sudo add-apt-repository ppa:deadsnakes/ppa
 
sudo apt install python3.8
sudo apt install python3.9
sudo apt install python3.10
# For MacBook
virtualenv -p /opt/homebrew/bin/python3.8 env3.8
virtualenv -p /opt/homebrew/bin/python3.9 env3.9
virtualenv -p /opt/homebrew/bin/python3.10 env3.10

# For Linux
virtualenv -p /usr/bin/python3.8 env3.8
virtualenv -p /usr/bin/python3.9 env3.9
virtualenv -p /usr/bin/python3.10 env3.10

source env3.8/bin/activate
source env3.9/bin/activate
source env3.10/bin/activate

deactivate

# STEPS
1. pip install virtualenv
2. Install python@x.x
3. virtualenv -p /usr/bin/pythonx.x envx.x
4. source envx.x/bin/activate
5. deactivate

# For Windows
via browser
