#python script to send whatsapp message using whatsapp web
# Developer: satishkushwah50@gmail.com

#requirement to use it (on windows)
#  1.  run 'pip install selenium' in cmd
#  2.  download chromedriver for windows
#  3.  whatsapp account 
# update class name of various elements if changed by inspecting elements

#change as per location of chrome driver in ur machine not required if driver is in same directory of this script but better to put path
driverpath='D:\\softwares\\chromedriver_win32\\chromedriver' #dont forget quotes 
try:
	from selenium import webdriver
	from selenium.common.exceptions import NoSuchElementException #raise exceptions when contact not found
except:
	print('Please wait, we are installing selenium on your machine...')
	from pip._internal import main as pipmain
	pipmain(['install', 'selenium'])
	try:
		from selenium import webdriver
		from selenium.common.exceptions import NoSuchElementException #raise exceptions when contact not found
	except:
		input("selenium not installed, run 'pip install selenium' command in cmd, press enter to exit and run script again after installation")
		quit()
import time
print('\n\n1. SCAN THE QR CODE AND DO NOT PRESS ANY KEY UNTIL NEXT INSTRUCTION, ignore lines stating errors if any\n\n')
try:
	driver = webdriver.Chrome('chromedriver')
except:
	driver = webdriver.Chrome(driverpath)
driver.get('https://web.whatsapp.com/')
input('\n\n2. PRESS ENTER KEY TO CONTINUE, after Whatsapp Webpage is fully loaded, ignore lines stating errors if any\n\n')
while(1):
	flag=1 # flag to check whether contact is in ur phone or not
	name = input('Enter name of contact or group or q to quit (case sensitive): ')
	if name=='q' or name=='Q': # exit the program
		break
	contactsearchbox=driver.find_element_by_class_name('jN-F5') #search box class name, update if required
	contactsearchbox.clear() #clear search box
	contactsearchbox.send_keys(name) #enter name to search box
	print('searching.........'+name)
	time.sleep(2) # wating 2 sec
	try:
		recipient = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	except NoSuchElementException:
		print('No contact or Group found with name: '+name)
		flag=0
	if flag==1:
		choice=input('contact found, send message? Y/N: ')
		if choice=='y' or choice=='Y':
			recipient.click() #select the contact
			count=input('Send same msg how many times? ')
			try:
				count=int(count)
			except:
				print('sending 1 time')
				count=1
			msg = input('Enter your message: ')	
			msg_box = driver.find_element_by_class_name('_2S1VP') #class name may change, update if required
			msg_box.clear()
			for i in range(count):
				msg_box.send_keys(msg)
				try:
					button = driver.find_element_by_class_name('_35EW6') # class name may change, update if required
				except NoSuchElementException:
					print('no messsage typed or class name changed of send button')
					continue
				button.click()
			print('message send successfully')
input('\n\nPRESS ENTER KEY TO EXIT THE PROGRAM\n\n')
driver.close()