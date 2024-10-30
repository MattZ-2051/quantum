# Quantum Country Notes

## Part 1 - The state of a qubit

- The state of a qubit is a vector in a two-dimensional vector space. This vector space is known as state space
- Example ket 0 := [[1
       0]]
- This special state (ket 0) is called a computational basis state
- Example ket 1 := [[0
          1]]
- Quantum states are represented by complex vector
- Quantum states as mathematical objects are 2D vectors in a complex vector space
- The sums of the squares of the amplitudes must be equal to 1 this is called the normalization constraint
- The quantum state of a qubit is a vector of unit length in a 2D complex vector space known as state space

## Part 2 - Introducing quantum logic gates

- A quantum logic gate is a way of manipulating quantum information, that is, the quantum state of a qubit or a collection of qubits
- Quantum wires are one of the hardest computations to implement because holding a quantum state is difficult as atoms and photons can be disturbed easily

### Hadamard Gate

- The Hadamard gate can expand the range of operations that our computer can perform

### Measuring a qubit

- The quantum state of any system is not directly observable, if you don't know alpha and beta (a(ket0) + b(ket1)) there is no way to figure them out if they start out unknown
- measurement in the computational basis is how we extract information from qubits

### General single-qubit states

- A general single-qubit gate works similarly. In particular, a general single-qubit gate can be represented as a 2×2 unitary matrix, U. (If you’re rusty, I’ll remind you what it means for a matrix to be unitary in a moment, and you can just think of it as a matrix for now.) If the input to the gate is the state
  ∣ψ⟩ then the output from the gate is U∣ψ⟩. And so the NOT and Hadamard gates correspond to the special cases where
  U=X and U=H, respectively.
- For flavor, let's give a few more examples of single-qubit quantum gates. Earlier in the essay, I mentioned that the NOT gate X was introduced by the physicist Wolfgang Pauli in the early days of quantum mechanics. He introduced two other matrices, Y and Z, which are also useful quantum gates. The three gates, X, Y, and X are known collectively as the Pauli matrices. The Y and Z gates will be useful extra tools in our toolkit of quantum gates; in terms of the earlier analogy they expand the repertoire of moves we have available to us. They're crucial, for example, in protocols such as quantum teleportation and quantum error correction.
- A single-qubit gate is represented as a 2 X 2 unitary matrix
