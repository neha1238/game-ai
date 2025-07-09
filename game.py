import streamlit as st
import io
import contextlib

st.set_page_config(page_title="Python Code Runner", layout="centered")

st.title("💡 Python Code Editor")
st.write("Write your Python code below and hit Run:")

# Code input
code = st.text_area("Python code", height=200, value="print('Hello, Prabhat!')")

# Run button
if st.button("Run Code"):
    st.subheader("🔧 Output:")
    output_buffer = io.StringIO()

    with contextlib.redirect_stdout(output_buffer):
        try:
            exec(code)
        except Exception as e:
            st.error(f"Error: {e}")

    st.code(output_buffer.getvalue(), language='text')
