
import pandas

def load_data_train():
    df = pandas.read_csv('./data/train.csv')
    return df

def load_data_test():
    df = pandas.read_csv('./data/test.csv')
    return df

def load_data():
    df_train = load_data_train()
    df_test = load_data_test()

    d = {
        'train': df_train,
        'test': df_test,
    }
    return d

def load_data_sample_submission():
    df = pandas.read_csv('./data/sample_submission.csv')
    return df


def load_original_data():
    path = './data/original_data/credit_risk_dataset.csv'
    df = pandas.read_csv(path)
    return df
    


import numpy

def logspace(array):
    min_ = numpy.log10(array.min())
    max_ = numpy.log10(array.max())
    return numpy.logspace(min_, max_, 50)
    
def logspace(array, **kwargs):
    min_ = numpy.log10(array.min())
    max_ = numpy.log10(array.max())
    num_bins = 50
    if 'num_bins' in kwargs:
        num_bins = kwargs['num_bins']
    return numpy.logspace(min_, max_, num_bins)

def linspace(array):
    return numpy.linspace(array.min(), array.max(), array.max() - array.min())
    