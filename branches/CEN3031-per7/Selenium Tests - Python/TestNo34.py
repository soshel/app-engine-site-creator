from selenium import selenium
import unittest, time, re

class TestNo34Evo0(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://change-this-to-the-site-you-are-testing/")
        self.selenium.start()
    
    def test_no34_evo0(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=Sign in")
        sel.wait_for_page_to_load("30000")
        sel.click("admin")
        sel.click("submit-login")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Edit page")
        sel.wait_for_page_to_load("30000")
        sel.click("dijit_layout__TabButton_2")
        time.sleep(NaN)
        for i in range(60):
            try:
                if sel.is_element_present("//textarea[@name='editorHtml']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("//textarea[@name='editorHtml']", "Administrator Logged in. Editing page.")
        sel.wait_for_page_to_load("30000")
        sel.click("dijit_form_Button_0")
        sel.wait_for_page_to_load("30000")
        sel.click("link=View page")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Sign out")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Sign in")
        sel.wait_for_page_to_load("30000")
        sel.click("submit-login")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Edit page")
        sel.wait_for_page_to_load("30000")
        time.sleep(NaN)
        for i in range(60):
            try:
                if sel.is_element_present("//textarea[@name='editorHtml']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        sel.type("//textarea[@name='editorHtml']", "Non-Admin Logged in. Editing page.")
        sel.wait_for_page_to_load("30000")
        sel.click("dijit_form_Button_0")
        sel.wait_for_page_to_load("30000")
        sel.click("link=View page")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()