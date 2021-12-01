## issue-01

В командной строке перейти в каталог с файлом ```tests_morse.py```, выполнить команду:
```
python -m doctest -v tests_morse.py
```



## issue-02

В командной строке перейти в каталог с файлом ```test_decode.py```.
Выполнить команду:

```
python -m pytest test_decode.py
```


## issue-03

В командной строке перейти в каталог с файлом ```test_one_hot_encoder.py```.
Выполнить команду:

```python -m unittest test_one_hot_encoder.py```

## issue-04

В командной строке перейти в каталог с файлом ```test_one_hot_encoder_pytest.py```.
Выполнить команду:

```python -m pytest test_one_hot_encoder_pytest.py```

## issue-05

В командной строке перейти в каталог с файлом ```test_what_year.py```.
Выполнить команды:

```
coverage run -m pytest test_what_year.py
coverage html
```

Отчет в виде html-файла будет находиться в папке htmlcov.