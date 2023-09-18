from Responses import profil_response
from colorama import Fore
from bs4 import BeautifulSoup
from ES_Connection import my_Connection

def profiler(userName):
    resp = profil_response(userName)
    soup = BeautifulSoup(resp.content , "html.parser")
    followers_list = soup.find('div', class_="f4").string
    
    print(Fore.LIGHTCYAN_EX+"Information Related To: "+userName)
    print(Fore.LIGHTBLUE_EX+"About")
    print(Fore.LIGHTGREEN_EX+followers_list) ##About...
    
    work_at  = soup.find('span' , class_="p-org").string
    if(work_at):
        print(" ")
        print(''+Fore.LIGHTBLUE_EX+userName+Fore.LIGHTGREEN_EX+' Works at : '+work_at)
    else:
        print("Has not mentioned his work place...")
    print(" ")
    print(Fore.LIGHTBLUE_EX+"Location & Time:")
    
    unordered_list = soup.find('ul', class_="vcard-details")
    if unordered_list:
        location_items = unordered_list.find_all('span', class_="p-label")
        for location in location_items:
          loca = location.text.strip()  
          print(Fore.LIGHTGREEN_EX+loca)
    else:
        print("Location Not Mentioned...")
        
    print(" ")
    print(Fore.LIGHTBLUE_EX+"Social Platforms:")
    linkedin_link = soup.find("a", class_="Link--primary", text="in/asadullah-refat")
    twitter_link = soup.find('a', class_='Link--primary')
    
    if linkedin_link:
        linkedin_url = linkedin_link['href']
        print("LinkedIn Link:", Fore.LIGHTGREEN_EX+linkedin_url)
    else:
        print(Fore.LIGHTRED_EX+userName+" Has not mentioned his 'Linkedin' url")
    if twitter_link:
        twitter_url = twitter_link['href']
        print(Fore.LIGHTBLUE_EX+"Twitter Link:", Fore.LIGHTGREEN_EX+twitter_url)
    else:
        print(Fore.LIGHTRED_EX+userName+" Has not mentioned his 'Twitter' url")
        
    myQuery = {
        "Work Place Name :" :work_at,
        "Location & Time:":loca,
        "LinkedIn URL:":linkedin_url,
        "Twitter URL:":twitter_url
    }
    
    ob = my_Connection()
    ob.index(index='github',doc_type='doc',body=myQuery)

    
    
if(__name__=='__main__'):
    profiler('asadullahrifat89')
    