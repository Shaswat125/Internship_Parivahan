Web Scrapper Tool
The ScrapperUsingXpath.py scraps the contents of the website using xpath and lxml. 
The PostRequest.py helps to post a request at https://parivahan.gov.in/rcdlstatus/?pur_cd=101 with given DL Number and DOB. 
But it also needs a captcha, so for now, it only brings all the contents of the Parivahan website after a post request.
The CommandLineUtility.py does the same post request thing using command line. 
The command is: python .\CommandLineUtility.py --dl_No DL-0420110149646 --dob 09-02-1976 --find res
For the CommandLineUtilty.py to run on the command line.  
