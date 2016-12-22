try:
    from setuptools import setup
except ImportError :
    from distutils.core import setup

config = {
    'description' : 'Sorting Algorithms project',
    'author' : 'Matthieu Sauboua-Beneluz',
    'url': 'https://github.com/matthieusb/Sorting-Algorithms',
    'download_url': 'https://github.com/matthieusb/Sorting-Algorithms',
    #'author_email': '',
    'version': '0.1',
    'install_requires': ['nose', 'rednose'],
    'packages': ['src'],
    'scripts': [],
    'name': 'sortingalgorithms'
}

setup(**config)
