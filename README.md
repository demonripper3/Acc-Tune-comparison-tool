# Acc Tune Comparison Tool

## Overview
The Acc Tune Comparison Tool is a Python-based utility designed to compare two JSON files used for tuning configurations in automotive setups, simulations, or similar applications. It provides a user-friendly way to identify differences in tuning parameters, including a specific focus on detecting significant discrepancies that might indicate "cheating" or unintended alterations.

## Features
- **File Selection**: Interactive file selection using a GUI dialog.
- **Key Exclusion**: Ignores specified keys (`staticCamber`, `toeOutLinear`, `fuelPerLap`, `rodLength`, `strategy`) in the comparison to focus on relevant data.
- **Tick Calculation**: Calculates the differences in values in terms of "ticks," a unit of change.
- **Cheat Warning**: Issues a warning if differences exceed a specified threshold (20 ticks), indicating significant alteration.

## Installation

### Prerequisites
- Python 3.x
- `deepdiff` Python package

### Steps
1. **Install Python**:
   - Download and install Python from [python.org](https://www.python.org/downloads/). Ensure you add Python to your system's PATH during installation.

2. **Install deepdiff**:
   - Open your command prompt or terminal.
   - Run the command `pip install deepdiff` to install the required Python package.

3. **Download the Script**:
   - Clone the repository or download the `compare_json.py` script from the GitHub repository.

4. **Running the Script**:
   - Double-click on `compare_json.py` if Python is your default script handler. Otherwise, run it from the command line using `python path_to_compare_json.py`.

## Usage

1. **Launch the Tool**:
   - Run the script. Two file dialog windows will appear sequentially.

2. **Select JSON Files**:
   - In each dialog, navigate to and select the JSON files you wish to compare.

3. **Review the Results**:
   - The script will output the differences in the console, including any "cheat warnings" if significant discrepancies are found.

4. **Exiting the Tool**:
   - Press Enter in the console to exit the tool after reviewing the comparison results.

## Contributing
Contributions to the Acc Tune Comparison Tool are welcome. Please feel free to fork the repository, make changes, and submit pull requests.
