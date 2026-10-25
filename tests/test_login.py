from pages.login_page import LoginPage
from pages.home_page import HomePage
login = LoginPage()
login.enter_username()
login.enter_password()
login.click_login()

home = HomePage()
a= home.verify_home_page()
if a:
    print("passed")   
else:
    print("failed")

