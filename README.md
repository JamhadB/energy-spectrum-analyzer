# Energy Spectrum Analyzer using a Binary Search Tree (BST)

## Overview
This project implements an Energy Spectrum Analyzer that stores photon energy measurements in an augmented Binary Search Tree (BST).  
The BST can perform insertion and fast range queries, enabling analysis of photon distributions from simulated or external datasets.

This README serves as the project’s documentation.

---

## Features
- Store photon energies in a BST  
- Track duplicate energies using a node counter  
- Maintain subtree counts for fast aggregated queries  
- Query how many photons fall within a user-specified energy range  
- Build the BST from simulated or hardcoded data  

---

## Project Structure

project/
|
├── node.py # Node class for the Binary Search Tree
├── bst.py # BST implementation with insert, traversal, and range query
|
├── main.py # Analyzer program that builds the tree and runs queries
└── README.md # Project documentation

---

## Data Structures Used

### **Binary Search Tree**
- Stores photon energies in sorted order  
- Supports recursive insertion and searching  
- Augmented with subtree counts  

### **Node**
- `energy`: photon value  
- `count`: number of duplicates  
- `subtree_count`: total values in subtree  
- `left` / `right` children  

### **Lists**
- Store raw energy data before BST construction  
- Used for test-case comparisons and validation  

### **Dictionaries**
- Used during testing to verify expected frequency counts  

---

## Algorithms

### **BST Insertion**
- Recursive  
- Places energies into the correct position  
- Updates `count` for duplicates  
- Recomputes `subtree_count` after each insertion  

### **Range Query**
Counts photon energies within the inclusive range `[low, high]` by:
- Ignoring subtrees that cannot contain valid energies  
- Recursively descending into only necessary branches  
- Summing counts of all nodes inside the range  

---

## Input Data

### **Simulated Data**
Photon energies may be generated mathematically (e.g., Gaussian distributions), allowing testing without external files.

### **External Files (Future Improvement)**
Potential support for:
- `.txt` files  
- `.csv` files  
(One energy value per line)

---

## How to Run

### **Basic Usage**
```bash
python main.py


