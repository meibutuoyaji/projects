import bs4, requests


def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(  #isert the css selector url here
        '#corePrice_feature_div > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)'
    )
    return elems[0].text.strip()


price = getAmazonPrice(  #url of the product
    'https://www.amazon.co.jp/Kogawa-Chemical-Industries-22-040-Trigger/dp/B006B07RYU/ref=zg-bs_automotive_1/355-9379450-7444766?pd_rd_w=Lsaet&pf_rd_p=061993fb-1a08-486a-9bea-d772d463ba7a&pf_rd_r=JG846TJSJ18V4D0MTRMJ&pd_rd_r=5fe10230-5af7-4230-80b1-cedba375428b&pd_rd_wg=vZtcx&pd_rd_i=B07W5Y39QK&psc=1'
)
print('The price is' + price)
