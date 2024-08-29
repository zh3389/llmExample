## 大模型数据分类分级

使用大模型的推理能力，根据表名称 表注释 字段名称 字段注释 字段样本，对表的属性 字段的属性进行一个推测并返回。

#### 模型AutoDL部署文档参考:

[Qwen2-7B-Instruct vLLM 部署](./docs/Qwen2-7B-Instruct%20vLLM%20部署调用.md)

#### 阿里 Dashscope API 与 AutoDL本地部署 切换:
```
self.llm_cfg = {
                # 使用 DashScope 提供的模型服务：
                'model': 'qwen2-7b-instruct',
                'model_server': 'dashscope',
                'api_key': 'sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                # 如果这里没有设置 'api_key'，它将读取 `DASHSCOPE_API_KEY` 环境变量。

                # 使用与 OpenAI API 兼容的模型服务，例如 vLLM 或 Ollama：
                # 'model': 'Qwen2-7B-Instruct',
                # 'model_server': 'http://192.168.31.206:11434/v1',  # base_url，也称为 api_base
                # 'model_server': 'http://127.0.0.1:11434/v1',  # base_url，也称为 api_base
                # 'api_key': 'EMPTY',
                }
```

#### 本项目使用指南

```
# 安装依赖
pip install -r requirements.txt
# 运行
python app.py
# 访问接口
# http://127.0.0.1:8000/docs
```

#### 模型输入输出

输入数据格式参考:  [input_schema](./assets/input_schema.json)

输出数据格式参考:  [output_schema](./assets/output_schema.json)


#### 接口演示

![image](./assets/input_example.png)

![image](./assets/output_example.png)


#### Docker 打包

```
# 打包
docker build -t qwen2-7b-instruct:v1 -f Dockerfile .
# 运行
# docker run -p 20000:20000 qwen2-7b-instruct:v1
docker run -v $(pwd)/embeddingg:/app/embedding -p 20001:20001 -d riskdata:latest
# 访问接口
# http://127.0.0.1:20001/docs
```

#### 上传docker镜像到服务器

```
# 如需保存到本地 并 上传至服务器 加载 运行
docker save -o ABC.tar ABC
scp ABC.tar siweicn@192.168.10.202:/home/siweicn/
# 登录到服务器 运行以下命令
docker load -i ABC.tar
docker run -v $(pwd)/embeddingg:/app/embedding -p 20001:20001 -d ABC:latest
# 访问接口文档: http://localhost:20001/docs
```
