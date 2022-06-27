import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0 #start eith some values of m and b and then take these baby steps to reach to a global minima
    iterations = 10000 #defining how many baby steps you are going to do
    n = len(x)
    learning_rate = 0.08 #defining learning rate. here random value is given. See hoe the algorithm behaves and then tweak those parameters

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr #calculate the predicted value of y
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)]) #printing cost which is the cost function
        md = -(2/n)*sum(x*(y-y_predicted)) #calculate m derivative
        bd = -(2/n)*sum(y-y_predicted) #calculate b derivative
        m_curr = m_curr - learning_rate * md #adjusting m current
        b_curr = b_curr - learning_rate * bd #adjusting b current
        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i)) #printing each iteration value along with cost at each iteration

x = np.array([1,2,3,4,5]) # np.array i.e. numpy array is used because matrix multiplication is very convenient with this, also this tends to be faster than simple python list
y = np.array([5,7,9,11,13])

gradient_descent(x,y)