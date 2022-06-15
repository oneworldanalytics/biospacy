FROM python:3.8.5

RUN pip install --upgrade pip

#RUN pip install en_core_bahamas_sm/en_core_web_sm-2.3.1/dist/en_core_web_sm-2.3.1.tar.gz

# copying everything over
COPY . .

# copy over and install packages
RUN pipenv install

# exposing default port for streamlit
EXPOSE 8501

# run app
CMD streamlit run ./host_app.py
