import random 

ops = [4, 5, 10, 11]
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
    sa = random.randint(0, 31)

    c = logic(a, b, op)
    return a, b, op, sa, c, v


def edge_case():
    a_list = [-2**31, 2**31-1, 0, 1, -1]
    b_list = [-2**31, 2**31-1, 0, 1, -1]
    for op in ops:
        for b in b_list:
            for a in a_list:
                sa = random.randint(0, 31)
                c = logic(a, b, op)
                writer.write(f'\n{a}\t\t{b}\t\t{op}\t\t{sa}\t\t{c}\t\t{v}')


with open('gate32.txt', 'w') as writer:
    text = [
        "\n#Test cases for gate32\n\n",
        "#Decimal\n",
        "#Op in [4, 5, 10, 11]\n",
        "#Edge Cases:\n", 
        "#A and B in [-2**31, 2**31-1, 0, 1, -1]\n", 
        "#Random Cases:\n",
        "#A and B from -2**31 and 2**31 - 1\n",
        "#Sa from 0 to 31\n",
        "#Output V = 0\n"
        ]
    writer.writelines(text)
    writer.write(f'\nA[32]\tB[32]\tOp[4]\tSa[5]\tC[32]\tV\n')
    # generate edge case
    writer.write(f"\n#Edge Cases")
    edge_case()

    #generate random cases
    writer.write(f"\n\n#Random Cases")
    for i in range(500):
        a, b, op, sa, c, v = random_case()
        writer.write(f'\n{a}\t\t{b}\t\t{op}\t\t{sa}\t\t{c}\t\t{v}')