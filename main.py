from PyQt5 import uic, QtWidgets
import re
import webbrowser


class Interface():
    def __init__(self):
        main_window = 'interfaces/main_window.ui'
        self.first_page = uic.loadUi(main_window)
        self.first_page.pushButton.clicked.connect(self.bot)
        self.first_page.toolButton.clicked.connect(self.open_git)
        
        
    def get_number(self):
        cellphone = self.first_page.cellphone_number.text()
        
        
        return cellphone
    
    
    def get_message(self):
        message = self.first_page.mensage.text()
        
        
        return message
    
   
    def str_formater(self, string):
        number_without_space = str(string).strip()
        number_without_especial_char = re.sub('[^A-Za-z0-9]+', '', number_without_space)
        
        
        return number_without_especial_char
    
    
    def bot (self):
        contry_code = '55'
        cellphone_number = contry_code+self.str_formater(self.get_number())
        message_to_send = self.get_message()
        try:
            self.link = f"https://web.whatsapp.com/send?phone={cellphone_number}&text={message_to_send}"
            webbrowser.open_new_tab(self.link)
                                            
        except:
            pass


    def open_git(self):
        webbrowser.open_new_tab('https://github.com/vbsx')
        
        
app=QtWidgets.QApplication([])        
start_interface = Interface()
start_interface.first_page.show()
app.exec()