fajriillahi@Fajris-MacBook-Pro ~ % which python3.8
/opt/homebrew/bin/python3.8

pip install virtualenv

sudo add-apt-repository ppa:deadsnakes/ppa
 
# Install python using Linux
1. sudo apt install python3.8
2. sudo apt install python3.9
3. sudo apt install python3.10

# Check python version using Linux
1. python3.8 -V
2. python3.9 -V
3. python3.10 -V

# For MacBook
1. virtualenv -p /opt/homebrew/bin/python3.8 env3.8
2. virtualenv -p /opt/homebrew/bin/python3.9 env3.9
3. virtualenv -p /opt/homebrew/bin/python3.10 env3.10

# For Linux
1. virtualenv -p /usr/bin/python3.8 env3.8
2. virtualenv -p /usr/bin/python3.9 env3.9
3. virtualenv -p /usr/bin/python3.10 env3.10

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
