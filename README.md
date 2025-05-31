# rmk_praktika
Praktika testülesanne

Ülesanne: Rita works in RMK Tallinn office. She takes the Tallinn city bus number 8 from Zoo to Toompark (names of bus stops) to get to work.
Rita has a meeting at 9:05 sharp every day from Monday to Friday. It takes her 300 seconds to walk from home to the departure bus stop and 240 seconds to walk from the destination bus stop to the meeting room.
Plot the probability of Rita being late to the meeting depending on the time she leaves home. (Assuming she can only use the bus to get to work.)

Paneme kirja andmed:
- Rita jalutab kodust bussipeatusesse 5 minutit (300 sekundit).
- Ta jalutab Toomparki jõudes kontorisse 4 minutit (240 sekundit).
- Koosolek hakkab 9:05

Otsustasin, et ei seo oma koodi reaalajaliste andmete või käsitsi korjatud infoga bussi nr 8 liikumise kohta, vaid võtan vaatluse alla MINIMAALSE ja MAKSIMAALSE aja, et Rita tööle jõuab. Selle abil on mul võimalik nende MIN ja MAX piiride vahel luua lugematul arvul simulatsioone ja see võimaldab mul teha graafiku, mis arvestab (peaaegu) igat võimalikku olukorda. PS! Selles lahenduses ei ole arvestatud Tallinna linna igaastaste "kevadekuulutajate" ehk teetööde ja muu sellisega, mis võiks veel liikumise aega mõjutada. 

Võtan vaatluse alla avalikud andmed bussi nr 8 kohta ja jälgin ajavahemikku kella 8 ja 9 vahel (nagu ülesande näidisgraafikul kujutatud):
Täpsustan, et bussigraafikul mainitud lubatud hilinemine (+- 2 min) on siin ülesandes arvestatud vaid selliselt, et kuigi buss võib peatusesse jõuda 2 min varem, siis väljub ta alati õigel kellaajal. Seega koodis arvestan +2 min just hilinemisena ehk maksimaalse aja alla.

Minimaalne aeg:

Oletame, et Rita kõnnib kogu aeg täpselt samal kiirusel ning peatusesse jõudmiseks ja uuest peatusest kontorisse kõndimiseks kulub alati vastavalt 5 ja 4 min. Selleks, et tööle jõudmise aeg oleks minimaalne, jõuab Rita bussipeatusesse, kuhu kohe saabub minutipealt buss, mis jõuab kiireima ajaga Toompargi peatusesse.
Vähim aeg uues bussi saabumiseks on 0 min.
Vähim aeg Zoo peatusest Toompargi peatusesse jõudmiseks on 13min.

Maksimaalne aeg:

Oletame, et Rita kõndimise ajad on taaskord 5 ja 4 min, kuid peatusesse jõudes lahkub just buss ning Rita peab ootama järgmist. Siinkohal tuleks arvestada suurimat aega, mis kulub uue bussi saabumiseks (vaatan bussigraafikult) ning arvestada ka hilinemisega peatusesse (oletame selleks +2 min).

Suurim aeg uue bussi saabumiseks on 12 min (+ 2min)
Suurim aeg Zoo peatusest Toompargi peatusesse jõudmiseks on 14 min (+ 2min)


Simulatsioon käivitub iga minut alates 08:00 kuni 09:00. Iga kodust lahkumise ajahetke kohta teostatakse 10 000 juhuslikku simulatsiooni (Monte Carlo meetod), et hinnata hilinemise tõenäosust.

Pythoni kood: (lisatud on numpy, matplotlib ja datetime, timedelta paketid)

(PS! Kasutasin Tehisintellekti abi ülesande lahendamisel. Tema andis idee, et proovida Monte Carlo meetodit (meetodit õppisin Youtube-st) ning aitas defineerida funktsiooni minu etteantud tingimustel)

Merilin Tkatšenko
