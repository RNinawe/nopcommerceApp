import pytest

from testCases.conftest import setup


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass