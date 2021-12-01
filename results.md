## issue-01

```
C:\Users\Arsen\PycharmProjects\AAAProject\venv\testing_hw>python -m doctest -v tests_morse.py
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode("AAA BBB AAA") # doctest: +ELLIPSIS
Expecting:
    '.- .- .- ... .- .- .-'
ok
Trying:
    encode("AAA BBB                AAA") # doctest: +NORMALIZE_WHITESPACE
Expecting:
    '.- .- .-   -... -... -...   .- .- .-'
ok
Trying:
    encode('abc')
Expecting:
    Traceback (most recent call last):
    KeyError: 'a'
ok
1 items had no tests:
    tests_morse
1 items passed all tests:
   4 tests in tests_morse.encode
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
```



## issue-02

```
C:\Users\Arsen\PycharmProjects\AAAProject\venv\testing_hw>python -m pytest test_decode.py
================================================ test session starts =================================================
platform win32 -- Python 3.9.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\Arsen\PycharmProjects\AAAProject\venv\testing_hw
plugins: anyio-2.2.0, Faker-8.14.0
collected 3 items

test_decode.py ...                                                                                              [100%]

================================================= 3 passed in 0.15s ==================================================
                                                                                                                                                  [100%]
```
## issue-03

```
C:\Users\Arsen\PycharmProjects\AAAProject\venv\testing_hw>python -m unittest test_one_hot_encoder.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## issue-04

```
C:\Users\Arsen\PycharmProjects\AAAProject\venv\testing_hw>python -m pytest test_one_hot_encoder_pytest.py
================================================ test session starts =================================================
platform win32 -- Python 3.9.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\Arsen\PycharmProjects\AAAProject\venv\testing_hw
plugins: anyio-2.2.0, Faker-8.14.0
collected 4 items

test_one_hot_encoder_pytest.py ....                                                                             [100%]

================================================= 4 passed in 0.18s ==================================================
```

## issue-05

```
C:\Users\Arsen\PycharmProjects\AAAProject\venv\testing_hw>coverage run -m pytest test_what_year.py
======================================================= test session starts =======================================================
platform win32 -- Python 3.9.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\Arsen\PycharmProjects\AAAProject\venv\testing_hw
plugins: anyio-2.2.0, Faker-8.14.0, cov-3.0.0
collected 4 items

test_what_year.py ....                                                                                                       [100%]

======================================================== 4 passed in 1.29s ========================================================

C:\Users\Arsen\PycharmProjects\AAAProject\venv\testing_hw>coverage report
Name                                                                 Stmts   Miss  Cover
----------------------------------------------------------------------------------------
C:\Users\Arsen\PycharmProjects\AAAProject\venv\what_is_year_now.py      19      0   100%
__init__.py                                                              0      0   100%
test_what_year.py                                                       38      0   100%
----------------------------------------------------------------------------------------
TOTAL                                                                   57      0   100%

```