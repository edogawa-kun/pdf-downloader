import requests, bs4, sys

### full_page_url = 'http://schedule.berkeley.edu/OSOCarchive.html'
### host = 'http://schedule.berkeley.edu'
def pdf_download(full_page_url, host):

    res = requests.get(page_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)


    file_list = []
    for link in soup.find_all('a'):

        file_loc = link.get('href')

        if file_loc.endswith('pdf'):
            file_list.append(file_loc)


    for file in file_list:

        # relative or absolute path?
        if file.startswith('http'):
            url = file
        else:
            url = '{}/{}'.format(host, file)

        print(url)

        filename = url.split('/')[-1]
        print(filename)

        download = requests.get(url)

        try:
            download.raise_for_status()
        except Exception as exc:
            print('There was a problem: {}'.format(exc))

        local_file = open('files/{}'.format(filename), 'wb')

        for chunk in download.iter_content(100000):
            local_file.write(chunk)

        local_file.close()
