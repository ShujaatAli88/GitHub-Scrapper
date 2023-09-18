from Responses import my_Res
from bs4 import BeautifulSoup
from colorama import Fore
from ES_Connection import my_Connection


def foll_list(userName):
    resp = my_Res(userName)
    try:
        soup = BeautifulSoup(resp.content , "html.parser")
        followers_list = soup.find_all('a', class_="mb-1")
            
        if(followers_list):
            ob = my_Connection()
            #store Followers...
            query_data = {
                "Followers":[]
            }
            print(" ")
            print(Fore.LIGHTBLUE_EX+"Followers of : "+Fore.LIGHTGREEN_EX+userName)
            for follower in followers_list :
                my_follow =  follower.find('span', class_ = "Link--primary").string
                print(str(my_follow))
            
                # ob.index(index='github',doc_type='doc',body=query)
                query_data["Followers"].append(my_follow)
                
            ob.index(index='github',doc_type='doc',body=query_data)   
        else:
            print(''+Fore.LIGHTCYAN_EX+userName+' Does not have any Follower Yet....')
            
    except Exception as e:
        print("Error At 'followers.py'",str(e))
        

if(__name__=='__main__'):
    foll_list('asadullahrifat89')