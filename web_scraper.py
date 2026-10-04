import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# send http request to webpage
url = 'https://www.wikihow.com' 
response= requests.get(url)

# chk if request was successful
if response.status_code == 200:
    #  parse html content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

else:
    print('failed to retrieve webpage')
    exit()


doc_link = soup.find('a', {'class': 'menuitem'})['href']

# print doc link to verify
print('document link found: ', doc_link)


#handle relative URLs 
bas_url= 'https://www.wikihow.com'
full_url= urljoin(bas_url, doc_link)
print('full URL: ', full_url)

#download the document
doc_response = requests.get(full_url)

#check if document request was successful
if doc_response.status_code == 200:
    # save the document to a file
    with open('wikihow_document.html', 'wb') as f:
        f.write(doc_response.content)
    print('document downloaded successfully')
else:
    print('failed to download document. Status code: ' , doc_response.status_code )

    