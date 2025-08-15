from labs.basics import hello_world
from labs.basics import echo
from labs.basics import add
from labs.basics import complicated_add

def test_hello_world():
    assert hello_world() == "Hello, world!"

def test_echo():
    assert echo("test") == "test"
    assert echo(123) == 123
    assert echo([1, 2, 3]) == [1, 2, 3]
    assert echo({"key": "value"}) == {"key": "value"}
    assert echo(hello_world()) == "Hello, world!"

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert echo(add("Hello, ", "world!")) == "Hello, world!"

def test_complicated_add():
    assert complicated_add(1, 2) == 3
    assert complicated_add("1", 1) == 2
    assert complicated_add("2", "3") == 5
    
