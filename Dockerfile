FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime

COPY ./requirements.txt /install/requirements.txt
RUN pip install -r /install/requirements.txt

WORKDIR /code
COPY ./UnderWaterGAN_pytorch/ /code/UnderWaterGAN_pytorch
COPY ./train_uwgan.sh /code/train_uwgan.sh

EXPOSE 8888

CMD [  "/bin/bash" ]