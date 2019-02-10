## WEB CRAWLER

This python script will create map of the website in a form of Python dictionary which will be printed in the terminal when the process is over.   


### GETTING STARTED

1. Checking Python version.
    - To be able to use this script you'll need to have Python installed, you can check whether you have it installed or not by typing in terminal:  
`python3 --version`  
or:  
`python --version`  
    - This script was written using version 3.7.0 and it is advised to use the same version, but script should work with 3.6 version as well.  
    - If you don't have Python installed you can go to [Python.org](https://www.python.org/downloads/) to download it.

1. Creating Virtual Environment  
    - To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:  
    `python3 -m venv your-env`  
    - Once you’ve created a virtual environment, you may activate it.  
    `source your-env/bin/activate`  
2. Download  
    - You need to clone repository to your local destination  
    `$ cd path/to/your/workspace`  
    `git clone https://github.com/henryy07/web_crawler.git`
    - if you have established ssh connection to github you can use this link to clone repo:  
    `git clone git@github.com:henryy07/web_crawler.git`  
3. Requirements
    - Once your virtual environment is activated and project is cloned you need to install requirements:  
    `$ pip install -r requirements.txt`  

### USAGE

- Using this script is very simple you need to just type this command:  
`python web_crawler.py -u http://your-website.com`  
or optionally  
`python web_crawler.py --url http://your-website.com`  

- This script will find all the a tags and define which of them are external(using regular expression) 
and then script will try to access all the links and repeat process excluding links which were already checked.
After all of the links were accessed, script will write result in the terminal in a form of python dictionary.  
- Technologies used:
    - Python 3.7.0
        - requests
        - beautifulsoup4

