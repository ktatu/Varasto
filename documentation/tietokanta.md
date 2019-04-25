# Tietokanta

## Tietokantakaavio

### Huomioitavaa

- Tauluissa Tuote ja Hyllypaikka esiintyy samoja piirteitä attribuuteissa, mutta kyse ei kuitenkaan ole denormalisoinnista:
  - Molemmissa on sarake "määrä", mutta Tuotteen määrä viittaa sen kokonaissaldoon ja Hyllypaikan määrä kyseisessä paikassa olevaan määrään. Samaa tuotetta voi olla useassa eri hyllypaikassa
  - Kyseisten taulujen sarakkeet "kategoria" ja "osasto" viittaavat myös samaan asiaan, vain eri nimellä. Tarkoituksena on ohjata tuotteiden sijoittamista hyllypaikoille - kategorian "vapaa-aika" tuotteet menevät menevät hyllypaikoille, jotka kuuluvat osastoon "vapaa-aika" jne<br>
  
<img src="https://github.com/ktatu/Varastojarjestelma/blob/master/documentation/tietokantakaavio.png">

## CREATE TABLE-lauseet

    CREATE TABLE tuote (
      tuotekoodi INTEGER NOT NULL,
      luotu DATETIME,
      muokattu DATETIME,
      nimi VARCHAR(144) NOT NULL,
      maara INTEGER NOT NULL,
      kategoria VARCHAR(100) NOT NULL,
      kuvaus VARCHAR(200), 
      hyllytettava INTEGER,
      PRIMARY KEY (tuotekoodi));
  
    CREATE TABLE account (
      id INTEGER NOT NULL,
      nimi VARCHAR(144) NOT NULL,
      username VARCHAR(144) NOT NULL,
      password VARCHAR(144) NOT NULL,
      rooli VARCHAR(20) NOT NULL,
      PRIMARY KEY (id));
    
    CREATE TABLE hyllypaikka (
      paikkanumero INTEGER NOT NULL,
      muokattu DATETIME,
      osasto VARCHAR(20) NOT NULL,
      tuotekoodi INTEGER,
      maara INTEGER NOT NULL,
      kapasiteetti INTEGER,
      PRIMARY KEY (paikkanumero),
      FOREIGN KEY(tuotekoodi) REFERENCES tuote (tuotekoodi));
      
    CREATE TABLE loki (
      id INTEGER NOT NULL,
      luotu DATETIME,
      tuotekoodi INTEGER NOT NULL,
      kuvaus VARCHAR(20) NOT NULL,
      account_id INTEGER NOT NULL,
      paikkanumero INTEGER,
      PRIMARY KEY (id),
      FOREIGN KEY(tuotekoodi) REFERENCES tuote (tuotekoodi),
      FOREIGN KEY (account_id) REFERENCES account (id),
      FOREIGN KEY (paikkanumero) REFERENCES hyllypaikka (paikkanumero));
