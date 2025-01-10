from openai import OpenAI


def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat", messages=messages, tools=tools,temperature=0, max_tokens=100, top_p=1.0, n=1, stop=None
    )
    return response.choices[0].message


client = OpenAI(
    api_key="key",
    base_url="https://api.deepseek.com",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取天气信息",
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
]

def get_weather(location: str):
    print(f"==> 调用get_weather函数，参数location={ location }")
    return {"location": location, "weather": "晴"}
def call_user(phone_number: str):
    print(f"==> 调用call_user函数，参数phone_number={ phone_number }")
    return {"phone_number": phone_number, "status": "calling"}
def select_protocol(position: str): 
    print(f"==> 调用select_protocol函数，参数position={ position }")
    return {"position": position, "protocol": "T1"}
messages=[]
while True:
    msg=input("请输入您的问题：")
    messages.append({"role": "user", "content": msg})
    message = send_messages(messages)
    if message.tool_calls!=None:
        messages=[]
        for tool in message.tool_calls:
            print(f"程序执行>\t 函数名:{tool.function.name},参数{tool.function.arguments}")
            func1_name = tool.function.name
            func1_args = tool.function.arguments
            func1_out = eval(f'{func1_name}(**{func1_args})')
            print(f"程序执行>\t 函数返回值:{func1_out}")
        print(f"assistant>\t {message.content}")   
    else:
        messages.append({"role": "assistant", "content": message.content})
        print(f"assistant>\t {message.content}")            
