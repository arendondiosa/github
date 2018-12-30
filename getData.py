import os
import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('config.ini')

secret_key = config['DEFAULT']['GITHUB_KEY']
username = config['DEFAULT']['USERNAME']

user = {}
repositories = []
organizations = []

# Check if Data folder exist
if not os.path.exists('./src/data'):
    os.makedirs('data')

def writeFile(filename, data):
    f = open(filename, 'w')
    f.write(json.dumps(data))
    f.close()

def getUser():
    r = requests.get("https://api.github.com/users/" + username)

    if (r.ok):
        return json.loads(r.text or r.content)
    else:
        return {}

def getRepositories():
    r = requests.get("https://api.github.com/users/" + username + "/repos")

    if (r.ok):
        return json.loads(r.text or r.content)
    else:
        return []

def getOrganizations():
    r = requests.get("https://api.github.com/users/" + username + "/orgs")

    if (r.ok):
        return json.loads(r.text or r.content)
    else:
        return []

def main():
    user = getUser()
    writeFile('./src/data/user.json', user)
    repositories = getRepositories()
    writeFile('./src/data/repositories.json', repositories)
    organizations = getOrganizations()
    writeFile('./src/data/organizations.json', organizations)

    print(user)

if __name__ == '__main__':
    main()