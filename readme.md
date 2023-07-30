# WhatsApp Bulk Message Sender

This is a Python script to send bulk messages to multiple WhatsApp contacts using Selenium and Chrome WebDriver.

**Warning: Use at Your Own Risk**
Sending bulk messages using automation tools may violate WhatsApp's terms of service, and it can potentially lead to your WhatsApp account being blocked. Use this script responsibly and at your own risk.

## Prerequisites

Before running the script, make sure you have the following:

1. Python (version X.X.X) installed on your system.
2. Google Chrome installed.
3. Chromedriver that matches your Chrome version. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Installation

1. Clone this repository or download the script directly.
2. Install the required Python packages like Pandas, Selenium and Openpyxl.
3. Place the `contacts.xlsx` file in the same directory as the script. The Excel file should contain a column named 'PhoneNumber' with the list of contacts' phone numbers.

## Usage

1. Open WhatsApp Web in your browser by visiting: https://web.whatsapp.com
2. Run the Python script:
3. Scan the QR code with your WhatsApp app to log in to WhatsApp Web.
4. The script will pause and prompt you to press `Enter` once you have scanned the QR code.
5. The script will start sending messages to the contacts one by one.

**Important Note:** Uncommenting the line `# + message + "&app_absent=1"` in the script could enable you to add a default message. However, keep in mind that sending unsolicited messages may lead to account suspension or other penalties from WhatsApp.


## Disclaimer

The authors of this script are not responsible for any misuse or damages caused by this script. Use it responsibly and at your own risk.

