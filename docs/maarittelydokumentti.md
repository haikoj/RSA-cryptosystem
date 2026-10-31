# Määrittelydokumentti

## Perustiedot

**Ohjelmointikieli:** Python  
**Riippuvuuksien hallinta:** Poetry  
**Muut ohjelmointikielet vertaisarviointeja varten:** C, Java, JavaScript  
**Dokumentaatiossa käytetty kieli:** suomi  
**Opinto-ohjelma:** tietojenkäsittelytieteen kandidaatti (TKT)  

## Ongelma
Työssä ratkaistava ongelma liittyy viestien turvalliseen salaamiseen ilman että lähettäjällä ja vastaanottajalla on yhteistä salaista avainta. RSA on epäsymmetristä salausta käyttävä salausmenetelmä, joka mahdollistaa salatun viestinvaihdon lähettäjän ja vastaanottajan välillä. Salausalgoritmi perustuu siihen, että kuka tahansa voi salata viestin vastaanottajan julkisella avaimella, mutta vain vastaanottaja voi purkaa salauksen käyttämällä omaa salaista ja yksityistä avaintaan. Yksityistä avainta ei voi käytännössä myöskään johtaa julkisesta avaimesta nykyisillä menetelmillä.

## Pääydin
Projektin ideana on toteuttaa RSA-salausalgoritmi, joka mahdollistaa viestien salaamisen ja purkamisen. Tavoitteena on generoida vähintään 2048-bittisiä RSA-avaimia. Työssä toteutetaan algoritmeja, joita tarvitaan RSA:n avainten luomiseen, ja käytetään modulaariseen potenssiinkorotukseen perustuvaa salausta ja purkamista.

## Toteutettavat algoritmit 
Projektissa totetutetaan **RSA:n avaingeneraattori** (keygen) sekä **salaus** (encryption) ja **purkaminen** (decryption).    

Avaingenerointia varten toteutan itse seuraavat algoritmit: **Miller–Rabin**, **Eratostheneen seula**, **Eukleideen algoritmi**, **Laajennettu Eukleideen algoritmi**.  

Miller–Rabin-algoritmia tarvitaan auttamaan suurten lukujen alkuluvuiksi tunnistamisessa. Eratostheneen seulaa käytetään pienten alkulukujen generoimiseen, jotta voidaan tunnistaa suuret luvut, jotka ovat jaollisia pienillä alkuluvuilla. Eukleiden algoritmia käytetään tarkistamaan, että julkinen eksponentti e ja Eulerin funktio φ(n) ovat keskenään jaottomia. Sen laajennettua versiota käytetään yksityisen eksponentin d laskemiseen.  

## Syötteet
Käyttäjä valitsee ensin pituuden avaimille, jonka on oltava vähintään 2048 bittiä. Sitten käyttäjä kirjoittaa tekstisyötteen, joka ei ylitä avaimen sallimaa pituutta.  
Ohjelma saa tämän jälkeen syötteenä kyseisen viestin ja ohjelman generoiman julkisen avaimen, jolla viesti salataan. Salauksen purkamiseen ohjelma saa tämän salatun viestin sekä yksityisen avaimen. 

## Tavoitteena olevat aika- ja tilavaativuudet
**Miller–Rabin:** Aikavaativuus O(t log³ n), tilavaativuus O(1)  
**Eratostheneen seula:** Aikavaativuus O(n log log n), tilavaativuus O(n)  
**Eukleideen algoritmi ja laajennettu:** Aikavaativuus O(log min(a, b)), tilavaativuus O(1) iteratiivisena toteutuksena  
**RSA-salaus:** Aikavaativuus O(k² log e), tilavaativuus O(k)  
**RSA-purkaminen:** Aikavaativuus O(k² log d), tilavaativuus O(k)  

## Lähteet
- [Handbook of Applied Cryptography, by A. Menezes, P. vanOorschot, and S. Vanstone, CRC Press, 1996. Chapter 4](https://cacr.uwaterloo.ca/hac/about/chap4.pdf)
- [Cryptography Academy - The RSA Cryptosystem](https://cryptographyacademy.com/rsa/)
- [CP-Algorithms - Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)
- [Wikipedia - RSA Cryptosystem](https://en.wikipedia.org/wiki/RSA_cryptosystem)

