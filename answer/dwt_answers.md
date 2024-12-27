### Differentiate between Al, machine learning and deep learning
AI stands for Artificial Intelligence. It is a broad field that encompasses the creation of intelligent machines that have human-like abilities such as problem-solving and learning. Machine learning is a subset of AI that focuses on algorithms and statistical models that enable computers to learn from data and make predictions or decisions without being explicitly programmed. Deep learning is a subset of machine learning that uses artificial neural networks, which are inspired by the structure and function of the human brain, to learn from large amounts of data and make predictions or decisions. 
 - Source: [18, 1, 11, 16]


### Differentiate between Al, machine learning and deep learning State the difference between Classification and Prediction. Can
a neural network be used both as a classifier and a Predictor?
The main objective of AI is to create intelligent machines that can think and act like humans. Whereas, machine learning is a subset of AI that involves algorithms and statistical models that enable machines to learn from data and make predictions without being explicitly programmed. Deep learning is a subset of machine learning that involves the use of artificial neural networks to learn from data and make complex decisions. 

Classification and prediction are two different tasks in machine learning. Classification involves predicting a class or category for a given data point, while prediction involves predicting a numerical value for a given data point. 

Yes, a neural network can be used for both classification and prediction tasks. The output layer of a neural network can be configured to have a single neuron for regression tasks (prediction) and multiple neurons for classification tasks. The neural network learns to map the input data to the desired output based on the specific task at hand.
 - Source: [5, 18, 11, 277]


### State 4 qualities of an ideal activation function. Which activation functions should be used in the hidden layers?

1. Non-linear: An ideal activation function should be non-linear in order to capture complex relationships in the data.
2. Continuous: The function should be continuous in order to facilitate gradient-based optimization.
3. Differentiable: It should have a well-defined derivative in order to enable efficient gradient calculations.
4. Monotonic: The function should be monotonic to preserve the ordering of inputs and outputs.

The activation functions used in hidden layers should have a non-linear nature, such as Sigmoid, Tanh, or ReLU neurons. These functions allow for complex relationships to be captured and can be easily differentiated for efficient optimization.
 - Source: [12, 10, 29, 175]


### What is the effect of learning rate if it is too high and, too low during training a Neural Network?
If the learning rate is too high, the training process may become unstable and may diverge away from the minimum, leading to poor performance. On the other hand, if the learning rate is too low, the training process may take a longer time to converge, resulting in slow learning and potentially getting stuck in local minima. Therefore, the learning rate needs to be carefully chosen to ensure efficient and effective training of a neural network.
 - Source: [29, 20, 26, 28]


### (ot What is vanishing gradient problem? Which activation functions
exhibit this problem? 

The vanishing gradient problem refers to the issue of gradients becoming increasingly small or vanishing as they are propagated through many layers in a deep neural network. This leads to slower or ineffective learning, as the small gradients are unable to update the weights effectively. 

Activation functions that exhibit this problem include the sigmoid and hyperbolic tangent (tanh) functions, as their gradients become small as the input value increases or decreases. This is especially problematic in recurrent neural networks, where the gradient must be propagated through multiple time steps. 
 - Source: [65, 176, 63, 175]


### Consider a neural network with one input layer, one hidden
layer with 2 neurons and one output layer with one neuron.
Draw the architecture of the neural network with the given data
and calculate the total learnable parameters.
The architecture of the neural network is:
  
  Input layer --> Hidden layer (2 neurons) --> Output layer (1 neuron)
  
  The total learnable parameters are:
  2 (weights between input and hidden layer) + 2 (biases for hidden layer) + 2 (weights between hidden and output layer) + 1 (bias for output layer) = 7 learnable parameters
 - Source: [29, 10, 32, 17]


### 20 State the difference between batch gradient descent, stochastic gradient descent
(SGD) and Mini batch gradient descent?
Batch gradient descent uses the entire dataset to calculate the gradient and update the weights, SGD uses one data point from the dataset to calculate the gradient and update the weights, and mini batch gradient descent uses a subset of the dataset (minibatch) to calculate the gradient and update the weights.
 - Source: [26, 25, 82, 76]


