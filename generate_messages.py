import pandas as pd
import sys

def generate_message(name, interest_level):
    valid_levels = {
        'Sign me up': "Hi {name}, Yay! I am glad to hear that you are interested in our bootcamp. Can't wait to get you started...",
        'Unlikely': "Hi {name}, we are sorry to hear that you are not interested in our bootcamp. Would you be keen to checkout other bootcamps that maybe better suited for you?",
        'Unsure': "Hi {name}, we see that you are unsure about our bootcamp. Please let us know if there's anything we can do to make up your mind."
    }
    if interest_level in valid_levels:
        return valid_levels[interest_level].format(name=name)
    else:
        raise ValueError(f"{interest_level} is an Invalid interest level")

def format_phone_number(number):
    number = str(number).strip().replace(" ", "").replace("-", "")
    if number.startswith('91'):
        number = '+' + number
    elif number.startswith('04'):
        number = '+614' + number[2:]
    elif number.startswith('4'):
        number = '+61' + number
    return number

# Determine the Excel file path
default_folder = 'C:\\Users\\callum.bir\\Downloads\\'
default_filename = 'Python Workshop form (Responses).xlsx'
default_excel_path = default_folder + default_filename

# Command line argument handling
if len(sys.argv) > 1:
    excel_path = sys.argv[1]  # Use the command line provided path
else:
    excel_path = default_excel_path  # Use the default path

try:
    # Adding dtype specification for the Mobile column
    df = pd.read_excel(excel_path, dtype={'Mobile': str})
    for index, row in df.iterrows():
        # Extract and check essential fields
        full_name = row.get('Full Name')
        phone = row.get('Mobile')
        interest_level = row.get('How likely are you to do the 4 weeks bootcamp?')

        if pd.notna(full_name) and pd.notna(phone) and pd.notna(interest_level):
            formatted_phone = format_phone_number(phone)
            message = generate_message(full_name, interest_level)
            # Uncomment the next line when the WhatsApp API integration is ready
            # send_whatsapp_message(formatted_phone, message)
            print(message)
        else:
            print(f"Skipping row {index + 1} due to missing information.")
except FileNotFoundError:
    print(f"Error: The file does not exist at the specified path: {excel_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
