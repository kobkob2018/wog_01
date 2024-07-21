FROM python:alpine
WORKDIR /app
COPY app .
RUN pip install -r pip_install.txt
CMD python main_score.py