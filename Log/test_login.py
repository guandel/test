from Common import Request, Assert
import allure

request = Request.Request()
assertion = Assert.Assertions()

@allure.feature("登录功能")
class Test_login():
    @allure.story("登录")
    def test_login(self):
        login_requ = request.post_request(url='http://192.168.1.137:8080/admin/login',
                                          json={"username": "admin", "password": "123456"})
        requ_text = login_requ.text
        print(type(requ_text))
        requ_dict = login_requ.json()
        print(type(requ_dict))
        assertion.assert_code(login_requ.status_code, 200)
        assertion.assert_in_text(requ_dict['message'], '成功')

