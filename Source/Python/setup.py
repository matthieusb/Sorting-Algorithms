try:
    from setuptools import setup
except ImportError :
    from distutils.core import setup

config = {
    'description' : 'My project',
    'author' : 'Matthieu Sauboua-Beneluz',
    'url': 'http://nowhere.com',
    'download_url': 'http://stillnowhere.com',
    'author_email': 'python_test@test.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
