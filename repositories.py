from Responses import repository_response
from bs4 import BeautifulSoup
from colorama import Fore
from ES_Connection import my_Connection

def my_repositories(userName):
    try:
        resp = repository_response(userName)
        soup = BeautifulSoup(resp.content, "html.parser")
        
        print(" ")
        repoCounter = soup.find('span' , class_= "Counter").text
        if(repoCounter):
            ob = my_Connection()
            
            ###For Storing all the data.....
            user_data = {
                "User": userName,
                "Total Repositories": repoCounter,
                "Repositories": []
            }

            print(Fore.LIGHTCYAN_EX+'Total Repositories of '+userName+' : '+Fore.LIGHTGREEN_EX+str(repoCounter))
            # print(Fore.LIGHTCYAN_EX + "All The Famous Repositories of: " + Fore.LIGHTGREEN_EX + userName)
            print(" ")
            print("Here They Are:")
            repo_Des_Container = soup.find_all('li', class_="source")
            for data in repo_Des_Container:
                repoName = data.find('a')
                repoNamed = repoName.text.strip()
                print(Fore.LIGHTCYAN_EX+"Repo Name: "+Fore.LIGHTGREEN_EX+repoNamed)
                repoLink = 'https://github.com/'+userName+'/'+repoNamed+''
                print(Fore.LIGHTCYAN_EX+"Repo Link:"+Fore.LIGHTGREEN_EX+repoLink)
                repoDes = data.find('p')
                if repoDes:
                    repo_Description = repoDes.text.strip()
                    print(Fore.LIGHTCYAN_EX+"Repo Description:"+Fore.LIGHTGREEN_EX+repo_Description)
                    print(" ")
                else:
                    print(Fore.LIGHTCYAN_EX+"Repo Description :"+Fore.LIGHTRED_EX+"No Description for This Repository...")
                
                repo_data = {
                    "Repository Name:":repoNamed,
                    "Repository Link":repoLink,
                    "Repository Description:":repo_Description
                }
                
                user_data["Repositories"].append(repo_data)
                # ob.index(index='github',doc_type='doc',body=query) 
            ob.index(index='github',id=userName, doc_type='doc', body=user_data)

        else:
            print(userName+" Has Not created any Repositories Yet...")
    except Exception as e:
        print("Exception Occuered at 'repositories.py'"+str(e))
        
if(__name__=='__main__'):
    my_repositories('asadullahrifat89')
