import pandas as pd
import spacy
import spacy_streamlit as st_nlp
import streamlit as st

nlp = spacy.load("en_core_web_sm")


def dataset_preview():
    uploaded_file = st.file_uploader("Choose a file..", type="csv")
    if uploaded_file is not None:
        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file)
        df = df.dropna()
        all_columns = df.columns
        selected_column = st.selectbox(
            "Select column to process", all_columns
        )  # ,default=None)
        new_df = df[selected_column]
        docs = nlp.pipe(iter(new_df))
        entities = []
        for doc in docs:
            entities.extend(
                {
                    "entity_text": ent.text,
                    "entuty_label": ent.label_,
                    "entity_start": ent.start,
                    "entity_end": ent.end,
                }
                for ent in doc.ents
            )
        df_ents = pd.DataFrame(entities)
        st.write("This is the first 5 rows preview of your output")
        st.write(df_ents.head(20))
