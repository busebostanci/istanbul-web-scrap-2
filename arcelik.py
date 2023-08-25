import requests
from bs4 import BeautifulSoup
import pandas as pd


# First Code Snippet
def extract_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    data = []

    srv_items = soup.find_all("div", class_="srv-item")
    for srv_item in srv_items:
        data_coor = srv_item["data-coor"]
        srv_name = srv_item.find("div", class_="srv-name").text.strip()
        srv_address = srv_item.find("div", class_="srv-address").text.strip()

        data.append({
            "data-coor": data_coor,
            "srv-name": srv_name,
            "srv-address": srv_address
        })

    return data


# Second Code Snippet
def get_names_from_url(url):
    headers = {
        cURL
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        names = [item.get("name") for item in data]
        return names
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return []


# Main Code
base_url = "https://www.arcelik.com.tr/istanbul-{}_arcelik-bayileri"
second_code_url = "https://www.arcelik.com.tr/my-addresses/add/new/filter-towns?cityId=34"

names = get_names_from_url(second_code_url)

all_data = []

for name in names:
    formatted_name = name.lower().replace(" ", "-")
    url = base_url.format(formatted_name)

    extracted_data = extract_data(url)

    for item in extracted_data:
        all_data.append(item)

df = pd.DataFrame(all_data)

# Export to Excel
excel_filename = "arcelik.xlsx"
df.to_excel(excel_filename, index=False)
print(f"Data exported to {excel_filename}")
