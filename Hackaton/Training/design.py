from classiq import *
import pprint
# authenticate()

@qfunc
def main(x: Output[QNum],z: Output[QNum], y: Output[QNum]):

    allocate(5, x)
    allocate(5, z)
    hadamard_transform(x)  # creates a uniform superposition
    hadamard_transform(z)  # creates a uniform superposition
    y |= 2*x + 4*z + 2

quantum_program = synthesize(create_model(main))
show(quantum_program)

job = execute(quantum_program)
results = job.result()[0].value.parsed_counts
pprint.pprint(results)