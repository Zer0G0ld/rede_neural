import math

input = 1
input_weight = 0.5

output_desire = 0
learning_rate = 0.1

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0
    
print('Entrada', input, 'desejado', output_desire)

error = math.inf

iteration = 0 

bias = 1
bias_weight = 0.5

while not error == 0:
    iteration += 1
    print("########## Interacao: ", iteration)
    print("peso", input_weight)

    sum = (input * input_weight) + (bias * bias_weight)

    output = activation(sum)

    print('saida', output)

    error = output_desire - output

    print('erro', error)

    if not error == 0:
        input_weight = input_weight + (learning_rate * input * error)
        bias_weight = bias_weight+ (learning_rate * bias * error)

print("PARABENS!!! A REDE APRENDEU")