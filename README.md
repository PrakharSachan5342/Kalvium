<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2024 Lok Sabha Election Results - Web Scraping Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: auto;
        }
        .section {
            margin-bottom: 30px;
        }
        .code {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
        }
        .emoji {
            font-size: 1.2em;
            margin-right: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>2024 Lok Sabha Election Results - Web Scraping Project 🗳️</h1>
            <p>Welcome to our GitHub repository for the 2024 Lok Sabha Election Results web scraping project. Here, we analyze and visualize the election data using Python and Selenium.</p>
        </header>

        <section class="section">
            <h2>Project Overview 📊</h2>
            <p>This project aims to scrape election results data from the Election Commission of India's website using Selenium WebDriver in Python. The scraped data includes party-wise results such as seats won, seats leading, and total seats contested.</p>
        </section>

        <section class="section">
            <h2>Exploratory Data Analysis (EDA) 📈</h2>
            <p>We have performed exploratory data analysis on the scraped data, exploring various insights and trends in the election results.</p>
            <ul>
                <li>Visualizations and graphs showcase the distribution of seats among different parties.</li>
                <li>Insights into regional party performance and coalition dynamics.</li>
            </ul>
        </section>

        <section class="section">
            <h2>Project Structure 📁</h2>
            <p>The repository includes:</p>
            <ul>
                <li><strong>Data Sets:</strong> Raw and processed election results data.</li>
                <li><strong>Scripts:</strong> Python scripts for web scraping, data preprocessing, and analysis.</li>
                <li><strong>EDA:</strong> Jupyter Notebooks or Python scripts for exploratory data analysis.</li>
                <li><strong>Graphs and Visualizations:</strong> Charts and graphs depicting election trends.</li>
            </ul>
        </section>

        <section class="section">
            <h2>Code Example 💻</h2>
            <div class="code">
                <pre><code>from selenium import webdriver
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

print("Data scraped and saved to lok_sabha_election_results_2024.csv")</code></pre>
            </div>
            <p>This script demonstrates the web scraping process using Selenium WebDriver to extract election results data from the ECI website.</p>
        </section>

        <footer>
            <p>For more details and updates, visit our GitHub repository: <a href="https://github.com/yourusername/your-repository">Your Repository</a></p>
        </footer>
    </div>
</body>
</html>
