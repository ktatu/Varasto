<h1>Varastojärjestelmä</h1>
<h2>https://varastojarjestelma.herokuapp.com/</h2>
<h2><a href="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/userstories.md">User stories</a></h2>

<p>
Yksinkertainen varastonhallintajärjestelmä. Järjestelmä koostuu itse varastosta (hyllypaikoista), käyttäjistä ja tuotteista. Normaalikäyttäjät voivat lisätä ja poistaa tuotteita hyllystä sekä tarkastella hylly- ja tuotetapahtumia. Admin-käyttäjät voivat lisäksi seurata käyttäjätapahtumia. 
</p>
<br>

<p>
-Tuotteen lisäys ja hyllytys:
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

