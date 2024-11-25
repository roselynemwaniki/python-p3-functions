# lib/testing/lib_test.py
import pytest
from lib.functions import greet_programmer, greet, greet_with_default, add, halve

def test_greet_programmer(capsys):
    greet_programmer()
    captured = capsys.readouterr()
    assert captured.out == "Hello, programmer!\n"

def test_greet(capsys):
    greet("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"

def test_greet_with_default(capsys):
    greet_with_default()
    captured = capsys.readouterr()
    assert captured.out == "Hello, programmer!\n"

    greet_with_default("Bob")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Bob!\n"

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_halve():
    assert halve(10) == 5.0
    assert halve(1) == 0.5
    assert halve(0) == 0.0
