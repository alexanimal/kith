from bs4 import BeautifulSoup
from selenium import webdriver
import urllib2
from fuzzywuzzy import fuzz, process
import time
import itertools

class Soup:
   def __init__(self):
      pass

   def scrape(self):
      url = 'http://shop.kithnyc.com/collections/latest'
      f = urllib2.urlopen(url)
      html = f.read()
      soup = BeautifulSoup(html)
      x = soup.findAll('a')
      prods = soup.findAll('a', { "class" : "replace-content" })
      rf_prods = soup.findAll('a', { "class" : "replace-content-rf" })
      global tags
      tags = []
      for tag in prods:
          link = tag['href']
          tags.append(link)
      for tag in rf_prods:
          link = tag['href']
          tags.append(link)
      return tags

   def fuzzness(self, x):
      item_name = "/products/%s"%x
      for item in tags:
          fuzz_rat = fuzz.ratio(item, item_name)
          if fuzz_rat > min_fuzz:
             fuzzy_ratios.append(fuzz_rat)
             links.append(item)

   def fuzzness_test(self, x):
      item_name = "/products/%s"%x
      global fuzzy_ratios, links
      fuzzy_ratios = []
      links = []
      for item in tags:
          fuzz_rat = fuzz.ratio(item, item_name)
          fuzzy_ratios.append(fuzz_rat)
          links.append(item)

   def fuzz_test(self, x):
      item_name = "/products/%s"%x
      global fuzzy_ratios, links
      fuzzy_ratios = []
      links = []
      for item in tags:
          fuzz_rat = fuzz.ratio(item, item_name)
          print (fuzz_rat, item)

   def link_slot(self):
      x = max(fuzzy_ratios)
      slot = fuzzy_ratios.index(x)
      return links[slot]

class Kith:
   def __init__(self):
      pass

   def go_to_item_page(self, x):
      url = "http://shop.kithnyc.com%s"%x
      browser.get(url)
      size_dropdown = browser.find_element_by_class_name("easy-select-box-disp")
      Kith().xpath_size(user_size)
      size = browser.find_element_by_xpath(xpath)
      size_dropdown.click()
      size.click()
      add_to_cart = browser.find_element_by_id('buyNowButton')
      add_to_cart.click()
      time.sleep(.5)
      checkout = browser.find_element_by_id("proceedToCheckoutButton")
      checkout.click()
      alert = browser.switch_to_alert()
      alert.accept()
      time.sleep(3)
   
   def cart(self):
      email = browser.find_element_by_name("order[email]")
      first_name = browser.find_element_by_name("billing_address[first_name]")
      last_name = browser.find_element_by_name("billing_address[last_name]")
      address1 = browser.find_element_by_name("billing_address[address1]")
      address2 = browser.find_element_by_name("billing_address[address2]")
      city = browser.find_element_by_name("billing_address[city]")
      zip_code = browser.find_element_by_name("billing_address[zip]")
      phone = browser.find_element_by_name("billing_address[phone]")
      email.send_keys(user_email)
      first_name.send_keys(user_first_name)
      last_name.send_keys(user_last_name)
      address1.send_keys(user_address1)
      address2.send_keys(user_address2)
      city.send_keys(user_city)
      zip_code.send_keys(user_zip_code)
      phone.send_keys(user_tel)
      country = browser.find_element_by_name('billing_address[country]')
      for option in country.find_elements_by_tag_name('option'):
         if option.text == 'United States':
            option.click()
      state = browser.find_element_by_name("billing_address[province]")
      for option in state.find_elements_by_tag_name('option'):
         if option.text == user_state:
            option.click()
      next_step = browser.find_element_by_name("commit")
      next_step.click()
      time.sleep(3)
      credit_card = browser.find_element_by_name("credit_card[number]")
      credit_card.send_keys(user_cc_num)
      credit_card_month = browser.find_element_by_name("credit_card[month]")
      for option in credit_card_month.find_elements_by_tag_name('option'):
         if option.text == cc_exp_month:
            option.click()
      credit_card_year = browser.find_element_by_name('credit_card[year]')
      for option in credit_card_year.find_elements_by_tag_name('option'):
         if option.text == user_cc_year:
            option.click()
      card_security_code = browser.find_element_by_name("credit_card[verification_value]")
      card_security_code.send_keys(user_cc_csc)
      check_box = browser.find_element_by_name("buyer_accepts_marketing")
      check_box.click()
      place_order = browser.find_element_by_name("commit")
      #place_order.click()

   def xpath_size(self, size_of_shoe):
      global xpath
      if size_of_shoe == '5':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li'
      elif size_of_shoe == '5.5':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[2]'
      elif size_of_shoe == '6':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[3]'
      elif size_of_shoe == '6.5':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[4]'
      elif size_of_shoe == '7':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[5]'
      elif size_of_shoe == '7.5':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[6]'
      elif size_of_shoe == '8':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[7]'
      elif size_of_shoe == '8.5':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[8]'
      elif size_of_shoe == '9':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[9]'
      elif size_of_shoe == '9.5':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[10]'
      elif size_of_shoe == '10':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[11]'
      elif size_of_shoe == '10.5':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[12]'
      elif size_of_shoe == '11':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[13]'
      elif size_of_shoe == '11.5':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[14]'
      elif size_of_shoe == '12':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[15]'
      elif size_of_shoe == '12.5':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[16]'
      elif size_of_shoe == '13':
         xpath = '/html/body/div[2]/div/div[10]/div/div[2]/div[3]/div/form/div/div[3]/ul/li[17]'
   
