import pytest


@pytest.mark.test_sidebar_page
def test_sidebar_page(sidebar_fixture):
    sidebar = sidebar_fixture
    assert sidebar.click_sidebar_button() is not None
    assert sidebar.verify_sidebar_page() is not None

@pytest.mark.test_sidebar_page
def test_settings_page(sidebar_fixture):
    sidebar = sidebar_fixture
    sidebar_fixture.click_sidebar_button()
    assert sidebar.click_settings_button() is not None
    assert sidebar.verify_settings_page() is not None
    sidebar.key_code(4)

@pytest.mark.test_sidebar_page
def test_help_page(sidebar_fixture):
    sidebar = sidebar_fixture
    sidebar_fixture.click_sidebar_button()
    assert sidebar.click_help_button() is not None
    assert sidebar.verify_help_page() is not None
    sidebar.key_code(4)

@pytest.mark.test_sidebar_page
def test_report_page(sidebar_fixture):
    sidebar = sidebar_fixture
    sidebar_fixture.click_sidebar_button()
    assert sidebar.click_report_problem_button() is not None
    assert sidebar.verify_report_problem_page() is not None
    sidebar.key_code(4)

@pytest.mark.test_sidebar_page
def test_add_hub_page(sidebar_fixture):
    sidebar = sidebar_fixture
    sidebar_fixture.click_sidebar_button()
    assert sidebar.click_add_hub_button() is not None
    assert sidebar.verify_add_hub_page() is not None
    sidebar.key_code(4)

@pytest.mark.test_sidebar_page
def test_terms_of_service_page(sidebar_fixture):
    sidebar = sidebar_fixture
    sidebar_fixture.click_sidebar_button()
    assert sidebar.click_term_of_service_button() is not None
    assert sidebar.verify_terms_of_service_page() is not None
    sidebar.key_code(4)