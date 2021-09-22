import numpy as np

class NeuralNetwork():
    layers = []
    hidden_layers = []
    def __init__(self, tam_layers, n_outputs):
        for i in range(0, len(tam_layers)):
            if i < len(tam_layers) -1:
                new_layer = self.createSynapticWeights(tam_layers[i], tam_layers[i+1])
                self.layers.append(new_layer)
            else:
                new_layer = self.createSynapticWeights(tam_layers[i], n_outputs)
                self.layers.append(new_layer)
        # self.layer1 = self.createSynapticWeights(3,5)
        # self.layer2 = self.createSynapticWeights(5,1)

    def createSynapticWeights(self, entrada, salida):
        return 2 * np.random.random((entrada, salida)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):

        for iteration in range(training_iterations):
            # Pass the training set through our neural network (a single neuron).

            # IMPORTANTE DEBES CREAR LAS HIDDEN LAYERS Y HACERLAS UNA LISTA
            for i in range(0, len(self.layers)):
                if len(self.hidden_layers) < len(self.layers):
                    if i == 0:
                        self.hidden_layers.append(self.think(training_inputs, self.layers[i]))
                    else:
                        self.hidden_layers.append(self.think(self.hidden_layers[i-1], self.layers[i]))
                else:
                    if i == 0:
                        self.hidden_layers[i] == self.think(training_inputs, self.layers[i])
                    else:
                        self.hidden_layers[i] == self.think(self.hidden_layers[i-1], self.layers[i])

            # l1 = self.think(training_inputs, self.layer1)
            # l2 = self.think(l1, self.layer2)

            # Calculate the error (The difference between the desired output
            # and the predicted output).
            errors = []
            for x in range(1, len(self.layers)+1):
                if x == 1:
                    l_error = training_outputs - self.hidden_layers[-x]
                    l_delta = l_error * self.sigmoid_derivative(self.hidden_layers[-x])
                else:
                    l_error = l_delta.dot(self.layers[-x + 1].T)
                    l_delta = l_error * self.sigmoid_derivative(self.hidden_layers[-x])
                errors.append(l_error)
            # l2_error = training_outputs - l2
            # l2_delta = l2_error * self.sigmoid_derivative(l2)
            # l1_error = l2_delta.dot(self.layer2.T)
            # l1_delta = l1_error * self.sigmoid_derivative(l1)

            # Multiply the error by the input and again by the gradient of the Sigmoid curve.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.
            ajustes = []
            for c in range(0, len(errors)):
                if c == 0:
                    ajuste = np.dot(training_inputs.T, errors[-(c+1)] * self.sigmoid_derivative(self.hidden_layers[c]))
                else:
                    ajuste = np.dot(self.hidden_layers[c-1].T, errors[-(c+1)] * self.sigmoid_derivative(self.hidden_layers[c]))
                ajustes.append(ajuste)

            # ajustes = np.dot(training_inputs.T, l1_error * self.sigmoid_derivative(l1))
            # ajustes2 = np.dot(l1.T, l2_error * self.sigmoid_derivative(l2))

            for d in range(0, len(ajustes)):
                self.layers[d] += ajustes[d]
            # self.layer1 += ajustes
            # self.layer2 += ajustes2

    def think(self, inputs, layer):
        output = self.sigmoid(np.dot(inputs, layer))
        return output
    def thinkNew(self, inputs):
        inputs = inputs.astype(float)
        for i in range(0, len(self.layers)):
            if i == 0:
                layer = self.think(inputs, self.layers[i])
            else:
                layer = self.think(layer, self.layers[i])
        return layer

        # l1 = self.think(inputs, self.layer1)
        # return self.think(l1, self.layer2)
