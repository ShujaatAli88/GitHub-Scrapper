from Responses import profil_response
from bs4 import BeautifulSoup
from colorama import Fore
from ES_Connection import my_Connection

def work_skills(userName):
   try:
        resp = profil_response(userName)
        soup = BeautifulSoup(resp.content , "html.parser")
        
        print(" ")
        list = soup.find_all('ul' , dir="auto")
        if(list):
            ob = my_Connection()
            query_Data = {
                "Work & Skills:":[]
            }
            print(Fore.LIGHTCYAN_EX+"All The Skills & Work Experience of : "+userName)
            for item in list:
                lis = item.find_all('li')
                for ok in lis:
                    okay = ok.text
                    print(okay)
                    
                    list_for_work_and_skills = query_Data["Work & Skills:"]
                    list_for_work_and_skills.append(okay)
            
            ob.index(index='github',doc_type='doc',body=query_Data)
                    
        else:
            print(Fore.LIGHTCYAN_EX+userName+Fore.LIGHTGREEN_EX+" Has Not shared his Work experience and Skills On Github...")
            
   except Exception as e:
       print("Exception Occured at 'work.py'"+str(e))
       
if(__name__=='__main__'):
    work_skills('asadullahrifat89')