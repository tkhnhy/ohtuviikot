Copilot osasi selittää koodiin tehdyt muutokset lyhyesti ja selkeästi.
Se tunnisti että koodi oli jaettu pienempiin metodeihin ja muuttujat nimetty uudelleen.
Se osasi ehdottaa yhden hyvän sovelluksen logiikkaan vaikuttavan parannuksen käyttää >=, > sijasta
joka mahdollisesti vaikuttaisi sovelluksen toiminnallisuuteen tapauksissa, joita testit eivät 
ehkä käyneet läpi. Testit suorittivat tämän muutoksen jälkeen, joten comittasin sen. 
Copilot myös ehdotti muita muutoksia pelaajien nimien käyttämiseen liittyen väittäen, että nykyinen rikkoisi testit, vaikka tämä
ei ollut tapaus, kun suoritin testit omalla koneellani. Jätin nämä ehdotuksen committaamatta, sillä jos pelaajalla olisi jokin 
muu nimi kuin player1 tai player2, ei sovellus näiden ehdotusten jälkeen toimisi toivotusti.