from pydantic import BaseModel
from pydantic import ConfigDict

from chassis.utils import Case
from chassis.utils import CaseEnforcer


class Component(BaseModel):
    """Base component for all API components.

    This class ensures that all derived components use consistent
    field naming conventions with camelCase by default. It also
    forbids any extra fields that are not explicitly defined.
    """

    model_config = ConfigDict(
        alias_generator=CaseEnforcer.get_enforcer(Case.CAMEL),
        validate_default=True,
        populate_by_name=True,
        use_enum_values=True,
        extra="forbid",
        frozen=True,
    )
