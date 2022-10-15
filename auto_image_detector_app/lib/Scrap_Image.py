import requests
from .Random_Name_Generator import Random_Name_Generetor

def Download_Image(url):
    res = requests.get(url)
    if res.status_code == 200:
        newname = Random_Name_Generetor(8)
        imgfile = open(f'pics/{newname}','wb')
        imgfile.write(res.content)

        imgfile.close()
        
        return newname
    else:
        return False
    
def Search_Image(url):
    res = requests.get(url)
    if res.status_code == 200: 
        return True
    else:
        return False
