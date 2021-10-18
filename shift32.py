import random 

a = 1
ops = [0, 1, 12, 13]
v = 0


def srl(b, sa): 
    return b>>sa if b >= 0 else (b+2**32)>>sa


def sra(b, sa):
    c = b>>sa
    return c


def sll(b, sa):
    c = b << sa
    if (c > 2**31-1) or (c < -2**31):
        c = c % (2**32)

    return c


def shift(b, sa, op):
    if op in [0, 1]:
        c = sll(b, sa)
    elif op == 12:
        c = srl(b, sa)
    else:
        c = sra(b, sa)

    return c

def random_case():
    op = random.choice(ops)
    b = random.randint(-2**31, 2**31-1)
    sa = random.randint(0,31)
    c = shift(b, sa, op)
    return b, op, sa, c



def edge_case():
    b_list = [-2**31, 2**31-1, 0, 1, -1]
    sa_list = [0, 31, 1]
    for op in ops:
        for sa in sa_list:
            for b in b_list:
                c = shift(b, sa, op)
                writer.write(f'\n{a}\t\t{b}\t\t{op}\t\t{sa}\t\t{c}\t\t{v}')


with open('shift32.txt', 'w') as writer:
    writer.write(f'A[32]\tB[32]\tOp[4]\tSa[5]\tC[32]\tV')
    # generate edge case
    writer.write(f"\n#Edge Cases")
    edge_case()

    #generate random cases
    writer.write(f"\n\n#Random Cases")
    for i in range(500):
        b, op, sa, c = random_case()
        writer.write(f'\n{a}\t\t{b}\t\t{op}\t\t{sa}\t\t{c}\t\t{v}')