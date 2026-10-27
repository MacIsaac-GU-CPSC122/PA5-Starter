# README

## To Setup (One Time Only)
`git clone (your github repo url here)`  
`cd` into your local repo you just cloned 

## To Run Unit Tests
Run `pytest --verbose`
* This command runs all the discovered tests in the project
* You can run individual test modules with
    * `pytest --verbose test_stack_calculator.py`
    * `pytest --verbose test_queue_sieve.py`
* Note: the `-s` flag can be helpful because it will show print statement output from test execution

## What not to Modify
You may not modify:
* Any files that start with `test_`
* Anything in the `test/` directory (if it exists)
* Any hidden files (e.g. files/folders that start with a `.`)