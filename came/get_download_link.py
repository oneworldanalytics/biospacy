import base64
from io import BytesIO

import pandas as pd
import spacy
import spacy_streamlit as st_nlp
import streamlit as st

nlp = spacy.load("en_core_web_sm")


# LAST PART-conversion and link for download
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(writer, index=False, sheet_name="Sheet1")
    writer.save()
    return output.getvalue()


def get_table_download_link(df):
    """Below is your generated link to download your csv output file"""
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download csv file</a>'  # decode b'ab


def get_table_download():
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
        st.write("column preview")
        st.write(df_ents.head(2))
        st.markdown(get_table_download_link(df_ents), unsafe_allow_html=True)
