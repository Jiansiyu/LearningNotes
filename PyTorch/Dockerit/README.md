
# PyTouch Docker Image
 
![](https://missinglink.ai/wp-content/uploads/2019/05/Pytorch.png)


# Table of Contents
1. [CS4501 Machine Learning for NLP](#cs4501-machine-learning-for-nlp)
2. [Compile CUDA Docker Image](#compile-cuda-docker-image)
3. [Connect pycharm to Docker Image](#connect-pycharm-to-docker-image)
4. [Deploy script to the docker Image](#deploy-your-script-to-the-docker-image)


## CS4501 Machine Learning for NLP
This is docker image is used for the Homework of class CS4501 [Machine Learning for NLP](http://yangfengji.net/uva-nlp-course/).

### Webpage 

[NLP](http://yangfengji.net/uva-nlp-course/schedule.html)

### Reference Books
* [JE] Eisenstein, [Natural Language Processing](https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf), 2018
* Jurafsky and Martin, [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/), 3rd Edition, 2019
* Smith, [Linguistic Structure Prediction](https://www.morganclaypool.com/doi/abs/10.2200/S00361ED1V01Y201105HLT013), 2009
* Shalev-Shwartz and Ben-David, [Understanding Machine Learning: From Theory to Algorithms](http://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/), 2014
* Goodfellow, Bengio and Courville, [Deep Learning](http://www.deeplearningbook.org/), 2016


## [Official Docker Image](https://hub.docker.com/r/pytorch/pytorch)

```shell script
docker pull pytorch/pytorch
```

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

