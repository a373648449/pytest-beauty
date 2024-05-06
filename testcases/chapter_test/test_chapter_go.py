import pytest
import allure
from common.logger import logger
from operation.chapter import get_chapter_list


class TestGetChaptGo:
    @allure.story("用例-进入具体关卡获得信息")
    @allure.description("该用例是针对获取具体关卡信息")
    def test_get_go(self, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_chapter_list()
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")
