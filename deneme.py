# myapp/views.py
import pypyodbc

 # Veritabanı bağlantısını aç
DataBase = pypyodbc.connect('Driver={SQL Server};'
                      'Server=CORTANA;'
                      'Database=Company;'
                      'Trusted_Connection=True')

imlec=DataBase.cursor()

def oluştur():
  imlec.execute('create table Mustafa(denemeid tinyint,denemead varchar(28))')
  DataBase.commit()
"""



#dışarıdan ekleme için
#ekleme sqlite da @p1 ve @p2 iken burada ? var
def veriekle(id,ders):
    imlec.execute('insert into dersler values(?,?)',(id,ad))
    imlec.commit()
id=int(input(" id si girin"))
ders=input(" adı giriniz")
veriekle(id,ad)





#normal ekleme için
def veriekle():
  imlec.execute('insert into dersler values(1,'mustafa')')
  imlec.commit()


"""


#listeleme
def getir ():
  imlec.execute("select*form Department")
  liste=imlec.fetchall()
  #bunu yaparsan yan yana olur
  # print(liste)
  #bunda ise alt alta
  for i in liste:
     print(i)


"""

#güncelleme
def guncelle():
  imlec.execute("update mustafa set denemeid='2' where denemeid= '1' ")
  imlec.commit




#çıkarma
def sil():
  imlec.execute("delete from mustafa where denemeid='1'")
  imlec.commit()


eriekid=int(input("ders idsi girin"))
ders=input("ders adı giriniz")
vle(id,ders)"""

DataBase.close()