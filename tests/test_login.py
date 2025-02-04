from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page =  LoginPage(browser)
    login_page.navigate()
    login_page.login("visual_user", "secret_sauce")