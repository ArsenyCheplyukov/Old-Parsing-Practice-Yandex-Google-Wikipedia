import requests
import bs4

# Open file to write and add encoding, because some errors with not utf-8 
f = open("Wikipedia_data.txt", "w",  encoding='utf-8')

# Enter site url 
site = input("Input site url ");

# Open and crawl site with requests
response = requests.get(site)

if response is not None:
    page = bs4.BeautifulSoup(response.text, 'html.parser')
    # Choose #firstHeading for title
    title = page.select("#firstHeading")[0].text
    
    # Choose select of "p" to open text
    paragraphs = page.select("p")
    
    print(title)
    
    # Filter parahraphs with new line symbol
    intro = '\n'.join([ para.text for para in paragraphs[0:10]])
    
    print(intro)
    
    # Write that we find in .txt file
    f.write(title + "\n")
    f.write(intro + "\n")

# Close the file
f.close()  
