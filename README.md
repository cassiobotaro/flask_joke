# :joy: Flask Joke
The Funniest Joke in the Flask World

Based on [python packaging](https://python-packaging.readthedocs.io).


## Usage

*library*

```python
>>> import flask_joke
>>> print(flask_joke.joke())
>>> print(flask_joke.joke_from_json())
```

*web server*

```
export FLASK_APP=flask_joke.web
flask run
```

*cli*

```bash
$ funniest-joke

$ funniest-joke-cli

```


## Install

`python setup.py install`

## Developer

```bash
# install envirnment
$ python setup.py develop
# test
$ python setup.py test
```
