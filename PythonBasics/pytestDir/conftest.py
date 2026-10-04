import pytest

#Global file, the filename has to be the same and can be used across the project
@pytest.fixture(scope="session")
def preWorkSetup():
    print("Setup session complete")

    # Runs for every test
    # @pytest.fixture(scope="function")
    # def preWorkSetup():
    #     print("Setup complete")

    # Runs once per test file
    # @pytest.fixture(scope="module")
    # def preWorkSetup():
    #     print("Setup complete")

    # Runs once per class, but it must be in created in a class
    # @pytest.fixture(scope="class")
    # def preWorkSetup():
    #     print("Setup complete")

    # Runs once, but for the entire execution across multiple files can be used
    # @pytest.fixture(scope="session")
    # def preWorkSetup():
    #     print("Setup complete")