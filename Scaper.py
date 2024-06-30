from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set up the Selenium WebDriver with the specific path to ChromeDriver
chrome_driver_path = r'C:\Users\prakh\Downloads\chromedriver-win64\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: run in headless mode to hide browser window
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Navigate to the Election Commission of India results page
driver.get("https://results.eci.gov.in/PcResultGenJune2024/index.htm")

# Wait for the results table to be present
wait = WebDriverWait(driver, 20)
results_table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.rslt-table table')))

# Extract data from the table rows
rows = results_table.find_elements(By.TAG_NAME, 'tr')
data = []
for row in rows[1:-1]:  # Exclude header and footer rows
    cols = row.find_elements(By.TAG_NAME, 'td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Close the browser
driver.quit()

# Create a DataFrame from the extracted data
columns = ["Party", "Won", "Leading", "Total"]
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('election_results_2024.csv', index=False)

print("Data scraped and saved to election_results_2024.csv")
