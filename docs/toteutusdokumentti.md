# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelmassa on seuraavat komponentit:

`main.py`: 
Vastaa koko ohjelman toiminnasta eri komponenttien välillä. Sisältää komentorivikäyttöliittymän. Käyttöliittymässä on valikko, jossa käyttäjä valitsee joko avainparin luomisen, viestin salaamisen tai sen purkamisen.

`generator.py`:
Koostuu kahdesta eri funktiosta: `primegen` ja `keygen`. `primegen`-funktio luo alkuluvut, joita käytetään `keygen`-funktion toimesta julkisen ja yksityisen avaimen generoinnissa. 

`sieve_of_eratosthenes.py`:
`sieve` toteuttaa Eratostheneen seulan, joka generoi pienimmät alkuluvut. Näitä tarvitaan, jotta ei-alkulukuisuuden tunnistaminen `primegen`-funktiossa olisi tehokkaampaa.

`rsa.py`:
Koostuu salauksen ja purkamisen toteuttavista funktioista `encrypt` ja `decrypt`. Nämä sisältävät RSA:n keskeisimmät salaus- ja purkufunktiot.

`miller_rabin.py`:
`miller_rabin` toteuttaa Miller-Rabinin probabilistisen alkulukutestin. Testiä käytetään selvittämään, onko `primegen`-funktion luoma alkulukuehdokas alkuluku. Testi ajetaan 40 kertaa, mikä tekee siitä äärimmäisen epätodennäköistä, että testi tunnistaisi alkuluvuksi ei-alkuluvun.
