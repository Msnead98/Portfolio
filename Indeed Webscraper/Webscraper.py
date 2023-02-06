import os
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import threading


class JobScraper:
    def __init__(self, search_term):
        self.search_term = search_term
        self.jobs = []
        DRIVER_PATH = os.environ.get('CHROME_DRIVER_PATH', '/your/path/')
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.wait = WebDriverWait(self.driver, 10)

    def collection(self):
        src = self.driver.page_source
        soup = BeautifulSoup(src, 'lxml')

        for job in soup.find_all('h2', {'class': "jobTitle css-1h4a4n5 eu4oa1w0"}):
            job_title = job.text.strip()
            company = job.find_next("span", {"class": "companyName"}).text.strip()
            location = job.find_next("div", {"class": "companyLocation"}).text.strip()

            self.jobs.append({
                "Title": job_title,
                "Company": company,
                "Location": location,

            })

    def startp(self):
        self.driver.get("https://www.indeed.com")
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys(self.search_term)
        search_bar.send_keys(Keys.RETURN)
        threads = []
        for i in range(30):
            thread = threading.Thread(target=self.collection)
            thread.start()
            threads.append(thread)

        # wait for all threads to finish
        for thread in threads:
            thread.join()
        df = pd.DataFrame(self.jobs)
        df.to_csv(f'jobs_{self.search_term}.csv', index=False)
        self.driver.close()
        # Send the generated csv file as an attachment in an email
        email = "senderemail@gmail.com"
        password = "Your password"
        send_to_email = 'receiveremail@gmail.com'
        subject = f'Jobs: {self.search_term}'
        message = MIMEMultipart()
        message['From'] = email
        message['To'] = send_to_email
        message['Subject'] = subject
        message.attach(MIMEText('Find attached the jobs for the search term: ' + self.search_term))
        filename = f'jobs_{self.search_term}.csv'
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        message.attach(part)
        text = message.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, send_to_email, text)
        server.quit()


