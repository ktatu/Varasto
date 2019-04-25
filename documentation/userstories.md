# User stories

## Huomioitavaa
- Kunkin SQL-lauseen kohdalla lukee ensimmäisenä metodi jossa toiminto toteutuu ja toisena hakemistopolku alkaen kansiosta application
- Kaikissa sovelluksen INSERT-lauseissa aikaleimat ovat "default"-arvoja eikä niitä itse metodeissa aseteta
- Tietokantatauluilla Loki ja Käyttäjä pääavain id inkrementoituu automaattisesti, joten jätin ne SQL-lauseista pois

## Käyttötapaukset
* Normaalikäyttäjänä voin lisätä uuden tuotteen varastoon
  - Rajoite: ei onnistu, jos tuote on järjestelmässä
  - SQL uusi tuote tauluun (luo_tuote(), tuotteet/views.py):
    ```
    INSERT INTO Tuote (luotu, muokattu, tuotekoodi, nimi, maara, kategoria, kuvaus, hyllytettava) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    ```

* Käyttäjänä voin listata kaikkien tuotteiden tiedot
  - SQL (tuotteet_indeksi(), tuotteet/views.py): 
    ```
    SELECT * FROM Tuote;
    ```

* Käyttäjänä voin hakea tietyn tuotteen tiedot tuotekoodilla
  - SQL (nayta_tuote(parametriTuote), tuotteet/views.py):
    - Parametrina annettu tuote: 
      ```
      SELECT * FROM Tuote WHERE Tuote.tuotekoodi = ? LIMIT 1;
      ```
    - Tuotteen hyllypaikat: 
      ```
      SELECT * FROM Hyllypaikka JOIN Tuote ON Tuote.tuotekoodi = Hyllypaikka.tuotekoodi 
      WHERE Hyllypaikka.tuotekoodi = ?;
      ```

* Käyttäjänä voin lisätä tuotteen saldoa tuotekoodin avulla
  - SQL (tuote_toiminnot(), tuotteet/views.py): 
    ```
    UPDATE Tuote SET maara = ? WHERE tuotekoodi = ?;
    ```

* Käyttäjänä saan järjestelmältä palautetta (flash-viestit)
  - Yrittää lisätä olemassaolevaa tuotetta
  - Yrittää hakea olematonta tuotetta
  - Yrittää lisätä tuotteen saldoon ei-positiivista määrää
  - Tuotteen saldolisäys onnistuu
  - Tuotteen hyllytys

* Käyttäjänä suorittamistani toiminnoista jää loki järjestelmään
  - Saldolisäys
    - SQL (tuote_toiminnot(), tuotteet/views.py): 
      ```
      INSERT INTO Loki (luotu, tuotekoodi, kuvaus, account_id) 
      VALUES (current_timestamp(), ?, "saldopäivitys määrä ?", ?); 
      ```
  - Saldovähennys
    - SQL (reduction(), hyllypaikat/views.py): 
      ```
      INSERT INTO Loki (luotu, tuotekoodi, kuvaus, account_id, paikkanumero) 
      VALUES (current_timestamp(), ?, "saldovähennys ? paikkanumero ?", ?, ?);
      ```
  - Tuotelisäys
    - SQL (luo_tuote(), tuotteet/views.py): 
      ```
      INSERT INTO Loki (luotu, tuotekoodi, kuvaus, account_id) 
      VALUES (current_timestamp(), ?, "tuotelisäys määrä ?", ?);
      ```
  - Hyllytys
    - SQL (product_to_shelf(tuotekoodi, paikkanumero), hyllypaikat/views.py): 
      ```
      INSERT INTO Loki (luotu, tuotekoodi, kuvaus, account_id, paikkanumero) 
      VALUES (current_timestamp(), ?, "hyllysiirto määrä ? paikkanumero ?", ?, ?);
      ```
  
* Käyttäjänä joudun kirjautumaan sisään järjestelmään, jotta voin tehdä muutoksia
  - SQL käyttäjätunnusten etsintä (auth_login(), auth/views.py): 
    ```
    SELECT * FROM Kayttaja WHERE username = ? AND password = ?;
    ```

* Käyttäjänä voin tarkastella omia tapahtumiani
  - Ylälaidan nappi "Tapahtumat"
  - SQL-kysely listaa kirjautuneen käyttäjän attribuutista "lokit" löytyvät rivit (user_logs(), lokit/views.py):
    ```
    SELECT lokit FROM Kayttaja WHERE id = ?
    ```
  
* Käyttäjänä voin hyllyttää tuotteita
  - Rajoite: järjestelmä etsii samasta kategoriasta (osasto) hyllypaikan
  - SQL sopivan hyllypaikan etsintä (find_shelf_location(tuote), hyllypaikat/models.py):
    - Tarkistetaan löytyykö paikkaa missä on kyseistä tuotetta ja tilaa:
      ```
      SELECT paikkanumero, maara FROM hyllypaikka 
      WHERE Hyllypaikka.tuotekoodi = ? AND Hyllypaikka.maara + ? <= kapasiteetti LIMIT 1;
      ```
    - Jos ei löytynyt paikkaa edellisellä kyselyllä, etsitään tyhjä paikka:
      ```
      SELECT paikkanumero FROM hyllypaikka WHERE osasto = ? AND maara = 0 LIMIT 1;
      ```
  - SQL tuotteen attribuutti "hyllytettava" nollataan ja muokkausajankohta päivitetään (sama metodi):
    ```
    UPDATE Tuote SET hyllytettava = 0, muokattu = current_timestamp() WHERE tuotekoodi = ?;
    ```
  - SQL tuote hyllypaikalle (sama metodi):
    ```
    UPDATE Hyllypaikka SET tuotekoodi = ?, muokattu = current_timestamp(), kapasiteetti = ?, maara = ? 
    WHERE paikkanumero = ?;
    ```

* Adminina voin luoda uusia normaalitason käyttäjätunnuksia
  - SQL uusi käyttäjä tauluun (create_user(), auth/views.py):
    - Tarkistetaan ensin onko username käytössä:
      ```
      SELECT * FROM Kayttaja WHERE username = ?;
      ```
    - Jos username vapaa:
      ```
      INSERT INTO Kayttaja (nimi, username, password) VALUES ( ?, ?, ?);
      ```

* Käyttäjänä voin tehdä saldovähennyksen hyllypaikalta
  - Vähentää myös tuotteen kokonaissaldoa
  - SQL haetaan parametrien osoittamat hyllypaikka ja tuote (reduction(paikkanumero, tuotekoodi), hyllypaikat/views.py):
    ```
    SELECT * FROM Hyllypaikka WHERE paikkanumero = ?;
    ```
    ```
    SELECT * FROM Tuote WHERE tuotekoodi = ?;
    ```
  - SQL jos hyllypaikka tyhjennettiin (sama metodi):
    ```
    UPDATE Hyllypaikka SET maara = 0, kapasiteetti = 0, tuotekoodi = NULL WHERE paikkanumero = ?;
    ```
  - SQL jos hyllypaikalle jäi tavaraaa (sama metodi):
    ```
    UPDATE Hyllypaikka SET maara = Hyllypaikka.maara - ? WHERE paikkanumero = ?;
    ```
  - SQL saldovähennys otetaan huomioon myös tuotteen kokonaissaldossa (sama metodi):
    ```
    UPDATE Tuote SET maara = Tuote.maara - ? WHERE tuotekoodi = ?;
    ```
