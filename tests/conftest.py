import pytest

@pytest.fixture()
def set_up():
    print("Test started")
    yield
    print("Test finished")