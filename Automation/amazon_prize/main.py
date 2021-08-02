import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = " "
my_password = " "
email_to_forward = " "
url = "https://www.amazon.in/Sharp-Purifier-FP-F40E-W-Filter-Cluster/dp/B01B0DT29A/?_encoding=UTF8&pd_rd_w=3og2h&pf_rd_p=a09353d8-6ac0-418e-ab17-914dd8724bc4&pf_rd_r=5YDH5BRYJGG77XCW157K&pd_rd_r=f4d55e40-ebf2-44e5-a8c9-ca8a71884538&pd_rd_wg=CkDTk&ref_=pd_gw_ci_mcx_mr_hp_d"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,gu;q=0.8,hi;q=0.7"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("₹\xa0")[1]
price_without_currency=price_without_currency.replace(',','')
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float<=9000:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=email_to_forward,
                            msg=f"the price of the given product is under your budget.https://www.amazon.in/Sharp-Purifier-FP-F40E-W-Filter-Cluster/dp/B01B0DT29A/?_encoding=UTF8&pd_rd_w=3og2h&pf_rd_p=a09353d8-6ac0-418e-ab17-914dd8724bc4&pf_rd_r=5YDH5BRYJGG77XCW157K&pd_rd_r=f4d55e40-ebf2-44e5-a8c9-ca8a71884538&pd_rd_wg=CkDTk&ref_=pd_gw_ci_mcx_mr_hp_d")
