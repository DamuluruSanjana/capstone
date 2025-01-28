# Text inconsistency detection model
# Function to Read and Process Dataset
def load_dataset(file_path):
    """
    Reads the dataset from a file and creates a dictionary mapping incorrect sentences to corrected ones.
    
    Args:
        file_path (str): Path to the dataset file.
    
    Returns:
        dict: A dictionary with incorrect sentences as keys and corrected sentences as values.
    """
    corrections = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line into incorrect and correct sentences
                parts = line.strip().split('|')
                if len(parts) == 2:
                    incorrect, correct = parts
                    corrections[incorrect.strip()] = correct.strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please ensure the file exists.")
    return corrections

# Function to Correct an Input Sentence
def correct_sentence(sentence, corrections):
    """
    Returns the corrected version of the input sentence if found in the dataset.
    
    Args:
        sentence (str): The input sentence to correct.
        corrections (dict): The dataset of corrections.
    
    Returns:
        str: The corrected sentence or a message if no correction is found.
    """
    return corrections.get(sentence, "No correction found for the given sentence.")

# Main Program
if __name__ == "__main__":
    # Specify the dataset file name
    dataset_file = "New data.txt"
    
    # Load corrections from the dataset
    corrections = load_dataset(dataset_file)
    
    # Check if the dataset was successfully loaded
    if not corrections:
        print("No corrections loaded. Exiting program.")
    else:
        print("Sentence Correction Tool")
        print("Type 'exit' to quit.")
        
        # Interactive loop to accept user input and provide corrections
        while True:
            user_input = input("\nEnter a sentence: ").strip()
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            # Get and display the corrected sentence
            result = correct_sentence(user_input, corrections)
            print(f"Corrected Sentence: {result}")
