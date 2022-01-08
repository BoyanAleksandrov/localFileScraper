
from bs4 import BeautifulSoup
import re
import requests
import glob
import os.path


dir_path = r"C:\Users\Boyan\OneDrive\Desktop\final"
for file_name in glob.glob(os.path.join(dir_path, "*.html")):
    with open(file_name) as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
        pattern = 'Per Lot Information'
        count = 0
        z = 0
        i = 14
    for match in soup.find_all('p', text=re.compile('Per')):
        z = z + 1
        
    for match in soup.find_all('p', text=re.compile('Per')):
        count = count + 1
        
        print(match.get_text())
        el = soup.find('a',class_="table_title", text=re.compile('Line'))
        
        print(el.getText())
        
        tables = soup.findChildren('table')
        

        if count == 1 :
            
            my_table = tables[i]
            rows = my_table.findChildren(['th', 'tr'])
            for row in rows:
                cells = row.findChildren('td')
                for cell in cells:
                    value = cell.string
                    print(value)

            new_table = tables[i+1]
            new_rows = new_table.findChildren(['th', 'tr'])
            for row in new_rows:
                new_cells = row.findChildren('td')
                for cell in new_cells:
                    new_value = cell.string
                    print(new_value)


        elif count >= 1 :
                i = i + 12
                my_table = tables[i]
                rows = my_table.findChildren(['th', 'tr'])
                for row in rows:
                        cells = row.findChildren('td')
                        for cell in cells:
                            value = cell.string
                            print(value) 
     
                new_table = tables[i+1]
                new_rows = new_table.findChildren(['th', 'tr'])
                for row in new_rows:
                    new_cells = row.findChildren('td')
                    for cell in new_cells:
                        new_value = cell.string
                        print(new_value)
              
               
                    