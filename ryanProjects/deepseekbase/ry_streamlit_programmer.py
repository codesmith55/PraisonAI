import streamlit as st
import ollama

from praisonaiagents import Agent, Tools
from praisonaiagents.tools import execute_code, analyze_code, format_code, lint_code, disassemble_code # Code Tools
from praisonaiagents.tools import execute_command, list_processes, kill_process, get_system_info # Shell Tools
from praisonaiagents.tools import duckduckgo # Web Search Tool

# Set page title
st.title("Chat with Ollama")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display chat input
user_input = st.chat_input("Your message:")

# Display chat history and handle new inputs
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get streaming response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        completion = ollama.chat(
            model="deepseek-r1:latest",
            messages=st.session_state.messages,
            stream=True
        )
        
        # Process the streaming response
        for chunk in completion:
            if 'message' in chunk and 'content' in chunk['message']:
                content = chunk['message']['content']
                full_response += content
                message_placeholder.write(full_response + "▌")
        
        message_placeholder.write(full_response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    
    


agent = Agent(
    instructions="You are a Programming Agent", self_reflect=True, min_reflect=5, max_reflect=10, 
    tools=[execute_code, analyze_code, format_code, lint_code, disassemble_code, execute_command, list_processes, kill_process, get_system_info, duckduckgo]
)
agent.start(
    "Write a python script using yfinance to find the stock price of Tesla"
    "First check if required packages are installed"
    "Run it using execute_code"
    "execute_command if you want to run any terminal command"
    "search internet using duckduckgo if you want to know update python package information"
    "Analyse the output using analyze_code and fix error if required"
    "if no package is installed, install it"
    "then run the code"
)