from .page import Page


class SideBarPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for sidebar page
    _sideBarButton = "com.ajaxsystems:id/menuDrawer" # id
    _versionBuild = "com.ajaxsystems:id/build" # id

    # locators for settings page
    _appSettingsButton = "com.ajaxsystems:id/settings" # id
    _verifySettingsPage = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.TextView[1]" # xpath
    
    # locators for help page
    _helpButton = "com.ajaxsystems:id/help" # id
    _verifyHelpPage = "Installation Manuals" # text

    # locators for report page
    _reportProblemButton = "com.ajaxsystems:id/logs" # id
    _verifyReportProblemPage = "Report a Problem" # text

    # locators for add hub page
    _addHubButton = "com.ajaxsystems:id/addHub" # id
    _verifyAddHubPage = "Add Hub" # text

    # locators for terms of service button
    _termsOfServiceButton = "com.ajaxsystems:id/documentation_text" # id
    _verifyTermsPage = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView" # xpath
    
    def click_sidebar_button(self):
        return self.click_element(self._sideBarButton, "id")
    
    def verify_sidebar_page(self):
        return self.is_displayed(self._versionBuild, "id")
    
    def click_settings_button(self):
        return self.click_element(self._appSettingsButton, "id")
    
    def verify_settings_page(self):
        return self.is_displayed(self._verifySettingsPage, "xpath")
    
    def click_help_button(self):
        return self.click_element(self._helpButton, "id")
    
    def verify_help_page(self):
        return self.is_displayed(self._verifyHelpPage, "text")
    
    def click_report_problem_button(self):
        return self.click_element(self._reportProblemButton, "id")
    
    def verify_report_problem_page(self):
        return self.is_displayed(self._verifyReportProblemPage, "text")
    
    def click_add_hub_button(self):
        return self.click_element(self._addHubButton, "id")
    
    def verify_add_hub_page(self):
        return self.is_displayed(self._verifyAddHubPage, "text")
    
    def click_term_of_service_button(self):
        return self.click_element(self._termsOfServiceButton, "id")
    
    def verify_terms_of_service_page(self):
        return self.is_displayed(self._verifyTermsPage, "xpath")