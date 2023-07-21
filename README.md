# Web Scraping Project: Indeed Job Scraper

![License](https://img.shields.io/badge/License-GPLv3-blue.svg)

**Note: This project is a work in progress, and the README may change to reflect updates and improvements in the future.**

**Disclaimer: This project is created for educational purposes only. The use of web scraping for certain websites, including Indeed, may be subject to legal restrictions in some regions. Please use this tool responsibly and in compliance with all applicable laws and regulations. The author does not condone or support the use of this tool for any illegal activities or violations of website terms of service.**

This is a web scraping project that scrapes job listings from Indeed using Selenium and ChromeDriver. The project is designed to extract job details such as job titles, company names, job descriptions, application links, and other relevant information. It then stores the data in a CSV file for further analysis.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3
- ChromeDriver (Download ChromeDriver from the official website: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads))

You can install the required Python packages using the following command:

```bash
pip install selenium undetected-chromedriver csv
```

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/indeed-job-scraper.git
cd indeed-job-scraper
```

2. Set up the `next_button_url.txt` file with the initial URL you want to scrape job listings from.

3. Download ChromeDriver and place it in the project directory.

4. Run the main script to start scraping job listings:

```bash
python main.py
```

The script will open Chrome with the provided URL and start extracting job details. It will then save the data to `job_details.csv`.

## Project Structure

- `main.py`: The main script that performs web scraping and saves data to CSV.
- `scrapper.py`: The helper script containing the scraping logic and functions.
- `next_button_url.txt`: Text file to store the URL for the next page.
- `job_details.csv`: CSV file to store the extracted job details.
- `LICENSE`: The GPL v3 license file.
- `README.md`: This file.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Please use this web scraping tool responsibly and in accordance with Indeed's terms of service. Web scraping may be subject to legal restrictions in some regions, so ensure you comply with all applicable laws and regulations. The author does not condone or support the use of this tool for any illegal activities or violations of website terms of service.

Happy scraping! 🚀