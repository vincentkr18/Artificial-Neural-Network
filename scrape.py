
import urllib.request

from selenium import webdriver
import csv
import sys
print(sys.executable)

from selenium.webdriver.common.keys import Keys
chromedriver = "C:\\Users\\Data Scientist\\CO2\\chromedriver"
driver = webdriver.Chrome(chromedriver)

driver.get('http://flow.gassco.no')

driver.find_element_by_class_name('accept').click()

table = driver.find_element_by_css_selector("#plannedTable")
with open('usman.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)

    # for row in table.find_elements_by_css_selector('tr'):
    for table in driver.find_elements_by_xpath('//*[@id="plannedTable"]//tr'):
        wr.writerow([d.text for d in table.find_elements_by_xpath(".//*[ self::th or self::td]")])

driver.get('http://flow.gassco.no/xlarchive')
#driver.find_element_by_class_name('accept').click()
import pandas as pd
df = pd.read_csv("C:\\Users\\Data Scientist\\PycharmProjects\\final\\usman.csv", encoding="ISO-8859-1")

print(df.head())

value = []
for i,j in zip(range(0, df.shape[0]) , df['Event id'].values):
    if j == 'Event id':
        value.append(i)


print(value[0])

df1 = df[0:value[0]]
print(df1)

df1.to_csv('C:\\Users\\Data Scientist\\PycharmProjects\\final\\usman1.csv')
df2 = df[(value[0] +1) :]
print(df2)
df2.to_csv('C:\\Users\\Data Scientist\\PycharmProjects\\final\\usman2.csv')