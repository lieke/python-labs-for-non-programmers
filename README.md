# Python Labs for Beginners

This project contains a series of Python 'labs' designed to teach non-programmers how to program. Each lab is a simple Python module with corresponding unit tests.

## Structure

- `labs/` — Contains individual lab modules (e.g., `basics.py`).
- `tests/` — Contains unit tests for each lab.

The labs are created in such a way that the only code you need to change is in the labs folder. The tests should stay the same the entire time.

## Getting Started

#### 1. Start a terminal

Go to 'Terminal' at the top of your screen and start a new Terminal

#### 2. Install all of the dependencies

In the terminal copy the following command and press enter.

```sh
pip install -r requirements.txt
```

This should install a couple of things that are needed to run the labs if they are not installed yet on the computer.

#### 3. Run the tests

In the terminal copy the following command and press enter.

```sh
ptw
```

This will continuously test your labs and will auto-reload when you save the adjusted code.

The tests will fail, but don't worry! They are supposed to. Your task is to make all the tests run smoothly one by one.

#### 4. Start fixing the tests

Start by reading and editing the code in `labs/basics.py`. Once you fix the first test, the automatic testing will fail on the next unit test.

The corresponding tests can be found in `tests/test_lab1.py`. Remember, you don't change any of the testing code!

#### 5. Make all the tests green

Make all of the tests in

`tests/test_lab1.py`
`tests/test_lab2.py`
`tests/test_lab3.py`

run smoothly. At the end of the labs you should be able to go to http://127.0.0.1:5000/greeting?messge=Hello&name=YourName. You can play around with the message and name!
