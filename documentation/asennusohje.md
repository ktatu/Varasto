# Asennusohje

Ennen kuin teet mitään muuta varmista että koneellasi on python asennettuna (testattu vain versiolla 3.6.7). Ohje on tarkoitettu Ubuntulle, mutta sovelluksen saa testatusti toimimaan myös <a href="https://gitforwindows.org/">Windowsilla</a>. Jotkut kansioiden ja tiedostojen nimet saattavat kuitenkin olla eriävät.

## Sovelluksen käyttöönotto paikallisesti

Kaikki asennusohjeen komennot suoritetaan hakemistossa tsoha

1. Lataa repositorion .zip <a href="https://github.com/ktatu/Varastojarjestelma">etusivulta</a> ja pura se 
2. Luo virtuaaliympäristö komennolla ```python -m venv venv``` (saattaa myös olla python3 -m venv venv)
3. Aktivoi virtuaaliympäristö komennolla ```source venv/bin/activate```. <strong>Tee tämä aina kun haluat käyttää sovellusta paikallisesti.</strong>
   - Komento ```deactivate``` sammuttaa virtuaaliympäristön
4. Asenna riippuvuudet komennolla ```pip -r requirements.txt```

Sovelluksen pitäisi nyt käynnistyä komennolla ```python run.py```. Käynnistä sovellus kerran, jotta tietokanta alustuu ennen kuin jatkat.

### Admin-tunnukset

Sovelluksen toimintoja varten tarvitaan käyttäjätunnukset. Syötä seuraavat lauseet komentorivillä, alkaen hakemistosta tsoha:
1. ```sqlite3 application/varasto.db```
2. ```INSERT INTO account (nimi, username, password, rooli) VALUES ('nimi', 'username', 'password', 'ADMIN');```
   - Voit itse valita sanan VALUES jälkeen tulevat arvot nimi, username ja password. Muista kuitenkin laittaa hipsut (') sanojen ympärille.
3. Sulje sqlite komennolla ```.exit```

Sovelluksen pitäisi nyt toimia niin kuin pitääkin. Käynnistä komennolla python run.py ja avaa haluamallasi selaimella. Oletussijainti on http://127.0.0.1:5000/

## Tietokanta verkossa (Postgresql ja Heroku)

### Heroku käyttöön

Tarvitset heroku-tunnukset sekä herokun <a href="https://devcenter.heroku.com/articles/heroku-cli">komentorivi-työkalut</a>. Jos et forkannut repositoriota niin git pitää myös olla alustettuna sovelluksen hakemistossa.

Sovelluksen paikan luominen herokuun onnistuu komennolla:
```heroku create omasovellus```, missä "omasovellus" kuvaa valitsemaasi nimeä. Liitä Herokun sovellus myös paikalliseen versionhallintaan (gittiin): ```git remote add heroku https://git.heroku.com/omasovellus.git```.

Lähetä sovelluksesi paikallinen versio Herokuun:
```
git add .
```
```
git commit -m "1. commit"
```
```
git push heroku master
```

### Postgresql

Komentoriville:
```
heroku config:set HEROKU=1
```
```
heroku addons:add heroku-postgresql:hobby-dev
```

Herokusta käynnistettäessä sovellus hyödyntää psgql:ää, paikallisesti käynnistettäessä sqliteä. Joudut muokkaamaan application-kansion tiedostoa __init__.py, jos haluat muuttaa tätä. <a href="https://materiaalit.github.io/tsoha-19/osa3/">Materiaalin osan 3 kappaleen 4</a> tutkiminen voi auttaa asiassa.

Psql:ssä ei myöskään ole valmiiksi käyttäjätunnuksia, vaan ne täytyy tehdä itse. Ylläoleva materiaalin linkki auttaa myös tässä.
