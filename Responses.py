import requests

def my_Res(userName):

      cookies = {
          '_octo': 'GH1.1.549730895.1694416409',
          '_device_id': '00a07cfdd241dcf5ae56e76abee4a593',
          'fileTreeExpanded': 'true',
          'user_session': 'lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M',
          '__Host-user_session_same_site': 'lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M',
          'logged_in': 'no',
          'preferred_color_mode': 'light',
          'tz': 'America%2FLos_Angeles',
          '_gh_sess': 'VcCGNjznnmUjvtH37r8lE6%2Fvgp8x9rLBTEJ%2B5UVN9hbr%2F9kIABEz8nlrGYaaYEAu9IihMt4Wm%2FDBdHkLYN3E3LfBn9zMIjnT6wffGqHhk7rK7iqwdFESFQhYAXSz8l0ZT3ketqEPgVSHo2oJN0o7kTNO3nAVGmtd4X%2BGgPyqUnvHlo55%2BLCXMjBUju7yBtwPZbkoC7uubWEwVt9HFzV1Pcia95w9UC7afxbKFixKcvY2vHOYCJ3f0ig18l9cXLPw8DD8W%2Fa7L2RL8kY4GBrmoQ%3D%3D--qPsCepdHgGfTW3fg--yzEmqP2wobO3s%2FKleDWnEw%3D%3D',
      }
      
      headers = {
          'authority': 'github.com',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
          'cache-control': 'max-age=0',
          # 'cookie': '_octo=GH1.1.549730895.1694416409; _device_id=00a07cfdd241dcf5ae56e76abee4a593; fileTreeExpanded=true; user_session=lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M; __Host-user_session_same_site=lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M; logged_in=no; preferred_color_mode=light; tz=America%2FLos_Angeles; _gh_sess=VcCGNjznnmUjvtH37r8lE6%2Fvgp8x9rLBTEJ%2B5UVN9hbr%2F9kIABEz8nlrGYaaYEAu9IihMt4Wm%2FDBdHkLYN3E3LfBn9zMIjnT6wffGqHhk7rK7iqwdFESFQhYAXSz8l0ZT3ketqEPgVSHo2oJN0o7kTNO3nAVGmtd4X%2BGgPyqUnvHlo55%2BLCXMjBUju7yBtwPZbkoC7uubWEwVt9HFzV1Pcia95w9UC7afxbKFixKcvY2vHOYCJ3f0ig18l9cXLPw8DD8W%2Fa7L2RL8kY4GBrmoQ%3D%3D--qPsCepdHgGfTW3fg--yzEmqP2wobO3s%2FKleDWnEw%3D%3D',
          'if-none-match': 'W/"c75cfdc4d4ba68c4ff37d7d0e7ea5f33"',
          'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'none',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
      }
      
      params = {
          'tab': 'followers',
      }
      
      response = requests.get('https://github.com/'+userName+'', params=params, cookies=cookies, headers=headers)
      return response
  


