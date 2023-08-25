import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.espressolab.com"
headers = {
cURL 
}

data = []

try:
    response = requests.get(base_url + "/subeler/", headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    anchor_elements = soup.find_all("a", class_="link", href=lambda href: href.startswith("/subeler/"))
    href_values = [anchor_element.get("href") for anchor_element in anchor_elements]

    for href_value in href_values:
        response = requests.get(base_url + href_value, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        p_element = soup.select_one(".menu-detail-content.address p")

        if p_element and "İstanbul" in p_element.get_text():
            branch_title = None

            title_elements = soup.select(".taxanomy-list .link")
            for title_element in title_elements:
                if title_element.get("href") == href_value:
                    branch_title = title_element.get("title")
                    break

            data.append({
                "Title": branch_title,
                "Href": base_url + href_value,
                "Address": p_element.get_text()
            })

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Write DataFrame to an Excel file
excel_filename = "eslab.xlsx"
df.to_excel(excel_filename, index=False)

print("Data written to", excel_filename)
