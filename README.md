
# Job Scraping Tool

This Python program performs **web scraping** to extract job descriptions from the Gupy website based on a search link provided by the user. The program uses libraries such as `Selenium` and `BeautifulSoup` to access the page and retrieve relevant information. The job descriptions are processed, and a **word cloud** is generated based on the job requirements.

## Features

- Automatically navigates job listing pages.
- Extracts the requirements and qualifications for each job.
- Filters the most relevant words.
- Generates a word cloud from job requirements.

## Requirements
1. Python 3.x
2. Google Chrome (and the corresponding version of chromedriver).
3. The required Python libraries, which can be installed with the command below:
   ```bash
   pip install selenium beautifulsoup4 nltk wordcloud matplotlib


## Configuring NLTK
The code automatically downloads the required NLTK packages for natural language processing, but in case of issues, you can manually run the following commands to download them:
  ```bash
      import nltk
      nltk.download('punkt')
      nltk.download('stopwords')
      nltk.download('averaged_perceptron_tagger')
```

  
## Setting up ChromeDriver
Selenium uses Google Chrome to browse web pages. To make this work, you need to download the ChromeDriver that matches your Chrome browser version.
Place the chromedriver in your PATH or in the same folder as the script.

## How to Use
      
1. Clone this repository or download the files.
```bash
   git clone https://github.com/milenafbn/Job-Scraping-Tool.git
   cd job_scraping_tool
```
2. Activate the virtual environment (if using one)
```bash
   source venv/bin/activate  # No Linux/Mac
    .\venv\Scripts\activate   # No Windows
```
3. Run the program.
```bash
   python main.py
   ```
## How It Works
1. When you run the program, it will prompt you to input a URL (e.g., https://portal.gupy.io/job-search/term=back).
2. The program will navigate the listing page, open each job posting, and extract the "Requirements and Qualifications" section.
3. The extracted text is processed, removing irrelevant words such as connectors, generic terms, and common words found in job descriptions.
4. After processing the descriptions, the program generates a word cloud with the main terms found, helping to identify the most requested qualifications in the job postings.

## Future Improvements
- Support for multiple job listing websites.
- Add visual data charts.
- Integrate AI for enhanced analysis.
