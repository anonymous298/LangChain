from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

# hf_model = pipeline('text-generation', model='gpt2')
model = AutoModelForCausalLM.from_pretrained('openai-community/gpt2')
tokenizer = AutoTokenizer.from_pretrained('openai-community/gpt2')

pipe = pipeline('text-generation', model=model, tokenizer=tokenizer)

llm = HuggingFacePipeline(pipeline=pipe)

prompt_template = PromptTemplate(
    input_variables=['topic'],
    template="Answer the following question: {topic}"
)

chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

response = chain.run('What is AI?')
print(response)
