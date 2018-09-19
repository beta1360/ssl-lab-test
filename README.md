# SSL-Lab-seminar-test

[![Build Status](https://travis-ci.org/KeonHeeLee/ssl-lab-test.svg?branch=master)](https://travis-ci.org/KeonHeeLee/ssl-lab-test)
[![Coverage Status](https://coveralls.io/repos/github/KeonHeeLee/ssl-lab-test/badge.svg?branch=master)](https://coveralls.io/github/KeonHeeLee/ssl-lab-test?branch=master)
[<img src="https://codedocs.xyz/KeonHeeLee/ssl-lab-test.svg">](https://codedocs.xyz/KeonHeeLee/ssl-lab-test)

SSL-Seminar-test repository:: Topic - Package Test and Deployment

## Synopsis

```python
from khleepkg03.app import Caculator 

calc = Caculator(isAdd=True,
                 isSub=False,
                 isMul=False,
                 isDiv=False,
                 isRem=False)
sum = calc.adder(1, 2)
print(sum) # sum = 3
```

## Installaion

```bash
$ pip3 install khleepkg03
``` 

Only install module with pip

## Dependancy

- pytest

```bash
$ pip3 install -U pytest
```

## Document Index

1. TDD (Test-Driven Development)
2. From unit-test to module-test
3. Package deployment (using pypi)

