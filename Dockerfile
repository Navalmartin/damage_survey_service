# pull the official docker image and enforce architecture
FROM --platform=linux/amd64 python:3.11

# set the working directory inside the container
WORKDIR /app

# copy the functionality
COPY ./run_streamlit.sh /app/run_streamlit.sh
COPY ./config.py /app/config.py
COPY ./damage_survey_app.py /app/damage_survey_app.py
COPY ./menu.py /app/menu.py

COPY ./pages /app/pages
COPY ./.streamlit /app/.streamlit
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8001

# run the API
CMD ["bash", "./run_streamlit.sh"]