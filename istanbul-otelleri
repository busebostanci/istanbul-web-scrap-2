import requests
import pandas as pd

def fetch_all_accommodations():
    base_url = "https://gateway.neredekal.com/v3/query/catalog"
    page = 1
    limit = 250
    total_records = 3878
    all_data = []

    while (page - 1) * limit < total_records:
        url = f"{base_url}?campaign=0&drty=false&dvc=Desktop&fls=%7B%22plim%22%3A{limit}%2C%22poff%22%3A{page}%2C%22flsp%22%3A%5B%7B%22flsg%22%3A%22location%22%2C%22fid%22%3A4%2C%22v%22%3A%2241%22%7D%5D%7D&poolData=eyJSZXF1ZXN0SWQiOiJiY2IyZGE2OTM1ODY2M2JiZjc1OTBmMGEzYWIzZTJkNjRmYjM3NjNmIiwiSGFzTmVhckJ5IjpmYWxzZSwiU3RhcnREYXRlIjoiMjAyMy0wOC0xMVQwMDoxNjoxOS4xODQ0MjQyMjYrMDM6MDAi&queryParams=%7B%22cin%22%3A%222023-09-28%22%2C%22cout%22%3A%222023-09-29%22%2C%22act%22%3A2%2C%22cas%22%3A%5B%5D%7D&slforg=41.0123%2C28.9761%2C20&slg=istanbul-otelleri&src=Unpaid&srcloc=41&srt=recommended_Default&stid=1&typ=Facility&issb=true&irb=true&irnb=true&owb=false"

        payload = {}
        headers = {
            'authority': 'gateway.neredekal.com',
            # ... (other headers)
        }

        response = requests.get(url, headers=headers, data=payload)
        data = response.json()

        # Extract and process data from each catalog entry
        for catalog in data.get("catalogs", []):
            category_name = catalog.get("category", {}).get("name")
            catalog_data = {
                "name": catalog.get("name"),
                "address": catalog.get("locationTree"),
                "latitude": catalog.get("latitude"),
                "longitude": catalog.get("longitude"),
                "type": category_name,
            }
            all_data.append(catalog_data)
            # Burada catalog_data'yı istediğiniz şekilde kullanabilirsiniz

        page += 1

    return all_data

all_accommodations = fetch_all_accommodations()

df = pd.DataFrame(all_accommodations)

excel_file_path = "accommodations_data2.xlsx"

df.to_excel(excel_file_path, index=False)

print("Total accommodations fetched:", len(all_accommodations))
print("Data exported to", excel_file_path)
