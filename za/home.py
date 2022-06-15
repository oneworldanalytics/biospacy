import pandas as pd
import spacy
import spacy_streamlit as st_nlp
import streamlit as st

nlp = spacy.load("en_core_web_sm")


def home_page():
    uploaded_file = st.file_uploader("Choose a file..", type="csv")
    if uploaded_file is not None:
        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file)
        st.write(df.head(3))
        all_columns = df.columns
        selected_column = st.selectbox("Select column to process", all_columns)
        new_df = df[selected_column]
        docs = nlp.pipe(new_df)
        for doc in docs:
            st_nlp.visualize_ner(
                doc, labels=nlp.get_pipe("ner").labels, key=len(doc)
            )
