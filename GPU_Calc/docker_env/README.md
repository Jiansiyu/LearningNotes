# NVIDIA CUDA Docker Image 

![](https://cloud.githubusercontent.com/assets/3028125/12213714/5b208976-b632-11e5-8406-38d379ec46aa.png)

# Table of Contents
1. [Compile CUDA Docker Image](#compile-cuda-docker-image)
2. [Connect pycharm to Docker Image](#connect-pycharm-to-docker-image)
3. [Deploy script to the docker Image](#deploy-your-script-to-the-docker-image)


## Compile cuda Docker Image
The customized docker Image are bassed on NVIDIA CUDA docker Image. Compile Your run enviroment:

```shell script
docker build -t [dockerImageName] .
```
The dockerfile will copy the requirements.txt file to the docker image and install all the dependents, so make sure you have updated the requirements.txt file if you need additional dependents. 

## connect pycharm to docker image 
Only the pycharm-professional can connect to the docker image. More details please refer to [link](../../dockerit/README.md)

 
## Deploy your script to the docker Image


## Useful tricks

1. run NVIDIA CUDA docker with interactive shell mode 
```shell script
 docker run    --gpus all -it nvidia/cuda:10.0-base bash
```

2. check the nvidia msi 
```shell script
docker run --gpus all --rm nvidia/cuda nvidia-smi
```

3. Check Docker Numba-CUDA
```shell script
sudo docker run  --gpus all --rm  gputest  python3 -c "import numba;from numba import cuda;print(numba.cuda.gpus)"
```

If it print out the following infortion:
```
<Managed Device 0>
```
It means you have install everything successfully!!

