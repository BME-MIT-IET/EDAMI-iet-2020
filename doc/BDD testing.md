## BDD tesztelés

### Összefoglalás
A Unit teszteléssel szemben a BDD (Behaviour Driven Testing) tesztelés
egy sokkal felhasználóbarátabb élményt nyújt mivel nem tesztelő programot
kell írni hanem csak egyszerű teszt eseteket kell definiálni könnyen olvasható
formában.

A következő könyvtárak lettek kiegészítve úgynevezett "step definition"-el:

* BFS
* Graph

aminek köszönhetően könnyedén lehet rájuk tetszőleges tesztet írni "Gherkin" nyelven.
Az ebben írt teszteket a "Behave" könyvtárral lehet lefuttatni.

### BFS step definitions
Ezek a `features/steps/bfs_definitions.py` fájlban találhatóak és a következőket
tudják:

* Négyzetrács létrehozása a `Given this grid...` kifejezéssel, ami után egy gherkin
táblázattal lehet meghatározni a négyzetrácsot (minden cella a négyzetrács megfelelő
rácspontja lesz)
* Szó lista létrehozása a `Given these words...` kifejezéssel, ami után egy gherkin
táblázatban lehet szavakat felsorolni és ezek kerülnek a listába
* Az így megadott négyzetrácsokon és szólistákon bármelyik - a BFS könyvtárban
található - függvény lefuttatása és eredményének ellenőrzése

A BFS könyvtárra létrehozott ősszes unit teszt BDD megvalósítása megtalálható a
`features/bfs_*.feature` fájlokban.

### Graph step definitions
Ezek a `features/steps/graph_definitions.py` fájlban találhatóak és a következőket
tudják:

* Gráf létrehozása a `Given these edges...` kifejezéssel, ami után egy gherkin
táblázattal lehet meghatározni a gráf éleit a kezdő és végpontjukkal
* Gráf létrehozása a `Given these weighted edges...` kifejezéssel, ami után egy
gherkin táblázattal lehet meghatározni a gráf éleit a kezdőpontjukkal,
végpontjukkal és az él súlyával
* Gráf létrehozása a `Given these connections...` kifejezéssel, ami után egy gherkin
táblázatban lehet négyzetrács szerűen megadni, hogy melyik két pont van összekötve
(minden sor és oszlop egy pontot jelent és a metszéspontjukban lévő cella az
őket összekötő él)
* Az így megadott gráfokon bármelyik - a Graph könyvtárban található -
függvény lefuttatása és eredményének ellenőrzése

A Graph könyvtárra létrehozott ősszes unit teszt BDD megvalósítása megtalálható a
`features/graph_*.feature` fájlokban.