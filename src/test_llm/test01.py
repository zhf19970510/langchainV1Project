from agent.my_llm import openai_llm

# resp = deepseek_llm2.invoke('用三句话介绍一下：机器学习的基本概念')
# print(type(resp))
# print(resp)

# resp = llm.invoke('用三句话介绍一下：机器学习的基本概念')
# print(type(resp))
# print(resp)

resp = openai_llm.invoke('用三句话介绍一下：机器学习的基本概念')
print(type(resp))
print(resp)
