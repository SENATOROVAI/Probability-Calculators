# Probability Calculator

This Python project calculates the probability of an event occurrence for different scenarios such as coin flipping and dice rolling. It includes modules for defining events, computing probabilities, and testing the functionality.

## Files

### 1. events.py

This file contains functions for calculating the probability of events in specific scenarios:

- `two_coins(a, b)`: Computes the probability of a specific outcome (heads or tails) occurring b times in a row for two coin flips.
- `two_dice(a, b)`: Computes the probability of a specific number occurring b times in a row for two dice rolls.

### 2. main.py

This file handles user input and initiates the project execution:

- `get_value()`: Prompts the user to select the type of event (coin or dice) and the specific outcome.
- Main logic for starting the project and calling relevant functions.

### 3. probability.py

This module defines functions for calculating probabilities based on user input:

- `calculator_probability()`: Computes the probability of an event occurrence based on the selected event type and outcome.

### 4. test_project.py

This file contains unit tests to verify the functionality of the `calculator_probability()` function:

- `test_coin()`: Tests the probability calculation for a coin flip scenario.
- `test_dice()`: Tests the probability calculation for a dice roll scenario.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the `test_project.py` file to execute the unit tests and verify the functionality.
4. Explore the other files to understand the project structure and functionality.
5. Modify or extend the code as needed for your own purposes.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [SENATOROVAI ) file for details{https://github.com/SENATOROVAI}.
