from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "What is the capital of France? Answer in one word.",
    "Explain what an API is in 2 sentences.",
    "Write a detailed 300-word essay on the history of artificial intelligence.",
]

for i, p in enumerate(prompts, 1):
    print(f"\n--- Prompt {i}: {p}")
    print(llm.invoke(p).content)