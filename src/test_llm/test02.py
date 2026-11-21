from agent.my_llm import bai_lian_custom_llm

for chunk in bai_lian_custom_llm.stream('用三句话简单介绍一下：机器学习的基本概念'):
    print(type(chunk))
    print(chunk)
    # reasoning_steps = [r for r in chunk.content_blocks if r["type"] == "reasoning"]
    # print(reasoning_steps if reasoning_steps else chunk.text)