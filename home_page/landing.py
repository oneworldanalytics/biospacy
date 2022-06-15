import base64
import os

import numpy as np
import pandas as pd
import spacy
import spacy_streamlit as st_nlp
import streamlit as st
from hydralit import HydraHeadApp
from PIL import Image


class landing_app(HydraHeadApp):
    def run(self):

        # st.image(image, use_column_width=False)

        new_title = (
            '<p style="font-family:chilanka; font-size: 40px;">Biospacy</p>'
        )
        st.markdown(new_title, unsafe_allow_html=True)

        st.write(
            """

        **Biospacy** is a Python Package containing pretrained **spaCy** models to extract biodiversity information
        from texts. **Biospacy** can extract information on **taxonomic names**, **common names**, **habitats**,
        **country names** and **locations**.

        **Biospacy {country}** is a country package that is trained to recognise terms and places from South Africa.
        **Biospacy {country}** is under active development and this is simply a demonstration.

        Country models supported are:

        - Biospacy Kenya
        - Biospacy South Africa
        - Biospacy Cameroon
        - Biospacy Madagascar
        - Biospacy Namibia

            """
        )

        st.write("Developers")
        st.write(
            """
        This app was developed by [Paul Oldham](https://github.com/poldham) and [Reuben Nyaribari](https://github.com/foscraft) from the data science team \
        at One World Analytics and Amband.\
        To learn more visit [oneworldanalytics.com](http://oneworldanalytics.com/) and [amband.co.ke](https://amband.co.ke/)
            """
        )
        st.write("Funding")
        st.write(
            """
        The development of Biospacy {COUNTRY} forms part of the [Bioinnovation Africa project](https://www.giz.de/en/worldwide/78516.html) of the \
        [ABS Initiative](http://www.abs-initiative.info/) coordinated by [GIZ](https://www.giz.de/en/html/index.html) in partnership with the \
        [South African Department of Environment, Forestry and Fisheries (DEFF)](https://www.environment.gov.za/).
            """
        )
