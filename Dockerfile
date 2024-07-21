FROM python:alpine
COPY app .
RUN pip install -r pip_install.txt
CMD python main_score.py