# Commutative Semiring Project

## Overview

This project implements various operations and extensions on commutative semirings, including verifying their properties and applying them to Maximum Independent Set (MIS) problems on graphs. The project includes classes and methods to define semiring operations, extend semirings, and calculate MIS using these extended semirings.

## Structure

The project is structured as follows:

- **CommutativeSemiring.py**: Defines the `CommutativeSemiring` class, which implements the basic operations and properties of a commutative semiring.
- **SemiringOperations.py**: Contains static methods defining various semiring operations like max, addition, multiplication, union, and combination.
- **SelectiveSemiringExtension.py**: Implements the `SelectiveSemiringExtension` class, which extends a base semiring with counting and sampling functionalities.
- **MISQuery.py**: Defines the `MISQuery` class, which uses the semiring extension to calculate the Maximum Independent Set (MIS) of a graph.
- **TestCommutativeSemiring.py**: Contains the `ConfirmCommutativeSemiring` class for testing and verifying the properties of commutative semirings.
- **main.py**: The main script that sets up the graph, initializes the semirings, and runs the MIS calculation.

## Installation

To run this project, ensure you have Python installed along with the necessary libraries:

```sh
pip install networkx matplotlib
``

## Usage

1. **Define Semiring Operations**: In `SemiringOperations.py`, various static methods are defined to perform operations like max, add, multiply, etc.

2. **Initialize Semirings**:
    - Create instances of `CommutativeSemiring` with specific operations, zero, and one elements.
    - Extend the base semiring using `SelectiveSemiringExtension` to include counting and sampling extensions.

3. **Generate Graphs**:
    - Use the `generate_edge_case_graphs` function in `main.py` to create a variety of test graphs.

4. **Calculate MIS**:
    - Instantiate `MISQuery` with a graph and semiring extension.
    - Call `calculate_mis` to compute the Maximum Independent Set using the semiring extension.

5. **Run the Main Script**:
    - Execute `main.py` to see the results of the MIS calculation on different graphs.

```sh
python main.py

