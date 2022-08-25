import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# create an empty table_body list
table_body = []

# initialize the webdriver, specify we're using the chrome browser
driver = webdriver.Chrome(executable_path="C:/Users/Dr. Ikedinma/PycharmProjects/100 Days of Python/chromedriver.exe")
# opens up the Chrome browser and go to the specified url
driver.get(url="https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1&SeasonType=Playoffs")

# collect all the table headings on the webpage
headings = driver.find_elements(By.CSS_SELECTOR, "table th")
# collect all the table rows on the webpage
body = driver.find_elements(By.CSS_SELECTOR, "table tr")

# create a list containing all the table heading
table_heading = [heading.text for heading in headings[0:30]]

# loop through all the rows excluding the first row
# the first row contains the table headings
for b in body[1:]:
    # get all the text in a row then split it into a list
    a = b.text.split()
    try:
        # get the item at index 1 and 2 which is the full name
        name = f"{a[1]} {a[2]}"
    except IndexError:
        break
    else:
        # delete the item at index 1 and 2
        del a[1:3]
        # insert the full name at index 1 into the row array
        a.insert(1, name)
        # add the row into the table_body list
        table_body.append(a)

# open a csv file in write mode
with open("./nba_player_stats", mode="w") as file:
    # create a csv writer object from the csv file
    writer = csv.writer(file)
    # write a row in the csv file
    writer.writerow(table_heading)

# open a csv file in append mode
with open("./nba_player_stats", mode="a") as file:
    # create a csv writer object from the csv file
    writer = csv.writer(file)
    # write multiple rows in the csv file
    writer.writerows(table_body)

# quit the Chrome browser
driver.quit()
