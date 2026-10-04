# Fixtures
import pytest

@pytest.fixture(scope="function")
def preWork():
    print("Setup module complete")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print("Second Setup module complete")
    yield #pause, it will run all the code once it hits the "yield" keyword, then it will return to the once all the other code is done
    print("\tTeardown will run")

@pytest.mark.smoketest
def test_initialCheck(preWork,secondWork):
    print("This is first test " + preWork)
    assert preWork == "pass"

#@pytest.mark.skip(reason="skip")
def test_secondCheck(preWork,secondWork):
    print("This is second test " + preWork)
    assert preWork == "pass"



# chocolate = "Chocolate"