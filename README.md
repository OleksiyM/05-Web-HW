 
# Exchange Rate Data Retriever

**This Python project asynchronously fetches exchange rate data from PrivatBank's API and stores it in a JSON file for further analysis.**

## Features

- Retrieves exchange rates for USD and EUR currencies for specified days.
- Uses asynchronous programming for efficient API calls and data processing.
- Handles errors gracefully and provides informative logging.
- Saves the retrieved data in a well-formatted JSON file.
- Includes validation for user input and configuration.

## Installation

1. Clone this repository:
   
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script, optionally specifying the number of days to retrieve data for:
   ```bash
   python main.py [days] [all]
   ```
   - If no `days` argument is provided, it defaults to retrieving data for the current day.
   - The maximum allowed value for `days` is 10.
   - If `all` argument is provided, extended currencies list is used for output: `('EUR', 'USD', 'CHF', 'CZK',  'GBP', 'PLN')`.
   - if `all` argument is not provided, it defaults to retrieving data for the base currencies list: `('EUR', 'USD')`

2. The retrieved exchange rate data will be saved in the `storage/data.txt` file.

## Project Structure

- **main.py:** Contains the main execution logic, including asynchronous data retrieval and storage.
- **utils.py:** Houses utility functions for input validation, directory creation, and data saving.
- **DateHandler.py:** Defines a class for generating lists of dates for data retrieval.
- **Constants.py:** This file contains configuration constants for the project.


## Contributing

We welcome contributions! Please follow these steps:

1. Fork this repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to merge your changes into the main repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
