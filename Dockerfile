FROM wbms/odoo-15.0
# FROM arm64v8/odoo:15.0
# FROM odoo:15

USER root

RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    libffi-dev \
    libssl-dev \
    cargo \
    zip

RUN pip3 install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
RUN rm /requirements.txt

# COPY ./misc.py /usr/lib/python3/dist-packages/odoo/tools/misc.py
