from Responses import following_Res
from bs4 import BeautifulSoup
from colorama import Fore
from ES_Connection import my_Connection


def follin_list(userName):
   try:
        resp = following_Res(userName)
        soup = BeautifulSoup(resp.content , "html.parser")
        followers_list = soup.find_all('a', class_="mb-1")
        
        if(followers_list):
            
            query_data = {
                "Followings":[]
            }
            print(" ")
            print(Fore.LIGHTBLUE_EX+''+userName+'' +Fore.LIGHTGREEN_EX+' Follows These:')
            for follower in followers_list :
                my_follow =  follower.find('span', class_ = "Link--primary").string
                print(str(my_follow))
                mylist = query_data["Followings"]
                mylist.append(my_follow)
            ob  = my_Connection()
            ob.index(index='github',doc_type='doc',body=query_data)
        else:
            print(Fore.LIGHTCYAN_EX+''+userName+''+Fore.LIGHTWHITE_EX+" does not Follows AnyOne...")
            
   except Exception as e:
       print("Exception Occured at 'followings.py'",str(e))

if(__name__=='__main__'):
    follin_list('asadullahrifat89')