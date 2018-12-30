# Github

## Requirements

* NodeJS >= 10.14
* Python >= 3.7

## Generate Data

### (Optional) Virtual Environment

* Install `virtualenv`

```bash
$ pip install virtualenv
```

* Create virtual environmet

```bash
$ virtualenv env
```

* Active virtual environment

```bash
# Linux
$ source env/bin/activate

# Windows
$ env\Scripts\activate
```

### Get Data

* Generate github access token from [Github](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)
* Rename file `config.ini.example` to `config.ini`
* Add access token to `config.ini`

``` ini
GITHUB_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```