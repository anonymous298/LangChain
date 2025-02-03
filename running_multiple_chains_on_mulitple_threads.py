import threading

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

llm = Ollama(model='deepseek-r1:1.5b')

def chain1(word):
    print('Chain1 Executing')

    prompt_template1 = PromptTemplate(
        input_variables=['word'],
        template='Make a poem on {word}'
    )

    chain1 = prompt_template1 | llm
    response = chain1.invoke({'word' : word})
    print(response)

def chain2(word):
    print('Chain2 Executing')

    prompt_template2 = PromptTemplate(
        input_variables=['word'],
        template='Make a joke on {word}'
    )

    chain2 = prompt_template2 | llm
    response = chain2.invoke({'word' : word})
    print(response)

def chain3(word):
    print('Chain3 Executing') 

    prompt_template3 = PromptTemplate(
        input_variables=['word'],
        template='What is {word}?'
    )

    chain3 = prompt_template3 | llm
    response = chain3.invoke({'word' : word})
    print(response)

word = 'AI'

thread1 = threading.Thread(target=chain1, args=(word, ))
thread2 = threading.Thread(target=chain2, args=(word, ))
thread3 = threading.Thread(target=chain3, args=(word, ))

if __name__ == '__main__':
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()