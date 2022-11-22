from bs4 import BeautifulSoup
import requests
# import pandas as pd

# Get the url
with open('rcmp.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml') # lxml is html parser
# source = requests.get('rcmp.html').text
# soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

# Grab the table
table = soup.find('table', {'class':'table table-condensed'})
print(table)

headers = []
#  For loop to get all the header names
# for h in table.find_all('th'):
#     col_name = h.text # if there is a white space use .strip() function.
#     headers.append(col_name)

# # Create the DataFrame
# df = pd.DataFrame(columns = headers)

# #  Populate the row elements
# for row in table.find_all('tr')[1:]:
#     data = row.find_all('td')
#     # Remove whitespace just in case
#     row_data = [td.text.strip() for td in data]
#     length = len(df)
#     df.loc[length] = row_data '''