import configparser
from github import Github

config = configparser.ConfigParser()
config.read('config.ini')

secret_key = config['DEFAULT']['GITHUB_KEY']

# or using an access token
g = Github(secret_key)

# Then play with your Github objects:
for repo in g.get_user().get_organization():
    print(repo)
