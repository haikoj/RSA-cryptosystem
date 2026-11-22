# Viikkoraportti 4

Viimeistelin yksikkötestit ohjelmalleni. Mittautin testikattavuuden, joka on 97%. Testien pitkä (n. 15s) suoritusaika tuli yllätyksenä, mutta en lähtenyt
sen takia muokkaamaan tai optimoimaan testejä, koska itse testien tehokkuudella ei taida olla lopulta ohjelman toteutuksen kannalta niin suurta 
merkitystä, etenkin kun suoritusaika on sekunteja eikä minuutteja. Lisäsin docstringit jokaiselle funktiolle ja lisäsin kommentteja helpottamaan ohjelman
ymmärtämistä. Siivosin pylintin antaman palautteen perusteella koodia. Tarkistin pylintillä koodini laadun, joka on tällä hetkellä pois lukien testit 10/10.  

Paransin ohjelman käyttöliittymää palautteen perusteella luomalla valikon, jossa on vaihtoehdot avaimen generoimiselle, viestin salaamisella ja 
purkamiselle. Ohjelma tulostaa nyt käyttäjälle avaimet, ciphertextin ja puretun viestin. Valikon ansiosta käyttäjä voi nyt kokeilla muualla muodostettuja
avaimia tässä ohjelmassa tai käyttää tässä ohjelmassa luotuja avaimia toisessa RSA-ohjelmassa. 

Valmistelin tällä viikolla testausdokumentin, jossa kirjoitin testien toteutuksesta, yksityiskohtaisesti jokaisesta testistä sekä annoin ohjeet testien
suorittamiseen. Aloitin myös toteutusdokumentin kirjoittamisen. Dokumentissa on nyt kirjattuna ohjelman yleisrakenne komponentteineen.

Arviolta käytin viikon 4 työhön noin 12 tuntia. Aikaa kului eniten testien toteuttamiseen. Käytin aikaa myös paddingin opiskeluun, mutta tämä osuus on 
vielä keskeneräinen. Seuraavalla viikolla käytän vertaisarvioinnin lisäksi aikaa toteutusdokumentin täyttämiseen, johon pitää täyttää vielä ainakin aika-
ja tilavaativuudet, kielimallien käyttö ja lähteet.  
