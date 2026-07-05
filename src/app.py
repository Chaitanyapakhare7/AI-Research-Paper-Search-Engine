import streamlit as st
from search_engine import PaperSearchEngine

st.set_page_config(
    page_title="AI Research Paper Intelligence System",
    page_icon="📚",
    layout="wide",
)

@st.cache_resource(show_spinner="Loading models and index...")
def get_engine():
    return PaperSearchEngine()

with st.sidebar:
    st.header("⚙️ Settings")
    top_k = st.slider("Number of results", min_value=1, max_value=10, value=5)
    show_summary = st.checkbox("Generate AI summary", value=True)
    show_keywords = st.checkbox("Extract keywords", value=True)
    st.markdown("---")
    st.markdown("**How it works**\n\n"
                "1. Query embedded via `all-MiniLM-L6-v2`\n"
                "2. FAISS similarity search\n"
                "3. BART abstract summarization\n"
                "4. KeyBERT keyword extraction")

st.title("📚 AI Research Paper Intelligence System")
st.caption("Semantic search over 50,000 ArXiv Machine Learning papers.")

query = st.text_input("🔍 Search research papers", placeholder="e.g. deep learning for medical image analysis")
search_clicked = st.button("Search", type="primary")

if search_clicked and query.strip():
    engine = get_engine()
    
    with st.spinner("Searching and analyzing..."):
        results = engine.search(query, k=top_k)
        for r in results:
            if show_summary:
                r["summary"] = engine.summarize(r["abstract"])
            if show_keywords:
                r["keywords"] = engine.extract_keywords(r["abstract"])

    st.success(f"Found {len(results)} relevant papers")

    for r in results:
        with st.container(border=True):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.subheader(f"{r.get('rank', '')}. {r['title']}")
            with col2:
                st.metric("Similarity", f"{r['score']:.2f}")

            if show_summary and "summary" in r:
                st.markdown(f"**🧠 AI Summary:** {r['summary']}")

            with st.expander("View full abstract"):
                st.write(r["abstract"])
            
            recommendations = engine.recommend_papers(r["row_index"], top_n=3)
            with st.expander("📚 Recommended Papers"):
                for rec in recommendations:
                    st.markdown(f"**{rec['title']}**")
                    st.caption(f"Similarity Score: {rec['score']:.2f}")
            
            if show_keywords and "keywords" in r:
                kw_tags = "  ".join([f"`{kw}` ({score:.2f})" for kw, score in r["keywords"]])
                st.markdown(f"**🏷️ Keywords:** {kw_tags}")

elif search_clicked:
    st.warning("Please enter a search query.")
else:
    st.info("Enter a query above and click **Search** to explore.")
