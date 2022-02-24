# Tomat

### Silesian Pomodoro. 

Tomat is a basic time tracking app. 
It opens a window on your machine, which contains 3 tabs: work tab, short break tab, long break tab. 
You may start tracking your time with start button on the left, and stop any time with stop button on the right.  

## Pre-requisites
- Python 3.8
- virtualenv

## How to use
To start using Tomat on your machine, follow these instructions:
1. Python 3.8 was used to write this app. Ensure you are using suitable Python version:
  - check if you already are using this version as default:  
  `python --version`
  - or find a path to relevant version on your machine and use this full path in your commands:   
  `which python3`  
2. Create and activate virtual environment:
  ```
    virtualenv -p your/path/to/python3 venv
    source venv/bin/activate
  ```  
3. Check out the repository:  
  `git clone https://github.com/awbox/tomat`  
4. Install requirements:  
  `pip3 install requirements.txt`  
5. Execute main module to start the app:  
  `python3 main.py`  
