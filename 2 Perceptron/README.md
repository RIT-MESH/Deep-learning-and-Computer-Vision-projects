# Perceptron
The perceptron mimics the function of neurons in machine learning algorithms. The perceptron is one of the oldest machine learning algorithms in existence. When it was first used in 1957 to perform rudimentary image recognition, the New York Times called it:\
"**The embryo of an electronic computer that [the Navy] expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence.**"

The whole idea behind the artificial neuron and Rosenblatt's thresholded perceptron model is to use a reductionist approach to mimic how a single neuron in the brain works
   - it either fires
   - or it doesn’t
The pseudo algorithm can be thought of as
   - Initialize the weights to 0 or small random numbers.
   - For each training sample x(i) :
       -  Compute the output value ˆy
       -  Update the weights.
 The perceptron works on these simple steps
a. All the inputs x are multiplied with their weights w. Let’s call it k
<img alt=" " src="https://github.com/RIT-MESH/Deep-learning-and-Computer-Vision-projects/blob/main/2%20Perceptron/pe1.JPG" />

b. Add all the multiplied values and call them Weighted Sum
<img alt=" " src="https://github.com/RIT-MESH/Deep-learning-and-Computer-Vision-projects/blob/main/2%20Perceptron/pe2.JPG" />

c. Apply that weighted sum to the correct Activation Function.
The activation functions are used to map the input between the required values like (0, 1) or (-1, 1). 

<img alt=" " src="https://github.com/RIT-MESH/Deep-learning-and-Computer-Vision-projects/blob/main/2%20Perceptron/pe3.JPG" />
________________________________________________________________________________________________________________________________________________________
&nbsp;  



This predictive linear model which was developed based on labeled data sets, let's place it inside of a node. Our model node is going to receive two input notes the X1 and X2 respectively.

We also implemented, gradient descent, which in every iteration minimizes the error and adjusts a linear model that better classifies our data until it comes up with the perfect.

**Final output:**

<img alt=" " src="https://github.com/RIT-MESH/Deep-learning-and-Computer-Vision-projects/blob/main/2%20Perceptron/Perceptron.gif" />


