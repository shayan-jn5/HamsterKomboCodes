import requests
from bs4 import BeautifulSoup
import re


def ExtractFromTags(tag, string):
    res = re.findall(f"<{tag} (.*?)>(.*?)</{tag}>", string)
    return res[-1][-1]

def GetCode(tag = 'p', class_ = "font-bold mb-[16px]"):
  source = requests.get('https://hamsterkombo.com/')
  soup = BeautifulSoup(source.content, 'html.parser')
  return  ExtractFromTags('p', str(soup.find(tag, class_ = class_)))