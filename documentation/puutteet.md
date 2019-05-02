# Puutteita 

- Vain taulussa tuote on täysi CRUD. Hyllypaikoista puuttuu tietojen muokkaus ja poistaminen
- Ei monesta moneen-suhdetta tietokannassa
- Tietokannassa olevien taulujen nimet eivät mene aivan yksi yhteen koodissa olevien kanssa joissain kohdissa. Esim. tietokannassa käyttäjistä vastaa taulu "account", mutta siihen saatetaan viitata Käyttäjänä.
- Salasanoja ei kryptattu

## Huomioitavaa

- Hyllyssä olevan tuotteen kategoriaa voi muuttaa, eli jos tuotteen "Televisio" kategoria muutetaan vapaa-ajasta kotiin niin tuote on yhä osastolla (hyllypaikan attribuutti) vapaa-aika.
  - Hyllypaikat toimivat ikään kuin fyysiset lokaatiot - tuotetietojen muuttaminen ei automaattisesti vaikuta todelliseen sijaintiin

# Jatkokehitysideoita (yllä mainittujen lisäksi)

- Tuotteita voisi tunnistaa tuotekoodin lisäksi "erien" mukaan. Esim. vanhimmat erät tuotteesta poistetaan hyllypaikoista ensin ja vanhimmat varastolle saapuneet erät hyllytettäisiin ensin (ylimpänä listassa)
