import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

d = {}
df = pd.DataFrame(data=d)
browser = webdriver.Chrome()
# Web sayfasını açma
url = "https://enyakinptt.ptt.gov.tr/Enyakinptt/?city=34&type=posta"
browser.get(url)

browser.implicitly_wait(10)

page_source = browser.page_source

soup = BeautifulSoup(browser.page_source, features="lxml")
# PTTSayisi = int(len(browser.find_element("xpath",'//*[@id="PTTIsYeriSonuc"]').text.split("\n")))
# print(PTTSayisi)

PTTTYPE = []
PTTAD = []
PTTLAT = []
PTTLONG = []


for j in range(0,3):
    browser.find_element("xpath",f'//*[@id="MainContent_ASPxSplitterPageContent_LeftMenu_pageControl_navBar_GCTC0_cmbPTTTur_0_RB{j}_I_D"]').click()
    PTTCounts = int(len(browser.find_element("xpath", '//*[@id="PTTIsYeriSonuc"]').text.split("\n")))
    print("Şube Count:",PTTCounts)
    print("-" * 50)

    for i in range(0,PTTCounts):
        # browser.find_element("xpath", f'//*[@id="MainContent_ASPxSplitterPageContent_LeftMenu_pageControl_navBar_GCTC0_cmbPTTTur_0_RB{j}_I_D"]').click()
        browser.find_element("xpath",f'//*[@id="PTTIsYeriSonuc"]')
        soup = BeautifulSoup(browser.page_source, features="lxml")
        # Şube adını almak için
        branch_type = browser.find_element("xpath", f'//*[@id="MainContent_ASPxSplitterPageContent_LeftMenu_pageControl_navBar_GCTC0_cmbPTTTur_0_RB{j}"]/tbody/tr/td[2]/label').text
        branch_name = browser.find_element("xpath",f'//*[@id="SelectedCompany{i}"]').text
        branch_lon = soup.find_all("div", attrs={"id": f"SelectedCompany{i}"})[0].attrs["onclick"][23:].split(",")[0]
        branch_lat = soup.find_all("div", attrs={"id": f"SelectedCompany{i}"})[0].attrs["onclick"][23:].split(",")[1]

        # soup.find_all("div", attrs={"id": ["SelectedCompany0"]}).attrs["onclick"]
        print("Şube Type:", branch_type)
        print("Şube Adı:", branch_name)
        print("Şube Long:", branch_lon)
        print("Şube Lat:", branch_lat)

        PTTTYPE.append(branch_type)
        PTTAD.append(branch_name)
        PTTLAT.append(branch_lat)
        PTTLONG.append(branch_lon)

df = pd.DataFrame({'POI_TYPE': PTTTYPE,'POI_ADI': PTTAD, 'LAT': PTTLAT, 'LONG': PTTLONG})

df.to_excel(r"*", index=False)

browser.quit()
