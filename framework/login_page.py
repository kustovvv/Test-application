from .page import Page


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for login page
    _loginButton = "com.ajaxsystems:id/authHelloLogin"  # id
    _enterEmail = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText"  # xpath
    _enterPassword = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText"  # xpath
    _verifyLoginPage = "com.ajaxsystems:id/authLoginForgotPassword"  # id
    _verifySuccessfullLogin = "com.ajaxsystems:id/addFirstHub" # id
    _wrongLoginOrPassword = "com.ajaxsystems:id/snackbar_action" # id
    _clickLoginButton = "com.ajaxsystems:id/bottomContent"  # id
    
    def click_login_form(self):
        return self.click_element(self._loginButton, "id")

    def verify_login_page(self):
        return self.is_displayed(self._verifyLoginPage, "id")

    def enter_email(self, email):
        return self.send_text(email, self._enterEmail, "xpath")

    def wrong_email_or_password(self):
        return self.is_displayed(self._wrongLoginOrPassword, "id")

    def enter_password(self, password):
        return self.send_text(password, self._enterPassword, "xpath")

    def click_login_button(self):
        return self.click_element(self._clickLoginButton, "id")

    def verify_successfull_login(self):
        return self.is_displayed(self._verifySuccessfullLogin, "id")