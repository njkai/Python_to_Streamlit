FROM python:3.7-apline

COPY . /Python_to_Streamlit

WORKDIR /Python_to_Streamlit

RUN pip3 install -r requirements.txt

USER 1001
EXPOSE 5000
CMD ["python3", "/Python_to_Streamlit/app.py"]
