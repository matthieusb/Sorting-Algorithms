# Sorting-Algorithms
This repository implements well known sorting algorithms. It's the occasion to practise some basic algorithmic notions and language specificities. This is just for training purposes, as the algorithms are well known and already implemented on most languages. I wanted to develop a simple Python project to practise the basic notions I had already learnt.


[![Build Status](https://travis-ci.org/matthieusb/sorting-algorithms-python-java.svg?branch=master)](https://travis-ci.org/matthieusb/sorting-algorithms-python-java)


## Algorithms implemented
----
The project should implement the following sorting algorithms :

  - Bubble sort
  - Insertion sort
  - Selection sort
  - Merge sort
  - Shell sort
  - Quick sort

The main programming language is Python, it would be interesting to compare performance with other languages like Java or C++.

## Running it
----
For now, following these steps :

  - Go to *Source/Python* and type ```source venv/bin/activate```
  - Then go to the *python_sort* folder and type ```paver test_all```, this will run all syntax and unit tests
  - If the previous stepped returned full green on unit tests, run the app with : ```paver run```

For now, I still have to implement the argument handling


### Python version
This project has been developed using python 2.7.12 on Ubuntu 16.04.

## Links used :
----
I went through a bit of documentation to implement these algorithms. See the *Documentation/Algorithms* for details

  - With schemas and explanations (I checked the algorithms used on this site) : [Tutorials point](https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm)
  - With animations for each sort according to sample types [Top tals](https://www.toptal.com/developers/sorting-algorithms)
