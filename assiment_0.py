import random
import matplotlib.pyplot as plt

# Function to read data from a text file and return its contents
# file_path_1 = "E:/New_project/input.txt"
def read_from_file(file_path):
    with open(file_path, 'r') as file:
        data_to_read = file.read()
    return data_to_read

# Function to write data to a text file
# file_path_2 = "E:/New_project/output.txt"
# data_to_write = "This is some text data that will be written to the file."
def write_to_file(file_path, data_to_write):
    with open(file_path, 'w') as file:
        file.write(data_to_write)

# Function to generate random sequences of numbers
# length = 10
# min_value = 1
# max_value =100
def generate_random_sequence(length, min_value, max_value):
    #This line is a list comprehension that generates a list of random integers-->
    return [random.randint(min_value, max_value) for num in range(length)]

# Function to generate and plot a graph
def generate_and_plot_graph(x_values, y_values, x_label, y_label, title):
    plt.plot(x_values, y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    
    
"""This is part of the code   is known as the "main" block in Python. 
It's a common convention in Python scripts to place code that should only run 
when the script is executed directly 
(as opposed to when it's imported as a module in another script)
within an if __name__ == "__main__": block."""

if __name__ == "__main__":
    file_path_1 = "E:/first_semster/assignment_0/input.txt"
    file_path_2 = "E:/first_semster/assignment_0/output.txt"
    data_to_write = "This is some text data that will be written to the file."


    # Example: Read the data form a text file
    data_to_read = read_from_file(file_path_1)
    print(data_to_read)

    # Example: Writing data to a text file
    write_to_file(file_path_2, data_to_write)

    # Example: Generating a random sequence of numbers
    random_sequence = generate_random_sequence(10, 1, 100)
    print("Random Sequence:", random_sequence)

    # Example: Generating and plotting a graph
    x_values = [1, 2, 3, 4, 5]
    y_values = [10, 15, 7, 12, 5]
    generate_and_plot_graph(x_values, y_values, "X-axis Label", "Y-axis Label", "Sample Graph")
