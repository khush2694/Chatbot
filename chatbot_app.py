{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "361dc68a-374d-4466-8793-997da0147d5b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-08 16:55:23.139 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /opt/anaconda3/lib/python3.12/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import openai\n",
    "import streamlit as st\n",
    "from dotenv import load_dotenv\n",
    "import os\n",
    "\n",
    "# Load OpenAI API key from .env file\n",
    "load_dotenv()\n",
    "openai.api_key = os.getenv(\"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\")\n",
    "\n",
    "# Function to get a response from OpenAI API (ChatGPT)\n",
    "def get_chatgpt_response(user_input):\n",
    "    try:\n",
    "        response = openai.Completion.create(\n",
    "            engine=\"gpt-3.5-turbo\",  # You can use different engines like 'gpt-3.5-turbo'\n",
    "            messages=[\n",
    "                {\"role\": \"system\", \"content\": \"You are a helpful assistant.\"},\n",
    "                {\"role\": \"user\", \"content\": user_input},\n",
    "            ]\n",
    "        )\n",
    "        message = response['choices'][0]['message']['content']\n",
    "        return message\n",
    "    except Exception as e:\n",
    "        return f\"Error: {e}\"\n",
    "\n",
    "# Streamlit UI setup\n",
    "st.title(\"ChatGPT Basic Chatbot\")\n",
    "\n",
    "# Create a text input box for user input\n",
    "user_input = st.text_input(\"You: \", \"\")\n",
    "\n",
    "if user_input:\n",
    "    # Get ChatGPT's response\n",
    "    response = get_chatgpt_response(user_input)\n",
    "    # Display the conversation\n",
    "    st.write(f\"ChatGPT: {response}\")\n",
    "\n",
    "# Optional: Display a welcome message\n",
    "if not user_input:\n",
    "    st.write(\"Start typing to chat with the bot!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "9f2a3c56-30d8-4d95-a550-c7f453f9568d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
