import re
from enum import Enum
from typing import Callable


class Case(Enum):
    """Possible string cases"""

    SNAKE = "snake"
    CAMEL = "camel"
    KEBAB = "kebab"
    PASCAL = "pascal"


class CaseEnforcer:
    """Expose method enforcing a string's case"""

    @classmethod
    def get_enforcer(cls, case: Case) -> Callable[[str], str]:
        """Get the enforcer for the given case"""
        enforcer_name = f"to_{case.value}"
        if not hasattr(cls, enforcer_name):
            raise NotImplementedError(f"CaseValidator.{enforcer_name}")
        return getattr(cls, enforcer_name)

    @staticmethod
    def get_components(string: str) -> list[str]:
        """Extract components from any case string.

        This method normalizes a string by replacing underscores, hyphens,
        and spaces with a single space, and then splitting the string into
        its lowercase components based on case transitions or delimiters.

        Examples:
            >>> CaseEnforcer.get_components('myVariableName')
            ['my', 'variable', 'name']
        """
        components_str = re.sub(r"(_|-)+", " ", string)
        components_str = re.sub(r"([A-Z])", r" \g<1>", components_str)
        components_str = components_str.lower()
        components_str = components_str.replace("'", " ")
        components_str = components_str.replace('"', " ")
        components_str = components_str.strip()
        components = components_str.split(" ")
        return [component for component in components if component]

    @classmethod
    def to_camel(cls, string: str) -> str:
        """Force the string to camel case.

        Examples:
            >>> CaseEnforcer.to_camel('my_variable_name')
            'myVariableName'
        """
        components = cls.get_components(string)
        return components[0] + "".join(x.title() for x in components[1:])

    @classmethod
    def to_snake(cls, string: str) -> str:
        """Force the string to snake case.

        Examples:
            >>> CaseEnforcer.to_snake('myVariableName')
            'my_variable_name'
        """
        return "_".join(cls.get_components(string))

    @classmethod
    def to_kebab(cls, string: str) -> str:
        """Force the string to kebab case.

        Examples:
            >>> CaseEnforcer.to_kebab('myVariableName')
            'my-variable-name'
        """
        return "-".join(cls.get_components(string))

    @classmethod
    def to_pascal(cls, string: str) -> str:
        """Force the string to pascal case.

        Examples:
            >>> CaseEnforcer.to_pascal('my_variable_name')
            'MyVariableName'
        """
        components = cls.get_components(string)
        return "".join(x.title() for x in components)
