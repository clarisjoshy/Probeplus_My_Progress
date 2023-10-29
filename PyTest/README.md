# **Learning PyTest**

## Install pytest
pip install pytest

## Rules for creating pytest files
Filename should start with 'test_'.
Test functions should also start with 'test_'

## To run pytest file
pytest < filename > 
pytest -v < filename >            # To get the detailed information about each test case while running.
pytest -m  < marker_name >        #To run tests that have specific markers 
pytest -k  < keyword >            #To run tests whose names match a specific keyword expression
pytest test_sample.py::test_num   #To run a test function test_num in the test_sample.py file

## Basics for writing test cases
In PyTest Basics folder,Basics including using assert statements,fixtures,markers,parametrize are explained.
conftest.py file is a special configuration file that allows you to define fixtures
and other configurations that can be shared across multiple test files.

## Test_APIs
Usually test cases for apis which include routes,controllers and models are written inside a class in which named as 'Test.....'
Validation,Mandatory fields  checking and all is included in the test_models.
Authorization,valid info for the api endpoint is included in test_apis
