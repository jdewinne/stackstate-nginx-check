# (C) StackState 2020
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest


@pytest.fixture(scope='session')
def sts_environment():
    # This conf instance is used when running `checksdev env start mycheck myenv`.
    # The start command places this as a `conf.yaml` in the `conf.d/mycheck/` directory.
    # If you want to run an environment this object can not be empty.
    return {"name": "nginx+",
            "location": "./tests/data/nginx_http.conf"}


@pytest.fixture
def http_instance():
    return {"name": "nginx_http",
            "location": "./tests/data/nginx_http.conf"}


@pytest.fixture
def events_instance():
    return {"name": "nginx_events",
            "location": "./tests/data/nginx_events.conf"}
