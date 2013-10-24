from bs4 import BeautifulSoup
from selenium import webdriver
import urllib2
from fuzzywuzzy import fuzz, process
import time

class Soup:
   def __init__(self):
      pass

   def soupify(self, what_shoes):
     http_in = 'http://shop.kithnyc.com/collections/latest'
     f = urllib2.urlopen(http_in)
     html_out = f.read()
     soup = BeautifulSoup(html_out)
     prods = soup.findAll('a', { "class" : "replace-content" })
     rf_prods = soup.findAll('a', { "class" : "replace-content-rf" })
     terms = "/products/" + what_shoes
################################# KITH NYC LINKS ################################################
     for tag in prods:
        link = tag['href']
        fuzzrat = fuzz.ratio(terms, link)
        if fuzzrat > 10:
           x = 'http://shop.kithnyc.com'+link
           shoes.append(x)
           fuzz_ratio.append(fuzzrat)
################################### RONNIE FIEG LINKS ###########################################
     for tag in rf_prods:
        link = tag['href']
        fuzzrat = fuzz.ratio(terms, link)
        if fuzzrat > 10:
           shoes.append(x)
           fuzz_ratio.append(fuzzrat)

if __name__ == "__main__":
   shoes=[]
   fuzz_ratio=[]
   what_shoes = "nike-free-inneva"
   Soup().soupify(what_shoes)
   if not shoes:
      print "This test failed, the program is not grabbing the links"
   else:
      print "Test Passed! The program works!"
