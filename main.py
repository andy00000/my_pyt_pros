from datetime import datetime, date, time

class PC:
    win_vrsz = {1: 'Win10', 2: 'Win8', 3: 'Win7', 4: 'WinXP'}
    name = '0000-SXXX'
    install_date = datetime.date(datetime.now())
    image_version = 1
    win_version = 1
    install_flag = false
    def _init_(self):
        Pass
    def get_version(self):
        return (self.image_version)
    def set_version(self, image_version):
        self.image_version = image_version


a = PC()
#print (dir(a))
a.set_version(2)
print (a.get_version())
print (a.install_date)