def following_Res(userName):
    
    cookies = {
        '_octo': 'GH1.1.549730895.1694416409',
        '_device_id': '00a07cfdd241dcf5ae56e76abee4a593',
        'fileTreeExpanded': 'true',
        'user_session': 'lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M',
        '__Host-user_session_same_site': 'lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M',
        'logged_in': 'no',
        'preferred_color_mode': 'light',
        'tz': 'America%2FLos_Angeles',
        '_gh_sess': 'CaUNV2NiB%2B4%2FTZ67amy7%2Fu%2FFyIfdCXysRunT53ScTzsojUKJk%2Bi%2BtFuT632e41fBhZv6oWANnRYnzDKrRgUwird6I0vfgIL5EO%2F4AsSfnw9CaeibF9Gtoj7xw5gtkET1d1Vt8uMJIDvtCH4XyycDI16rZzDTmKSmtfMDkW6wtHf0h9bB163EX0y7obUuPNWq0r%2BQB%2B6JIbBGl8tQui6jcSvjlWYwdsBsq%2Fr42%2BYnvhidjj9rC0rRmvdB7%2BZKZRykgHCaoiJZXRVWQ%2B4iNMwSwg%3D%3D--bfOM23CvahSIf4TT--0NQB%2FTYyhr4xKIHxxfkkrA%3D%3D',
    }
    
    headers = {
        'authority': 'github.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': '_octo=GH1.1.549730895.1694416409; _device_id=00a07cfdd241dcf5ae56e76abee4a593; fileTreeExpanded=true; user_session=lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M; __Host-user_session_same_site=lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M; logged_in=no; preferred_color_mode=light; tz=America%2FLos_Angeles; _gh_sess=CaUNV2NiB%2B4%2FTZ67amy7%2Fu%2FFyIfdCXysRunT53ScTzsojUKJk%2Bi%2BtFuT632e41fBhZv6oWANnRYnzDKrRgUwird6I0vfgIL5EO%2F4AsSfnw9CaeibF9Gtoj7xw5gtkET1d1Vt8uMJIDvtCH4XyycDI16rZzDTmKSmtfMDkW6wtHf0h9bB163EX0y7obUuPNWq0r%2BQB%2B6JIbBGl8tQui6jcSvjlWYwdsBsq%2Fr42%2BYnvhidjj9rC0rRmvdB7%2BZKZRykgHCaoiJZXRVWQ%2B4iNMwSwg%3D%3D--bfOM23CvahSIf4TT--0NQB%2FTYyhr4xKIHxxfkkrA%3D%3D',
        'if-none-match': 'W/"37dcfaab1d7685fddc6dae30ba1d74da"',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    
    params = {
        'tab': 'following',
    }
    
    response = requests.get('https://github.com/'+userName+'', params=params, cookies=cookies, headers=headers)
    return response


def profil_response(userName):

     cookies = {
         '_octo': 'GH1.1.549730895.1694416409',
         '_device_id': '00a07cfdd241dcf5ae56e76abee4a593',
         'fileTreeExpanded': 'true',
         'user_session': 'lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M',
         '__Host-user_session_same_site': 'lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M',
         'logged_in': 'no',
         'preferred_color_mode': 'light',
         'tz': 'America%2FLos_Angeles',
         '_gh_sess': '1ZaUyvmMl%2FDDF3Plduqva0Fc%2FFYqcU1Ka%2Fz02w6eE9ByNtvq%2FdbDLOeO5rL6QNkWubsITy8ZdZS0R5G3Zu%2Bpmoxe0thcjP8yXgh%2ByftrBD%2B%2F6PS1%2Fjhl%2FOC5eiBdPBEm88sv5gBaks7iqx0hF7b%2FZRAs8Ok0q8dCMxpCYlNLsvYIzE%2FwtwWQTZm7rdNk4xKVgORrEYk86ipKEaNQD%2BSXljZoZPSrlew%2FXcqyvw%2FcMGO7tZEmFMdOLfKZUY8wk2HEnJjj52jcENETkOeQtvOdLw%3D%3D--%2BlolPmRRXi8aUDgp--7OGVo2WLFB4v%2B7O9q40wOw%3D%3D',
     }
     
     headers = {
         'authority': 'github.com',
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
         # 'cookie': '_octo=GH1.1.549730895.1694416409; _device_id=00a07cfdd241dcf5ae56e76abee4a593; fileTreeExpanded=true; user_session=lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M; __Host-user_session_same_site=lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M; logged_in=no; preferred_color_mode=light; tz=America%2FLos_Angeles; _gh_sess=1ZaUyvmMl%2FDDF3Plduqva0Fc%2FFYqcU1Ka%2Fz02w6eE9ByNtvq%2FdbDLOeO5rL6QNkWubsITy8ZdZS0R5G3Zu%2Bpmoxe0thcjP8yXgh%2ByftrBD%2B%2F6PS1%2Fjhl%2FOC5eiBdPBEm88sv5gBaks7iqx0hF7b%2FZRAs8Ok0q8dCMxpCYlNLsvYIzE%2FwtwWQTZm7rdNk4xKVgORrEYk86ipKEaNQD%2BSXljZoZPSrlew%2FXcqyvw%2FcMGO7tZEmFMdOLfKZUY8wk2HEnJjj52jcENETkOeQtvOdLw%3D%3D--%2BlolPmRRXi8aUDgp--7OGVo2WLFB4v%2B7O9q40wOw%3D%3D',
         'if-none-match': 'W/"6e20264d4ceeedbe826ee9fd7c013971"',
         'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
         'sec-ch-ua-mobile': '?0',
         'sec-ch-ua-platform': '"Windows"',
         'sec-fetch-dest': 'document',
         'sec-fetch-mode': 'navigate',
         'sec-fetch-site': 'none',
         'sec-fetch-user': '?1',
         'upgrade-insecure-requests': '1',
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
     }
     
     response = requests.get('https://github.com/'+userName+'', cookies=cookies, headers=headers)
     return response
 


def repository_response(userName):
    cookies = {
        '_octo': 'GH1.1.549730895.1694416409',
        '_device_id': '00a07cfdd241dcf5ae56e76abee4a593',
        'fileTreeExpanded': 'true',
        'user_session': 'lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M',
        '__Host-user_session_same_site': 'lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M',
        'logged_in': 'no',
        'preferred_color_mode': 'light',
        'tz': 'America%2FLos_Angeles',
        '_gh_sess': 'Dx3PJD9i963FjxFEkrnu%2FjyndJj17VKlI5AkmvGP0twcqP%2BUaY5oXdlrNzNsbk5t%2F8TCsCz%2BZRmROe9ZdxaHFcr%2FOeiTREkQXWocP1sahE9EkbYQR7g5uUf72QgDDrunS0uel0XPMD3tzHhYhiVJPHUgrBxnaqFk6S8a5enukri5PfqCbBiJi%2F2YRXq091%2BtDvnhCzEJq2ieEIZG2DZfdWtLZe5OIId8vNxm31f%2FSzBJfBNIWw%2BJbYslbBSet2rnyAu8PK90WPK9dCcuKdWGAw%3D%3D--0qT%2FujXxYbvm8Z3h--b3JhpHkNB8My8FLLTF%2B5MA%3D%3D',
    }
    
    headers = {
        'authority': 'github.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': '_octo=GH1.1.549730895.1694416409; _device_id=00a07cfdd241dcf5ae56e76abee4a593; fileTreeExpanded=true; user_session=lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M; __Host-user_session_same_site=lZXfk_Ti0PgPioqS-fYcIYMMO8R1lv4h3-E6SflQCagWnC0M; logged_in=no; preferred_color_mode=light; tz=America%2FLos_Angeles; _gh_sess=Dx3PJD9i963FjxFEkrnu%2FjyndJj17VKlI5AkmvGP0twcqP%2BUaY5oXdlrNzNsbk5t%2F8TCsCz%2BZRmROe9ZdxaHFcr%2FOeiTREkQXWocP1sahE9EkbYQR7g5uUf72QgDDrunS0uel0XPMD3tzHhYhiVJPHUgrBxnaqFk6S8a5enukri5PfqCbBiJi%2F2YRXq091%2BtDvnhCzEJq2ieEIZG2DZfdWtLZe5OIId8vNxm31f%2FSzBJfBNIWw%2BJbYslbBSet2rnyAu8PK90WPK9dCcuKdWGAw%3D%3D--0qT%2FujXxYbvm8Z3h--b3JhpHkNB8My8FLLTF%2B5MA%3D%3D',
        'if-none-match': 'W/"ee68e6f56cce08d4e068bb23a8b0e0bc"',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    
    params = {
        'tab': 'repositories',
    }
    
    response = requests.get('https://github.com/'+userName+'', params=params, cookies=cookies, headers=headers)
    return response