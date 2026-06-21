import streamlit as st

from src.rag_pipeline import RAGPipeline


st.set_page_config(
    page_title="Document Q&A Bot",
    page_icon="📚",
    layout="wide"
)


@st.cache_resource
def load_pipeline():
    return RAGPipeline()


rag = load_pipeline()

if "history" not in st.session_state:
    st.session_state.history = []

st.title("📚 Document Q&A Bot")

st.markdown(
    """
    Ask questions about your document collection using
    Retrieval-Augmented Generation (RAG).
    """
)

question = st.text_input(
    "Enter your question:",
    placeholder="What is cloud computing?"
)

if st.button("Ask Question", type="primary"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching documents..."
        ):

            response = rag.ask(
                question
            )
        st.session_state.history.append(
            {
                "question": question,
                "answer": response["answer"],
                "sources": response["sources"]
            }        )

        st.subheader("Answer")

        st.write(
            response["answer"]
        )

        if response["sources"]:

            st.subheader("Sources")

            grouped_sources = {}

            for source in response["sources"]:

                document = source["source"]
                page = source["page"]

                if document not in grouped_sources:
                    grouped_sources[document] = []

                grouped_sources[document].append(page)

            source_data = []

            for document, pages in grouped_sources.items():

                source_data.append(
                    {
                        "Document": document,
                        "Pages": ", ".join(
                            map(str, sorted(set(pages)))
                        )
                    }
                )

            st.table(source_data)

        else:
            st.info(
                "No supporting sources found."
            )

if st.session_state.history:

    st.subheader("Recent Questions")

    for item in st.session_state.history[:5]:

        with st.expander(
            item["question"]
        ):

            st.write(
                item["answer"]
            )
st.divider()

st.caption(
    "Built using Sentence Transformers, ChromaDB, Gemini, and Streamlit."
)