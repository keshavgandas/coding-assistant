from decouple import config
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

# Load the Hugging Face API token from environment variables
HUGGINGFACEHUB_API_TOKEN = config('HUGGINGFACEHUB_API_TOKEN')
# Define the model repository ID
repo_id = "deepseek-ai/deepseek-coder-1.3b-instruct"

def askproblem(query):
    # Initialize the HuggingFace LLM
    llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)
    
    # Initialize the chat model
    chat = ChatHuggingFace(llm=llm, verbose=True)
    
    # Define the system message template
    system_message_prompt = SystemMessagePromptTemplate.from_template(
        "You are a highly skilled AI coding assistant. Your task is to analyze the given query and provide accurate, detailed, and optimized coding solutions. Always ensure your responses align with best practices, are efficient, and consider edge cases. Introduce yourself as a coding assistant."
    )
    
    # Define the human message template
    human_message_prompt = HumanMessagePromptTemplate.from_template('{query}')
    
    # Combine the system and human message templates into a ChatPromptTemplate
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    
    # Format the messages with the query
    formatted_messages = chat_prompt.format_messages(query=query)
    
    # Invoke the chat model with the formatted messages
    response = chat.invoke(formatted_messages)
    
    # Return the response content
    return response.content


# from decouple import config
# from langchain_core.prompts import ChatMessagePromptTemplate , HumanMessagePromptTemplate , SystemMessagePromptTemplate
# from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace

# HUGGINGFACEHUB_API_TOKEN = config('HUGGINGFACEHUB_API_TOKEN')
# repo_id = "deepseek-ai/deepseek-coder-33b-instruct"

# def askproblem(query):
#     llm = HuggingFaceEndpoint(repo_id=repo_id , huggingfacehub_api_token= HUGGINGFACEHUB_API_TOKEN)
    
#     chat = ChatHuggingFace(llm=llm , verbose=True)
#     systemMessagePrompt = SystemMessagePromptTemplate.from_template(
#         "you are a highly skilled AI coding assistant , your task is to analyze the given query and provide accurate detaled , and optimized coding solution. Always ensure your response align with best practicees , is efficent and consider edge cases. Introduce yourself as a coding assistant "
#     )
    
#     HumanMessagePrompt = HumanMessagePromptTemplate.from_template('{query}')
#     chatprompt = ChatMessagePromptTemplate.format_messages([systemMessagePrompt , HumanMessagePrompt])
    
#     formattedChatPrompt = chatprompt.format_messages(query = query)
#     response = chat.invoke(formattedChatPrompt)
#     return response.content
