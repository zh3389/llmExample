from qwen_agent.gui import WebUI
from bot import CreateBot


def app_gui():
    # Define the agent
    bot_base = CreateBot().init_base_agent_service()
    bot_doctor = CreateBot().init_doctor_agent_service()
    bot_teacher = CreateBot().init_teacher_agent_service()
    bot_waiter = CreateBot().init_waiter_agent_service()
    bot_bank = CreateBot().init_bank_agent_service()
    bot_knowledge = CreateBot().init_knowledge_agent_service()
    bot_writing = CreateBot().init_writing_agent_service()
    bot_problem = CreateBot().init_problem_agent_service()
    bot_emotional = CreateBot().init_emotional_agent_service()
    chatbot_config = {
        'prompt.suggestions': [
            {
                'text': f'@基础大模型 '
            },
            {
                'text': f'@知识问答 '
            },
            {
                'text': f'@创意写作 '
            },
            {
                'text': f'@问题解决 '
            },
            {
                'text': f'@情感支持 '
            },
            {
                'text': f'@医生 医生，我最近几天一直感到头痛，尤其是在下午的时候，而且总是觉得很累。是不是有什么严重的问题？'
            },
            {
                'text': f'@老师 老师，我不明白为什么10减去6等于4，能不能用一个简单的例子告诉我？'
            },
            {
                'text': f'@餐厅服务员 我们第一次来这里，你能推荐一下哪些菜比较特别吗？我们不吃辣，还有没有什么清淡一点的选择？',
            },
            {
                'text': f'@银行客户服务代表 我刚收到我的信用卡账单，上面有一笔我不记得的费用，这笔钱是什么时候扣的？我可以争议这笔费用吗？'
            },
        ]
    }
    WebUI([bot_base, bot_doctor, bot_teacher, bot_waiter, bot_bank, bot_knowledge, bot_writing, bot_problem, bot_emotional],
          chatbot_config=chatbot_config).run(messages=[{'role': 'assistant',
                                                        'content': [{'text': '试试看 @基础大模型 来问我~'}]
                                                        }],
                                             enable_mention=True,
                                             server_name='0.0.0.0')


if __name__ == '__main__':
    app_gui()
