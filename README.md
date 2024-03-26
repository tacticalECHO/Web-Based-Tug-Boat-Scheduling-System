# Web-Based-Tug-Boat-Scheduling-System

## Introduction
This is a demo of tugboat scheduling system. It is a web-based automatical scheduling system.

## Requirement
This sytem is based on python enviornment.

Overview:
```
Python >= 3.10
Django == 5.0.2
pandas == 2.2.1
Requests == 2.31.0
node.js == 20.11.1
npm == 10.2.4
Vue == 3.4.21
```
### Python Environment
```
Python version >=3.10
```
If have ever installed Python, use the command following in command prompt to check the version.
```
>python

Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
If have not ever installed Python, please go to [Python official website](https://www.python.org/) to download and install.
### Back-End: Django
Make sure the Python has been installed successfully before install the back-end.


- Install the **Django**:

```
$ python -m pip install Django
```
The last version of Django is `v5.0.2`. 

- Install **pandas**:
```
$ pip install pandas
```
Pandas is an open-source, BSD licensed library that provides high-performance, easy-to-use data structures and analysis tools

- Install **requests**:
```
$ pip install requests
```
Requests is a commonly used HTTP request library that facilitates sending HTTP requests to websites and obtaining response results.

- Install **pytz**:
```
$ pip install pytz
```
Pytz is a library for time and date.

### Front-End: Vue.js and Node.js
- Install node.js

The vue is depending on node.js. If have ever installed `node.js` and `npm`, please check the version:
```
$ node -v
$ npm -v
```
If have not ever installed, please go to [node.js official website](https://nodejs.org/en/download/) to download and install.

- Install Vue.js
```
$ npm install vue -g
```
Check the version of `vue.js`:
```
$ npm list vue
```
- Install `vue-cli`
Open the folder `website\NingboHarbour` and run command in command prompt:
```
$ npm install
``` 

### Start Server
#### At Back-End
- Run server

Open folder `web\WBTBSsystem` and run command in command prompt:
```
$ py manage.py runserver
```
Default run at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Successfully run example:
```
System check identified no issues (0 silenced).
March 26, 2024 - 22:54:55
Django version 4.2.7, using settings 'WBTBSsystem.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
- Access Database through super-user

create Super-user:
```
$ py manage.py createsuperuser
```
Enter the use name and password to create super user.

Access database through [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/)

**NO `#` BETWEEN 8000 and admin** Otherwise, **CAN NOT** go into admin page.

#### At Front-End

-Run server

Open folder `website\NingboHarbour` and run command in command prompt:
```
$ npm run serve
```
Successfully run example:
```
 DONE  Compiled successfully in 175ms                                                                                                                                                                               23:00:55


  App running at:
  - Local:   http://localhost:8080/
  - Network: http://172.19.39.208:8080/

```