# leadbook1 Setup Guide:

## 1. Virtual Environment!

## 1.1 Upgrading/Setting up python-dev and pip for Ubuntu
```
sudo apt-get install python3-pip
sudo apt-get install python3-dev
pip3 install -U pip setuptools
```

In case of comflicting pip3 and current pip2 of ubuntu, just reinstall pip3:
python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall

## 1.2 Setup virtual environment for quest
```
sudo pip3 install virtualenvwrapper

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3  
source `which virtualenvwrapper.sh`  

echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
bash
mkvirtualenv leadbook1
```
To activate virtual environment: `workon leadbook1`

To deactivate: `deactivate`

Then run 'pip3 install -r requirements.txt'
This will download and install the python packages in 2.

## 2. Django, MongoEngine and Python packages
```
Django==2.2.3
```

# 3. Load data to SQLite
```
python load_data.py
```

# 3. Deploy locally and test

```
workon leadbook1
python manage.py runserver
```

test urls:
1) Fetch list of contacts
http://127.0.0.1:8000/contacts
2) Fetch specific contact:
http://127.0.0.1:8000/contacts/1000
3) Filter contacts based on company
http://127.0.0.1:8000/contacts?company_id=10
4) Filter contacts by company revenue:
http://127.0.0.1:8000/contacts?revenue_gte=51791437
5) Filter contacts based on contact name:
http://127.0.0.1:8000/contacts?name=Glenn%20Austin


