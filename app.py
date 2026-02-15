import streamlit as st
import google.generativeai as genai

# Настройка страницы
st.set_page_config(page_title="AI Конфликт-Транслятор")
st.title("🕊️ Конфликт-Транслятор")

# 1. ПОЛУЧЕНИЕ КЛЮЧА (БЕЗОПАСНО)
# Проверяем наличие ключа в Secrets
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("🔑 Ошибка: Ключ GEMINI_API_KEY не найден в Secrets!")
    st.info("Зайдите в Settings -> Secrets в Streamlit Cloud и добавьте ключ.")
    st.stop()

# 2. ИНТЕРФЕЙС
user_input = st.text_area("Введите ваше сообщение (как оно звучит сейчас):")

if st.button("Трансформировать"):
    if user_input:
        try:
            prompt = f"Перефразируй это сообщение, чтобы оно звучало конструктивно и без агрессии, сохраняя смысл: {user_input}"
            response = model.generate_content(prompt)
            st.subheader("Результат:")
            st.success(response.text)
        except Exception as e:
            st.error(f"Произошла ошибка при обращении к ИИ: {e}")
    else:
        st.warning("Пожалуйста, введите текст.")
