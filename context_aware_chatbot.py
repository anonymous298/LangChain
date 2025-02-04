from langchain_ollama import ChatOllama
from langchain.schema import AIMessage, SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model='deepseek-r1:1.5b')

chat_history = []

system_message = SystemMessage(content='You are an helpful assitant')
chat_history.append(system_message)

while True:
    user = input('Enter what you want to ask? ')

    if user.lower() == 'exit' or user.lower() == 'quit':
        break

    human = HumanMessage(content=user)
    chat_history.append(human)

    chain = llm | StrOutputParser()
    response = chain.invoke(chat_history)
    print(response)

    aimessage = AIMessage(content=response)
    chat_history.append(aimessage)