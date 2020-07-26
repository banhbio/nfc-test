FROM ubuntu:18.04

RUN apt update -y
RUN apt upgrade -y

RUN apt -y install python3 python3-pip python-dev python-usb wget git usbutils kmod

RUN pip3 install -U nfcpy
RUN git clone https://github.com/nfcpy/nfcpy.git
