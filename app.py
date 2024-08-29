from fastapi import FastAPI
from pydantic import BaseModel, Field
from main import IntelligentMatrix

"""关闭 422 错误"""
_openapi = FastAPI.openapi


def openapi(self: FastAPI):
    _openapi(self)

    for _, method_item in self.openapi_schema.get('paths').items():
        for _, param in method_item.items():
            responses = param.get('responses')
            # remove 422 response, also can remove other status code
            if '422' in responses:
                del responses['422']

    return self.openapi_schema


FastAPI.openapi = openapi


"""正式的应用程序开始行"""
app = FastAPI(title="AI API",
              description="这是一个 AI 智能矩阵 API 的示例",
              version="0.1.0",
              contact={"name": "SiWei API",
                       "url": "http://192.168.101.118:20002/docs",
                       "email": "zhanghao@siweicn.com",
                       },
              license_info={"name": "SiWei Apache 2.0",
                            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                            },
              redoc_url=None
              )


class InputData(BaseModel):
    stepNum: int = Field(1, description="步骤数")
    guid: str = Field("474bff4abb7f41928ec2992718df247d", description="唯一标识")
    data: str = Field("(用户需要查找的内容)我想了解数据安全评估的内容与方法", description="数据")


class OutputData(BaseModel):
    success: bool = Field(True, description="请求是否成功")
    isEnd: bool = Field(True, description="大模型返回的data是否结束标识")
    stepNum: int = Field(1, description="步骤数")
    guid: str = Field("474bff4abb7f41928ec2992718df247d", description="唯一标识")
    data: str = Field("[683871918508032, 700681154037760]", description="数据")


@app.post("/api/v1/ai/aiIntelligentMatrix", response_model=OutputData, summary="AI智能矩阵")
async def process_data(cla: InputData):
    """
    此接口通过分析用户的语言描述请求，并返回相应的评估矩阵数据
    """
    if cla.stepNum not in [1, 3]:
        return OutputData(success=False, isEnd=True, stepNum=1, guid=cla.guid, data="输入有误")
    if "错误" in cla.data:
        return OutputData(success=False, isEnd=True, stepNum=cla.stepNum, guid=cla.guid, data="模拟出错")
    try:
        result = IntelligentMatrix().run(cla.stepNum, cla.guid, cla.data)
        return OutputData(success=True, isEnd=True, stepNum=cla.stepNum + 1, guid=cla.guid, data=result)
    except Exception as e:
        return OutputData(success=False, isEnd=True, stepNum=cla.stepNum, guid=cla.guid, data="模拟出错")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
