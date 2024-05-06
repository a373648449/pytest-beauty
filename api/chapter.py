import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Chapter(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Chapter, self).__init__(api_root_url, **kwargs)

        def submit_test(self, **kwargs):
            return self.post("/chapter/challenge/answer/submit", **kwargs)

        def check_test(self, **kwargs):
            return self.post("/chapter/challenge/check", **kwargs)

        def hint_test(self, **kwargs):
            return self.get("/chapter/challenge/get/hint", **kwargs)

        def go_test(self, **kwargs):
            return self.get("/chapter/challenge/go", **kwargs)

        def index_test(self, **kwargs):
            return self.get("/chapter/challenge/index", **kwargs)

        def list_test(self, pageNo, pageSize, **kwargs):
            base_url = "/chapter/list"
            params = {
                "pageNo": pageNo,
                "pageSize": pageSize
            }
            return self.get(base_url, params=params, **kwargs)


chapter = Chapter(api_root_url)
