from bs4 import BeautifulSoup as bs
import pandas as pd

with open('page_source.html', 'r') as f:
    contents = f.read()
    soup = bs(contents, 'lxml')

def has_class(tag):
    return tag.has_attr('class')

tag_with_class_attribute = soup.find_all(has_class)

classes = [(cl.name,tuple(cl['class'])) for cl in tag_with_class_attribute]


df=pd.DataFrame(classes,columns=['Name','Class'])
df=df.drop_duplicates(keep=False)
df.to_csv('classes.csv')

print(set(classes))