# DeepSeek Chat Application

## 项目简介

该项目是一个基于OpenAI的聊天应用程序，能够处理用户输入并调用特定的函数来执行任务。应用程序使用了DeepSeek的API来生成聊天响应，并根据需要调用不同的工具函数。

## 功能

- **获取天气信息**: 用户可以询问特定城市或地区的天气信息。
- **呼叫用户**: 用户可以请求呼叫特定的电话号码。
- **选择MRI检查协议**: 用户可以选择病人进行MRI检查的协议。

## 安装

1. 克隆项目到本地:
    ```bash
    git clone <repository_url>
    ```
2. 进入项目目录:
    ```bash
    cd deepseek-ex1
    ```
3. 安装依赖:
    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

1. 运行应用程序:
    ```bash
    python app.py
    ```
2. 根据提示输入您的问题:
    ```plaintext
    请输入您的问题：
    ```
3. 应用程序将处理您的输入，并根据需要调用相应的工具函数。

## 示例

```plaintext
请输入您的问题：北京的天气怎么样？
==> 调用get_weather函数，参数location=北京
程序执行>	 函数名:get_weather, 参数:{'location': '北京'}
程序执行>	 函数返回值:{'location': '北京', 'weather': '晴'}
assistant>	 北京的天气是晴
```

## 依赖

- openai==1.59.6
- python-certifi-win32==1.6.1

## 许可证

此项目使用MIT许可证 - 有关更多信息，请参阅LICENSE文件。
