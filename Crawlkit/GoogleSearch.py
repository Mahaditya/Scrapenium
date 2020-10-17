
class GoogleSearch:
    def __init__(self,driver):
        self.driver=driver
    def SearchGoogle(self,*args,link_contains=".linkedin.com"):
        number_of_values=len(args)-1
        link="https://www.google.com/search?q="+"%s"+("+%s"*number_of_values)+"&oq="+"%s"+("+%s"*number_of_values)+'&sourceid=chrome&ie=UTF-8'
        values=args*2
        final_url=link%values
        self.driver.get(final_url)
        xpath="//a[contains(@href,\'%s\')]"%link_contains
        site_links = [x.get_attribute('href') for x in self.driver.find_elements_by_xpath(xpath)]
        print(site_links)
        if(site_links!=[]):
            site_links=',\n'.join(site_links)
        else:site_links="none"
        return site_links 
    
