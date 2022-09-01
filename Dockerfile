FROM python:3
RUN pip install growattServer
RUN pip install flask
RUN pip install flask-restful
ADD GWpyth.py /
CMD [ "python", "./GWpyth.py"]
