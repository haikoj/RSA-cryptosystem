# Viikkoraportti 3

Toteutin tällä viikolla ohjelman ydintoiminnot ja algoritmit. Ohjelma toimii, kaikki funktiot ovat valmiita, ja ohjelma siis käytännössä 
toiminnallisuuksiltaan valmis.

Toteutin ensin Eratosthenen seulan, joka laskee ja tallentaa pienimmät alkuluvut nopeasti. Toteutuin alkkulukujen generoinnin ja probabilistisen 
varmistuksen Miller-Rabinin avulla sille, että luodut luvut ovat alkulukuja. Toteutin 2048-bittisten avainten generoinnin RSA:n mukaisesti.
Lopuksi ydintoiminnoista implementoin vielä RSA salaus- ja purkualgoritmin. 

Ohjelmassani on toimiva komentorivikäyttöliittymä. Se ottaa ensin käyttäjältä syötteen, minkä jälkeen ohjelma ajetaan ja tulostaa sitten salatekstin 
(ciphertext) ja puretun viestin, joka on (toivottavasti) sama kuin käyttäjän itse kirjoittama viesti. Käyttöliittymä on siis hyvin yksinkertainen (syöte -> 
tuloste), mutta luulisin sen kuitenkin olevan riittävä?

Ohjelman oikein toimimisen varmistamiseksi loin yksikkötestejä ja integraatiottestin ohjelmassa käytettäville algoritmeille. Otin käyttöön testikattavuuden
seurannan. Lisäksi otin pylintin käyttöön.
En huomannut juuri lisätä kommentteja tai "docstringejä" ohjelmaani, ja tämän takia pylint antaa vielä huonon tuloksen. Tämä on yksi asia, jonka korjaan
heti seuraavalla viikolla. Tiedostot ja muuttujat kuitenkin nimesin mielestäni selkeästi, jotta ohjelman lukeminen ja ymmärtäminen on helpompaa. 

Käytän ensi viikolla työaikaa dokumentointiin. Testausdokumentissa on vasta testikattavuustaulukko. Lisäksi teen vielä loput yksikkötestit ohjelmaan.
Olen jo kiinnittänyt ohjelman tehokkuuteen huomiota, mutta katson, jos saan sitä optimoinnilla vielä nopeammaksi. Parannan ohjelman kommentointia 
työn vertaisarvioijaa ajatellen. Luulen, että aikaa jää, joten voisin ehkä ensi viikolla myös tutkia paddingia (OAEP) ja sen mahdollista toteuttamista, 
vaikka sitä ei ohjeen mukaan tarvitse toteuttaa.

Käytin tekemääni työhön tällä viikolla noin 12 tuntia.
