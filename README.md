# WhatsApp Messaging Automation for Bootcamp Interest

## Description

This Python script automates the process of sending personalized WhatsApp messages to individuals based on their expressed interest in attending a 4-week bootcamp. It reads contact details and interest levels from an Excel spreadsheet, formats the contact information, generates custom messages based on the interest level, and sends these messages via WhatsApp.

## Features

- **Excel Integration**: Automatically reads and processes data from an Excel file.
- **Custom Message Generation**: Dynamically creates personalized messages based on user interest.
- **WhatsApp Integration**: Uses the `pywhatkit` library to send messages directly to specified phone numbers.

## Prerequisites

Before running the script, ensure you have Python installed on your system. Python 3.6 or higher is recommended. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

To install the required packages, use the following command:

```bash
pip install -r requirements.txt
```

## Usage
Prepare the Excel File: Ensure your Excel file is formatted correctly with columns for Full Name, Mobile, and How likely are you to do the 4 weeks bootcamp?.

Edit Script Settings (if necessary): Modify the excel_path in the script to point to your Excel file's location.

Run the Script: Execute the script from the command line or your preferred Python IDE.
To run the script from the command line, navigate to the script's directory and run:

```bash
python script_name.py
```
You can also specify an alternative path for the Excel file directly in the command line:

```bash
python script_name.py "path/to/your/excel/file.xlsx"
```

## Note
Ensure WhatsApp is installed on the same device where the script is running, as pywhatkit uses the web version of WhatsApp to send messages. Also, make sure you have sufficient permissions to send messages and comply with all privacy regulatory requirements in Australia and wherever you are located.
