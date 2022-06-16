import base64
import os

import numpy as np
import pandas as pd
import spacy
import spacy_streamlit as st_nlp
import streamlit as st
from hydralit import HydraHeadApp
from PIL import Image

from mada.data_preview import dataset_preview
from mada.download_demo_csv import get_binary_file_downloader_html
from mada.get_download_link import get_table_download
from mada.home import home_page


class madagascar_app(HydraHeadApp):
    def run(self):

        # image = Image.open("logoos.png")
        nlp = spacy.load("en_core_web_sm")
        menu = ["Home", "Dataset preview", "Download Entity File"]
        choice = st.selectbox("Menu", menu)

        # st.image(image, use_column_width=False)

        new_title = '<p style="font-family:chilanka; font-size: 40px;">Madagascar Biospacy Model</p>'
        st.markdown(new_title, unsafe_allow_html=True)

        st.write(
            """

        **Biospacy** is a Python Package containing pretrained **spaCy** models to extract biodiversity information
        from texts. **Biospacy** can extract information on **taxonomic names**, **common names**, **habitats**,
        **country names** and **locations**.

        **Biospacy Madagascar** is a country package that is trained to recognise terms and places from South Africa.
        **Biospacy Madagascar** is under active development and this is simply a demonstration.

        To use it:

        - Enter the sample text or your own text into the box. Then use Control and Enter to start the model (Command + Enter on a Mac).
            Wait a short while and you will see the results.
        - Try using a **spreadsheet/csv file**. You can download the sample dataset for South Africa given below.
            When you upload you will be asked to choose a column containing the texts you want to process. For the sample just use **text** and press Go.
            Bear in mind that this can take a few moments to produce the results if your CSV file is  large.
            """
        )

        new_t = '<p style="font-family:chilanka; font-size: 15px;">To try the model copy and paste this message in the text field below and press Ctrl + Enter.</p>'
        st.markdown(new_t, unsafe_allow_html=True)

        st.write(
            """
        text

                Local plants as repellents against Anopheles arabiensis, in
            Mpumalanga Province, South Africa..
            OBJECTIVE: To assess the repellency effect of three local plants;
            fever tea (Lippia javanica), rose geranium (Pelargonium reniforme) and
            lemon grass (Cymbopogon excavatus) against laboratory reared Anopheles arabiensis mosquitoes.
            DESIGN: A laboratory experimental study. SETTING: Mpumalanga Province, South Africa.
            SUBJECTS: Three adult male volunteers. """
        )

        # Enter/pasting sample text
        doc = nlp(st.text_area("Paste sample text"))
        st_nlp.visualize_ner(doc, labels=nlp.get_pipe("ner").labels)

        new_text = '<p style="font-family:chilanka; font-size: 15px;">To try a sample dataset, click the on Download dataset below to download dataset</p>'
        st.markdown(new_text, unsafe_allow_html=True)

        st.markdown(
            get_binary_file_downloader_html("africa_short.csv", "dataset"),
            unsafe_allow_html=True,
        )

        # def madagascar_a():
        if choice == "Home":
            home_page()
        elif choice == "Dataset preview":
            dataset_preview()
        elif choice == "Download Entity File":
            get_table_download()

        # if __name__ == "__main__":
        # main()
