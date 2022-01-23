#Web Scrapper Tool

### *The PostRequest.py helps to post a request at https://parivahan.gov.in/rcdlstatus/?pur_cd=101 with given DL Number and DOB. Run it using python idle.

### *But it also needs a captcha, so for now, it only brings all the contents of the Parivahan website after a post request.

### *The CommandLineUtility.py does the same post request thing using command line. This runs on command line using:

### *python .\CommandLineUtility.py --dl_No DL-0420110149646 --dob 09-02-1976 --find res

### *The ScrapperUsingXpath.py scraps the contents of the website using xpath and lxml. Just run the file independently to scrap the details according to the given xml.

