from Common import Request,Assert,read_excel
import allure
import pytest
url = 'http://192.168.1.137:8080/'
head = {}
request = Request.Request()
assertion = Assert.Assertions()
idsList = []
item_id=0
excel_list = read_excel.read_excel_list('./document/优惠券.xlsx')
length=len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())
@allure.feature("添加优惠券")
class Test_yhq:

    @allure.story("登录")
    def test_login(self):
        login_requ = request.post_request(url=url + 'admin/login',
                                          json={"username": "admin", "password": "123456"})
        requ_text = login_requ.text
        print(type(requ_text))
        resp_dict = login_requ.json()
        print(type(resp_dict))
        assertion.assert_code(login_requ.status_code, 200)
        assertion.assert_in_text(resp_dict['message'], '成功')
        data_dict = resp_dict['data']
        token = data_dict['token']
        tokenHead = data_dict['tokenHead']
        global head
        head = {'Authorization': tokenHead + token}


    @allure.story("获取优惠券")
    def test_yhq(self):
        param = {'pageNum': '1', 'pageSize': '10'}
        get_yhq_resp=request.get_request(url=url+'coupon/list',params=param,headers=head)
        resp_json = get_yhq_resp.json()
        json_data=resp_json['data']
        data_list=json_data['list']
        item=data_list[0]
        global item_id
        item_id=item['id']
        assertion.assert_code(get_yhq_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')
    @allure.story("删除优惠券")
    def test_shanchu(self):
        get_shanchu_resp=request.post_request(url=url+'coupon/delete/'+str(item_id),headers=head)
        resp_json=get_shanchu_resp.json()
        assertion.assert_code(get_shanchu_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')
    @allure.story("批量添加优惠券")
    @pytest.mark.parametrize('name,amount,minPoint,publishCount,msg',excel_list,ids=idsList)
    def test_add_yhq_list(self,name,amount,minPoint,publishCount,msg):
        json={"type":0,"name":name,"platform":0,"amount":amount,"perLimit":1,"minPoint":minPoint,"startTime":"2019-04-24T16:00:00.000Z",
              "endTime":"2019-04-29T16:00:00.000Z","useType":0,"note":"","publishCount":publishCount,"productRelationList":[],
              "productCategoryRelationList":[]}
        add_resp=request.post_request(url=url+'coupon/create',json=json,headers=head)
        resp_json=add_resp.json()
        assertion.assert_code(add_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], msg)
