<h1>Varastojärjestelmä</h1>
<h2>https://varastojarjestelma.herokuapp.com/</h2>
<h2><a href="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/userstories.md">User stories</a></h2>
<h3>Heroku: Käyttäjänimi = testi salasana = kayttaja</h3>
<h3>Päivitys: Osa 3</h3>
Uudet tietokantataulut sovelluksesssa: Loki ja Varasto. Jokaisesta käyttäjän tuotteisiin tai hyllypaikkoihin kohdistuvasta toimesta syntyy loki. Varaston toiminnallisuudet työn alla.

Ohjaajapalautteen myötä muokkasin tietokantakaaviota. User ja Loki ovat irrallaan Tuotteesta ja Varastosta - en keksinyt tapaa linkittää näitä, sillä en keksi mitään käyttöä yhteyksille. Jokaisesta käyttäjän varastoon tai tuotteisiin vaikuttavasta toimesta kuitenkin syntyy loki.

Etapissa haluttiin CRUD-toiminnallisuus, mutta en pystynyt vielä toteuttamaan tätä haluamallani tavalla. Tuotteiden saldovähennys tulee tapahtumaan hyllypaikkojen avulla - hyllystä vähennetään tuotetta ja tuotteen kokonaismäärä Tuote-tietokantataulussa myös vähenee. Varastoimisen toteutus ei ole vielä valmis.

<h2>Kuvaus</h2>
<p>
Yksinkertainen varastonhallintajärjestelmä. Järjestelmä koostuu itse varastosta (hyllypaikoista), käyttäjistä ja tuotteista. Normaalikäyttäjät voivat lisätä ja poistaa tuotteita hyllystä sekä tarkastella hylly- ja tuotetapahtumia. Admin-käyttäjät voivat lisäksi seurata käyttäjätapahtumia. 
</p>
<br>

<p>
Tuotteen lisäys ja hyllytys:
</p>
<p>
Järjestelmä kysyy käyttäjältä lisättävän tuotteen tuotekoodia ja tarkastaa onko se uusi tuote. Mikäli tuote on entuudestaan tuttu ja sitä on hyllyssä, ehdottaa järjestelmä tuotteen nykyistä hyllypaikkaa jos siinä on tilaa, muutoin käyttäjä valitsee itse hyllypaikan. (tuotteet varastoidaan kategorioittain). Täysin uudesta tuotteesta käyttäjä kirjaa ylös tuotetiedot ennen hyllypaikan valintaa. 
</p>

<p>
Alustavat luokat:
</p>
<ul>
 <li>Kayttaja</li>
 <li>Tuote</li>
 <li>Varasto</li>
 <li>Loki</li>
</ul>

<p>
Alustavat toiminnot:
</p>
<ul>
 <li>Sisäänkirjautuminen</li>
 <li>Tuotteen lisäys</li>
 <li>Tuotteen poisto</li>
 <li>Tuotteen hyllytys</li>
 <li>Tuotteen poisto hyllystä</li>
 <li>Tapahtumaloki: tuoteseuranta</li>
 <li>Tapahtumaloki: käyttäjävalvonta</li>
 <li>Tapahtumaloki: hyllypaikan tapahtumahistoria</li>
</ul>

