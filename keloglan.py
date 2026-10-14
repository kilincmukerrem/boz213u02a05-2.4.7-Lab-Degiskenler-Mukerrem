keloglan = 3
balkiz = 5
keloglan_anasi = 6

print(keloglan, balkiz, keloglan_anasi, sep= ",")

toplam_elma = keloglan + balkiz + keloglan_anasi

print ("Keloğlan'ın elmaları:", keloglan,
       "\nBalkız'ın elmaları:", balkiz,
       "\nKeloğlan'ın Anasının Elmaları:", keloglan_anasi)

print ("Toplam Elma Sayısı:", toplam_elma)
print ("-" *40)

yenen_elma = 5
toplam_elma -= yenen_elma

print ("Bilgecan dede gelip elmalardan 5 tane yedi. \nKalan elma sayısı:", toplam_elma)
print ("-" *40)

print ("Bilgecan dede yediği elmanın 5 katı elma alıp Keloğlan'a verdi.")
print ("-" *40)

alinan_elma = yenen_elma * 5
toplam_elma += alinan_elma
print ("Mevcut Elma Sayısı:", alinan_elma)

print("Keloğlan elmaların ikisini yedi herkesin elmasını annesi ile \nbalkız arasında eşit paylaştırdı")

toplam_elma -= 2


balkiz_yeni = toplam_elma/2
keloglan_anasi_yeni = balkiz_yeni
print("Balkızın ve Keloğlanın Anası'nın elmaları:", balkiz_yeni)
