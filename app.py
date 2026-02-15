import streamlit as st
from groq import Groq

st.title("Conflict Translator")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

text = st.text_area("Что случилось? (введи фразу)")
style = st.radio("Как ответить?", ["Вежливо", "Официально", "Задать вопрос"])

if st.button("Перевести"):
    if text:
        my_prompt = f"""
        Разбери фразу: {text}
        1. Какая тут эмоция?
        2. Какой скрытый смысл?
        3. Переделай в стиле {style}.
        4. Будет ли конфликт дальше (в %)?
        """
        
        try:
            chat = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": my_prompt}]
            )
            
            result = chat.choices[0].message.content
            st.write("---")
            st.write(result)
            
        except Exception as e:
            st.error(f"Ошибка: {e}")
    else:
        st.write("Пусто, напиши что-нибудь")
