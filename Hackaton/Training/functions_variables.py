from classiq import *
import pprint
@qfunc
def flip_msb(reg: QArray):
    X(reg[reg.len - 1])

@qfunc
def main(indicator: Output[QBit]):
    x = QNum("smiley")
    allocate(4,x)
    hadamard_transform(x)
    flip_msb(x)
    indicator |= x == 8

quantum_program = synthesize(create_model(main))
show(quantum_program)

job = execute(quantum_program)
results = job.result()[0].value.parsed_counts
pprint.pprint(results)