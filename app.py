import streamlit as st
import random

def generate_question():
    elements = [
        ("Na+", "Ion"), ("Cl-", "Ion"), ("O", "Átomo neutro"),
        ("Ca2+", "Ion"), ("N", "Átomo neutro"), ("H+", "Ion"),
        ("Fe", "Átomo neutro"), ("K+", "Ion"), ("Br-", "Ion"), ("He", "Átomo neutro")
    ]
    return random.choice(elements)

if "question" not in st.session_state:
    st.session_state.question, st.session_state.answer = generate_question()

st.title("¿Ion o Átomo Neutro?")
st.write("Determina si el elemento mostrado es un ion o un átomo neutro.")

st.subheader(f"Elemento: {st.session_state.question}")

user_answer = st.radio("Selecciona una opción:", ["Ion", "Átomo neutro"], index=None)

if st.button("Verificar respuesta"):
    if user_answer:
        if user_answer == st.session_state.answer:
            st.success("¡Correcto!")
        else:
            st.error(f"Incorrecto. La respuesta correcta es: {st.session_state.answer}")
    else:
        st.warning("Selecciona una respuesta antes de verificar.")

if st.button("Nueva pregunta"):
    st.session_state.question, st.session_state.answer = generate_question()
    st.experimental_rerun()
