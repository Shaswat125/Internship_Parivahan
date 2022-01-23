from lxml import html
import requests
def scrap(url):
    resp=requests.get(url)
    tree=html.fromstring(resp.content)
    elements=tree.xpath('//*[@id="form_rcdl:j_idt41"]/div/div[*]/span')
    print(elements[0].text)


if __name__ == '__main__':
    url="https://parivahan.gov.in/rcdlstatus/?pur_cd=101"
    scrap(url)
    
