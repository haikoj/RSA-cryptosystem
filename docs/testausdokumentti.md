# Testausdokumentti


## Testauksen kattavuusraportti

```text
Name                           Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------------
src/generator.py                  29      0     10      0   100%
src/main.py                       42      1     10      1    96%   60
src/miller_rabin.py               24      0     16      0   100%
src/rsa.py                        11      0      2      0   100%
src/sieve_of_eratosthenes.py       8      0      6      0   100%
--------------------------------------------------------------------------
TOTAL                            114      1     44      1    99%

```


## Testauksen toteutus

Ohjelmaan on toteutettu pytest-testikehystä käyttämällä yksikkö- ja integraatiotestejä. Testikattavuutta on seurattu ja testikattavuusraportti on luotu coverage.py:n avulla. 

Yksikkötesteillä on testattu kaikkien ohjelman komponenttien toimintaa.

Integraatiotestillä `test_rsa_integ.py` varmistetaan, että avainten luominen, viestin salaaminen ja salauksen purkaminen toimivat yhdessä. 


## Testit
Testitiedostot on nimetty viittaamaan testattavaan komponenttiin. Esimerkiksi `test_generator.py` testaa tiedostoa `generator.py`.

### Yksikkötestit

`test_generator.py`

- `test_number_is_odd` testaa, että luku on pariton, eli oikeanpuolisin bitti on 1
- `test_number_is_1024_bits` testaa, että luku koostuu 1024 bitistä
- `test_number_not_divisible_with_small_primes` testaa, ettei `primegen`-funktion palauttama luku ole jaollinen pienillä alkuluvuilla
- `test_calls_miller_rabin` testaa, että Miller–Rabinia kutsutaan oikeilla parametreilla. Testissä käyetään mock-oliota Miller–Rabinin kutsumiseen. Satunnaisgeneraattorin palautusarvoksi on asetettu 131 ja Miller–Rabinin palautusarvoksi True. `primegen`-funktiota kutsutaan parametreilla [2, 3, 5]  ja bits=8. Lopuksi tarkistetaan, että Miller–Rabinia kutsuttiin kerran parametrilla (131, 40), jossa 131 on mockattu alkulukuehdokas ja 40 toistettujen kierrosten määrä.
- `test_e_is_65537` testaa, että julkinen eksponentti on oikein 
- `test_n_is_2048_bits` testaa, että moduluksen (generoitujen alkulukujen tulo) pituus on täsmälleen 2048 bittiä
- `test_encryption_and_decryption` testaa, että luotu avainpari toimii viestin salauksessa ja purkamisessa. Testissä viesti on kokonaisluku 12345 ja se salataan ja puretaan pow-funktiolla (pythoniin sisäänrakennettu modulaarinen potenssiin korotus). Testi läpäistään, jos purettu viesti täsmää viestiin 12345.
- `test_equal_primes_rejection` testaa, että moduluksen muodostama lukupari hylätään, kun sen muodostaa kaksi samaa lukua. Testissä mockataan `primegen`-funktion palauttamat luvut niin, että ensimmäisellä kierroksella molemmat luvut ovat `p = 2^1024 - 1` ja toisella luvut ovat `p` ja `q = 2^1024 - 2`. Testi tarkistaa, että `primegen`-funktiota kutsuttiin neljästi ja että modulus saatiin toisen kierroksen luvuista.
- `test_keygen_rejects_non_coprime_exponent` testaa, että lukupari hylätään, jos julkinen eksponentti e ja laskettu phi eivät ole keskenään jaottomia. `primegen`-funktion palauttamat arvot mockataan niin, että ensimmäisellä keirroksella phi on jaollinen julkisella eksponentilla 65537, eli `invalid_p = 2^1024 - 65537` ja toisella kierroksella ne ovat keskenään jaottomia. Testi tarkistaa, että `primegen`-funktiota kutsuttiin neljästi, että modulus vastaa hyväksyttyjen lukujen tuloa ja että modulaarinen käänteisluku on oikein.

`test_miller_rabin.py`

- `test_primes` testaa, että Miller–Rabin tunnistaa neljä alkulukua: 65537 ja Mersenneen suuret alkuluvut 2^107-1, 2^607-1 ja 2^4253-1.
- `test_composite_numbers` testaa, että Miller–Rabin tunnistaa neljä suurta yhdistettyä lukua: 2^1500, ja ylemmät Mersenneen alkuluvut kokonaisluvuilla kerrottuina. 
- `test_composite_numbers_without_small_prime_factors testaa`, että Miller–Rabin tunnistaa myös sellaiset yhdistetyt luvut, joilla ei ole pieniä alkutekijöitä. Testattavat neljä lukua muodostetaan kertomalla ylempiä Mersennen alkulukuja keskenään.
- `test_small_primes testaa`, että Miller–Rabinin algoritmi käsittelee pienet luvut oikein. Tääm testi on vain Miller-Rabinin algoritmia, ei koko ohjelmaa varten.

`test_rsa.py`

- `test_too_long_msg` testaa, että jos viesti on liian pitkä, ohjelma nostaa virheen

`test_sieve_of_eratosthenes.py`

- `test_primes_up_to_100` testaa, että ohjelmassa toteutettu Eratostheneen seula palauttaa kaikki alkuluvut välillä 2-100
- `test_prime_count_up_to_1_million` testaa, että Eratostheneen seula palauttaa oikean määrän alkulukuja

`test_main.py`

- `test_key_generation` testaa, että avainten generointi ja tulostaminen toimii oikein.
- `test_encrypt_message` testaa, että salausfunktiota kutsutaan oikein ja salattu viesti tulostetaan.
- `test_decrypt_message` testaa, että purkufunktiota kutsutaan oikein ja purettu viesti tulostetaan.
- `test_invalid_encryption_input` testaa, että virheellinen syöte viestin salauksessa aiheuttaa virheilmoituksen.
- `test_invalid_decryption_input` testaa, että virheellinen syöte salauksen purkamisessa aiheuttaa virheilmoituksen.
- `test_invalid_option_input` testaa, että virheellinen valikkovalinta käsitellään oikein.

### Integraatiotestit
`test_rsa_integ.py` testaa, että avainten luominen, viestin salaaminen ja salauksen purkaminen toimivat yhdessä. Testi kutsuu ensin `sieve_of_eratosthenes.py`:n `sieve`-funktiota parametrilla 10000, joka palauttaa pienet alkuluvut välillä 2-10000, ja generoi sitten 2048-bittisen RSA-avainparin `keygen`-funktiolla parametrinaan pienet alkuluvut. Viestin syötteenä käytetään viestiä, joka sisältää rivinvaihtoja, isoja ja pieniä kirjaimia ja erikoismerkkkejä. Sitten testi kutsuu `encrypt`-funktiota parametreinaan viesti ja julkinen avain. Funktio palauttaa ciphertextin, jota käytetään yksityisen avaimen kanssa parametrina `decrypt`-funktion kutsumisessa. Lopuksi testi katsoo, että purettu viesti vastaa alkuperäistä viestiä.



## Testien ajaminen

Testit voi suorittaa ohjelman juuresta seuraavilla komennolla:

`poetry run pytest`

Testikattavuusraportin saa näkyviin komennoilla:

`poetry run coverage run --branch -m pytest`

`poetry run coverage report -m`

Ja HTML-muodossa: 

`poetry run coverage html`

Testien ajamiseen kuluu aikaa noin 20 sekuntia. Tämä johtuu pitkälti test_generator.py -yksikkötesteistä, joissa ohjelman pitää generoida 1024-bittisiä alkulukuja ja 2048-bittisiä avaimia.
