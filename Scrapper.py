from lxml import html
import requests
def scrapper():
    url="https://parivahan.gov.in/rcdlstatus/?pur_cd=101"
    resp=requests.get(url)
    tree=html.fromstring(resp.content)
    elements=tree.xpath('//*[@id="form_rcdl:j_idt16"]')
    print(elements[0].text)
scrapper()
