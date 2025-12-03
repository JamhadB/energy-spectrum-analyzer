from bst import BST
import numpy as np
import matplotlib.pyplot as plt

def load_df(filename):
    """
    load dataset of energies from .csv or .txt file
    assumes one energy val / line, or a single column
    returns list of floats.
    """
    data = np.loadtxt(filename, delimiter=',')
    return data.tolist()

def gen_sim_data(n=1000, mu=30.0, sigma=5.0):
    """
    simulated photon-energy dataset using a Gaussian distribution
    E ~ N(mu, sigma), in keV
    returns list of floats
    """
    data = np.random.normal(loc=mu, scale=sigma, size=n)
    return list(data)

def build_tree(energies):
    """
    builds BST from list of energy vals
    returns constructed BST
    """
    tree = BST()
    for energy in energies:
        tree.insert(energy)
    return tree


def print_inorder(tree):
    """
    prints inorder traversal in a readable way
    showing energy values in ascending order with counts.
    """
    inorder_list = tree.inorder()

    print("\nInorder Traversal (energy, count):")
    for energy, count in inorder_list:
        print(f"  {energy} keV -> {count} hits")


def run_range_query(tree):
    """
    ask for energy range and
    perform range query
    """
    print("\nRange Query")
    low = float(input("Enter lower energy bound: "))
    high = float(input("Enter upper energy bound: "))

    result = tree.range_query(low, high)
    print(f"Photons in [{low}, {high}] keV: {result}")

def visualize_spectrum(energies):
    """
    viz spectrum
    """
    plt.figure(figsize=(10, 4))

    # histogram from raw energies
    plt.hist(energies, bins=20)
    plt.xlabel("Energy (keV)")
    plt.ylabel("Counts")
    plt.title("Histogram from raw list")
    plt.tight_layout()
    plt.show()

def main():
    print("Energy Spectrum Analyzer")
    print("(1) Use hardcoded sample list")
    print("(2) Load energies from file (.csv/.txt)")
    print("(3) Generate simulated Gaussian dataset")
    choice = input("Select an option (1/2/3): ")

    if choice == "2":
        filename = input("Enter dataset filename: ")
        energies = load_df(filename)
        print(f"Loaded {len(energies)} energies from {filename}")
    elif choice == "3":
        n = int(input("How many simulated events? "))
        energies = gen_sim_data(n=n, mu=30.0, sigma=5.0)
        print(f"Generated {len(energies)} simulated photon energies.")
    else:
        energies = [30, 10, 50, 20, 10, 50, 50, 35, 27]
        print("Using hardcoded sample dataset:", energies)

    print("\nBuilding Binary Search Tree...")
    tree = build_tree(energies)

    print_inorder(tree)
    run_range_query(tree)

    # show plot
    visualize_spectrum(energies)


if __name__ == "__main__":
    main()

