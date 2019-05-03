# Käyttöohje

<p>Sovelluksessa navigointi pohjautuu ylävalikkoon, josta pääsee suoraan tärkeisiin toimintoihin. Etusivulla on lyhyt kuvaus kustakin napista. Rekisteröityminen ei ole mahdollista, mutta admin voi luoda uusia käyttäjätunnuksia.</p>
<img src="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/navbar.png">

## Sisäänkirjautuminen

<p>Ennen kuin voit suorittaa mitään varastoon vaikuttavia toimintoja, täytyy sinun kirjautua sisään. Paina ylävalikon "Kirjaudu sisään"-nappia.</p>
<img src="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/kirjautuminen.png">
<p>Kirjaudu sisään omilla tunnuksillasi. Sovellus ohjaa käyttäjän takaisin etusivulle, jos sisäänkirjautuminen onnistuu.</p>

## Tuotteen elinkaari varastolla

### Uusi tuote ja hyllytys

<p>Käydään läpi tuotteisiin liittyvät toiminnot järjestyksessä. Jos tuote on varastolla uusi, niin sen tiedot täytyy ensin ottaa ylös. Paina ylävalikon nappia "Tuotesivu".</p>
<img src="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/tuotesivu1.png">
<p>Lisätäksesi uuden tuotteen, syötä sen tuotekoodi ylempään kenttään ja paina "Lisää tuote". (Huom! Täytä alempi kenttä vain jos tuotetta on jo varastolla.)</p>
<br>
<img src="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/uusituote.png">
<p>Syötä tuotteen tiedot ja paina "Luo uusi tuote". Kuvaus-kenttä on vapaaehtoinen. Lisäämisen onnistuessa sovellus palaa takaisin tuotesivulle.</p>

<br>

<p>Nyt tuote pitää hyllyttää. Paina ylävalikon nappia "Hyllytys".</p>

<img src="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/hyllytettavat.png">
<p>Sivulla on lista tuotteista jotka voidaan hyllyttää. Valitse haluamasi tuote painamalla "Hyllyyn". Siirryt uudelle sivulle jos sovellus löytää mahdollisen hyllypaikan.</p>

<img src="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/hyllyyn.png">
<p>Järjestelmä valitsi hyllytettävälle tuotteelle tyhjän hyllypaikan, joten joudut määrittämään paikalle kapasiteetin. Tämä tarkoittaa arvioimaasi määrää siitä kuinka paljon juuri hyllytettävissä olevaa tuotetta mahtuisi hyllypaikalle. Tämä on vähintään sen verran kuin olet juuri laittamassa ja enimmillään 1000000.</p> 
<p>Uusille tuotteille tulee aina määrittää kapasiteetti hyllytettäessä, mutta jos tuotetta on ennestään saldoilla niin sille saattaa löytyä jo käytössä oleva hyllypaikka. Paina "Hyllyyn".</p>

<br>

<img src="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/hyllytysonnistuu.png" height=300px>
<p>Hyllytys onnistui. Muita hyllytettäviä tuotteita ei ollut, joten sovellus ohjasi käyttäjän takaisin etusivulle.</p>

### Saldovähennys

<p>Saldovähennys tapahtuu sen hyllypaikan sivulta jota vähennys koskee. Sivulle navigoidakseen käyttäjän täytyy tietää joko vähennettävän tuotteen tuotekoodi tai hyllypaikan paikkanumero. Molemmissa tapauksissa tämä onnistuu helpoiten ylävalikon hakutoiminnolla.</p>

<img src="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/hakutoiminto.png">

<p>Syötä hakukenttään tuotekoodi tai paikkanumero, valitse hakutyyppi ja paina "Etsi".</p>

Tuotetiedot                |  Hyllypaikkatiedot
:-------------------------:|:-------------------------:
![](https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/tuotetiedot.png)  |  ![](https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/hyllypaikkatiedot.png)

<p>Tuotehaulla käyttäjä päätyy vasemmanpuoleiselle sivulle, hyllypaikkahaulla oikeaan. Tuotetietojen sivulta pääsee hyllypaikkasivulle painamalla linkkiä listasta "Hyllypaikat" siitä numerosta, jonka vastaavalta hyllypaikalta haluaa toteuttaa saldovähennyksen.</p>
<p>Käyttäjä syöttää vähennettävän määrän ja painaa "Vähennä". Jos hyllypaikka tyhjenee, niin tuotteeksi tulee "None" - hyllypaikka on nyt vapaa ja siihen voi hyllyttää muita saman osaston tuotteita.</p>

## Muuta

### Admin-toiminnot

- Admin-käyttäjä pääsee luomaan uusia normaalitason käyttäjätunnuksia, tarkastelemaan tilastoja ja luomaan hyllypaikkoja ylävalikon oikean laidan napista "Admin".

- Admin voi poistaa tuotteen pysyvästi varastolta tai siirtyä päivittämään sen tietoja <a href="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/tuotetiedot.png">tuotetietojen näkymässä</a> (toiminnallisuudet puuttuvat kuvasta)

### <a href="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/tuotesivu1.png">Tuotesivu</a>

- Käyttäjä voi <a href="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/listaus.png">listata</a> kaikkien tuotteiden tiedot painamalla tuotesivun nappia "Listaa tuotteet". Jokaisen tuotekoodin kohdalla on linkki kyseisen tuotteen omalla tuotesivulle, josta löytää myös mahdolliset hyllypaikat. Listaus sisältää myös tuotteet joiden määrä varastolla on 0.

- <a href="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/saldolisays.png">Saldolisäys</a> tehdään, kun jo varaston tietokannassa olevaa tuotetta on tullut lisää. Syötä yläkenttään tuotekoodi, alakenttään tullut määrä ja paina "Lisää saldoon". Uusi erä tuotetta täytyy hyllyttää aivan kuin muutkin tuotteet.

- <a href="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/tuotesivuhaku.png">Tuotehaun</a> voi tehdä myös tuotesivulla kirjoittamalla yläkenttään tuotekoodin ja painamalla "Hae tuotetta".

### Lokit

- Varaston tietokantaan vaikuttavista toimista, kuten uuden tuotteen lisäämisestä ja saldovähennyksestä jää tapahtumaloki tietokantaan. Kirjautunut käyttäjä näkee <a href="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/omattapahtumat.png">omat tapahtumansa</a> painamalla ylävalikon nappia "Omat tapahtumat". Hyllypaikkaan liittyviä tapahtumia voi tarkastella navigoimalla <a href="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/kayttoohjekuvat/hyllypaikkatiedot.png">hyllypaikan tietoihin</a> ja painamalla "Tapahtumat".
