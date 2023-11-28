import math
import numpy as pn

class Perceptron:
    def __init__(self):
        self.input_value = 1
        self.input_weight = 0.5
        self.output_desire = 0
        self.learning_rate = 0.1
        self.error = math.inf
        self.bias = 1
        self.bias_weight = 0.5

    def activation(self, value):
        if value >= 0:
            return 1
        else:
            return 0

perceptron = Perceptron()

iteration = 0

print("Entrada: ", perceptron.input_value, "desejado: ", perceptron.output_desire)

while not perceptron.error == 0:
    iteration += 1

    print("####### Interação: ", iteration)
    print("Peso: ", perceptron.input_weight)

    _sum = (perceptron.input_value * perceptron.input_weight) + (perceptron.bias * perceptron.bias_weight)
    output = perceptron.activation(_sum)

    print("Saída: ", output)

    perceptron.error = perceptron.output_desire - output

    print("Erro: ", perceptron.error)

    if not perceptron.error == 0:
        perceptron.input_weight = perceptron.input_weight + (perceptron.learning_rate * perceptron.input_value * perceptron.error)
        perceptron.bias_weight = perceptron.bias_weight + (perceptron.learning_rate * perceptron.bias * perceptron.error)

print("PARABÉNS!!! A REDE APRENDEU")

