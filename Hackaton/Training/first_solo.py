from classiq import *
import pprint
# authenticate()

@qfunc
def flip_msb(reg: QArray):
    X(reg[reg.len - 1])

alpha = 0
@qfunc
def apply_control(x: QNum, y: QNum):
    control(ctrl=(x == 15), stmt_block=(lambda: inplace_xor(17, y)))
    if alpha == 0:
        print("Yes")
@qfunc
def main(x: Output[QNum], y: Output[QNum]):
    allocate(4,x)
    allocate(5, y)
    hadamard_transform(x)
    apply_control(x, y)


quantum_program = synthesize(create_model(main))
show(quantum_program)

job = execute(quantum_program)
results = job.result()[0].value.parsed_counts
pprint.pprint(results)

write_qmod(create_model(main), "quantum_operations")