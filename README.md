# License Status Checker

## Overview
The **License Status Checker** is a Python script that allows users to check the status of their driver's license using the official Indian government website (Parivahan). The script scrapes the necessary data from the website, handles CAPTCHA solving, and submits the form with user details to retrieve the status of the driver's license.

## Features
- Fetches the necessary hidden form fields from the Parivahan website.
- Downloads the CAPTCHA image and allows the user to manually solve it.
- Submits the form with the driver's license number and date of birth.
- Displays the results of the license status check.

## Requirements
Before running the script, ensure that you have the following Python libraries installed:

- `requests` - For making HTTP requests.
- `BeautifulSoup` - For parsing and extracting data from HTML.
- `logging` - For logging and debugging.
- `PIL` (Pillow) - For handling and displaying CAPTCHA images.

You can install the required libraries using `pip`:

```bash
pip install requests beautifulsoup4 Pillow
