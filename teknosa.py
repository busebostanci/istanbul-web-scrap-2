from bs4 import BeautifulSoup
import requests

url = "https://www.teknosa.com/magaza-bul"
headers = {
cURL

}

response = requests.get(url, headers=headers)

print("Response Status Code:", response.status_code)
print("Response Content:", response.content)  

response = requests.get(url, headers=headers)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

# Find the relevant elements using the HTML structure and class names
store_elements = soup.find_all("div", class_="store-item")

for store_element in store_elements:
    display_name = store_element.find("h2", class_="store-name").text.strip()
    latitude = store_element.get("data-lat")
    longitude = store_element.get("data-lon")
    line1 = store_element.find("p", class_="store-address").text.strip()

    print("Display Name:", display_name)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Line1:", line1)
    print("-" * 50)
