import math
import numpy as np

class Perceptron:
    def __init__(self, input_size):
        self.input_values = np.ones(input_size) # Assuming bias is included in input
        self.input_weights = np.random.rand(input_size)
        self.output_desire = 0
        self.learning_rate = 0.1
        self.error = np.inf

    def activation(self, value):
        return 1 if value >=0 else 0

perceptron = Perceptron(input_size=2) # Assuming two input values

iteration = 0

print("Entrada: ", perceptron.input_values, "desejado: ", perceptron.output_desire)

while not np.array_equal(perceptron.error, np.zeros_like(perceptron.error)):
    iteration += 1

    print("####### Interação: ", iteration)
    print("Peso: ", perceptron.input_weights)

    _sum = np.dot(perceptron.input_values, perceptron.input_weights)
    output = perceptron.activation(_sum)

    print("Saída: ", output)

    perceptron.error = perceptron.output_desire - output

    print("Erro: ", perceptron.error)

    if not np.array_equal(perceptron.error, np.zeros_like(perceptron.error)):
        perceptron.input_weights = perceptron.input_weights + (perceptron.learning_rate * perceptron.input_values * perceptron.error)

print("PARABÉNS!!! A REDE APRENDEU")

