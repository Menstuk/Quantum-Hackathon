from classiq import *
import pprint
# authenticate()
@qfunc
def main(x: Output[QNum], y: Output[QNum]):

    allocate(4, x)
    hadamard_transform(x)  # creates a uniform superposition
    y |= x**2 + 1

quantum_program = synthesize(create_model(main))
# show(quantum_program)
job = execute(quantum_program)
results = job.result()[0].value.parsed_counts
pprint.pprint(results)