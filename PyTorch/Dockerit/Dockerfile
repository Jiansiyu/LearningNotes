# NVIDIA CUDA Docker runtime enviroment for GPU Calc
#          first CUDA Toy
# author : Siyu Jian (jiansiyu@gmail.com)
#   University of Virginia
#         Go Hoos
#TODO, need to add the command to create user and login as non-root user

FROM nvidia/cuda:latest
#COPY ./requirements.txt /workfolder/requirements.txt

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y python3.8 \
    && apt-get install -y python3-pip \
    && apt-get install -y vim \
    && pip3 install --upgrade pip \
    && pip3 install torch torchvision \
    && apt-get autoremove \
    && apt-get autoclean

    #&& pip install -r /workfolder/requirements.txt \
    #&& rm /workfolder/requirements.txt \

# end