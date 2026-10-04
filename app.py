import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📚",
)

st.title("📚 AI Document Assistant")
st.write("输入问题，Gemini 会生成回答。")

question = st.text_area(
    "你的问题",
    placeholder="例如：什么是 RAG？",
)

if st.button("生成回答"):
    if not question.strip():
        st.warning("请先输入问题。")
    else:
        try:
            with st.spinner("正在生成回答..."):
                client = genai.Client()
                response = client.interactions.create(
                    model="gemini-3.5-flash",
                    input=question[:1000],
                )

            st.subheader("回答")
            st.write(response.output_text)

        except Exception as error:
            st.error("暂时无法生成回答，请检查 API 配置或免费额度。")
            # st.error("生成回答时发生错误。")
            # st.code(f"{type(error).__name__}: {error}")