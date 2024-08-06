import streamlit as st

# User input for the chat
user_message = st.text_input("You:", "")

# Check if there's any message entered by the user
if user_message:
    # Display user's message on the left side (default)
    with st.chat_message("user"):
        st.markdown(user_message)
    
    # Simulate a response (this could be from a chatbot model, for example)
    bot_response = "Hello! How can I help you today?"
    
    # Display bot's response on the right side
    with st.chat_message("assistant"):
        st.markdown(bot_response)
