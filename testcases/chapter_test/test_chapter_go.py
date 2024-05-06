import allure
from common.logger import logger
from operation.chapter import get_chapter_list


class TestGetChaptList:
    @allure.story("用例-进入具体关卡获得信息")
    @allure.description("该用例是针对获取具体关卡信息")
    def test_get_go(self):
        logger.info("*************** 开始执行用例 ***************")

        # 执行测试操作
        result = get_chapter_list()

        # 断言响应状态码
        assert result.response.status_code == 200, "响应状态码错误"

        # 断言业务逻辑
        assert result.success, result.error
        assert result.response.json().get("code") == 0, f"接口返回错误码: {result.response.json().get('code')}"
        assert "成功" in result.msg, f"接口返回信息不正确: {result.msg}"

        # 记录日志
        logger.info("接口返回码：{}".format(result.response.json().get("code")))
        logger.info("接口返回信息：{}".format(result.msg))

        logger.info("*************** 结束执行用例 ***************")
