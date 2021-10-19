import random 

exec(open("shift32.py").read())
exec(open("compare32.py").read())
exec(open("gate32.py").read())
exec(open("add32.py").read())

with open('alu32.txt', 'w') as writer, \
        open("shift32.txt") as r1, \
        open("compare32.txt") as r2, \
        open("gate32.txt") as r3, \
        open("add32.txt") as r4:

    writer.write("#ALU test file, including all subcircuit test cases\n")
    # generate edge case
    writer.write(r1.read().strip() + r2.read().strip() + r3.read().strip() + r4.read().strip())

with open("alu32.txt", "r") as r:
    lines = r.readlines()


with open('alu32.txt', 'w') as writer:
    is_first = True
    for line in lines:
        if line.strip("\n") != "A[32]\tB[32]\tOp[4]\tSa[5]\tC[32]\tV":
            writer.write(line)
        else:
            if is_first:
                writer.write(line)
                is_first = False





    

