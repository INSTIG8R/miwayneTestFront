import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory


@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, headless):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
    elif browser == "Edge":
        options = webdriver.EdgeOptions()
    else:
        options = webdriver.EdgeOptions()
    if headless:
        options.add_argument("--headless")
    driver = wdf.getWebDriverInstance(options)

    # if headless:
    #     if browser == "Chrome":
    #         options = webdriver.ChromeOptions()
    #         options.add_argument("--headless")
    #         driver = webdriver.Chrome(options=options)
    #     elif browser == "Edge":
    #         options = webdriver.EdgeOptions()
    #         options.add_argument("headless")
    #         driver = webdriver.Edge(options=options)
    #
    #     else:
    #         options = webdriver.EdgeOptions()
    #         options.add_argument("headless")
    #         driver = webdriver.Edge(options=options)
    #     #... other browsers...
    # else:
    #     driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    #after completion of tests we have the teardown
    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser", default="Chrome")
    parser.addoption("--headless", action="store_true", help="Run the browser in headless mode")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")