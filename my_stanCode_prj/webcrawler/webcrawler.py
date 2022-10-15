"""
File: webcrawler.py
Name: Yi-Ju Lu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features='html.parser')

        # ----- Write your code below this line ----- #
        """
        1. catch the info in class t-stripe
        2. catch string from 'tr'  
        """

        # table = soup.find('table', {'class': 't-stripe'})
        # # catch string from 'tr', list exclude first, second info & last info
        # tags = table.find_all('tr')[2:202]
        # male_list = []  # empty male list to hold number of male or female
        # female_list = []
        # male_num = 0  # initiate num of male or female
        # female_num = 0
        # # nested for-loop to separate for each row and data into a list
        # for row in range(len(tags)):  # for each row
        #     row_list = []   # empty list to hold data of each row
        #     all_data = tags[row].find_all('td')
        #     for data in all_data:  # for each data
        #         raw_data = data.text.replace(',', '')  # to get rid of ','
        #         row_list.append(raw_data)
        #     male = row_list[2]
        #     female = row_list[4]
        #     male_list.append(male)
        #     female_list.append(female)
        # # b/c sum() can only use to calculate int, need to change each str into int
        # for males in male_list:
        #     male_num += int(males)
        # for females in female_list:
        #     female_num += int(females)

        male_num = 0
        female_num = 0
        tags = soup.find_all('table', {'class': 't-stripe'})
        for tag in tags:
            text = tag.tbody.text.split()
            for i in range(len(text)):
                if i <= 1000:
                    if i % 5 == 2:  # boy
                        male_num += int(text[i].replace(',', ''))
                    if i % 5 == 4:  # girl
                        female_num += int(text[i].replace(',', ''))
        print('Male number: ' + str(male_num))
        print('Male number: ' + str(female_num))


if __name__ == '__main__':
    main()
