# Importing Necessary modules
from fastapi import FastAPI
import uvicorn

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

# Loading Iris Dataset
iris = load_iris()

# Getting features and targets from the dataset
X = iris.data
Y = iris.target

# Fitting our Model on the dataset
clf = GaussianNB()
clf.fit(X, Y)

app = FastAPI()


@app.get('/')
def main():
    return {'message': 'Welcome to GeeksforGeeks!'}


@app.get('/{name}')
def hello_name(name: str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f'Welcome to GeeksforGeeks!, {name}'}
