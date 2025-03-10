class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
       
        self.weights = [0] * input_size 
        self.bias = 0
        self.learning_rate = learning_rate
        self.epochs = epochs
    
    def activation(self, x):
        return 1 if x >= 0 else 0
    
    def train(self, X, y):
        for _ in range(self.epochs):
            for inputs, target in zip(X, y):
                weighted_sum = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
                prediction = self.activation(weighted_sum)
                error = target - prediction
                self.weights = [w + self.learning_rate * error * i for w, i in zip(self.weights, inputs)]
                self.bias += self.learning_rate * error
    
    def predict(self, inputs):
        weighted_sum = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        return self.activation(weighted_sum)

X = [[0, 0],[0, 1],[1, 0],[1, 1]]
y = [0, 0, 0, 1]

perceptron = Perceptron(input_size=2)
perceptron.train(X, y)

for inputs in X:
    output = perceptron.predict(inputs)
    print(f"Inputs: {inputs} -> Output: {output}")
