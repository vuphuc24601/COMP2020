import random 

a = 1
ops = [4, 5, 10, 11]
sa = 0
op = 12
v = 0

def logic(a, b, op):
    if op == 4:
        c = a & b
    elif op == 5:
        c = a|b
    elif op == 10:
        c = a^b
    else:
        c = ~(a|b)

    return c

def random_case():
    a = random.randint(-2**31, 2**31-1)
    b = random.randint(-2**31, 2**31-1)
    op = random.choice(ops)

    c = logic(a, b, op)
    return a, b, op, c


def edge_case():
    a_list = [-2**31, 2**31-1, 0, 1, -1]
    b_list = [-2**31, 2**31-1, 0, 1, -1]
    for op in ops:
        for b in b_list:
            for a in a_list:
                c = logic(a, b, op)
                writer.write(f'\n{a}\t\t{b}\t\t{op}\t\t{sa}\t\t{c}\t\t{v}')


with open('gate32.txt', 'w') as writer:
    writer.write(f'A[32]\tB[32]\tOp[4]\tSa[5]\tC[32]\tV')
    # generate edge case
    writer.write(f"\n#Edge Cases")
    edge_case()

    #generate random cases
    writer.write(f"\n\n#Random Cases")
    for i in range(500):
        a, b, op, c = random_case()
        writer.write(f'\n{a}\t\t{b}\t\t{op}\t\t{sa}\t\t{c}\t\t{v}')