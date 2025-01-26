from openai import OpenAI
import time
import os
start_time = time.time()
# send a ChatCompletion request to count to 100

client = OpenAI(
    api_key=os.environ.get("KEY") or "key",  # 从环境变量获取API密钥
    #base_url="https://api.deepseek.com",  # DeepSeek API地址
    base_url="http://127.0.0.1:11434/v1",  # DeepSeek API地址
)
messages = [{"role": "user", "content": "4 9 20 35 66 下一个数字."}]
response = client.chat.completions.create(
    #model="deepseek-reasoner",
    model="deepseek-r1:14b", 
    messages=messages,
    stream=True  # again, we set stream=True
)

reasoning_content = ""
content = ""

for chunk in response:
    if hasattr(chunk.choices[0].delta, "reasoning_content") and chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end="")
        reasoning_content += chunk.choices[0].delta.reasoning_content
    elif chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
            content += chunk.choices[0].delta.content