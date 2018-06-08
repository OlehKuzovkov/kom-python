from kom_framework.src.web.data_types import Name, Id
from kom_framework.src.web.data_types.element_types import Input
from kom_framework.src.web.support.page_factory import find_by
from kom_framework.src.web.web_page import WebPage


class Frame:

    def __init__(self):
        self.lucky = Input(Name("btnI"), action_element=True)


@find_by(Id('viewport'))
class PageTest(WebPage, Frame):

    some_variable = 'SOMETHING NEW'

    def __init__(self, module_name=None):
        Frame.__init__(self)
        self._set_module(module_name)
        self.user = Input(Id("lst-ib"))

    def open_actions(self):
        self.browser_session.open("http://www.google.com")


class TestSomething:

    def test_decorator(self):
        print(PageTest.some_variable)
        obj_1 = PageTest('asdasd')
        obj_2 = PageTest('asdasdass')
        obj_3 = PageTest('asdasd')
        assert True

    def test_session_factory_close(self):
        from kom_framework.src.web.support.session_factory import WebSessionsFactory
        obj_1 = PageTest('asdasd').open()
        obj_2 = PageTest('asdasda2ss').open()
        WebSessionsFactory.close_sessions()
        assert True

    def test_action_element(self):
        page = PageTest().open()
        page.lucky.click()
        assert page.exists()

    def test_web_frame(self):
        page = PageTest()
        page.open().lucky.click()
        assert True

    def test_locator(self):
        from kom_framework.src.web.data_types import Xpath
        asda = Xpath('vale')
        print(asda)


