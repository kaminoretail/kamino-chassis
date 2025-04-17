import pytest

from chassis.utils import Case
from chassis.utils import CaseEnforcer


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("myVariableName", ["my", "variable", "name"]),
        ("my_variable_name", ["my", "variable", "name"]),
        ("my-variable-name", ["my", "variable", "name"]),
        ("MyVariableName", ["my", "variable", "name"]),
        ("My'Variable_name", ["my", "variable", "name"]),
        ("my variable name", ["my", "variable", "name"]),
    ],
)
def test_get_components(input_string, expected):
    result = CaseEnforcer.get_components(input_string)
    assert result == expected


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("my_variable_name", "myVariableName"),
        ("MyVariableName", "myVariableName"),
        ("my-variable-name", "myVariableName"),
        ("my variable name", "myVariableName"),
    ],
)
def test_to_camel(input_string, expected):
    result = CaseEnforcer.to_camel(input_string)
    assert result == expected


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("myVariableName", "my_variable_name"),
        ("MyVariableName", "my_variable_name"),
        ("my-variable-name", "my_variable_name"),
        ("my variable name", "my_variable_name"),
    ],
)
def test_to_snake(input_string, expected):
    result = CaseEnforcer.to_snake(input_string)
    assert result == expected


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("myVariableName", "my-variable-name"),
        ("MyVariableName", "my-variable-name"),
        ("my_variable_name", "my-variable-name"),
        ("my variable name", "my-variable-name"),
    ],
)
def test_to_kebab(input_string, expected):
    result = CaseEnforcer.to_kebab(input_string)
    assert result == expected


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("my_variable_name", "MyVariableName"),
        ("myVariableName", "MyVariableName"),
        ("my-variable-name", "MyVariableName"),
        ("my variable name", "MyVariableName"),
    ],
)
def test_to_pascal(input_string, expected):
    result = CaseEnforcer.to_pascal(input_string)
    assert result == expected


@pytest.mark.parametrize(
    "case,input_string,expected",
    [
        (Case.SNAKE, "myVariableName", "my_variable_name"),
        (Case.CAMEL, "my_variable_name", "myVariableName"),
        (Case.KEBAB, "myVariableName", "my-variable-name"),
        (Case.PASCAL, "my_variable_name", "MyVariableName"),
    ],
)
def test_get_enforcer(case, input_string, expected):
    enforcer = CaseEnforcer.get_enforcer(case)
    assert enforcer(input_string) == expected
