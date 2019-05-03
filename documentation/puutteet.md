# Puutteita 

- Vain taulussa tuote on täysi CRUD. Hyllypaikoista puuttuu tietojen muokkaus ja poistaminen
- Ei monesta moneen-suhdetta tietokannassa
- Salasanoja ei kryptattu
- Aivan kaikista toiminnoista ei synny lokeja (mm. kun admin poistaa tuotteen)
- Tuotetta tyhjälle hyllypaikalle hyllytettäessä kapasiteetin voi määrittää alhaisemmaksi kuin mitä ollaan juuri hyllyttämässä.
  - Tarkoittaa sitä että hyllypaikalle ei voi hyllyttää enempää tuotteita ennen kuin se tyhjenee

## Huomioitavaa

- Hyllyssä olevan tuotteen kategoriaa voi muuttaa, eli jos tuotteen "Televisio" kategoria muutetaan vapaa-ajasta kotiin niin tuote on yhä osastolla (hyllypaikan attribuutti) vapaa-aika.
  - Hyllypaikat toimivat ikään kuin fyysiset lokaatiot - tuotetietojen muuttaminen ei automaattisesti vaikuta todelliseen sijaintiin

# Jatkokehitysideoita (yllä mainittujen lisäksi)

- Tuotteita voisi tunnistaa tuotekoodin lisäksi "erien" mukaan. Esim. vanhimmat erät tuotteesta poistetaan hyllypaikoista ensin ja vanhimmat varastolle saapuneet erät hyllytettäisiin ensin (ylimpänä listassa)
