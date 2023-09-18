from followers import foll_list
from followings import follin_list
from profile_Info import profiler
from repositories import my_repositories
from work import work_skills
from colorama import Fore
from Responses import my_Res , following_Res , profil_response , repository_response
from colorama import Fore

def my_main(userName):
    
    ####Callings All Functions Here and Passing The userName.........
    try:
        ##Calling and Passsing only if User With the Name Exists....
        follower_reponse = my_Res(userName)
        if(follower_reponse.status_code == 200):
           print(Fore.WHITE+"Repositories:")
           my_repositories(userName)
           print(" ")
           print(Fore.WHITE+"Work and Skills Related Information:")
           work_skills(userName)
           print(Fore.WHITE+"Followers:")
           foll_list(userName)  
           print(" ")
           print(Fore.WHITE+"Followings:")
           follin_list(userName)
           print(" ")
           print(Fore.WHITE+"Basic Information:")
           profiler(userName)
           print(" ")
           
           print(Fore.LIGHTYELLOW_EX+"Relevent Data Also Being Dumped into Elasticsearch...")
           
        else:
           print(Fore.LIGHTRED_EX+"No User Found on Github with userName : "+Fore.LIGHTCYAN_EX+userName)
        
    except Exception as e:
        print("Error while Executing 'main.py'"+str(e))
        
    
if(__name__=='__main__'):
    my_main('asadullahrifat89')