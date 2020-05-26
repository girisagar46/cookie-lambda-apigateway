"""Tests for `{{ cookiecutter.project_directory }}` package."""

import pytest
from {{ cookiecutter.lambda_file_name }} import say_hello, add_2


def test_say_hello():
    """Test something."""
    assert say_hello() == "Hello World!"

@pytest.fixture()
def some_data():
    """Use fixtures instead of setUp & tearDown methods to provide data or do whatever...
    https://docs.pytest.org/en/latest/fixture.html"""
    return 42.

def test_add_2_to_42(some_data):
    assert add_2(some_data) == 44.

@pytest.mark.parametrize("input,expected", [
    (1.,3.),
    (4.,6.),
    (123.,125.)
])
def test_add_2(input, expected):
    """..or parameterize testing"""
    assert add_2(input) == expected
