from Common import Request,Assert, Tools
import allure
import types
request=Request.Request()
assertion=Assert.Assertions()
url='http://192.168.1.137:1811/'
phone = Tools.phone_num()
uname = Tools.random_str_abc(3)+Tools.random_123(3)
head={}

@allure.feature("用户模块")
class Test_yonghu:
    @allure.story("注册")
    def test_zhuce(self):
        json={"phone": phone,"pwd": "gdl123","rePwd": "gdl123","userName": uname}
        test_zhuce_resp=request.post_request(url=url+'user/signup',json=json)
        resp_json=test_zhuce_resp.json()
        assertion.assert_code(test_zhuce_resp.status_code, 200)
        assertion.assert_in_text(resp_json['respBase'], '成功')
    @allure.story("登录")
    def test_login(self):
        json={ "pwd": "727101ll","userName": "727101gg"}
        test_login_resp=request.post_request(url=url+'user/login',json=json)
        resp_json=test_login_resp.json()
        assertion.assert_code(test_login_resp.status_code,200)
        assertion.assert_in_text(resp_json['respDesc'],'成功')

    @allure.story("修改密码")
    def test_xiugai(self):
        json = {"newPwd": "727101ll", "oldPwd": "gdl123", "reNewPwd": "727101ll", "userName": "727101gg"}
        test_xiugai_resp = request.post_request(url=url + 'user/changepwd', json=json)
        resp_json = test_xiugai_resp.json()
        assertion.assert_code(test_xiugai_resp.status_code, 200)
        assertion.assert_in_text(resp_json['respDesc'], '成功')



