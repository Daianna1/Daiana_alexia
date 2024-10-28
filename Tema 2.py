text = ("""Becali s-a arătat indignat de faptul că Dan Petrescu l-a schimbat pe atacant cu câteva zeci de secunde înainte de ultimul fluier al arbitrului, în condițiile în care l-a introdus pe teren la pauză.

Finanțatorul campioanei a reamintit că și l-a dorit mult pe Munteanu în perioada de mercato din vară, însă internaționalul U21 a ales să meargă la gruparea din Gruia, îndrumat de impresarul său, susține Gigi Becali, care a transmis în mai multe rânduri că a fost dispus să plătească două milioane de euro în schimbul vârfului.""")
jumatate_lungime = len(text) //2
text[0:jumatate_lungime]
prima_parte = text[0:jumatate_lungime]
majuscule = prima_parte.upper()
print(majuscule)
fara_spatiu = prima_parte.strip()
a_doua_parte = text[jumatate_lungime:]
inversate = text[jumatate_lungime:0:-1]
litere_mari = a_doua_parte.title()
import string
fara_semne = a_doua_parte.translate(str.maketrans(" , " , string.punctuation))
rezultate = fara_spatiu+fara_semne
print(rezultate)