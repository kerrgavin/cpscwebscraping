# Web Scraping Tutorial CSPC 1301
This will be the instruction set for getting [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) and [Requests](http://docs.python-requests.org/en/master/) working on your computer and some additional instruction on how to get some example code we used in class working.

## Installing the Modules
Installing the modules will be different for Windows and Mac users. To install the packages we will need to use the "pip" program that is packaged with Python. If you can not run the "pip" command, then I advise you uninstall and reinstall Python. When reinstalling Python, there is an option to have Python set up the environment paths for you. Without these paths being defined the computer will be unable to locate the "pip" program. While you may be installing a newer version, you should see a page like this with the option presented as such. Please make sure to check the box

![Python set paths](https://loadbalancerblog.com/sites/default/files/images/image003.jpg)

### For Windows

1. Go to the search bar in you start menu and type in "cmd". This will find your Command Prompt program. Click to run the program and a black and white terminal will appear.
2. Type in the following into the command prompt and click enter to install the Requests module:
```bash
pip install requests
```
3. After that has finished running, you can then type the following to install BeautifulSoup:
```bash
pip install beautifulsoup4
```
4. After that has finished running you can close the Command Prompt

### For Mac
1. Go to your Application folder. From there open your Utilities folder. There you will find your "Terminal" application. Run the program and a black and white terminal will appear.
2. Type in the following into the terminal and click enter to install the Requests module:
```bash
pip3 install requests
```
3. After that has finished running, you can then type the following to install BeautifulSoup:
```bash
pip3 install beautifulsoup4
```
4. After that has finished running you can close the Command Prompt

## Writing the Python code

This code will be written to scrape data from the websites we used in class. You can find the code for those websites [here](https://github.com/kerrgavin/cpscwebscraping/tree/master/app/templates) and you can use that has reference for our Python code.

The first thing we need to do is import the necessary modules into our Python program. To scrape data from websites we need the Requests and Beautiful Soup modules.
```Python
import requests
from bs4 import BeautifulSoup
```

We then need to get the page information from our target site. The requests module gives us this capability. Using the requests module, we can make various types of HTTP requests to our target site. For this situation, we will just need to make a "GET" request using the "get" function. This will return to use the HTML that makes up our target site. We can optionally include some additional header information. Every request will have a header embedded into it that provides the server some information about us. We can add some header information here(e.g. our name and email address) to provide the server operator a way of contacting us in the case that something happens or they would like us to stop. This is optional however, an can be excluded from our code. I will include it as an example though.
```python
headers = {
  'User-Agent': 'Gavin Kerr',
  'From': 'kerr_gaivn@columbusstate.edu'
}
```
With the additional headers defined we can then make our request. We are going to store the result in the "page" variable and it will contain the HTML of the target site. Note that for the second parameter we say "headers = headers". The left side of the equals sign is referencing the parameter and the right side is referencing the variable we just made. This is the normal format for an optional parameter, and we can just leave it out all together if we felt like it. The first parameter was the URL used in class to the previously mentioned websites. The url will no longer work.
```python
page = requests.get("http://168.26.127.68:5000/first", headers = headers)
```
Once we have the page information, we need to parse it using Beautiful Soup. To do this, we need to make a Beautiful Soup object similar to how we would make Turtle objects near the beginning of the semester. We can then perform the desired operations to get the information from the site. The first parameter is the HTML from the "page" variable we just made. The second is a specific string that tells Beautiful Soup that we are parsing HTML.
```python
soup = BeautifulSoup(page.text, "html.parser")
```
Looking at the HTML code for the first of the [sites](https://github.com/kerrgavin/cpscwebscraping/blob/master/app/templates/BlueEyesWhiteDragon.html), we can see that the content of the page is divided into three different "div" blocks. We want to only look at the information located in the div block with the "info" class. We can use some python code to limit our scope to just this block by running the "find" function. We then store that information into the "info" variable. Note that the "class" parameter is optional just like the "headers" parameter above. However, in this situation we very much need to specify the class and we are not providing an HTML tag to search by.
```python
info = soup.find(class_="info")
```
From there we can see that all the information is stored in a table. However, each individual piece of information is stored in "th" blocks that are inside of the "table" blocks. Looking at how the information is presented to the user, it seems that all the information is in label-value pairs. For instance "Name" is associated with "Blue-Eyes White Dragon". In that case, lets collect the labels and values separately. Luckily, all the "th" blocks with labels are of the "label" class and all the "th" blocks with the values are of the "content" class. This makes collecting them individually relatively simple.
```python
labels = info.find_all("th", class_="label")

content = info.find_all("th", class_="content")
```
Once we have collect the labels and values we can then decided what we would like to do with them. In this tutorial we will just format and display them, but you can decide to store the information in a file. The simplest way to display the information is to print the label then the associated value on a single line, separated by a colon. We stored each set of information in different list that are of equal size. We can just choose one to determine the range we will loop over. To get the contents of each HTML tag block, we need to use the "contents" variable. We know that it is a variable because there are no parenthesis. This is a list of information located in the block but we only want the information stored at the first index.
```python
for index in range(0, len(labels)):
    print(labels[index].contents[0] + ": " + content[index].contents[0])
```
When put all together our code look like this:
```python
import requests
from bs4 import BeautifulSoup

headers = {
'User-Agent': 'Gavin Kerr',
'From': 'kerr_gaivn@columbusstate.edu'
}

page = requests.get("http://168.26.127.68:5000/third", headers = headers)

soup = BeautifulSoup(page.text, "html.parser")

info = soup.find(class_="info")

labels = info.find_all("th", class_="label")

content = info.find_all("th", class_="content")

for index in range(0, len(labels)):
    print(labels[index].contents[0] + ": " + content[index].contents[0])

```
Again, this code will not work because there is no way to access the web pages we used in class. If you were so inclined, you are free to download the HTML files linked above and pass them in after reading them from your local machine.

***

If you have any other questions you can contact me at kerr_gavin@columbsstate.edu.

-Gavin Kerr
