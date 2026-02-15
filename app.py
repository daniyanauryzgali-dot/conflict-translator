import streamlit as st
from groq import Groq

st.set_page_config(page_title="Конфликт-Транслятор", page_icon="🕊️")
st.title("🕊️ Конфликт-Транслятор")

# Проверяем ключ
if "GROQ_API_KEY" in st. secrets:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
else:
    st.error("Ключ GROQ_API_KEY не найден в Secrets!")
    st.stop()

user_input = st.text_area("Введите ваше сообщение:")

if st.button("Трансформировать"):
    if user_input:
        try:
            # Используем модель Llama 3 - она очень мощная и быстрая
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "Ты помощник, который перефразирует агрессивные сообщения в конструктивные и вежливые на русском языке."},
                    {"role": "user", "content": user_input}
                ],
            )
            st.subheader("Результат:")
            st.success(completion.choices[0].message.content)
        except Exception as e:
            st.error(f"Ошибка: {e}")
    else:
        st.warning("Сначала введите текст!")
