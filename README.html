# 2024 Lok Sabha Election Results - Web Scraping Project 🗳️

## Project Overview 📊

Welcome to our GitHub repository for the 2024 Lok Sabha Election Results web scraping project. Here, we analyze and visualize the election data using Python and Selenium.

## Exploratory Data Analysis (EDA) 📈

We have performed exploratory data analysis on the scraped data, exploring various insights and trends in the election results:
- 📊 Visualizations and graphs showcase the distribution of seats among different parties.
- 🔍 Insights into regional party performance and coalition dynamics.

## Project Structure 📁

The repository includes:
- 📂 **Data Sets:** Raw and processed election results data.
- 💻 **Scripts:** Python scripts for web scraping, data preprocessing, and analysis.
- 📝 **EDA:** Jupyter Notebooks or Python scripts for exploratory data analysis.
- 📈 **Graphs and Visualizations:** Charts and graphs depicting election trends.

## Code Example 💻

Here's an example of the code used for web scraping the election results:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set up the Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://results.eci.gov.in/PcResultGenJune2024/index.htm")

# Wait for the page to load and the table to be present
wait = WebDriverWait(driver, 20)
results_table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.rslt-table table')))

# Extract rows from the table
rows = results_table.find_elements(By.TAG_NAME, 'tr')

# Extract data from rows
data = []
for row in rows[1:-1]:  # Skip header and footer rows
    cols = row.find_elements(By.TAG_NAME, 'td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Close the browser
driver.quit()

# Create a DataFrame
columns = ["Party", "Won", "Leading", "Total"]
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('lok_sabha_election_results_2024.csv', index=False)

print("Data scraped and saved to lok_sabha_election_results_2024.csv")
