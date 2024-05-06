from core.result_base import ResultBase
from api.chapter import chapter

def get_chapter_list():
    """
    获取具体关卡信息
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    res = chapter.get_chapter_list_all()
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
