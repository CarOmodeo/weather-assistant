from langchain_openai import ChatOpenAI


def create_llm_model():
    llm_openai = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
    )
    return llm_openai
