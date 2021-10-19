# COMP2020

## Table of contents
- [COMP2020](#comp2020)
  - [Table of contents](#table-of-contents)
  - [General info](#general-info)
  - [Design Implementation](#design-implementation)
  - [Critical Path](#critical-path)
  - [Gate Count](#gate-count)

## General info
Name: Vu Hong Phuc\
Email: 20phuc.vh@vinuni.edu.vn

## Design Implementation
ALU.circ contains LeftShift32, Add32, ALU32 circuits. Also there are subcircuits for carry-lookahead adder with ALU32_CLA.

## Critical Path
Total: 66 units of gate delay\
The critical path starts from input Op (opcode) through AddSub32 subcircuit to ouput V (overflow).
	
## Gate Count
Total: 1297 gates
* AddSub: 226
* Compare: 104
* LogicGate: 291
* Shift: 676
