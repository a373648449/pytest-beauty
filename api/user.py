import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    #修改用户信息
    def editUserInfo(self, **kwargs):
        return self.post("/user/editUserInfo", **kwargs)

    #微信用户注册
    def register(self, **kwargs):
        return self.get("/user/loginOrRegister", **kwargs)

    #获取用户信息
    def login(self, **kwargs):
        return self.get("/user/uinfo", **kwargs)


user = User(api_root_url)
