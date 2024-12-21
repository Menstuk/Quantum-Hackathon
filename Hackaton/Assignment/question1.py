from classiq import *
import matplotlib.pyplot as plt
# authenticate()

@qfunc
def main(cntrl: Output[QArray[QBit]], target: Output[QBit]) -> None:
    allocate(5, cntrl)
    allocate(1, target)
    control(ctrl=cntrl, stmt_block=lambda: X(target))

qmod = create_model(main, out_file="mcx_example")


# Synthesize 3 different implementations of an MCX (multi-control-x) with 5 control qubits and 1 target qubit (you should use the control quantum operation for
# implementing an MCX, follow this tutorial). One implementation should be optimized for minimized depth, the other for minimized width, and the third
# somewhere in between (choose yourself what is the maximal width / depth you apply).

qmod_with_constrains = set_constraints(qmod, Constraints(optimization_parameter='depth'))
qprog = synthesize(qmod_with_constrains)
circuit_depth = QuantumProgram.from_qprog(qprog).transpiled_circuit.depth
circuit_width = QuantumProgram.from_qprog(qprog).data.width
print(f"The depth circuit width is {circuit_width} and the circuit_depth is {circuit_depth}")
show(qprog)

qmod_with_constrains = set_constraints(qmod, Constraints(optimization_parameter='width'))
qprog = synthesize(qmod_with_constrains)
circuit_depth = QuantumProgram.from_qprog(qprog).transpiled_circuit.depth
circuit_width = QuantumProgram.from_qprog(qprog).data.width
print(f"The width constrained circuit width is {circuit_width} and the circuit_depth is {circuit_depth}")
show(qprog)


qmod_with_constrains = set_constraints(qmod, Constraints(max_width=7, max_depth=116))
qprog = synthesize(qmod_with_constrains)
circuit_depth = QuantumProgram.from_qprog(qprog).transpiled_circuit.depth
circuit_width = QuantumProgram.from_qprog(qprog).data.width
print(f"The custom constrained circuit width is {circuit_width} and the circuit_depth is {circuit_depth}")
show(qprog)

