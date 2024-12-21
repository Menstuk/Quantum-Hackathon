from classiq import *
import matplotlib.pyplot as plt
# authenticate()

@qfunc
def main(cntrl: Output[QArray[QBit]], target: Output[QBit]) -> None:
    allocate(20, cntrl)
    allocate(1, target)
    control(ctrl=cntrl, stmt_block=lambda: X(target))

# Synthesize 9 different implementations of an MCX with 20 control qubits and 1 target qubit, while varying the max number of qubits within the “max width”
# constraint - from 22 to 30. For each implementation, optimize for minimal depth. Plot a graph of the transpiled circuit depth as a function of the number of
# qubits used (i.e. the circuit width) in each implementation.
valid_widths = range(22, 31)
circuit_depth = []
qmod = create_model(main, out_file="mcx_example")
for width in valid_widths:
    qmod_with_constrains = set_constraints(qmod, Constraints(optimization_parameter = 'depth', max_width=width))
    qprog = synthesize(qmod_with_constrains)
    circuit_depth.append(QuantumProgram.from_qprog(qprog).transpiled_circuit.depth)
plt.plot(valid_widths, circuit_depth)
plt.xlabel('Number of qubits')
plt.ylabel('Circuit depth')
plt.title('Circuit depth as a function of the number of qubits used')
plt.show()
