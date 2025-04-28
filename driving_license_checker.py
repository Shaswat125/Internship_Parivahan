import requests
from bs4 import BeautifulSoup
import logging
import re

# Set up logging for better debugging and monitoring
logging.basicConfig(level=logging.INFO)

class LicenseStatusChecker:
    def __init__(self, dl_No, dob):
        """
        Initialize the checker with the driver's license number and date of birth.
        """
        self.dl_No = dl_No
        self.dob = dob
        self.url = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36'
        }

    def fetch_form_data(self):
        """
        Fetches the form data from the Parivahan website to get the necessary hidden fields.
        """
        try:
            with requests.Session() as session:
                response = session.get(self.url, headers=self.headers)
                response.raise_for_status()  # Make sure the request was successful
                soup = BeautifulSoup(response.content, 'html5lib')

                # Extract necessary hidden fields from the page
                form_data = {
                    'form_rcdl:tf_dlNO': soup.find('input', attrs={'name': "form_rcdl:tf_dlNO"}).get('value', ''),
                    'form_rcdl:tf_dob_input': soup.find('input', attrs={'name': 'form_rcdl:tf_dob_input'}).get('value', '')
                }
                return form_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching form data: {e}")
            return None

    def submit_form(self, form_data):
        """
        Submits the form with the provided data and returns the result.
        """
        try:
            with requests.Session() as session:
                response = session.post(self.url, data=form_data, headers=self.headers)
                response.raise_for_status()  # Ensure the request was successful
                return response.content
        except requests.exceptions.RequestException as e:
            logging.error(f"Error submitting the form: {e}")
            return None

    def check_license_status(self):
        """
        Fetches the form data, submits the form to check the license status, and returns the result.
        """
        # Fetch the hidden form data from the page
        form_data = self.fetch_form_data()
        if form_data is None:
            return "Error fetching form data from the website."

        # Update the form data with the user's DL number and DOB
        form_data['form_rcdl:tf_dlNO'] = self.dl_No
        form_data['form_rcdl:tf_dob_input'] = self.dob

        # Submit the form and return the result
        result = self.submit_form(form_data)
        if result is None:
            return "Error submitting the form."
        
        # Return the response content (the status page)
        return result


# Example usage
if __name__ == '__main__':
    dl_No = 'DL-0420110149646' 
    dob = '09-02-1976'  

    checker = LicenseStatusChecker(dl_No=dl_No, dob=dob)

    result = checker.check_license_status()

    print(result)
