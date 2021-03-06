import numpy as np
import matplotlib.pyplot as plt
from sklearn import   datasets,manifold

def load_data():
    '''
    load the iris data
    :return: train_data, train_value
    '''
    iris=datasets.load_iris()
    return  iris.data,iris.target

def test_Isomap(*data):
    '''
    test Isomap method
    :param data: train_data, train_value
    :return: None
    '''
    X,y=data
    for n in [4,3,2,1]:
        isomap=manifold.Isomap(n_components=n)
        isomap.fit(X)
        print('reconstruction_error(n_components=%d) : %s'%
            (n, isomap.reconstruction_error()))
def plot_Isomap_k(*data):
    '''
    test the performance with different n_neighbors and reduce to 2-D
    :param data: train_data, train_value
    :return: None
    '''
    X,y=data
    Ks=[1,5,25,y.size-1]

    fig=plt.figure()
    for i, k in enumerate(Ks):
        isomap=manifold.Isomap(n_components=2,n_neighbors=k)
        X_r=isomap.fit_transform(X)

        ax=fig.add_subplot(2,2,i+1)
        colors=((1,0,0),(0,1,0),(0,0,1),(0.5,0.5,0),(0,0.5,0.5),(0.5,0,0.5),
            (0.4,0.6,0),(0.6,0.4,0),(0,0.6,0.4),(0.5,0.3,0.2),)
        for label ,color in zip( np.unique(y),colors):
            position=y==label
            ax.scatter(X_r[position,0],X_r[position,1],label="target= {0}"
            .format(label),color=color)

        ax.set_xlabel("X[0]")
        ax.set_ylabel("X[1]")
        ax.legend(loc="best")
        ax.set_title("k={0}".format(k))
    plt.suptitle("Isomap")
    plt.show()
def plot_Isomap_k_d1(*data):
    '''
    test the performance with different n_neighbors and reduce to 1-D
    :param data: train_data, train_value
    :return: None
    '''
    X,y=data
    Ks=[1,5,25,y.size-1]

    fig=plt.figure()
    for i, k in enumerate(Ks):
        isomap=manifold.Isomap(n_components=1,n_neighbors=k)
        X_r=isomap.fit_transform(X)

        ax=fig.add_subplot(2,2,i+1)
        colors=((1,0,0),(0,1,0),(0,0,1),(0.5,0.5,0),(0,0.5,0.5),(0.5,0,0.5),
            (0.4,0.6,0),(0.6,0.4,0),(0,0.6,0.4),(0.5,0.3,0.2),)
        for label ,color in zip( np.unique(y),colors):
            position=y==label
            ax.scatter(X_r[position],np.zeros_like(X_r[position]),
            label="target= {0}".format(label),color=color)

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend(loc="best")
        ax.set_title("k={0}".format(k))
    plt.suptitle("Isomap")
    plt.show()
if __name__=='__main__':
    X,y=load_data()
    test_Isomap(X,y)
    plot_Isomap_k(X,y)
    plot_Isomap_k_d1(X,y)