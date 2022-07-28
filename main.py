from PyQt5 import uic, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class Interface():
    def __init__(self):
        
        main_window = 'interfaces/main_window.ui'
       
        self.first_page = uic.loadUi(main_window)
        self.first_page.pushButton.clicked.connect(self.bot)
        
    def get_number(self):
        cellphone = self.first_page.cellphone_number.text()
        return cellphone
    
    def get_mensage(self):
        mensage = self.first_page.mensage.text()
        return mensage
 
        
        
        
    def bot (self):
        self.browser = webdriver.Chrome()
        ('https://web.whatsapp.com/')
        cellphone_number = self.get_number()
        mensage_to_send = self.get_mensage()       
                

        self.link = f"https://web.whatsapp.com/send?phone={cellphone_number}&text={mensage_to_send}"

        self.browser.get(self.link)

        while len(self.browser.find_elements_by_id("side")) < 1:
            # O navegador vai aguardar o whats até que o elemento "side" seja renderizado após o logon
            time.sleep(1)

        self.browser.find_element_by_xpath(
                                            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(
                                                Keys.ENTER
        )#Será feito a busca do elemento da mesagem e logo após apertará o enter


        
app=QtWidgets.QApplication([])        
start_interface = Interface()  


start_interface.first_page.show()
app.exec()