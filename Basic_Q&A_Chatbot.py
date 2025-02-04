import streamlit as st
from langchain.chat_models import ChatOllama
from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Custom CSS for a stunning UI
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stApp {
            background: linear-gradient(to right, #141e30, #243b55);
            color: white;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #00D4FF;
        }
        .chat-container {
            border-radius: 10px;
            padding: 15px;
            background-color: rgba(255, 255, 255, 0.1);
        }
        .chat-bubble {
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .user-message {
            background-color: #0084ff;
            color: white;
            align-self: flex-end;
        }
        .ai-message {
            background-color: #282c34;
            color: white;
            align-self: flex-start;
        }
        .stButton>button {
            background-color: #00D4FF !important;
            color: black !important;
            font-size: 18px;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 8px;
        }
        .stTextInput>div>div>input {
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Creating our main class
class ChatBot:
    def __init__(self):
        self.llm = ChatOllama(model='deepseek-r1:1.5b')

    def getPromptTemplate(self):
        '''
        This method will create a Scheme Template and returns it.

        Returns:
            ChatPromptTemplate
        '''

        try:
            prompt_template = ChatPromptTemplate.from_messages(
                [
                    ('system', 'You are a helpful assistant'),
                    ('user', 'Question: {question}')
                ]
            )
            return prompt_template
        except Exception as e:
            print(e)

    def get_chain(self):
        '''
        This method will create a chain and returns it.

        Returns:
            Chain
        '''

        try:
            llm = self.llm
            prompt_template = self.getPromptTemplate()
            parser = StrOutputParser()
            chain = prompt_template | llm | parser
            return chain
        except Exception as e:
            print(e)

    def get_llm_response(self, question):
        '''
        This is the main method which will take user input and returns the LLM response.

        Params:
            question: User Input query.

        Returns:
            LLM Response
        '''
        
        try:
            chain = self.get_chain()
            response = chain.invoke({'question': question})
            return response
        except Exception as e:
            print(e)

# UI Header
st.markdown("<div class='title'>🚀 AI-Powered ChatBot</div>", unsafe_allow_html=True)

# Chat Interface
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

user_question = st.text_input("💬 Enter your query:")
chatbot = ChatBot()

if st.button("Ask AI 🤖"):
    response = chatbot.get_llm_response(user_question)
    
    # Chat bubbles for user and AI responses
    st.markdown(f"<div class='chat-bubble user-message'><b>You:</b> {user_question}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-bubble ai-message'><b>AI:</b> {response}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)