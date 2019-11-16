# Control-F for video

[![Build Status](https://travis-ci.com/ubclaunchpad/cmd-fam.svg?branch=master)](https://travis-ci.com/ubclaunchpad/cmd-fam)

## Setup

```sh
git clone https://github.com/ubclaunchpad/cmd-fam.git
cd cmd-fam/
pip install pipenv
pipenv install --dev
```

## Server

```sh
pipenv shell
export FLASK_APP=server/server.py
flask run
```
