import requests
import argparse
import sys
from bs4 import BeautifulSoup
def post_dl(dl_No, dob):
    headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36'}
    dl_details_data={
            'form_rcdl':'form_rcdl',
            'form_rcdl:tf_dlNO': dl_No,
            'form_rcdl:tf_dob_input':dob,
            'form_rcdl:j_idt29:CaptchaID':''
            }
    with requests.Session() as Site:
            url='https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
            resp=Site.get(url, headers=headers)
            soup=BeautifulSoup(resp.content, 'html5lib')
            dl_details_data['form_rcdl:tf_dlNO']=soup.find('input', attrs={'name':"form_rcdl:tf_dlNO"})
            dl_details_data['form_rcdl:tf_dob_input'] = soup.find('input', attrs={'name': 'form_rcdl:tf_dob_input'})
            dl_details_data['form_rcdl:j_idt29:CaptchaID'] = soup.find('input', attrs={'name': 'form_rcdl:j_idt29:CaptchaID'})
            resp=Site.post(url,data=dl_details_data,headers=headers)
            print(resp.content)


def post(args):
    if args.find=='res':
        return post_dl(args.dl_No, args.dob)
    else:
        return 'Something went wrong'


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--dl_No', type=str, default="DL-0420110149646")
    parser.add_argument('--dob', type=str, default='09-02-1976')
    parser.add_argument('--find', type=str, default="f")
    args=parser.parse_args()
    sys.stdout.write(str(post(args)))


# python .\CommandLineUtility.py --dl_No DL-0420110149646 --dob 09-02-1976 --find res
# to test use this on command line


    
    
