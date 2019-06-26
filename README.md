# test_web_browser
Simple web browser test project using Selenium

## Instalation
You will need the following tools/programs already installed:
* [Homebrew](https://brew.sh/) or any other package manager
* [Python 3](https://www.python.org/)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/)

An installation example could be like this:
```
brew install python3
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
## Usage
Having active virtual env, to run the tests:
```
pytest
```
To deactivate the virtual env you just have to type:
```
deactivate
```
