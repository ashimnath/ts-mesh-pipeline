import requests
from bs4 import BeautifulSoup
import pandas as pd

class NasaEarthDataScraper:
    def __init__(self):
        self.base_url = "https://www.earthdata.nasa.gov"

    def scrape_data(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, "html.parser")

        data = []  # Define the data variable as an empty list

        # Example: Extract dataset titles and descriptions
        datasets = soup.find_all("div", class_="dataset-card")
        for dataset in datasets:
            title = dataset.find("h3", class_="dataset-card__title").text.strip()
            description = dataset.find("p", class_="dataset-card__description").text.strip()

            data.append({
                "Title": title,
                "Description": description
            })

        df = pd.DataFrame(data)
        df.to_csv("nasa_data.csv", index=False)

        return data

if __name__ == "__main__":
    scraper = NasaEarthDataScraper()
    scraped_data = scraper.scrape_data()
    print("Data scraped successfully and saved to 'nasa_data.csv'.")