class User:
   def __init__(self):
      pass

   def ins(self):
      global user_first_name, user_last_name, user_email, user_tel, user_address1, user_address2, user_zip_code, user_city, user_state, user_cc_type, user_cc_num, user_cc_exp_month, user_cc_year, user_cc_csc, user_size
      with open("user_info.txt") as f:
         content = f.readlines()
         user_email = content[1].strip()
         user_first_name = content[3].strip()
         user_last_name = content[5].strip()
         user_address1 = content[7].strip()
         user_address2 = content[9].strip()
         user_city = content[11].strip()
         user_zip_code = content[13].strip()
         user_state = content[15].strip()
         user_tel = content[17].strip()
         user_cc_num = content[19].strip()
         user_cc_exp_month = content[21].strip()
         user_cc_year = content[23].strip()
         user_cc_csc = content[25].strip()
         user_size = content[27].strip()
      User().cc_month_format(user_cc_exp_month)
      if len(user_state)==2:
         print "Your State's name is formatted incorrectly, please type full state name"
      if len(user_zip_code)!=5:
         print "Your ZIP code is formatted incorrectly, 5 numbers please"
      if len(user_cc_num)!=16:
         print "Your credit card number is not 16 numbers no spaces, try again"
      if len(user_cc_year)!=4:
         print "Your credit card expiration year is not formatted correctly, it should be the full year (2013)"
      if len(user_cc_csc)!=3:
         print "Your Credit Card Security Code is not 3 numbers, make sure it is 3 numbers"
      #print (user_email, user_first_name, user_last_name, user_address1, user_address2, user_city, user_zip_code, user_state, user_tel, user_cc_num, cc_exp_month, user_cc_year, user_cc_csc, user_size)

   def cc_month_format(self, user_cc_exp_month):
      global cc_exp_month
      if user_cc_exp_month == '01':
         cc_exp_month = '1 - January'
      elif user_cc_exp_month == '02':
         cc_exp_month = '2 - February'
      elif user_cc_exp_month == '03':
         cc_exp_month = '3 - March'
      elif user_cc_exp_month == '04':
         cc_exp_month = '4 - Arpil'
      elif user_cc_exp_month == '05':
         cc_exp_month = '5 - May'
      elif user_cc_exp_month == '06':
         cc_exp_month = '6 - June'
      elif user_cc_exp_month == '07':
         cc_exp_month = '7 - July'
      elif user_cc_exp_month == '08':
         cc_exp_month = '8 - August'
      elif user_cc_exp_month == '09':
         cc_exp_month = '9 - September'
      elif user_cc_exp_month == '10':
         cc_exp_month = '10 - October'
      elif user_cc_exp_month == '11':
         cc_exp_month = '11 - November'
      elif user_cc_exp_month == '12':
         cc_exp_month = '12 - December'
   
