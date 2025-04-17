from collections import namedtuple

from flask import Blueprint

from chassis.api.endpoints.boomz import get_boomz
from chassis.api.endpoints.healthz import get_healthz

Route = namedtuple("Route", ["method", "path", "name", "handler"])

ROUTES = [
    Route("GET", "/healthz", "get_healthz", get_healthz),
    Route("GET", "/boomz", "get_boomz", get_boomz),
]


blueprint = Blueprint(
    name="blueprint",
    import_name=__name__,
)


for route in ROUTES:
    blueprint.add_url_rule(
        rule=route.path,
        endpoint=route.name,
        view_func=route.handler,
        methods=[route.method],
    )
