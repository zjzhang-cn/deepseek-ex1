from openai import OpenAI
import os


def send_messages(messages):
    """
    发送消息到DeepSeek API并获取响应
    :param messages: 消息列表，包含用户和助手的对话历史
    :return: 返回API的响应消息对象
    """
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools,
        temperature=0,
        max_tokens=100,
        top_p=1.0,
        n=1,
        stop=None,
    )
    return response.choices[0].message


client = OpenAI(
    api_key=os.environ.get("KEY"),  # 从环境变量获取API密钥
    base_url="https://api.deepseek.com",  # DeepSeek API地址
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取省市的天气信息，用户需要提供城市或地区名称",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市或地区名称，如北京、上海等",
                    }
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "call_user",
            "description": "呼叫用户的电话，用户需要提供电话号码",
            "parameters": {
                "type": "object",
                "properties": {
                    "phone_number": {
                        "type": "string",
                        "description": "电话号码，例如 +86 13611111111",
                    }
                },
                "required": ["phone_number"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "select_protocol",
            "description": "选择病人进行MRI检查的协议",
            "parameters": {
                "type": "object",
                "properties": {
                    "position": {
                        "type": "string",
                        "description": "扫描的位置，如头部、胸部、腹部等",
                    }
                },
                "required": ["position"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "light_switch",
            "description": "控制灯的开关,用户需要提供灯的位置和状态",
            "parameters": {
                "type": "object",
                "properties": {
                    "position": {
                        "type": "string",
                        "description": "灯的位置，如卧室、客厅等",
                    },
                    "status": {
                        "type": "string",
                        "description": "灯的状态，如开、关等",
                    },
                },
                "required": ["position", "status"],
            },
        },
    },
]


def get_weather(location: str):
    """
    获取指定地区的天气信息
    :param location: 城市或地区名称
    :return: 包含位置和天气信息的字典
    """
    print(f"==> 调用get_weather函数，参数location={location}")
    return {"location": location, "weather": "晴"}


def call_user(phone_number: str):
    """
    呼叫指定电话号码
    :param phone_number: 要呼叫的电话号码
    :return: 包含电话号码和呼叫状态的字典
    """
    print(f"==> 调用call_user函数，参数phone_number={phone_number}")
    return {"phone_number": phone_number, "status": "calling"}


def select_protocol(position: str):
    """
    为指定身体部位选择MRI扫描协议
    :param position: 要扫描的身体部位
    :return: 包含部位和协议信息的字典
    """
    print(f"==> 调用select_protocol函数，参数position={position}")
    return {"position": position, "protocol": "T1"}


def light_switch(position: str, status: str):
    """
    控制指定位置的灯光状态
    :param position: 灯光位置（如卧室、客厅）
    :param status: 灯光状态（开/关）
    :return: 包含位置和状态的字典
    """
    print(f"==> 调用light_switch函数，参数position={position},status={status}")
    return {"position": position, "status": status}


messages = []  # 存储对话历史
count = 1  # 对话轮次计数器
while True:  # 主消息处理循环
    msg = input(f"请输入您的问题 #{count}：")  # 获取用户输入
    messages.append({"role": "user", "content": msg})  # 将用户消息加入对话历史
    message = send_messages(messages)  # 发送消息并获取响应
    if message.tool_calls:  # 如果响应包含工具调用
        count = 1  # 重置对话轮次计数器
        messages = []  # 清空对话历史
        for tool in message.tool_calls:  # 遍历所有工具调用
            print(f"程序执行>\t 函数名:{tool.function.name}, 参数:{tool.function.arguments}")  # 打印工具调用信息
            func1_name = tool.function.name  # 获取函数名
            func1_args = tool.function.arguments  # 获取函数参数
            func1_out = eval(f"{func1_name}(**{func1_args})")  # 动态执行函数
            print(f"程序执行>\t 函数返回值:{func1_out}")  # 打印函数返回值
        print(f"assistant>\t {message.content}")  # 打印助手回复
    else:  # 如果没有工具调用
        count = count + 1  # 增加对话轮次
        messages.append({"role": "assistant", "content": message.content})  # 将助手回复加入对话历史
        print(f"assistant>\t {message.content}")  # 打印助手回复
