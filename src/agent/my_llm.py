"""
Model Class 方式初始化模型
创建各类LLM模型
"""
from langchain.chat_models import init_chat_model
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI

from agent.my_custom_llm import BailianCustomChatModel
from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, OPENAI_API_KEY, OPENAI_BASE_URL, ALIBABA_BASE_URL, ALIBABA_API_KEY

deepseek_llm = ChatDeepSeek(    # langchain-deepseek
    api_key=DEEPSEEK_API_KEY,
    api_base=DEEPSEEK_BASE_URL,
    model="deepseek-chat",
)

deepseek_llm2 = ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
    model="deepseek-chat",
)

bai_lian_custom_llm = BailianCustomChatModel(   # 自定义的类来调用大模型
    api_key=ALIBABA_API_KEY,
    base_url=ALIBABA_BASE_URL,
    model_name="deepseek-v4.1-flash-1017",
)

#
openai_llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    temperature=0.5,
    model="gpt-4.1-mini",
)

llm = ChatOpenAI(
    api_key=ALIBABA_API_KEY,
    base_url=ALIBABA_BASE_URL,
    model="qwen-plus",
)

# 速率限制
rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.1,  # 1 request every 10s
    check_every_n_seconds=0.1,  # Check every 100ms whether allowed to make a request
    max_bucket_size=10, # Controls the maximum burst size
)

rate_limiter_model_llm = init_chat_model(
    model="deepseek-v4.1-flash-1017",
    model_provider="openai",
    api_key=ALIBABA_API_KEY,
    base_url=ALIBABA_BASE_URL,
    rate_limiter=rate_limiter,
)

#
# anthropic_llm = ChatAnthropic(
#     api_key=ANTHROPIC_API_KEY,
#     base_url=ANTHROPIC_BASE_URL,
#     # model="claude-3-5-haiku-latest",
#     model="claude-3-5-haiku-20241022",
# )
#
#
# ollama_llm = ChatOllama(
#     base_url="http://192.168.1.106:11434",
#     model="deepseek-r1:1.5b",
# )
#
# hunyuan_llm = ChatHunyuan(
#     hunyuan_app_id = HUNYUAN_APP_ID,
#     hunyuan_secret_id = HUNYUAN_SECRET_ID,
#     hunyuan_secret_key = HUNYUAN_SECRET_KEY,
#     model="hunyuan-lite",
# )
#
# tongyi_llm = ChatTongyi(
#     api_key=DASHSCOPE_API_KEY,
#     model="qwen-plus",
# )
#
#
# zhipu_llm = ChatZhipuAI(
#     api_key=ZHIPUAI_API_KEY,
#     model="glm-4",
# )
#
# zhipu_llm2 = ChatOpenAI(
#     api_key=ZHIPUAI_API_KEY,
#     base_url=ZHIPUAI_BASE_URL,
#     model="glm-4",
# )
