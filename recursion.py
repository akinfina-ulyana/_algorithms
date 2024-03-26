def sum_array(list):
    if list == []:
        return 0
    return list[0]+sum_array(list[1:])


def generate_numbers(N:int, M:int, prefix=None):  # N - основание системы счисления, M - количество чисел
    """Генерирует все числа с  лид.0, в N-ричной системе, длины М"""
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()



def find(number, A):
    for x in A:
        if number == x:
            return True
    return False
def generate_permutations(N:int, M:int=-1, prefix=None):
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(4)












