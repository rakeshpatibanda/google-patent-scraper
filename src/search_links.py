from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import sys
import time
import socket
import re
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SearchLinks:

    def __init__(self, ip = None):
        socket.setdefaulttimeout(30)
        self.ua_generator = UserAgent()
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--incognito")
        # UserAgent.chrome will generate random Chrome user-agent
        self.options.add_argument(f'user-agent={self.ua_generator.chrome}')
        if ip:
            self.options.add_argument('--proxy-server=http://' + ip)
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=self.options)
        self.driver.get('http://patents.google.com/advanced')
        self.prefix = 'https://patents.google.com/patent/'
        self.number_of_results = None
        self.links = []
        self.titles = []
        self.max_results = 200
        self.results_per_page = 100

    def search(self, search_terms):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, 'searchInput')))
        except:
            print('Error loading https://patents.google.com/advanced')
            sys.exit()
        
        time.sleep(3)
        
        # Format the search terms
        formatted_terms = ' AND '.join(f'"{term.strip()}"' for term in search_terms.split('AND'))
        
        search_input = self.driver.find_element(By.ID, 'searchInput')
        search_input.clear()  # Clear any existing text
        search_input.send_keys(formatted_terms)
        
        time.sleep(3)
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        # set Results/page to 100, so we can perform less "Next page"
        try:
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, '//dropdown-menu[@label="Results / page"]')))
            self.driver.find_element(By.XPATH, '//dropdown-menu[@label="Results / page"]').click()
            self.driver.find_element(By.XPATH, '//dropdown-menu[@label="Results / page"]/'
                                               'iron-dropdown/div/div/div/div[4]').click()
        except:
            print('Error selecting 100 results/page')
            sys.exit()

    def check_page_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((
                    By.XPATH, '//paper-tab/div[@class="tab-content style-scope paper-tab"]')))
        except:
            print('Error loading searching results page')
            sys.exit()

    def search_links(self):
        self.check_page_loaded()
        if not self.number_of_results:
            # \d+ means one or more digits
            self.number_of_results = int(
                re.search('\\b\\d+\\b', self.driver.find_element(By.ID, 'numResultsLabel').text).group())
        link_elements = self.driver.find_elements(By.XPATH,
            '//search-result-item//article//h4[@class="metadata style-scope search-result-item"]//'
            'span[@class="bullet-before style-scope search-result-item"]//'
            'span[@class="style-scope search-result-item"]')
        title_elements = self.driver.find_elements(By.XPATH,
            '//search-result-item//article//state-modifier//a//h3//span')
        self.links.extend([e.text for e in link_elements if e.text != ''])
        self.titles.extend([e.text for e in title_elements if e.text != ''])

    def collect_links(self):
        page = 1
        while len(self.links) < self.max_results:
            time.sleep(3)
            self.search_links()
            
            if len(self.links) >= self.max_results:
                break
            
            try:
                WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, '//iron-icon[@id="icon"]')))
                next_btn = self.driver.find_elements(By.XPATH, '//iron-icon[@id="icon"]')[1]
                if next_btn.is_displayed():
                    next_btn.click()
                    page += 1
                else:
                    print('No more pages available.')
                    break
            except:
                print(f'Reached final page or error occurred on page {page}')
                break

        # Trim excess links if we've collected more than max_results
        self.links = self.links[:self.max_results]
        self.titles = self.titles[:self.max_results]

        return self.links, self.titles