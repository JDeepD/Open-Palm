## :warning: This project is no longer maintained :warning:

# Open Palm



![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/JDeepD/Open-Palm)
![GitHub last commit](https://img.shields.io/github/last-commit/JDeepD/Open-Palm)
![GitHub contributors](https://img.shields.io/github/contributors/JDeepD/Open-Palm)
![GitHub issues](https://img.shields.io/github/issues/JDeepD/Open-Palm)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/JDeepD/Open-Palm)

[![Build Status](https://dev.azure.com/jaydeepjd1125/jaydeepjd1125/_apis/build/status/JDeepD.Open-Palm?branchName=master)](https://dev.azure.com/jaydeepjd1125/jaydeepjd1125/_build/latest?definitionId=2&branchName=master)

[![forthebadge](https://forthebadge.com/images/badges/just-plain-nasty.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/ctrl-c-ctrl-v.svg)](https://forthebadge.com)

## Welcome to Open Palm Open Source Project. This is a project which will be mainly based on Python 3.x and MySql
##### Note : For Windows Users , there are certain bugs which I am aware of and it is caused because of the different directory navigation style used by Windows and Linux. For example: `/` in linux is `\\` for Windows.I will be making a separate branch for Windows shortly 
#### Q : What do I get with this software?
#### A : This software is mainly built to aid the teachers in conducting CS practicals.The following are the things which are currently present in the software as of 7 October 2020 :
| Features                    |                 Description |
| ------------------------- | --------------------------- |
| Reviewing the code on different test cases | Students can submit code on the default editor and Open-Palm can run it on pre-determined test cases      |
| Maintaining a \*secured interface between Teacher's Page and Editor| It uses username - password based style of entry to the teacher's page|
| Maintaining a responsive database of students | Open-Palm uses local database file to store data of students|

#### Q : What more features does it offer other than evaluating scripts?
#### A : We are working on adding the following features in coming releases :
- [ ] Sending the result of students directly through mail to the teacher.
- [ ] Developing a website where students can check their solution and their result.

#### Q : How can I contribute and/or request for a new feature?
 A : You can make an issue with the *feature-request* label with the description of feature.

#### Note : All Pull Requests made without an issue will be rejected.
#### Note : Pull requests must be made to the feature branch.
\* *We neither claim nor advertise the security of the ciphering mechanism. We are working on implementing a more secure encryption system in the future releases.*

| Codes                    |                Question Description |
| ------------------------- | --------------------------- |
| #1 | Write a function that inputs an integer and returns `True` if its even else it returns False  |
| #2| Write a function that inputs an array and returns a sorted array. (Use Bubble Sort)|
| #3 | Write a function that that inputs an interger `n` and returns `n`th fibonacci number. (Fibonacci series starts with 1)|
| #4 | Write a function that that inputs a string and returns `True` if its a palindrome else it returns `False`|

### How to Use ?

As of now, there is no pre build source. You have to manually run `MainUI.py` . Make sure you follow the exact steps. Raise an issue if there is some problem/error.

1. Check your python version.Python version should be above 3.6 .Open your shell

   **Windows**: `python --version` or `python3 --version`
   
   **Ubuntu/Debian** : `python --version` or `python3 --veersion`
   
   **Note : Cpython is the preferred version.**
 
2. If you have virtual environment installed , Go to step 3.
   **else:**
   1. Install virtual environment using the following command :    
    `pip install virtualenv`     
 3. Clone/Download the repository.Navigate to the folder and  create a virtual environment using `virtualenv open-palm`.
 4. Activate the virtual environment using `source open-palm/bin/activate` 
 5. Install `Pillow`  while in venv using `pip install Pillow` 
 6. While in Virtual Environment, Navigate to src and run the `MainUI.py` file using `python MainUI.py` or `python3 MainUI.py` 
   

**NOTE** : If you dont use Virtual environment , then in some python versions which comes preinstalled with `PIL` , MainUI.py will throw an error. 


### Screenshots :
![alt text](https://github.com/Nova-Striker/Open-Palm/blob/master/screenshots/Screenshot%20from%202020-10-09%2023-17-20.jpg)
![alt text](https://github.com/Nova-Striker/Open-Palm/blob/master/screenshots/Screenshot%20from%202020-10-09%2023-18-44%20(1).jpg)
![alt text](https://github.com/Nova-Striker/Open-Palm/blob/master/screenshots/Screenshot%20from%202020-10-09%2023-19-19.jpg)

