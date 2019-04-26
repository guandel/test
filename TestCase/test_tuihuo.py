from Common  import  read_excel,Request,Assert,login_py
import allure
import pytest
request=Request.Request()
assertions =Assert.Assertions()
idslist=[]
excel_list = read_excel.read_excel_list('./document/退货原因.xlsx')
length = len(excel_list)
for i in range(length):
    idslist.append(excel_list[i].pop())
url = 'http://192.168.1.137:8080/'
head = {}
item_id=0

@allure.feature("订单模块")
class Test_tuihuo:
    @allure.story("查询退货原因列表")
    def test_get_tuihuo_list(self):
        global head
        head =login_py.Login().get_token()
        get_tuihuo_list_resp = request.get_request(url=url + 'returnReason/list', params={'pageNum': 1, 'pageSize': 5},
                                           headers=head)
        resp_json=get_tuihuo_list_resp.json()
        json_data=resp_json['data']
        data_list=json_data['list']
        item=data_list[0]
        global item_id
        item_id = item['id']
        assertions.assert_code(get_tuihuo_list_resp.status_code, 200)
        assertions.assert_in_text(resp_json['message'], '成功')
    @allure.story("删除订单")
    def test_del_list(self):
        del_list_resp=request.post_request(url=url+'returnReason/delete',params={'ids':item_id},headers=head)
        resp_json=del_list_resp.json()
        assertions.assert_code(del_list_resp.status_code, 200)
        assertions.assert_in_text(resp_json['message'], '成功')
    @allure.story("批量添加退货原因")
    def test_add_list(self):
        add_list_resp=request.post_request




