import random 

ops = [2, 3, 6, 7]
v = 0

def add(a, b, op):
    c = a + b
    v = 0
    if op in [2, 3]:
        c = a + b
    else:
        c = a - b

    if c > 2**31-1 or c < -2**31:
        v = 1

    return c, v


def random_case():
    a = random.randint(-2**31, 2**31-1)
    b = random.randint(-2**31, 2**31-1)
    op = random.choice(ops)
    sa = random.randint(0, 31)

    c, v = add(a, b, op)

    return a, b, op, sa, c, v


def edge_case():
    a_list = [-2**31, 2**31-1, 0, 1, -1]
    b_list = [-2**31, 2**31-1, 0, 1, -1]
    v = 0
    for op in ops:
        for a in a_list:
            for b in b_list:
                sa = random.randint(0, 31)
                c, v = add(a, b, op)
                writer.write(f'\n{a}\t\t{b}\t\t{op}\t\t{sa}\t\t{c}\t\t{v}')
                v = 0



with open('add32.txt', 'w') as writer:
    text = [
        "\n#Test cases for add32\n\n",
        "#Decimal\n",
        "#Op in [2, 3, 6, 7]\n",
        "#Edge Cases:\n", 
        "#A and B in [-2**31, 2**31-1, 0, 1, -1]\n", 
        "#Random Cases:\n",
        "#A and B from -2**31 and 2**31 - 1\n",
        "#Sa from 0 to 31\n"
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


    

