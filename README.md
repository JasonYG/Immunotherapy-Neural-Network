Immunotherapy-Neural-Network
-----
This project uses a simple neural network created from scratch in Python to predict the results of immunotherapy treatment given several characteristics of patients. Although not perfect, this simple neural network was created to practice prominent techniques and algorithms used in AI and machine learning.  

The dependencies in this project are numpy and sympy.  

The dataset was acquired from the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Immunotherapy+Dataset). There are a total of 7 features per patient, and a label which is a classification of either 0 or 1, i.e. the result of the treatment.

The project uses a squared error cost function and backpropagation to update the weights of the neural network. The sigmoid function is used as the activation function.

Next Steps
---
As of now, the backpropagation algorithm using sympy is incorrect. The weights are not being updated correctly. 
