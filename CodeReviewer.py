import streamlit as st
import google.generativeai as ai

# Configure the API key
ai.configure(api_key="AIzaSyBCkRgwswkl6yfhmhZvUgtue6VDZsa3hSU")

# Streamlit Page Configuration
st.set_page_config(page_title="AI Code Reviewer")

# Custom CSS for better UI
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .stTextArea, .stTextInput {
            background-color: white !important;
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button {
            background-color: #007BFF;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# System prompt for AI Code Reviewer
sys_prompt = """
You are an AI Code Reviewer.

Your task is to review the given code and provide feedback on:
- Code efficiency and optimization
- Readability and maintainability
- Best practices and coding standards
- Potential errors or security vulnerabilities
- Suggestions for improvement

Provide your analysis in a structured format with examples where necessary.
If the provided input is not code, ask the user to enter a valid code snippet.
"""

# Initialize the Generative Model
model = ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=sys_prompt)

# Streamlit App Title
st.markdown("<h1 style='text-align: center;'>🧑‍💻 AI Code Reviewer</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #555;'>Get AI-powered feedback on your code!</h4>", unsafe_allow_html=True)
st.write("---")

# User Input for code review with Syntax Highlighting
st.subheader("📝 Paste Your Code Below:")
user_code = st.text_area("Enter your code:", placeholder="Paste your code here...", height=250)

# Button to trigger review
if st.button("🔍 Review Code"):
    if user_code.strip():
        with st.spinner("Analyzing your code... ⏳"):
            try:
                # Generate response from the model
                response = model.generate_content(f"Review the following code:\n\n{user_code}")

                # Display the review in an expandable section
                st.success("✅ Code Review Completed!")
                with st.expander("📌 **Review Summary**"):
                    st.write(response.text if hasattr(response, 'text') else response)
                
                # Syntax Highlighting for better readability
                st.subheader("📜 **Your Code:**")
                st.code(user_code, language="python")  # Adjust language as needed

            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter a valid code snippet for review.")

# Footer
st.write("---")

