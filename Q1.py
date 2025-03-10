class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def activation_function(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, inputs):
        weighted_sum = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        return self.activation_function(weighted_sum)
        
if __name__ == "__main__":
    weights = [0.5, -0.8, 0.1]
    bias = 0.2  
    neuron = Neuron(weights, bias)
    
    test_inputs = [
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 0]
    ]
    
    for inputs in test_inputs:
        output = neuron.predict(inputs)
        print(f"Inputs: {inputs} -> Output: {output}")
