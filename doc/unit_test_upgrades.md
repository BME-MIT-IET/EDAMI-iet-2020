## Unit tesztek írása és kiegészítése

### Összefoglalás
A projekthez eredendően járt egy test suite, de annak a lefedettsége igencsak
hiányos volt, mivel sok egységre igaz volt legalább egy az alábbiak közül:

* a tesztje nem a tesztek között, hanem a saját kódjában volt
* a tesztje az általános használatot lefedte, edge case-eket viszont nem
* szimplán nem írtak hozzá tesztet
* rossz osztályt vagy függvényt használtak a teszteléskor

Ezeket a hibákat javítottam több modulban is. A legtöbb változtatást a `set`, a
`dp`, és az `arrays` modulokban ejtettem.

### Menedzsment
A munkát három ágon végeztem el, elszeparálva a `set`, a `dp`, és a többi modul
tesztjeinek kiegészítését. Ezekből született az alábbi három pull request,
melyek review után bekerültek a főágra.

* [PR#9: Set test suite](https://github.com/BME-MIT-IET/EDAMI-iet-2020/pull/9)
* [PR#10: DP test suite](https://github.com/BME-MIT-IET/EDAMI-iet-2020/pull/10)
* [PR#11: Miscellaneous test suites](https://github.com/BME-MIT-IET/EDAMI-iet-2020/pull/11)

Emellett nem találtam szükségesnek több külön issue-t felvenni ehhez a munkához,
így az egész [egy issue alatt van](https://github.com/BME-MIT-IET/EDAMI-iet-2020/issues/12),
ehhez van hozzárendelve a három PR.

### Eredmények
Habár a globális kódlefedettség csak pár százalékot ugrott, a feldolgozott
modulokra leosztott növekmény már sokkal szembetűnőbb. A lefedettségben
legtöbbet javuló modulok az alábbiak:

* DP: 52.45% -> 80.21%
* Queues: 73.65% -> 91.67%
* Set: 8.00% -> 98.53%

Forrás: coveralls.io ([előtte](https://coveralls.io/builds/30845535), [utána](https://coveralls.io/github/BME-MIT-IET/EDAMI-iet-2020))
