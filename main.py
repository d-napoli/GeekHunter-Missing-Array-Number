def ordena_array(array):
    array_ordenado = []
    array_ordenado.append(int(array[0]))

    del array[0]

    for i in array:
        num_atual = int(i)
        j = len(array_ordenado)
        k = 0
        while k < j:
            temp_pos = -999
            if num_atual < array_ordenado[k]:
                temp_pos = k
                k = j + 1
            k += 1

        if temp_pos != -999:
            array_ordenado.insert(temp_pos, num_atual)
        else:
            array_ordenado.append(num_atual)
    return array_ordenado

def numero_faltando_array(array):
    i = 0
    while i < len(array) - 1:
        if array[i] + 1 != array[i + 1]:
            return array[i] + 1
        i += 1
    return array[len(array) - 1] + 1

def main():
    print("Informe a quantidade de arrays")
    qtd_inputs = input()
    count = 0

    while count < int(qtd_inputs):
        print("Informe o array:")
        array_ordenado = ordena_array(input()[1:-1].split(','))
        numero_faltando = numero_faltando_array(array_ordenado)
        print(numero_faltando)
        count += 1

main()
