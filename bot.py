from qwen_agent.agents import Assistant
import os


class CreateBot:
    def __init__(self):
        self.llm_cfg = {
            # 使用 DashScope 提供的模型服务：
            'model': 'qwen2-7b-instruct',
            'model_server': 'dashscope',
            'api_key': 'sk-',
            # 如果这里没有设置 'api_key'，它将读取 `DASHSCOPE_API_KEY` 环境变量。

            # 使用与 OpenAI API 兼容的模型服务，例如 vLLM 或 Ollama：
            # 'model': 'Qwen2-7B-Instruct',
            # 'model': 'qwen2:72b',
            # 'model_server': 'http://192.168.31.206:11434/v1',  # base_url，也称为 api_base
            # 'model_server': 'http://127.0.0.1:11434/v1',  # base_url，也称为 api_base
            # ‘model_server': 'http://host.docker.internal:11434/v1',  # base_url，docker打包本地地址
            # 'api_key': 'EMPTY',

            # （可选） LLM 的超参数：
            'generate_cfg': {
                'seed': 1234,
                'repetition_penalty': 1,
                'temperature': 0.8,
                'top_p': 0.8,
                'max_input_tokens': 120000
            }
        }
        self.files_path = self.load_file_path_list()

    def load_file_path_list(self, folder_path="./ragData"):
        files_path = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".txt"):
                    files_path.append(os.path.join(root, file))
        return files_path

    def init_base_agent_service(self):
        system_instruction = """你是一个友好的对话助手，能够回答用户提出的各种问题。请尽量提供详细、准确的信息，并用简洁易懂的语言表达。"""
        tools = [
            # 'my_image_gen',
            'code_interpreter']  # `code_interpreter` 是框架自带的工具，用于执行代码。
        files = self.files_path  # 给智能体一个文件阅读。
        bot = Assistant(llm=self.llm_cfg,
                        system_message=system_instruction,
                        files=files,
                        name='基础大模型',
                        description=f'''友好的对话助手，能够回答用户提出的各种问题。''')
        return bot

    def init_doctor_agent_service(self):
        system_instruction = """你是一名内科医生，正在为一位抱怨头痛和疲劳的患者进行问诊。请根据患者的症状进行诊断，
        并提出进一步的检查或治疗建议。确保你的语言专业且易于理解，以便患者能够清楚地了解他们的健康状况。"""
        tools = [
            # 'my_image_gen',
            'code_interpreter']  # `code_interpreter` 是框架自带的工具，用于执行代码。
        files = self.files_path  # 给智能体一个文件阅读。
        bot = Assistant(llm=self.llm_cfg,
                        system_message=system_instruction,
                        files=files,
                        name='医生',
                        description=f'''为一位抱怨头痛和疲劳的患者进行问诊''')
        return bot

    def init_teacher_agent_service(self):
        system_instruction = """你是一位小学教师，正在帮助一位八岁的学生理解简单的数学概念。
        学生对数学有点害怕，所以请你用温和、鼓励的语气解释，加上生活中的例子，让学生感到轻松并愿意学习。"""
        tools = [
            # 'my_image_gen',
            'code_interpreter']  # `code_interpreter` 是框架自带的工具，用于执行代码。
        files = self.files_path  # 给智能体一个文件阅读。
        bot = Assistant(llm=self.llm_cfg,
                        system_message=system_instruction,
                        files=files,
                        name='老师',
                        description=f'''帮助一位八岁的学生理解简单的数学概念''')
        return bot

    def init_waiter_agent_service(self):
        system_instruction = """你是一个高档餐厅的服务员，正在为一对夫妇提供服务。这是他们第一次来这家餐厅，你需要推荐菜单上的特色菜，
        并根据他们的口味和饮食习惯提供合适的选择。你需要礼貌而专业地应对他们的所有问题，并确保他们有一个愉快的用餐体验。"""
        tools = [
            # 'my_image_gen',
            'code_interpreter']  # `code_interpreter` 是框架自带的工具，用于执行代码。
        files = self.files_path  # 给智能体一个文件阅读。
        bot = Assistant(llm=self.llm_cfg,
                        system_message=system_instruction,
                        files=files,
                        name='餐厅服务员',
                        description=f'''为一对夫妇提供服务''')
        return bot

    def init_bank_agent_service(self):
        system_instruction = """你是一名银行的客户服务代表，正在帮助一位客户解决信用卡账单的争议问题。
        客户对账单上的一些费用产生疑问并有些焦虑。你需要耐心地解释账单细节，并提供解决方案，确保客户感到满意和理解。"""
        tools = [
            # 'my_image_gen',
            'code_interpreter']  # `code_interpreter` 是框架自带的工具，用于执行代码。
        files = self.files_path  # 给智能体一个文件阅读。
        bot = Assistant(llm=self.llm_cfg,
                        system_message=system_instruction,
                        files=files,
                        name='银行客户服务代表',
                        description=f'''帮助客户解决信用卡账单的争议问题''')
        return bot

    def init_knowledge_agent_service(self):
        system_instruction = """你是一个知识丰富的助手，擅长回答关于科学、历史、技术、文化等领域的问题。请确保你的回答基于事实，并提供必要的解释。"""
        tools = [
            # 'my_image_gen',
            'code_interpreter']  # `code_interpreter` 是框架自带的工具，用于执行代码。
        files = self.files_path  # 给智能体一个文件阅读。
        bot = Assistant(llm=self.llm_cfg,
                        system_message=system_instruction,
                        files=files,
                        name='知识问答',
                        description=f'''擅长回答关于科学、历史、技术、文化等领域的问题。''')
        return bot

    def init_writing_agent_service(self):
        system_instruction = """你是一位擅长写作的助手，能够帮助用户进行创意写作。无论是故事、诗歌、还是描述性的段落，你都能提供灵感和建议，确保内容富有创意且结构清晰。"""
        tools = [
            # 'my_image_gen',
            'code_interpreter']  # `code_interpreter` 是框架自带的工具，用于执行代码。
        files = self.files_path  # 给智能体一个文件阅读。
        bot = Assistant(llm=self.llm_cfg,
                        system_message=system_instruction,
                        files=files,
                        name='创意写作',
                        description=f'''擅长写作的助手，能够帮助用户进行创意写作。''')
        return bot

    def init_problem_agent_service(self):
        system_instruction = """你是一个逻辑清晰的助手，能够帮助用户分析问题并提出解决方案。请仔细理解用户的问题，并提供可行的建议或步骤，以帮助用户解决他们面临的挑战。"""
        tools = [
            # 'my_image_gen',
            'code_interpreter']  # `code_interpreter` 是框架自带的工具，用于执行代码。
        files = self.files_path  # 给智能体一个文件阅读。
        bot = Assistant(llm=self.llm_cfg,
                        system_message=system_instruction,
                        files=files,
                        name='问题解决',
                        description=f'''帮助用户分析问题并提出解决方案。''')
        return bot

    def init_emotional_agent_service(self):
        system_instruction = """你是一位关心用户情感的助手，善于提供情感上的支持和鼓励。无论用户面临什么样的情感困扰，你都应以温和、理解的语气进行回应，并提供积极的建议。"""
        tools = [
            # 'my_image_gen',
            'code_interpreter']  # `code_interpreter` 是框架自带的工具，用于执行代码。
        files = self.files_path  # 给智能体一个文件阅读。
        bot = Assistant(llm=self.llm_cfg,
                        system_message=system_instruction,
                        files=files,
                        name='情感支持',
                        description=f'''关心用户情感的助手，善于提供情感上的支持和鼓励。''')
        return bot
