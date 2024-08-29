

class IntelligentMatrix:
    def __init__(self):
        pass

    def variable_aggregation(self):
        """聚合变量"""
        pass

    def check_variable_empty(self, **kwargs):
        """检查变量是否为空"""
        for key, value in kwargs.items():
            if not value:
                return True
        return False

    def get_unexist_variable(self, **kwargs):
        unexist = []
        for key in kwargs:
            if not kwargs[key]:
                unexist.append(key)
        return unexist

    def run(self, stepNum, guid, data):
        if stepNum == 1:
            print(guid)
            print(data)
            return str([683871918508032, 700681154037760])
        elif stepNum == 3 and data == "第一个":
            print(guid)
            print(data)
            return str(683871918508032)
        elif stepNum == 3 and data == "第二个":
            print(guid)
            print(data)
            return str(700681154037760)


if __name__ == '__main__':
    result = IntelligentMatrix().run(stepNum=1, guid="474bff4abb7f41928ec2992718df247d",
                                     data="(用户需要查找的内容)我想了解数据安全评估的内容与方法")
    print(result)
