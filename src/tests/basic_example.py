from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from src.utils.config import load_config

config = load_config()

llm = OpenAI(temperature=0.9, openai_api_key=config["openai"]["api_key"])
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("custom doors"))
