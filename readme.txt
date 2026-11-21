set UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
pip install -U langchain
pip install -U langchain-openai
pip install -U dotenv
 pip install langchain-deepseek
pip install langchain langchain-core langchain-anthropic langchain-ollama langchain-community dashscope zhipuai pyjwt httpx tencentcloud-sdk-python
pip install --upgrade "langgraph-cli[inmem]"

合成一个命令：
pip install langchain langchain-openai dotenv
另一种命令方式：
pip install 'langchain[openai]' dotenv

启动agent方式，项目根目录下执行命令：
langgraph dev
windows启动agent报错，需要修改对应python虚拟环境下的Lib\site-packages\langgraph_api\validation.py下的改文件：
with open(pathlib.Path(__file__).parent.parent / "openapi.json") as f:
改为：
with open(pathlib.Path(__file__).parent.parent / "openapi.json", encoding="utf-8") as f:
使用utf-8编码读取，不然启动会报错。
还有import加载包时，需要从src下agnt下的包开始import，否则会报错。
比如：
from agent.env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, OPENAI_API_KEY, OPENAI_BASE_URL, ALIBABA_BASE_URL, ALIBABA_API_KEY
不要写成：
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, OPENAI_API_KEY, OPENAI_BASE_URL, ALIBABA_BASE_URL, ALIBABA_API_KEY
其他包导入同理。