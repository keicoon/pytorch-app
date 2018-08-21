from __future__ import print_function

from torch
from model import main, test

def str2data(str):
    # @TODO:
    data = str
    return data

def preprocessing(data):
    # @TODO:
    perf_data = data
    return perf_data

def loadModel(mnistModel):
    path_pretrained_model = './pretraied_model.pt'
    model.load_state_dict(torch.load(path_pretrained_model))
    return model

def evaluation(text):
    imgData = str2data(text)
    
    X = preprocessing(imgData)

    model = loadModel(main())

    predict_num = model(X)

    return predict_num