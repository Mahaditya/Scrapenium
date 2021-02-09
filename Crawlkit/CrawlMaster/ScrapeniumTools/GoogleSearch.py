import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class GoogleSearch:
    def __init__(self,driver):
        self.driver=driver
    def isLinkedInLink(self,link):
        if(link.startswith("https://www.linkedin.com")):
            return True
        else:
            if(link.startswith("https://")):
                indexOfDot = link.find(".")
                if(indexOfDot == -1):return False
                link=link[indexOfDot+1:]
                if(link.startswith("linkedin")):
                    return True
                else: return False
            else:
                return False
    def isRequiredLink(self,link,link_contains):
        if(link_contains==".linkedin.com"):
            return isLinkedInLink(link)
        return link_contains in link


    def link_score(self,*args,link):
        ## score for first argument and second argument is 3 for rest is 1
        score=0
        if(len(args)==0):
            return 0
        if(len(args)==1):
            if(link.find(args[0])!=-1):
                return 3
            else: return 0
        if(len(args)==2):
            if(link.find(args[0])!=-1):
                score=score+3
            if(link.find(args[1])!=-1):
                score=score+3
            return score
        if(len(args)>2):
            score=0
            for i in range(len(args)):
                if(i<2):
                    if(link.find(args[i])!=-1):
                        score=score+3
                if(i>2):
                    if(link.find(args[i])!=-1):
                        score=+1
            return score

    def flatten_list(self,arguments):
        result=[]
        for arg in arguments:
            if(type(arg)==list):
                result=result+self.flatten_list(arg)
            else:
                result.append(arg)
        return result
        

    def filter(self,args,links,link_contains):
        try:
            if(links==[]):
                return []
            links = [x.lower() for x in links]
            args_array=[x.lower().split() for x in args]
            args=self.flatten_list(args_array)
            args=[arg for arg in args if len(arg)>1]
            links= [x for x in links if self.isRequiredLink(x,link_contains)]
            links= { link:self.link_score(*args,link=link) for link in links}
            links= {key: value for key, value in sorted(links.items(), key=lambda item: item[1],reverse=True) if value>0}
        except:
            print("Error Occured")
            return None
        return links

    def SearchGoogle(self,*args,randomize=False,filter=True,link_contains=".linkedin.com",getAll=False):
        # print(args)
        number_of_values=len(args)-1
        link="https://www.google.com/search?q="+"%s"+("+%s"*number_of_values)+"&oq="+"%s"+("+%s"*number_of_values)+'&sourceid=chrome&ie=UTF-8'
        values=args*2
        final_url=link%values
        self.driver.get(final_url)
        xpath="//a[contains(@href,\'%s\')]"%link_contains
        site_links=[]
        try:
            site_links = [x.get_attribute('href') for x in WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))]
        except:
            print("search failed")
        if(filter):
            site_url_dic=self.filter(args,links=site_links,link_contains=link_contains)
            site_links=list(site_url_dic.keys())
        if(site_links!=[] and getAll==False):
            return site_links[0]
        if(site_links!=None):
            site_links=',\n'.join(site_links)
        else:site_links="Nothing found"
        if(randomize):
            t=random.randrange(120, 300, 3)
            time.sleep(t)
        return site_links 
    