def link_test(terms, link):
   x = fuzz.ratio(terms, link)
   fuzz_ratios_test.append(x)
   return (x, link)

def term_test(lst, term):
   combs = []
   lst.insert(0,"x-rf")
   for x in itertools.permutations(lst):
      link = "/products/%s-%s-%s-%s-%s"%(x[0], x[1], x[2], x[3], x[4])
      link_test(term, link)

def term_test1(lst, term):
   combs = []
#   s = "%s-"
#   end_string = s*(len(lst)-1)+"%s"
   for x in itertools.permutations(lst):
      s = '-'.join(x)
      link = "/products/%s"%s
      link_test(term, link)

def test():
   item = raw_input("Item Name w/ dashes (ie: asics-gel-lyte-5-volcano): ")
   x = "/products/%s"%(item)
   Soup().scrape()
   Soup().fuzzness_test(x)
   print "The search term used was '%s'"%x
   print "The max fuzz ratio of the page links is %s"%max(fuzzy_ratios)
   global fuzz_ratios_test
   fuzz_ratios_test = []
   lst = item.split('-')
   lst1 = item.split('-')
#   print "Combinations Tested: %s"%(', '.join(map(str, lst)))
#   term_test(lst, x, item_type, color)
   print "Combinations Tested: %s"%(', '.join(map(str, lst1)))
   term_test1(lst1, x)
   fuzziness = (max(fuzz_ratios_test), min(fuzz_ratios_test)) 
   print "For combinations tested max fuzz ratio ,min fuzz ratio): (%s,%s)"%(fuzziness[0],fuzziness[1])

def get_the_shoes(x):
   print "going to the muthafuckin website"
   Kith().go_to_item_page(x)
   print "at the muthafuckin cart"
   Kith().cart()

def kith():
   item = raw_input("Item Name w/ dashes (ie: asics-gel-lyte-5-volcano): ")
   x = "/products/%s"%(item)
   global fuzzy_ratios, links
   fuzzy_ratios = []
   links = []
   User().ins()
   global browser
   browser = webdriver.Firefox()
   s = Soup()
   print "soup initialized"
   s.scrape()
   print "scraping soup"
   s.fuzzness(x)
   print "comparing values"
   i=0
   while not links:
      s.scrape()
      s.fuzzness(x)
      print "Shoe Link Not Available: Try #%s"%i
      i+=1
   else:
      y = s.link_slot()
      print get_the_shoes(y)

def set_fuzz_ratio():
   global min_fuzz
   min_fuzz = max(fuzzy_ratios)
   print "Fuzz Ratio has been set."

def quit():
   pass

def main():
   menu()
   
def kith_test():
   keywords = raw_input("Item Link (only put in what you see after shop.kithnyc.com/products/): ")
   User().ins()
   global browser
   browser = webdriver.Firefox()
   s = "/products/"+keywords
   try:
      Kith().go_to_item_page(s)
      Kith().cart()
   except IOError:
      pass
   else:
      print "Not a real product"

def menu():
   menu_text = """
You Should Complete these Steps in Order
Type Item Selection Number, then Hit Enter
1. Test Links On Site
2. Set Fuzz Ratio
3. Buy Item
4. Program Test
Type 'quit' to exit."""
   print menu_text
   x = raw_input("What would you like to do? ")
   if x=='1':
      test()
      main()
   elif x=='2':
      set_fuzz_ratio()
      main()
   elif x=='3':
      kith()
      main()
   elif x=='4':
      kith_test()
      main()
   elif x=='quit':
      quit()
   else:
      print "Do you suck at reading?"
      main()

if __name__ == "__main__":
   main()

