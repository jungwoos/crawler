import urllib.request 
from bs4 import BeautifulSoup 

def main(page): 
    soup = BeautifulSoup(urllib.request.urlopen("https://www.clien.net/service/board/park?&od=T31&po="+str(page)).read(), "html.parser") 
    
    list_title = [] 
    for i in soup.find_all("span", class_="subject_fixed"):
        string = i.get_text() 
        if 'gif' in string:
                list_title.append(string) 
        
    for j in list_title:
        print(j)
    
if __name__ == "__main__": 
    main(9)
    main(8)
    main(7)
    main(6)
    main(5)
    main(4)
    main(3)
    main(2)
    main(1)
    main(0)
