# WiFi Strength Meter

This Python script allows you to measure the strength of your WiFi signal and display it in real-time with an animated progress bar. The goal is to help locate the position of the router based on the WiFi signal strength in your environment.

## Features

- Measures the WiFi signal strength in percentage.
- Displays the signal in an animated progress bar.
- Uses colors to indicate the signal strength:
  - **Red**: Weak signal (less than 25%).
  - **Orange**: Moderate signal (25% - 50%).
  - **Yellow**: Good signal (50% - 75%).
  - **Green**: Excellent signal (more than 75%).

## Requirements

The script is compatible with Windows and Linux operating systems. For Linux, you need to have `nmcli` installed (a network management tool).

## Installation

1. Clone this repository or download the source code.

2. Create a virtual environment for the project:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On Linux/Mac:
      ```bash
      source venv/bin/activate
      ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the script, simply execute the following command:

```bash
python wifi_strength_meter.py
```