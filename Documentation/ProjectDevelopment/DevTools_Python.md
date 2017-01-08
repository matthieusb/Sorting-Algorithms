# Development Tools used

General documentation for python : [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/)

**TUTORIAL USED** Tutorial with project template : [Github tempalte with instructions](https://github.com/seanfisk/python-project-template)

## Project setup
----

### General

#### Tools used from github template

Just use the tutorial set up in seanfisk github repository, it's well explained, the project uses the following tools :

  - [Paver](http://paver.github.io/paver/) for running miscellaneous tasks, see the **pavement.py** file for details
  - [Setuptools](http://pythonhosted.org/setuptools/merge.html) for distribution (Setuptools and Distribute_ have merged_)
  - [Sphinx](http://sphinx-doc.org/) for documentation
  - [flake8](https://pypi.python.org/pypi/flake8) for source code checking
  - [pytest](http://pytest.org/latest/) for unit testing
  - [mock](http://www.voidspace.org.uk/python/mock/) for mocking (not required by the template, but included anyway)
  - [tox](http://testrun.org/tox/latest/) for testing on multiple Python versions

#### Where to go  

### Virtualenv and install

This is used to isolate the python for the project. This is not mandatory, just good practice

To set it up :

```
virtualenv /path/to/my-project-venv
```

To activate it (**Do it before each time you start working**) :

```
source /path/to/my-project-venv/bin/activate
```

To deactivate it :
```
deactivate
```


Then, when activated, install the requirements :

```
pip install -r requirements-dev.txt
```

To finish, run tests with paver (This runs unit and style check tests, it might display failed if you modified some files):
```
paver test_all
```

### Testing

Unit tests can be laucnhed with this :
```
paver test
```

Unit tests + Lint check :
```
paver test_all
```

If you want to test code coverage :
```
paver coverage
```

If you want to change some *paver* commands, go to the *setup.py* file


For more information, ask for help : ```paver help```
