from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta
import os

#chang the dates to the range you would like to import
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 7, 31)
date_list = []

while start_date <= end_date:
    date_list.append(start_date.strftime('%Y-%m-%d'))
    start_date += timedelta(days=1)


url = "https://www.besoccer.com/livescore/"

def goto_site_download(url,dir,file_name):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()

        page.goto(url)

        for i in range(4):
            # Scroll to the bottom of the page using JavaScript
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for a moment to allow content to load (you can adjust the wait time)
            page.wait_for_timeout(2000)  # Adjust the timeout as needed

        # Get the HTML content of the pageexit

        html_content = page.content()

        # Save the HTML content to a file
        with open(os.path.join(dir, file_name), "w", encoding="utf-8") as file:
            file.write(html_content)

        browser.close()

print(len(date_list), " pages to scrape")
for i in range(len(date_list)):
    goto_site_download(url=url+date_list[i], dir="htmls", file_name="games_"+date_list[i]+".html")
    print(i+1, "scraped")