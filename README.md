# KamusyEngine
KamusyEngine is the backend foundation of a translation dictionnary engine.

*Kamusy means dictionnary in swahili.*

## Implemented Features
* Add languages to the engine
* Add translation from one language to another
* See languages stats (number of words per languages)

## Coming soon features
* Expression translation
* Quizz
* User authentification in order to record who performs actions
* Vote for the most accurate translation
* Reward for contribution
* Export the dictionnary into a printable format

## Tech stack
* The backend of the app is written in Python Flask. 
* We use API rest in order to allow communication with other services (web front-end or mobile app ).

*NB : this project can be used with any front end.*

## Installation
Use following instruction in order to setup and run the project locally.
### Setup environment
Setup the following env var for Flask.
```sh
export FLASK_APP=app.py
export FLASK_ENV=development
```

### Install required packages
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements listed in `requirements.txt`
```bash
pip3 install -r requirements.txt
```

## Usage

### Run flask app
```bash
python3 main.app
```

### Run test
```bash
python3 app/test/test.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)