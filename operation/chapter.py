from core.result_base import ResultBase
from api.chapter import Chapter

def get_chapter_list(pageNo, pageSize):
    """
    获取具体关卡信息
    :param pageNo: 页面编号
    :param pageSize: 页面大小
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    try:
        # 创建 Chapter 对象
        chapter = Chapter(api_root_url="https://beauty-dev.man4fun.com/beauty")

        # 调用 list_test 方法来发送请求
        res = chapter.list_test(pageNo=pageNo, pageSize=pageSize)

        # 处理响应
        json_data = res.json()
        result.response = json_data

        if "code" in json_data:
            result.success = json_data["code"] == 0
            result.msg = json_data.get("msg", "接口返回成功") if result.success else f"接口返回失败，返回信息：{json_data.get('msg')}"
        else:
            result.error = "接口返回数据缺少 'code' 键"
            result.msg = "接口返回数据格式错误"

    except Exception as e:
        result.error = f"调用接口失败: {str(e)}"
        result.msg = "调用接口失败"

    return result
