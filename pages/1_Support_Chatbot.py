import streamlit as st
from openai import OpenAI

# Set up page configuration
st.set_page_config(page_title="MiniStore Support Chatbot", page_icon="💬", layout="centered")

st.title("💬 MiniStore Customer Support")
st.write("Ask questions about products, orders, shipping, returns, refunds, and payments.")

# 1. Securely check and grab the OpenAI API key from secrets
if "OPENAI_API_KEY" not in st.secrets or not st.secrets["OPENAI_API_KEY"]:
    st.error("Missing OpenAI API Key! Please configure your `.streamlit/secrets.toml` file correctly.")
    st.stop()

# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 2. Define the system instructions to make it behave like a store support agent
SYSTEM_PROMPT = """
You are a helpful, friendly, and professional customer support assistant for 'MiniStore', an e-commerce platform.
Your job is to assist users with questions regarding:
- Products and inventory
- Order status and tracking
- Shipping rates and delivery times
- Returns, refunds, and payment issues

Always stay polite, keep answers concise, and guide the customer clearly.
"""

# 3. Initialize chat history in session state so it remembers context
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# 4. Display previous chat messages (excluding the hidden system prompt)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 5. Handle new user inputs
if user_input := st.chat_input("How can I help you today?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Call OpenAI API (using gpt-4o-mini as a fast, cost-effective model)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,  # Streams text live to the screen
            )
            
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
                    
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"An error occurred while communicating with OpenAI: {e}")
            full_response = "I'm sorry, I'm having trouble connecting right now. Please try again later."
            message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})