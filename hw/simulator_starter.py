import random
import numpy as np
from collections import defaultdict

class QuantumSimulator:
    # n = number of qubits
    # m = number of classical bits
    def __init__(self, n, m):
        self.n = n 
        self.m = m
        self.cbits = [0] * m

    def h(self,q):
        # TODO
        pass

    def x(self,q):
        # TODO
        pass

    def t(self,q):
        # TODO
        pass

    def cx(self,qa, qb):
        # TODO
        pass

    def measure(self,qbit,cbit):
        # TODO
        pass

    def to_string(self):
        return "".join([str(c) for c in self.cbits])


# Creates a quantum circuit that can be simulated many times
class QuantumCircuit:
    def __init__(self, n, m):
        self.n = n 
        self.m = m
        self.circuit = []
    def x(self, q):
        self.circuit.append(('x',q))
    def t(self, q):
        self.circuit.append(('t',q))
    def h(self, q):
        self.circuit.append(('h',q))
    def cx(self, qa, qb):
        self.circuit.append(('cx',(qa,qb)))
    def measure(self, q, c):
        self.circuit.append(('measure',(q,q)))

    def run_circuit(self,shots=1000):
        results = defaultdict(int)
        for _ in range(1000):
            qs = QuantumSimulator(self.n, self.m)
            for (instruction, params) in self.circuit:
                if instruction == 'h':
                    qs.h(params)
                if instruction == 't':
                    qs.t(params)
                if instruction == 'x':
                    qs.x(params)
                if instruction == 'cx':
                    qs.cx(params[0], params[1])
                if instruction == 'measure':
                    qs.measure(params[0], params[1])
            results[qs.to_string()]+=1
        print(dict(results))


# test
results = defaultdict(int)
qc = QuantumCircuit(2,2)
qc.h(0)
qc.h(1)
qc.measure(0,0)
qc.measure(1,1)
qc.run_circuit()

qc = QuantumCircuit(1,1)
qc.h(0)
qc.t(0)
qc.h(0)
qc.measure(0,0)
qc.run_circuit()

qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure(0,0)
qc.measure(1,1)
qc.run_circuit()
