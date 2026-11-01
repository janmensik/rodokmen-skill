# Přímí předci podle Kekulého čísel: 1 = výchozí osoby (děti Kryštof a Tea Menšíkovi),

# otec osoby n má číslo 2n (2 = Jan Menšík), matka 2n+1 (3 = Julie Menšík Čákiová),

# 4–7 prarodiče dětí (rodiče Jana a Julie), 8–15 praprarodiče dětí (prarodiče Jana a Julie)…

#

# JEDNOTNÁ STRUKTURA OSOBY (stejná u předků v P i u bočních příbuzných ve SIDE → "vetev"; popis v tools/fakta.py):

#   n      jméno (tituly patří sem, ne do faktů)

#   y      jen roky: "* 1895", "1890–1944", "asi 1720–1785", "1857 – po 1914", "† před 1888"; plná data patří do f

#   f      události v pořadí  "* datum místo"  →  "× datum místo manžel/ka"  →  "† datum místo",

#          pak ostatní volné údaje (čí syn/dcera, poznámky)

#   roz    rodné příjmení      zam    povolání / postavení      bydl   bydliště

#   puvod  odkud pochází       pohreb místo pohřbu              vztah  (boční příbuzní) vztah k linii

#   st, r, note  stav, klíče zápisů, poznámka



P = {

    # 0. generace – děti Jana a Julie

    1: dict(n="Kryštof, Tea, Hynek a Jonáš Menšíkovi", y="* 2010–2017", st="fam", sex="M",
            f=["Kryštof Adam Menšík (* 20. 3. 2010 Praha)",
               "Tea Apolena Menšíková (* 14. 2. 2013 Praha)",
               "Hynek Albert Menšík (* 10. 7. 2015 Praha)",
               "Jonáš Alex Menšík (* 5. 12. 2017 Praha)",
               "domov v Libčicích nad Vltavou"],
            bydl="Libčice nad Vltavou", puvod="Praha",
            deti=[
                dict(n="Kryštof Adam Menšík", y="* 2010", sex="M",
                     f=["* 20. 3. 2010 Praha", "domov v Libčicích nad Vltavou"],
                     bydl="Libčice nad Vltavou", puvod="Praha", r=[],
                     note="Nejstarší syn Mgr. Jana Menšíka a Mgr. Julie Menšík Čákiové. Narozen 20. 3. 2010 v Praze, žije v Libčicích nad Vltavou."),
                dict(n="Tea Apolena Menšíková", y="* 2013", sex="F",
                     f=["* 14. 2. 2013 Praha", "domov v Libčicích nad Vltavou"],
                     bydl="Libčice nad Vltavou", puvod="Praha", r=[],
                     note="Dcera Mgr. Jana Menšíka a Mgr. Julie Menšík Čákiové. Narozena 14. 2. 2013 v Praze, žije v Libčicích nad Vltavou."),
                dict(n="Hynek Albert Menšík", y="* 2015", sex="M",
                     f=["* 10. 7. 2015 Praha", "domov v Libčicích nad Vltavou"],
                     bydl="Libčice nad Vltavou", puvod="Praha", r=[],
                     note="Syn Mgr. Jana Menšíka a Mgr. Julie Menšík Čákiové. Narozen 10. 7. 2015 v Praze, žije v Libčicích nad Vltavou."),
                dict(n="Jonáš Alex Menšík", y="* 2017", sex="M",
                     f=["* 5. 12. 2017 Praha", "domov v Libčicích nad Vltavou"],
                     bydl="Libčice nad Vltavou", puvod="Praha", r=[],
                     note="Nejmladší syn Mgr. Jana Menšíka a Mgr. Julie Menšík Čákiové. Narozen 5. 12. 2017 v Praze, žije v Libčicích nad Vltavou.")
            ],
            r=[],
            note="Čtyři děti Mgr. Jana Menšíka a Mgr. Julie Menšík Čákiové, narozené v Praze, žijící v Libčicích nad Vltavou."),

    # 1. generace – rodiče (Jan a manželka Julie)

    2: dict(n="Mgr. Jan Menšík", y="* 1980", st="fam",

            f=["* 7. 1. 1980 Praha", "× 12. 9. 2009 Zvíkov Mgr. Julie Menšík Čákiová"],

            zam="právník", bydl="Libčice nad Vltavou (od roku 2009)", r=[],

            note="Výchozí osoba rodokmenu, manžel Mgr. Julie Menšík Čákiové (sňatek 12. 9. 2009 Zvíkov). Vystudoval Právnickou fakultu Univerzity Karlovy v Praze (Mgr.), dříve Gymnázium Buďánka a SŠ Nad Štolou. Od roku 2009 žije v Libčicích nad Vltavou."),

    3: dict(n="Mgr. Julie Menšík Čákiová", y="* 1979", st="fam",

            f=["* 22. 5. 1979 Praha", "× 12. 9. 2009 Zvíkov Mgr. Jan Menšík"],

            roz="Čákiová", bydl="Libčice nad Vltavou (od roku 2009)", r=[],

            note="Mgr., roz. Čákiová, manželka Mgr. Jana Menšíka (sňatek 12. 9. 2009 Zvíkov). Narozena v Praze, od roku 2009 žije v Libčicích nad Vltavou."),



    # 2. generace – prarodiče dětí (rodiče Jana a rodiče Julie)

    4: dict(n="Ing. Radim Menšík", y="1946–2021", st="fam",

            f=["* 13. 9. 1946 Praha", "× asi 1972 Praha Ing. Zdeňka Jarolímová", "† 15. 1. 2021 Praha", "pohřben 27. 1. 2021 Praha"],

            zam="inženýr", r=[], note="Ing. Radim Menšík, otec Jana a Jakuba Menšíkových. Syn doc. RNDr. Miroslava Menšíka a MUDr. Ludmily Menšíkové. Narozen v Praze, sňatek s Ing. Zdeňkou Jarolímovou kolem roku 1972 v Praze."),

    5: dict(n="Ing. Zdeňka Menšíková", y="* 1949", st="fam",

            f=["* 6. 5. 1949", "× asi 1972 Praha Ing. Radim Menšík"],

            roz="Jarolímová", zam="inženýrka dopravy (GŘ ČD, MDČR)", bydl="Praha 6 (Pod Beránkou)", r=[],

            note="Ing., roz. Jarolímová, matka Jana a Jakuba Menšíkových. Dcera Richarda Jarolíma (1927–2012) a Zdenky roz. Holánkové (* 1928). Působila na Ministerstvu dopravy a na Českých drahách. Žijící v Praze 6."),

    6: dict(n="JUDr. Miloslav Čáki", y="* 1947", st="fam",

            f=["* 1. 6. 1947 Vlčice (u Trutnova)", "× PhDr. Eva Krejzková"],

            zam="právník (JUDr., Ministerstvo financí ČR)", bydl="Praha 4 - Háje (Hviezdoslavova); v dětství Červeněves čp. 88", r=[],

            note="Právník (JUDr.), působil na Ministerstvu financí ČR, manžel PhDr. Evy Čákiové. Narozen ve Vlčicích u Trutnova, dětství prožil v Červeněvsi čp. 88 (syn Juraje Čákiho a Marie roz. Bubancové ze Slovenska)."),

    7: dict(n="PhDr. Eva Čákiová", y="* 1946", st="fam",

            f=["* 1. 11. 1946 Rychnov nad Kněžnou", "× JUDr. Miloslav Čáki"],

            roz="Krejzková", bydl="Praha 4 - Háje (Hviezdoslavova), Vrabsko; v dětství Žamberk", r=[],

            note="PhDr., roz. Krejzková, manželka JUDr. Miloslava Čákiho, dcera MUDr. Miroslava Krejzka a MUDr. Věry roz. Černé. Narozena v Rychnově nad Kněžnou, dětství prožila v Žamberku."),



    # 3. generace – praprarodiče dětí / prarodiče Jana a Julie (8–13)

    8: dict(n="doc. RNDr. Miroslav Vladimír Menšík", y="1906–1968", st="doc",

            f=["* 3. 8. 1906 Praha (křest u Nejsv. Trojice v Podskalí)", "× MUDr. Ludmila Menšíková", "† 12. 1. 1968 Praha"],

            zam="docent deskriptivní geometrie a fotogrammetrie na Stavební fakultě ČVUT; vedoucí redaktor Rozhledů matematicko-fyzikálních (1956–1968)",

            r=["podskali_krest_miroslav_mensik_1906"], note="Matematik, vysokoškolský docent deskriptivní geometrie a fotogrammetrie na Stavební fakultě ČVUT, autor učebnic a vědeckých prací. Narozen 3. 8. 1906 v Praze na Novém Městě čp. 1717 (pokřtěn 9. 8. 1906 u Nejsv. Trojice v Podskalí jako Miroslav Vladimír). Syn Františka Menšíka (* 1873 Jistebnice) a Pavlíny roz. Jirkovské (* 1882 Praha). Z matčiny strany byli jeho bratranci z druhého kolena slavní bratři Linhartové – hrdinové protinacistického odboje v čele s Bedřichem Linhartem (popraveným 1944 na Pankráci) a radiotelegrafistou vysílačky Sparta I Otto Linhartem."),

    9: dict(n="MUDr. Ludmila Menšíková", y="1909–2007", st="doc",
            f=["* 22. 8. 1909 Praha (křest u sv. Apolináře)",
               "× 1. asi 1935 MUDr. Pech",
               "× 2. 1940–1942 doc. RNDr. Miroslav Menšík",
               "† 2007 Praha", "pohřbena Olšanské hřbitovy (část 006, odd. 7a, hrob 134)"],
            roz="Pivničková", zam="dětská lékařka (pediatr)",
            bydl="Praha 6 - Hradčany (Pod baštami 277/4), dříve Dejvice (Vítězné nám. 1)",
            r=["jindrich_oddani_jan_pivnicka_1908"],
            note="MUDr. Ludmila Menšíková, roz. Pivničková, poprvé provdaná Pechová. Dětská lékařka v Praze, manželka doc. RNDr. Miroslava Menšíka, matka Radima a Ivana Menšíkových. Narozena 22. 8. 1909 v Praze (dle křestního výtahu u sv. Apolináře), dcera učitele měšťanské školy na Hradčanech Jana Emanuela Pivničky a Emmy Marie roz. Tomíčkové. V roce 1928 maturovala na reálném gymnáziu v Bubenči, v roce 1934 promovala na Lékařské fakultě UK v Praze (MUDr.). Působila v Krči, Nemocnici Německý Brod, Plzni a v Dejvicích. Zemřela v roce 2007 a je pohřbena v rodinném hrobě na Olšanech spolu se svou matkou Emmou Pivničkovou. V rodinné paměti se uchoval tragický odkaz příbuzného jménem Linhart, popraveného za války v Praze – jednalo se o Bedřicha Linharta (* 1886, popraven 20. 10. 1944 na Pankráci), bratrance její tchyně Pavlíny Menšíkové roz. Jirkovské."),

    10: dict(n="Richard Jarolím", y="1927–2012", st="fam",

             f=["* 26. 3. 1927 Žleby čp. 17", "× 30. 10. 1948 Rumburk Zdenka Holánková", "† 24. 3. 2012 Hradec Králové"],

             bydl="Hradec Králové",

             r=[], note="Narozen ve Žlebech čp. 17 jako syn Emilie Jarolímové (* 1899 Žleby čp. 37) a Fridricha Hůlka. Nesl rodné příjmení své matky Jarolím, navazující na obuvnické kořeny dědečka Jana Jarolíma (1863–1903) a pradědečka Josefa Jarolíma ve Žlebech. S manželkou Zdenkou roz. Holánkovou prožil život v Hradci Králové, kde zemřel 24. 3. 2012 ve věku 84 let; dědeček Jana z matčiny strany."),

    11: dict(n="Zdenka Jarolímová", y="* 1928", st="fam",

             f=["* 20. 11. 1928 Hluboká čp. 36", "× 30. 10. 1948 Rumburk Richard Jarolím"],

             roz="Holánková", bydl="Hradec Králové",

             r=[], note="Narozena v Hluboké čp. 36 u Krucemburku jako dcera zámečníka Julia Holánka (* 1889 Staré Ransko) a Sofie roz. Henzlové (* 1904 Hluboká). Propojila tradiční železářský a hamernický rod Holánků z Ranska se selským rodem Henzlů z Hluboké. S manželem Richardem Jarolímem žili v Hradci Králové. Dožila se požehnaného věku 92 let († 10. 1. 2021); babička Jana z matčiny strany."),

    12: dict(n="Juraj (Jiří) Čáki", y="* 1919", st="doc",
             f=["* 13. 4. 1919 Dúbrava čp. 42 (okres Snina)", "× Marie Bubancová",
                "syn roľníka Andreje Čakyho (* 5. 3. 1891 Dúbrava) a Maryi (* 21. 10. 1896 Strihovce, sobáš 15. 4. 1918)",
                "vnuk Júlie Čakyové (* 15. 9. 1868 Strihovce, ovdověla 5. 10. 1926 v Dúbravě po dědkovi Čakym)",
                "sourozenci v Dúbravě: Michal (* 1922), Marya (* 1925), Wasil (* 1927), Júlia (* 1930)",
                "bratr Miroslav Čáky se narodil později po r. 1930",
                "příjmení v matrikách a sčítání: Čaky / Čáki / Csáky"],
             puvod="Dúbrava čp. 42 (okres Snina, Zemplín)", bydl="Červeněves čp. 88 (dříve Dúbrava čp. 42)",
             r=["dubrava_scitanie_1930_caki_juraj"],
             note="Dědeček Julie Čákiové z otcovy strany (otec JUDr. Miloslava Čákiho, uváděn též jako Jiří Čáki / Čaky). Narozen 13. 4. 1919 v Dúbravě čp. 42 v okrese Snina na Zemplíně jako nejstarší syn řeckokatolického roľníka Andreje Čakyho (* 5. 3. 1891) a Maryi roz. ze Strihoviec (* 21. 10. 1896). Rodina byla řeckokatolického vyznání a slovenské národnosti. Podle sčítání lidu 1930 žil v Dúbravě čp. 42 s rodiči, babičkou Júlií (* 1868) a sourozenci Michalem, Maryou, Wasilem a sestrou Júlií (* 14. 6. 1930, po níž nese křestní jméno jeho vnučka Mgr. Julie Menšík Čákiová!). Později přesídlil do Čech a žil v Červeněvsi čp. 88 u Smidar."),

    13: dict(n="Marie Čákiová", y="* 1919 / 1922", st="doc",
             f=["* cca 1919–1924 (Šmigovec / Dúbrava, okres Snina)", "× Juraj (Jiří) Čáki"],
             roz="Bubancová", puvod="Šmigovec (příp. Dúbrava, okres Snina)", bydl="Červeněves čp. 88",
             r=["smigovec_scitanie_1930_bubanec_cp_10", "smigovec_scitanie_1930_bubanec_cp_34"],
             note="Babička Julie Čákiové z otcovy strany (matka JUDr. Miloslava Čákiho). Rozená Bubancová (v úředních sčítacích operátech 1930 psáno Búbanec / Búbancová), původem ze Šmigovce v okrese Snina (kde rod Búbanec vlastnil řadu usedlostí, mj. čp. 10 a čp. 34). Nejpravděpodobnější kandidátky ze sčítání lidu 1930 podle věkové shody s manželem Jurajem (* 1919): Marie Búbancová * 21. 11. 1919 v Šmigovci čp. 10 (dcera Vasila Búbance * 1878 a Anny roz. z Ladomírova * 1883), nebo Maria Búbancová * 8. 9. 1922 v Šmigovci čp. 34 (dcera Andreje Búbance * 1875 a Anny * 1882)."),

    14: dict(n="MUDr. Miroslav Krejzek", y="1914–1978", st="doc",
             f=["* 3. 9. 1914 Bystřice nad Pernštejnem č. p. 147", "× MUDr. Věra Černá", "† 27. 5. 1978 Žamberk",
                "maturita 7. 6. 1933 Tišnov (reálné gymnázium)",
                "promoce 23. 6. 1939 Praha (Lékařská fakulta UK, MUDr.)",
                "syn mistra kolářského Otakara Krejzka a Františky roz. Sýsové z Bystřice n. P. č. p. 147 / 433",
                "měl 5 bratrů (Ladislav * 1905, Otakar ml., Bedřich, MUDr. Emil * 1910, MUDr. Václav * 1919)"],
             zam="lékař (MUDr.), primář plicního oddělení a hrudní chirurg v léčebně Albertinum v Žamberku",
             bydl="Žamberk (Habrmanova čp. 627); dříve Bystřice nad Pernštejnem č. p. 147, Hradec Králové, Nymburk",
             puvod="Bystřice nad Pernštejnem",
             r=["cuni_doktori_miroslav_krejzek_1939", "bystrice_oddani_vaclav_krejzek_1949"],
             note="Lékař (MUDr.), významný český ftiseolog a hrudní chirurg, dlouholetý primář plicního oddělení v léčebně Albertinum v Žamberku. Narozen 3. 9. 1914 v Bystřici nad Pernštejnem č. p. 147 (předměstí Nové Dvory, po přečíslování čp. 433) jako čtvrtý ze šesti synů mistra kolářského Otakara Krejzka a Františky roz. Sýsové (dcery hajného Leopolda Sýse z Borovníka). Po maturitě na reálném gymnáziu v Tišnově (1933) vystudoval Lékařskou fakultu Karlovy univerzity v Praze (promoce 23. 6. 1939). Za války pracoval na chirurgické klinice prof. Jana Bedrny v Hradci Králové a na chirurgii v nemocnici v Nymburce (kde poznal svou manželku MUDr. Věru Černou z Poděbrad). V dubnu 1945 se při noční službě v Nymburce nakazil těžkou formou tuberkulózy od vězňů z koncentračních táborů transportovaných vlaky. Po zotavení nastoupil v březnu 1946 do Albertina v Žamberku, kde vybudoval moderní hrudní chirurgii a provedl tisíce plicních operací. Dne 7. 4. 1949 byl spolu s bratrem MUDr. Emilem Krejzkem svědkem na svatbě nejmladšího bratra Václava na Starém Brně (tehdy bydlel v Žamberku v Habrmanově ulici čp. 627). Zemřel 27. 5. 1978 v Žamberku."),

    15: dict(n="MUDr. Věra Krejzková", y="1917–2005", st="doc",
             f=["* 8. 2. 1917 Poděbrady", "× MUDr. Miroslav Krejzek", "† 7. 11. 2005 Žamberk",
                "dcera Josefa Černého a Marie roz. Měšťánkové z Poděbrad"],
             zam="lékařka (MUDr.), primářka v léčebném ústavu Albertinum v Žamberku",
             bydl="Žamberk; dříve Poděbrady",
             roz="Černá", puvod="Poděbrady",
             r=["podebrady_oddani_josef_cerny_1911", "koncice_krest_marie_mestankova_1885"],
             note="Lékařka (MUDr.), ftiseoložka a primářka v odborném léčebném ústavu Albertinum v Žamberku, manželka MUDr. Miroslava Krejzka, matka PhDr. Evy Čákiové a MUDr. Ivy Gajdošové (babička Julie). Narozena 8. 2. 1917 v Poděbradech jako dcera mistra kovářského Josefa Černého a Marie roz. Měšťánkové. Po boku manžela MUDr. Miroslava Krejzka působila po desetiletí v Žamberku."),



    # 4. generace – pradědečci a prababičky (16–23, 30)

    16: dict(n="František Xaver Menšík", y="* 1873", st="doc",

             f=["* 8. 7. 1873 Jistebnice čp. 56", "× 8. 5. 1902 Praha (Týnský chrám) Pavlína Rosalie Jirkovská"],

             zam="c. k. policejní strážník v Praze, poštovní úředník / kancista",

             bydl="Praha I čp. 12 (1902), Staré Město čp. 78, Nové Město čp. 355",

             puvod="Jistebnice č. 56",

             r=["tyn_oddani_frantisek_mensik_1902", "jistebnice_krest_frantisek_mensik_1873"],

             note="Narozen 8. 7. 1873 v Jistebnici čp. 56 jako manželský syn pekaře Josefa Menšíka a Marie roz. Šmedlové. Dne 8. 5. 1902 oddán u Týna s Pavlínou Jirkovskou."),

    17: dict(n="Pavlína Rosalie Menšíková", y="* 1882", st="doc",

             f=["* 2. 11. 1882 Praha I čp. 12", "× 8. 5. 1902 Praha (Týnský chrám) František Menšík"],

             roz="Jirkovská", bydl="Praha I čp. 12", puvod="Praha",

             r=["tyn_krest_pavlina_jirkovska_1882", "tyn_oddani_frantisek_mensik_1902"],

             note="Narozena 2. 11. 1882 v Praze I čp. 12 (pokřtěna 12. 11. 1882 v Týnském chrámu). Dcera kamnáře Aloise Jirkovského a Aloisie roz. Tiché. Dne 8. 5. 1902 oddána u Týna s Františkem Menšíkem. Její kmotrou při křtu byla teta Pavlína Berta Linhartová roz. Jirkovská (* 1854), jejíž synové (vlastní bratranci Pavlíny) Bedřich, Zdeněk, Václav a Otto Linhartovi vytvořili jednu z nejstatečnějších rodin protinacistického odboje (vysílačka Sparta I, Obrana národa, Tři králové); Bedřich Linhart byl v říjnu 1944 popraven v pražské sekyrárně na Pankráci."),
    18: dict(n="Jan Emanuel Pivnička", y="1872 – po 1921", st="doc",
             f=["* 14. 1. 1872 Praha Nové Město čp. 1356 (křest u sv. Štěpána)",
                "× 27. 4. 1908 Praha (kostel sv. Jindřicha) Emma Marie Tomíčková",
                "vystoupil z církve 15. 2. 1921 (Magistrát čj. 3738 C)"],
             zam="definitivní učitel měšťanské chlapecké školy na Hradčanech (dříve u Panny Marie Sněžné)",
             bydl="Praha IV - Hradčany čp. 277 (Pod baštami 4), dříve Malá Strana čp. 196 a 623",
             puvod="Praha Nové Město",
             r=["stepan_krest_jan_pivnicka_1872", "jindrich_oddani_jan_pivnicka_1908"],
             note="Definitivní učitel měšťanské chlapecké školy na Hradčanech. Narozen 14. 1. 1872 v Praze na Novém Městě čp. 1356 (pokřtěn 21. 1. 1872 u sv. Štěpána). Syn mistra krejčovského Josefa Pivničky (rodem z Čechtic) a Antonie roz. Grubnerové z Dobříše. Dne 27. 4. 1908 oddán u sv. Jindřicha s Emmou Marií Tomíčkovou. V roce 1921 vystoupil z církve římskokatolické."),
    19: dict(n="Emma Marie Pivničková", y="1886–?", st="doc",
             f=["* 7. 4. 1886 Warta čp. 59 (Stráž nad Ohří)",
                "× 27. 4. 1908 Praha (kostel sv. Jindřicha) Jan Emanuel Pivnička",
                "pohřbena Olšanské hřbitovy (část 006, odd. 7a, hrob 134)"],
             roz="Tomíčková", bydl="Praha IV - Hradčany čp. 277, dříve Kamenné Žehrovice čp. 164",
             puvod="Warta (Stráž nad Ohří u Hauenštejnu, okres Kadaň)",
             r=["jindrich_oddani_jan_pivnicka_1908"],
             note="Manželka Jana Emanuela Pivničky a matka MUDr. Ludmily Menšíkové. Narozena 7. 4. 1886 ve Wartě čp. 59 (dnes Stráž nad Ohří u hradu Hauenštejn, okres Kadaň). Dcera c. k. železničního přednosty stanice Hauenstein-Warta Antonína Tomíčka a Anny roz. Halíkové z Lobče čp. 63. Pohřbena v rodinném hrobě na Olšanech spolu s dcerou Ludmilou. V rodině Jana Menšíka je pamatována jako „paní Pivničková“ (babička otce Ing. Radima Menšíka), u níž rodina na Hradčanech (Pod baštami 277/4) pobývala."),



    # Pokračování 4. generace (20–23, 30)

    20: dict(n="Fridrich Hůlek", y="", st="fam",

             f=[], zam="lesní inženýr", r=[],

             note="Údaje z rodinného stromu PDF (datum a místo narození zatím neuvedeny; syn Richard nesl příjmení matky Jarolím)."),

    21: dict(n="Emilie Jarolímová", y="1899 – po 1927", st="doc",

             f=["* 15. 4. 1899 Žleby čp. 37", "† po 1927"],

             zam="dělnice",

             r=["zleby_krest_emilie_jarolimova_1899"],

             note="Narozena 15. 4. 1899 ve Žlebech čp. 37 v podzámčí jako dcera obuvnického tovaryše Jana Jarolíma (1863–1903) a Antonie roz. Havlové (* 1857). Pravnučka učitele Ignáce Jeřábka z Čachotína. Matka Richarda Jarolíma (* 1927 Žleby čp. 17). Později provdána za Rudolfa Kačoura; prababička Jana Menšíka."),

    22: dict(n="Julius Holánek", y="1889–1952", st="fam",

             f=["* 20. 7. 1889 Staré Ransko čp. 55", "× 20. 5. 1926 Sofia Henzlová", "† 1952"],

             zam="zámečník", r=[],

             note="Narozen ve Starém Ransku čp. 55 jako syn hamerníka a kováře Františka Holánka a Julie roz. Šímové. V duchu rodové tradice raneckých hutníků se vyučil zámečníkem a kovářem. V květnu 1926 se oženil se Sofií Henzlovou (* 1904), dcerou truhláře a hostinského Franze Henzla z Hluboké (věkový rozdíl manželů byl 15 let). Žil v Hluboké čp. 36; pradědeček Jana Menšíka."),

    23: dict(n="Sofia Henzlová", y="1904–1985", st="fam",

             f=["* 8. 5. 1904 Hluboká čp. 38", "× 20. 5. 1926 Julius Holánek", "† 1985"], r=[],

             note="Narozena v Hluboké jako dcera truhláře a hostinského Franze Henzla z rodového gruntu čp. 15 v Hluboké a Aloisie roz. Pospíchalové z Radostína. V květnu 1926 se provdala za zámečníka Julia Holánka ze Starého Ranska a žili v Hluboké čp. 36. Maminka Zdenky Jarolímové roz. Holánkové (* 1928); prababička Jana Menšíka."),

    24: dict(n="Andrej Čáki", y="* 1891", st="doc",
             f=["* 5. 3. 1891 Dúbrava čp. 42 (okres Snina)", "∞ 15. 4. 1918 Marya ...",
                "otec Juraje (Jiřího) Čákiho (* 1919)",
                "syn ... Čákiho († 1926) a Júlie (* 1868)",
                "příjmení v záznamech: Čaky / Čáki"],
             zam="roľník v Dúbravě čp. 42",
             bydl="Dúbrava čp. 42 (okres Snina, Zemplín)", puvod="Dúbrava čp. 42",
             r=["dubrava_scitanie_1930_caki_juraj"],
             note="Řeckokatolický roľník v Dúbravě čp. 42 v okrese Snina na Zemplíně, otec Juraje (Jiřího) Čákiho a dědeček JUDr. Miloslava Čákiho (pradědeček Julie). Narozen 5. 3. 1891 v Dúbravě čp. 42. Dne 15. 4. 1918 se oženil s Maryou pocházející ze sousedních Strihoviec (* 1896). Spolu hospodařili na rodové usedlosti čp. 42 a v roce 1930 měli děti: Juraj (* 1919, dědeček Julie), Michal (* 1922), Marya (* 1925), Wasil (* 1927) a novorozenou Júlii (* 1930). V domácnosti s nimi žila i jeho ovdovělá matka Júlie (* 1868)."),

    25: dict(n="Marya Čákiová", y="* 1896", st="doc",
             f=["* 21. 10. 1896 Strihovce (okres Snina)", "∞ 15. 4. 1918 Andrej Čáki (Čaky)",
                "matka Juraje (Jiřího) Čákiho (* 1919)",
                "přistahována do Dúbravy čp. 42 po sňatku 15. 4. 1918"],
             roz="", bydl="Dúbrava čp. 42 (dříve Strihovce)", puvod="Strihovce (okres Snina, Zemplín)",
             r=["dubrava_scitanie_1930_caki_juraj"],
             note="Řeckokatolická hospodyně v Dúbravě čp. 42, matka Juraje (Jiřího) Čákiho a babička JUDr. Miloslava Čákiho (prababička Julie). Narozena 21. 10. 1896 ve Strihovcích v okrese Snina na Zemplíně. Dne 15. 4. 1918 se provdala za roľníka Andreje Čákiho (Čakyho) a přistahovala se do Dúbravy čp. 42. Ve sčítání lidu 1930 doložena s manželem, pěti dětmi a tchýní Júlií."),

    28: dict(n="Otakar Jan Krejzek", y="1877 – po 1949", st="doc",
             f=["* 6. 5. 1877 Blažkov čp. 20 (pokřtěn 10. 5. 1877 farářem Ferd. Císařem)",
                "× před 1905 Františka Sýsová", "† po 7. 4. 1949",
                "otec primáře MUDr. Miroslava Krejzka a jeho 5 bratrů (Ladislav, Otakar ml., Bedřich, MUDr. Emil, MUDr. Václav)"],
             zam="mistr kolářský na Nových Dvorech u Bystřice nad Pernštejnem č. p. 147 (později č. p. 433)",
             bydl="Bystřice nad Pernštejnem č. p. 147 / č. p. 433 (Nové Dvory)", puvod="Blažkov čp. 20",
             r=["cuni_doktori_miroslav_krejzek_1939", "bystrice_oddani_emil_krejzek_1943", "bystrice_oddani_vaclav_krejzek_1949", "blazkov_krest_otakar_krejzek_1877"],
             note="Mistr kolářský v Bystřici nad Pernštejnem na předměstí Nové Dvory č. p. 147, po přečíslování č. p. 433 (doložen v Adresářích Republiky Československé 1931–1939 i v oddacích zápisech synů z let 1943 a 1949). Narozen 6. května 1877 v Blažkově čp. 20 v rodině evangelického rolníka Václava Krejska a Marie rozené Hamříkové. S manželkou Františkou rozenou Sýsovou (dcerou hajného Leopolda Sýse z Borovníka) vychovali šest synů: Ladislava (* 1905, odborný učitel v Bystřici n/P. čp. 451), Otakara ml. (* cca 1908–1909, učitelský ústav v Brně, poručík pěšího pluku 31 v Jihlavě), Bedřicha (* cca 1909–1910, učitelský ústav v Brně), MUDr. Emila (* 11. 10. 1910 Bystřice n/P., praktický lékař v Bystřici n/P.), MUDr. Miroslava (* 3. 9. 1914 Bystřice n/P., primář Albertina v Žamberku) a MUDr. Václava (* 25. 3. 1919 Bystřice n/P., lékař)."),

    29: dict(n="Františka Krejzková", y="asi 1880 – po 1949", st="doc",
             f=["* asi 1880–1885", "× před 1905 Otakar Krejzek", "† po 7. 4. 1949",
                "dcera hajného Leopolda Sýse z Borovníka",
                "matka primáře MUDr. Miroslava Krejzka a jeho 5 bratrů"],
             roz="Sýsová",
             bydl="Bystřice nad Pernštejnem č. p. 147 / č. p. 433 (Nové Dvory)", puvod="Borovník",
             r=["cuni_doktori_miroslav_krejzek_1939", "bystrice_oddani_emil_krejzek_1943", "bystrice_oddani_vaclav_krejzek_1949"],
             note="Rozená Sýsová, dcera hajného Leopolda Sýse z Borovníka. Manželka mistra kolářského Otakara Krejzka v Bystřici nad Pernštejnem na Nových Dvorech č. p. 147 / 433, matka šesti synů včetně primáře MUDr. Miroslava Krejzka a praktického lékaře MUDr. Emila Krejzka (prababička Julie). Doložena v univerzitní matrice doktorů Karlovy univerzity (1939) a v oddacích zápisech synů Emila (1943) a Václava (1949), které odhalily její rodné příjmení Sýsová a otce Leopolda Sýse, hajného z Borovníka. V dubnu 1949 byla římskokatolického vyznání a naživu."),

    30: dict(n="Josef Černý", y="* 1886", st="doc",
             f=["* 16. 2. 1886 Poděbrady č. 15/II", "× 14. 6. 1911 Poděbrady Marie Měšťánková"],
             zam="mistr kovářský v Poděbradech na Zámostí čp. 15/II",
             bydl="Poděbrady č. 15/II", puvod="Poděbrady",
             r=["podebrady_oddani_josef_cerny_1911", "podebrady_oddani_jan_cerny_1885"],
             note="Mistr kovářský v Poděbradech na Zámostí (čp. 15/II). Narozen 16. 2. 1886 v Poděbradech jako syn kováře Jana Černého a Anny roz. Hromadové z Chvalovic. Dne 14. 6. 1911 byl v Poděbradech oddán s Marií Měšťánkovou z Končic. Otec lékařky MUDr. Věry Krejzkové roz. Černé (pradědeček Julie)."),

    31: dict(n="Marie Černá", y="1885–1972", st="doc",
             f=["* 13. 12. 1885 Končice čp. 14", "× 14. 6. 1911 Poděbrady Josef Černý", "† 25. 10. 1972 Žamberk (léčebna Albertinum)"],
             roz="Měšťánková", zam="v domácnosti, dříve obchodnice",
             bydl="Poděbrady č. 13/II a 15/II, v závěru života Žamberk",
             puvod="Končice čp. 14 (farnost Žiželice)",
             r=["koncice_krest_marie_mestankova_1885", "podebrady_oddani_josef_cerny_1911"],
             note="Narozena 13. 12. 1885 v Končicích čp. 14 (pokřtěna 20. 12. 1885 v kostele sv. Prokopa v Žiželicích) jako dcera rolníka Josefa Měšťánka a Kateřiny roz. Ouzké. Dne 14. 6. 1911 se v Poděbradech provdala za mistra kovářského Josefa Černého. Matka lékařky MUDr. Věry Krejzkové roz. Černé (prababička Julie). V říjnu 1921 vystoupila z římskokatolické církve a přestoupila k Církvi československé. V závěru života žila v Žamberku u rodiny své dcery a zetě primáře Miroslava Krejzka; zemřela 25. 10. 1972 v Albertinu v Žamberku ve věku nedožitých 87 let."),



    # 5. generace – praprarodiče (32–35, 42–47)

    32: dict(n="Josef Menšík", y="* 1832", st="doc",

             f=["* 18. 3. 1832 Jistebnice čp. 156", "× 31. 1. 1865 Jistebnice Marie Šmedlová"],

             zam="pekař v Jistebnici čp. 156 a 56", puvod="Jistebnice",

             r=["jistebnice_krest_josef_mensik_1832", "jistebnice_krest_frantisek_mensik_1873", "jistebnice_oddani_josef_mensik_1865"],

             note="Mistr pekařský v Jistebnici čp. 156 a 56. Narozen 18. 3. 1832 v Jistebnici čp. 156 (pokřtěn 20. 3. 1832 kaplanem P. Fabriciem Dvořákem). Syn pekaře Josefa Menšíka a Barbory roz. Horychové. Oddán 31. 1. 1865 v Jistebnici s Marií Šmedlovou."),

    33: dict(n="Marie Menšíková", y="* 1835", st="doc",

             f=["* 18. 6. 1835 Jistebnice čp. 48", "× 31. 1. 1865 Jistebnice Josef Menšík"],

             roz="Šmedlová", puvod="Jistebnice",

             r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_krest_frantisek_mensik_1873", "jistebnice_oddani_josef_mensik_1865"],

             note="Narozena i pokřtěna 18. 6. 1835 v Jistebnici čp. 48. Dcera Antonína Šmedly, punčocháře a pozdějšího kostelníka v Jistebnici čp. 48, a Františky roz. Šebelové z Vlasenic."),

    34: dict(n="Alois Jirkovský", y="* 1859", st="doc",

             f=["* 7. 4. 1859 Praha (křest u sv. Haštala)", "× 19. 1. 1885 Praha (Týnský chrám) Aloisie Marie Tichá"],

             zam="kamnář v Praze", bydl="Praha I čp. 12",

             r=["hastal_krest_alois_jirkovsky_1859", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882", "tyn_oddani_frantisek_mensik_1902"],

             note="Kamnářský dělník a kamnář v Praze na Starém Městě čp. 12. Narozen 7. 4. 1859 v Praze (pokřtěn ve farnosti sv. Haštala). Syn Františka Jirkovského, hrnčířského tovaryše v Praze (rodilého z Kutné Hory) a Aloisie roz. Franzové z Prahy. Oddán 19. 1. 1885 u Týna s Aloisií Marií Tichou. Jeho sestra Pavlína Berta Jirkovská (* 1854) se v roce 1883 provdala za mlynářského Jana Linharta a stala se matkou odbojářů bratří Linhartových."),

    35: dict(n="Aloisie Marie Jirkovská", y="* 1858", st="doc",

             f=["* 12. 7. 1858 Praha Nové Město čp. 501 (křest u sv. Apolináře)", "× 19. 1. 1885 Praha (Týnský chrám) Alois Jirkovský"],

             roz="Tichá", bydl="Praha I čp. 12", puvod="Březnice",

             r=["apolinar_krest_aloisie_ticha_1858", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882", "tyn_oddani_frantisek_mensik_1902"],

             note="Narozena 12. 7. 1858 v Praze na Novém Městě čp. 501, pokřtěna 18. 7. 1858 u sv. Apolináře, příslušná do Březnice. Dcera mistra krejčího Františka Tichého v Praze (rodilého z Březnice) a Anny roz. Svobodové z Prahy. Manželka kamnáře Aloise Jirkovského a matka Pavlíny Rosalie Menšíkové."),
    36: dict(n="Josef Pivnička", y="* 1844", st="doc",
             f=["* 10. 3. 1844 Čechtice",
                "× 3. 10. 1869 Praha (kostel sv. Jiljí) Antonie Grubnerová"],
             zam="mistr krejčovský v Praze na Novém Městě čp. 1356-II",
             bydl="Praha Nové Město čp. 1356, dříve Staré Město čp. 326",
             puvod="Čechtice (okres Dolní Kralovice / Ledeč nad Sázavou)",
             r=["jilji_oddani_josef_pivnicka_1869", "stepan_krest_jan_pivnicka_1872"],
             note="Mistr krejčí v Praze. Narozen 10. 3. 1844 v Čechticích. Syn souseda a provazníka v Čechticích Josefa Pivničky a Josefy roz. Boháčkové. Dne 3. 10. 1869 oddán u sv. Jiljí na Starém Městě s Antonií Grubnerovou z Dobříše."),
    37: dict(n="Antonie Pivničková", y="* 1843", st="doc",
             f=["* 6. 2. 1843 Dobříš",
                "× 3. 10. 1869 Praha (kostel sv. Jiljí) Josef Pivnička"],
             roz="Grubnerová", bydl="Praha Nové Město čp. 1356", puvod="Dobříš (okres Příbram)",
             r=["jilji_oddani_josef_pivnicka_1869", "stepan_krest_jan_pivnicka_1872"],
             note="Manželka mistra krejčího Josefa Pivničky. Narozena 6. 2. 1843 v Dobříši. Dcera dobříšského mistra krejčovského Antonína Grubnera a Barbory roz. Filoridové."),
    38: dict(n="Antonín Tomíček", y="† před 1908", st="doc",
             f=["× Anna Halíková", "† před 1908"],
             zam="c. k. železniční přednosta stanice Hauenstein-Warta (Buštěhradská dráha)",
             bydl="Warta čp. 59 (Stráž nad Ohří)", puvod="Čechy",
             r=["jindrich_oddani_jan_pivnicka_1908"],
             note="C. k. železniční přednosta nádraží Hauenstein-Warta (dnes Stráž nad Ohří na trati Chomutov–Cheb bývalé Buštěhradské dráhy) ve Wartě čp. 59. Manžel Anny roz. Halíkové a otec Emmy Marie Pivničkové."),
    39: dict(n="Anna Tomíčková", y="† před 1908", st="doc",
             f=["* Lobeč čp. 63", "× Antonín Tomíček", "† před 1908"],
             roz="Halíková", bydl="Warta čp. 59", puvod="Lobeč čp. 63 (okres Slaný / Mšeno)",
             r=["jindrich_oddani_jan_pivnicka_1908"],
             note="Manželka c. k. přednosty stanice Antonína Tomíčka a matka Emmy Marie Pivničkové. Pocházela z Lobče čp. 63."),

    42: dict(n="Jan Jarolím", y="1863–1903", st="doc",

             f=["* 4. 6. 1863 Žleby čp. 126", "× 29. 5. 1888 Dolní Krupá Antonie Havlová", "† 31. 7. 1903 Žleby čp. 37"],

             zam="obuvník", bydl="Žleby čp. 37",

             r=["krupa_oddani_jan_jarolim_1888", "zleby_umrti_jan_jarolim_1903", "zleby_krest_jan_jarolim_1863", "zleby_krest_emilie_jarolimova_1899"],

             note="Křest (Žleby 10, pag. 285, sn. 290), sňatek (Dolní Krupá 5946, sn. 102) i úmrtí na tuberkulózu (Žleby 35, pag. 666, sn. 337) doloženy přímo ze snímků matrik."),

    43: dict(n="Antonie Havlová", y="1857 – po 1914", st="doc",

             f=["* 13. 1. 1857 Dolní Krupá čp. 42", "× 29. 5. 1888 Dolní Krupá Jan Jarolím", "† po 1914"],

             r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888", "zleby_krest_emilie_jarolimova_1899", "zleby_umrti_jan_jarolim_1903"],

             note="Narození v Dolní Krupé čp. 42 (sign. 2840, sn. 206) i sňatek 29. 5. 1888 (sign. 5946, sn. 102) doloženy ze snímků matrik SOA Zámrsk. Dcera mistra krejčovského Jana Havla a Anny roz. Jeřábkové."),

    44: dict(n="František Holánek", y="1854 – po 1896", st="doc",

             f=["* 4. 8. 1854 Staré Ransko čp. 53", "× Julie Šímová", "† po 1896"],

             zam="zámečník",

             r=["ransko_krest_frantisek_holanek_1854"],

             note="Narození ve Starém Ransku čp. 53 doloženo přímo z matriky SOA Zámrsk / ARON (sign. 711, sn. 188, pag. 185). Pokřtěn 4. 8. 1854. Zámečník ve Starém Ransku."),

    45: dict(n="Julie Šímová", y="1854 – po 1896", st="fam",

             f=["* 16. 3. 1854 Staré Ransko čp. 46", "× František Holánek", "† po 1896"], r=[],

             note="Narozena ve Starém Ransku čp. 46 jako dcera horníka Matěje Šímy a Františky roz. Benové (dcery hamernického mistra Františka Bena). Manželka kováře Františka Holánka v čp. 55 a maminka zámečníka Julia Holánka (* 1889)."),

    46: dict(n="Franz Henzl", y="1872–1954", st="fam",

             f=["* 12. 7. 1872 Hluboká čp. 15", "× Aloisie Pospíchalová", "† 15. 2. 1954 Havlíčkův Brod čp. 539"],

             zam="truhlář a hostinský", r=[],

             note="Narozen 12. 7. 1872 v Hluboké čp. 15. Truhlář a hostinský na rodové usedlosti čp. 15 v Hluboké u Krucemburku. Syn čtvrtláníka Václava Henzla (* 1844) a Marie roz. Procházkové z čp. 7; vnuk kováře a zámečníka Jana Henzla. S manželkou Aloisií roz. Pospíchalovou představovali třetí generaci rodu Henzlů na gruntě čp. 15; otec Sofie Holánkové roz. Henzlové."),

    47: dict(n="Aloisie Pospíchalová", y="1875–1957", st="fam",

             f=["* 6. 1. 1875 Chlum čp. 35", "× Franz Henzl", "† 1957"], r=[],

             note="Narozena v Chlumu / Radostíně jako dcera Františka Pospíchala a Anny roz. Bencové. Manželka truhláře a hostinského Franze Henzla na rodovém gruntě čp. 15 v Hluboké a maminka Sofie Holánkové roz. Henzlové (* 1904)."),



    48: dict(n="... Čáki", y="† 1926", st="doc",
             f=["∞ 30. 9. 1888 Júlia ...", "† 5. 10. 1926 Dúbrava čp. 42",
                "otec roľníka Andreje Čákiho (* 1891) a dědeček Juraje (* 1919)",
                "příjmení v záznamech: Čaky / Čáki"],
             zam="roľník v Dúbravě čp. 42",
             bydl="Dúbrava čp. 42", puvod="Dúbrava čp. 42 (okres Snina, Zemplín)",
             r=["dubrava_scitanie_1930_caki_juraj"],
             note="Řeckokatolický roľník v Dúbravě čp. 42, otec Andreje Čákiho a dědeček Juraje Čákiho (prapradědeček Julie). Dne 30. 9. 1888 se oženil s Júlií ze Strihoviec (* 1868). Hospodařili na usedlosti čp. 42 v Dúbravě. Měli celkem 12 dětí (do roku 1930 jich 9 zemřelo a 3 zůstaly naživu). Zemřel 5. 10. 1926 v Dúbravě čp. 42 (datum sňatku i úmrtí zapsáno v operátu sčítání 1930 u jeho ovdovělé manželky). Křestní jméno bude ověřeno v řeckokatolické matrice farnosti Ruský Hrabovec."),

    49: dict(n="Júlia Čákiová", y="* 1868", st="doc",
             f=["* 15. 9. 1868 Strihovce (okres Snina)", "∞ 30. 9. 1888 ... Čáki (Čaky)",
                "† po 1930 (ovdověla 5. 10. 1926)",
                "matka 12 dětí (mj. roľníka Andreje Čákiho * 1891)"],
             roz="", bydl="Dúbrava čp. 42 (dříve Strihovce)", puvod="Strihovce (okres Snina, Zemplín)",
             r=["dubrava_scitanie_1930_caki_juraj"],
             note="Řeckokatolická hospodyně a výminkářka v Dúbravě čp. 42, matka Andreje Čákiho a babička Juraje Čákiho (praprababička Julie). Narozena 15. 9. 1868 ve Strihovcích v okrese Snina na Zemplíně. Dne 30. 9. 1888 se provdala za roľníka Čákiho do Dúbravy čp. 42. Byla matkou 12 dětí, z nichž 9 zemřelo a 3 žily v roce 1930. Dne 5. 10. 1926 ovdověla. Při sčítání lidu 1930 žila na výminku u svého syna Andreje (* 1891) a vnoučat včetně Juraje (* 1919) a novorozené vnučky Júlie (* 14. 6. 1930)."),

    56: dict(n="Václav Krejsek", y="* cca 1848 – po 1885", st="doc",
             f=["* cca 1848 Blažkov čp. 26", "× 24. 11. 1867 Zvole / Blažkov Marie Hamříková", "† po 1885",
                "otec mistra kolářského Otakara Jana Krejzka (* 1877)"],
             zam="rolník v Blažkově čp. 20 a čp. 26",
             bydl="Blažkov čp. 20 (dříve čp. 26)", puvod="Blažkov čp. 26",
             r=["blazkov_oddani_vaclav_krejsek_1867", "blazkov_krest_otakar_krejzek_1877"],
             note="Evangelický rolník v Blažkově na Novoměstsku. Narodil se kolem roku 1848 v Blažkově čp. 26 jako syn sedláka Jana Krejska a Anny rozené Procházkové z Josefsdorfu (Storfu). Dne 24. listopadu 1867 byl ve věku 19 let oddán s Marií Hamříkovou z Blažkova čp. 14. Hospodařili na usedlosti čp. 20 v Blažkově, kde se jim v květnu 1877 narodil syn Otakar Jan Krejzek, budoucí bystřický mistr kolářský a pradědeček Julie."),

    57: dict(n="Marie Krejsková", y="* 1849 – po 1885", st="doc",
             f=["* 16. 4. 1849 Blažkov čp. 14 (pokřtěna 17. 4. 1849 ve Zvoli)", "× 24. 11. 1867 Václav Krejsek", "† po 1885",
                "matka mistra kolářského Otakara Jana Krejzka (* 1877)"],
             roz="Hamříková", zam="v domácnosti / hospodyně",
             bydl="Blažkov čp. 20 (rodný dům čp. 14)", puvod="Blažkov čp. 14",
             r=["blazkov_krest_marianna_hamrikova_1849", "blazkov_oddani_vaclav_krejsek_1867", "blazkov_krest_otakar_krejzek_1877"],
             note="Narozena 16. dubna 1849 v Blažkově čp. 14 jako dcera svobodníka Františka Hamříka a Anny rozené Falské ze Zvole. Pokřtěna následujícího dne ve Zvoli jménem Marianna. Dne 24. listopadu 1867 se provdala za rolníka Václava Krejska a byla matkou šesti dětí včetně mistra kolářského Otakara Krejska (prababička Julie)."),

    58: dict(n="Leopold Sýs", y="", st="doc",
             f=["otec Františky Krejzkové roz. Sýsové"],
             zam="hajný v Borovníku", bydl="Borovník", puvod="Borovník",
             r=["bystrice_oddani_emil_krejzek_1943", "bystrice_oddani_vaclav_krejzek_1949"],
             note="Hajný v Borovníku (u Březí a Osové Bítýšky na Tišnovsku / Velkobítešsku), otec Františky Krejzkové roz. Sýsové a dědeček šesti bratří Krejzkových včetně primáře MUDr. Miroslava Krejzka (prapradědeček Julie). Doložen v oddacích zápisech vnuků MUDr. Emila Krejzka (12. 6. 1943 v Bystřici nad Pernštejnem) a MUC. Václava Krejzka (7. 4. 1949 na Starém Brně)."),

    60: dict(n="Jan Černý", y="* 1860", st="doc",
             f=["* 12. 3. 1860 Dobšice čp. 27", "× 20. 7. 1885 Poděbrady Anna Hromadová"],
             zam="mistr kovářský v Malém Zboží čp. 15 a Poděbradech čp. 15/II",
             bydl="Poděbrady / Malé Zboží čp. 15", puvod="Dobšice čp. 27 (fara Žehuň)",
             r=["dobsice_krest_jan_cerny_1860", "podebrady_oddani_jan_cerny_1885", "podebrady_oddani_josef_cerny_1911"],
             note="Mistr kovářský v Malém Zboží čp. 15 a v Poděbradech čp. 15/II. Narozen 12. 3. 1860 v Dobšicích čp. 27 (v oddacím zápise z roku 1885 byl chybně zapsán měsíc prosinec místo března, což spolehlivě vyvrací křestní matrika s úředním přípisem o vydání křestního listu k sňatku z 3. 7. 1885) jako manželský syn kováře Františka Černého a Kateřiny roz. Michlové. Dne 20. 7. 1885 byl v Poděbradech oddán s Annou Hromadovou z Chvalovic. Otec poděbradského mistra kovářského Josefa Černého (* 1886)."),

    61: dict(n="Anna Černá", y="* 1864", st="doc",
             f=["* 29. 6. 1864 Chvalovice čp. 21", "× 20. 7. 1885 Poděbrady Jan Černý"],
             roz="Hromadová", bydl="Poděbrady / Malé Zboží čp. 15", puvod="Chvalovice čp. 21",
             r=["chvalovice_krest_anna_hromadova_1864", "podebrady_oddani_jan_cerny_1885", "podebrady_oddani_josef_cerny_1911"],
             note="Narozena 29. 6. 1864 v Chvalovicích čp. 21 jako manželská dcera rolníka Václava Hromady a Anny roz. Kovaříkové z Chvalovic čp. 21. Dne 20. 7. 1885 se v Poděbradech provdala za mistra kovářského Jana Černého. Matka poděbradského mistra kovářského Josefa Černého (* 1886) a prababička Julie."),

    62: dict(n="Josef Měšťánek", y="* 1859", st="doc",
             f=["* 16. 1. 1859 Bojiště čp. 10 (okres Kolín)", "× 3. 4. 1883 Končice čp. 71 Kateřina Ouzká"],
             zam="mistr tesařský, rolník v Končicích čp. 14, později obchodník v Poděbradech čp. 13/II",
             bydl="Poděbrady čp. 13/II, dříve Končice čp. 14", puvod="Bojiště čp. 10 (okres Kolín)",
             r=["bojiste_krest_josef_mestanek_1859", "koncice_oddani_josef_mestanek_1883", "koncice_krest_marie_mestankova_1885", "podebrady_oddani_josef_cerny_1911"],
             note="Mistr tesařský a rolník v Končicích čp. 14, později obchodník v Poděbradech čp. 13/II. Narozen 16. 1. 1859 v Bojišti čp. 10 jako syn tesaře Václava Měšťánka a Barbory roz. Kosové. Pokřtěn 17. 1. 1859 kaplanem Ferdinandem Cvejnem. Dne 3. 4. 1883 oddán v Končicích s Kateřinou Ouzkou. Otec Marie Černé roz. Měšťánkové (pradědeček Julie)."),

    63: dict(n="Kateřina Měšťánková", y="* 1862", st="doc",
             f=["* 11. 4. 1862 Končice čp. 14", "× 3. 4. 1883 Končice čp. 71 Josef Měšťánek"],
             roz="Ouzká", bydl="Poděbrady čp. 13/II, dříve Končice čp. 14", puvod="Končice čp. 14",
             r=["koncice_krest_katerina_ouzka_1862", "koncice_oddani_josef_mestanek_1883", "koncice_krest_marie_mestankova_1885", "podebrady_oddani_josef_cerny_1911"],
             note="Narozena 11. 4. 1862 v Končicích čp. 14 (pokřtěna 13. 4. 1862) jako nemanželská dcera svobodné matky Kateřiny Ouzké a vnučka baráčníka Jiřího Ouzkého z čp. 14 a Barbory roz. Daníčkové z čp. 12. V oddacím zápise z roku 1883 byl její věk chybně zapsán jako 26 let (tedy narození cca 1857), ve skutečnosti se však vdávala necelé dva týdny před svými 21. narozeninami a jako nezletilá musela mít vrchnoporučenské svolení soudu v Chlumci n. C. Na okraji křestního zápisu je autentický přípis: 'List křestní k oddavkám vydán dne 29. března 1883 čj. 2868'. Matka Marie Černé roz. Měšťánkové (prababička Julie)."),



    # 6. generace (64–70, 84–93)

    64: dict(n="Josef Menšík st.", y="* cca 1801/1806", st="doc",

             f=["* 13. 7. 1806 Jistebnice čp. 156", "× 12. 2. 1828 Jistebnice Barbora Horychová"],

             zam="měšťan a pekař v Jistebnici čp. 156", puvod="Jistebnice",

             r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1828", "jistebnice_oddani_josef_mensik_1865"],

             note="Měšťan a mistr pekařský v Jistebnici čp. 156, syn řezníka Františka Menšíka (v matrice 1832 zapsán Faustin) a Anny roz. Dvořákové. Narozen 13. 7. 1806 v čp. 156. Oddán 12. 2. 1828 v Jistebnici s Barborou Horychovou (v oddací matrice zapsán ve věku 26 let, bydliště čp. 165)."),

    65: dict(n="Barbora Menšíková", y="* 1801", st="doc",

             f=["* 3. 9. 1801 Jistebnice čp. 136", "× 12. 2. 1828 Jistebnice Josef Menšík"],

             roz="Horychová", puvod="Jistebnice",

             r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1828", "jistebnice_oddani_josef_mensik_1865"],

             note="Narozena 3. 9. 1801 v Jistebnici čp. 136. Dcera Františka Horycha, mistra zednického a měšťana v Jistebnici (čp. 136 a 86), a Barbory roz. Dědové. Oddána 12. 2. 1828 v Jistebnici (z čp. 86, věk 26 let) s pekařem Josefem Menšíkem."),

    66: dict(n="Antonín Šmedla", y="", st="doc",

             f=["× Františka Šebelová"],

             zam="punčochář, později kostelník v Jistebnici čp. 48 / 73", puvod="Jistebnice",

             r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

             note="Punčochář a později kostelník v Jistebnici, syn Antonína Šmedly, punčocháře z Jistebnice, a Anny roz. Kostkové."),

    67: dict(n="Františka Šmedlová", y="", st="doc",

             f=["× Antonín Šmedla"],

             roz="Šebelová", puvod="Vlasenice",

             r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

             note="Dcera Václava Šebeleho, správčího ve Vlasenicích, a jeho choti Apolonie."),

    68: dict(n="František Jirkovský", y="† před 1882", st="doc",

             f=["× 15. 2. 1852 Praha (sv. František) Aloisie Franzová", "† před 2. 11. 1882"],

             zam="hrnčířský tovaryš a kamnář v Praze", puvod="Kutná Hora", bydl="Praha I čp. 783",

             r=["hastal_krest_alois_jirkovsky_1859", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882"],

             note="Hrnčířský tovaryš v Praze, rodilý z Kutné Hory. Syn Václava Jirkovského, patentního invalidy v Čáslavi, a Anny roz. Pilzové z Kutné Hory. Oddán 15. 2. 1852 u sv. Františka v Praze s Aloisií Franzovou. K listopadu 1882 již zemřelý."),

    69: dict(n="Aloisie Jirkovská", y="", st="doc",

             f=["× 15. 2. 1852 Praha (sv. František) František Jirkovský"],

             roz="Franzová", puvod="Praha", bydl="Praha I čp. 783",

             r=["hastal_krest_alois_jirkovsky_1859", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882"],

             note="Manželka hrnčířského tovaryše Františka Jirkovského v Praze, rozená Franzová z Prahy (dcera Barbory Franzové, pradleny v Praze). Oddána 15. 2. 1852 u sv. Františka. Matka kamnáře Aloise Jirkovského."),

    70: dict(n="František Tichý", y="† před 1882", st="doc",

             f=["× Anna Svobodová", "† před 2. 11. 1882"],

             zam="mistr krejčovský v Praze čp. 501-II", puvod="Březnice", bydl="Praha Nové Město čp. 501-II",

             r=["apolinar_krest_aloisie_ticha_1858", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882", "tyn_oddani_frantisek_mensik_1902"],

             note="Mistr krejčovský v Praze na Novém Městě čp. 501-II, rodilý z Březnice. Syn Josefa Tichého, vrchnostenského poddaného v Březnici, a Anny roz. Satrové (Šatrové) z Koupě. Manžel Anny roz. Svobodové a otec Aloisie Marie Jirkovské roz. Tiché. K listopadu 1882 již zemřelý."),

    71: dict(n="Anna Tichá", y="† před 1882", st="doc",

             f=["× František Tichý", "† před 2. 11. 1882"],

             roz="Svobodová", puvod="Praha", bydl="Praha Nové Město čp. 501-II / Březnice",

             r=["apolinar_krest_aloisie_ticha_1858", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882"],

             note="Manželka mistra krejčího Františka Tichého v Praze, rozená Svobodová z Prahy. Dcera Václava Svobody, policejního komisionáře v Praze čp. 501-II, a Anny roz. Schneiderové. K listopadu 1882 již zemřelá."),
    72: dict(n="Josef Pivnička", y="", st="doc",
             f=["× Josefa (Barbora) Boháčková", "† před 1872"],
             zam="soused a provazník v Čechticích", puvod="Čechtice",
             r=["stepan_krest_jan_pivnicka_1872", "jilji_oddani_josef_pivnicka_1869"],
             note="Soused a mistr provaznický v Čechticích (okres Dolní Kralovice / Ledeč nad Sázavou). Otec mistra krejčovského Josefa Pivničky (* 1844)."),
    73: dict(n="Josefa Pivničková", y="", st="doc",
             f=["× Josef Pivnička"],
             roz="Boháčková", puvod="Čechtice",
             r=["stepan_krest_jan_pivnicka_1872", "jilji_oddani_josef_pivnicka_1869"],
             note="Manželka čechtického souseda a provazníka Josefa Pivničky a matka Josefa Pivničky (* 1844). V matrice oddaných z r. 1869 psána Josefa roz. Boháčková, v matrice narozených z r. 1872 Barbora roz. Boháčková."),
    74: dict(n="Antonín Grubner", y="", st="doc",
             f=["× Barbora Filoridová"],
             zam="mistr krejčovský v Dobříši", puvod="Dobříš",
             r=["jilji_oddani_josef_pivnicka_1869", "stepan_krest_jan_pivnicka_1872"],
             note="Mistr krejčovský v Dobříši (okres Příbram). Otec Antonie Pivničkové roz. Grubnerové (* 1843)."),
    75: dict(n="Barbora Grubnerová", y="", st="doc",
             f=["× Antonín Grubner"],
             roz="Filoridová", puvod="Dobříš",
             r=["jilji_oddani_josef_pivnicka_1869", "stepan_krest_jan_pivnicka_1872"],
             note="Manželka dobříšského mistra krejčovského Antonína Grubnera a matka Antonie Pivničkové roz. Grubnerové (* 1843). Příjmení psáno též Filoridy / Tilorády."),

    84: dict(n="otec neuveden", y="", st="unk",

             f=[], r=["zleby_krest_jan_jarolim_1863"], note="Jan Jarolím (* 1863) byl nemanželským synem Barbory Jarolímové; otec v křestní matrice Žlebů neuveden (kolonka otce prázdná)."),

    85: dict(n="Barbora Jarolímová", y="† před 1888", st="doc",

             f=["† před 29. 5. 1888", "dcera obuvníka Josefa Jarolíma a Kateřiny Táborské"],

             bydl="Žleby čp. 126",

             r=["krupa_oddani_jan_jarolim_1888", "zleby_krest_jan_jarolim_1863", "zleby_krest_emilie_jarolimova_1899"],

             note="Doložena v křestních zápisech syna Jana i vnučky Emilie ve Žlebech; v oddacím zápise syna Jana (1888) uvedena jako již zesnulá."),

    86: dict(n="Jan Havel", y="† před 1888", st="doc",

             f=["× Anna Jeřábková", "† před 29. 5. 1888", "syn Martina Havla a Magdaleny Dolanské"],

             zam="mistr krejčovský", bydl="Dolní Krupá čp. 42",

             r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888", "zleby_krest_emilie_jarolimova_1899"],

             note="Mistr krejčovský v Dolní Krupé čp. 42. Syn domkaře Martina Havla z Dolní Krupé čp. 42 a Magdaleny roz. Dolanské z čp. 22. Doložen v křtu dcery Antonie (1857) i vnučky Emilie (1899); k 1888 již zesnulý."),

    87: dict(n="Anna Jeřábková", y="† před 1888", st="doc",

             f=["× Jan Havel", "† před 29. 5. 1888", "dcera učitele Ignáce Jeřábka a Josefy Hoffmannové"],

             bydl="Čachotín čp. 15",

             r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888", "zleby_krest_emilie_jarolimova_1899"],

             note="Dcera učitele Ignáce Jeřábka a Josefy roz. Hoffmannové z Frauenthalu (Pohledu) čp. 5. Doložena v křtu dcery Antonie (1857), oddavkách (1888) i křtu vnučky Emilie (1899)."),

    88: dict(n="Jan Holánek", y="* 1820", st="doc",

             f=["* 18. 6. 1820 Staré Ransko čp. 45", "× Johanna Hlaváčková",

                "syn mistra kovářského Josefa Holánka a Barbory Slámové"],

             zam="domkař", bydl="Staré Ransko čp. 53",

             r=["ransko_krest_frantisek_holanek_1854"],

             note="Domkař ve Starém Ransku čp. 53. Doložen v křestní matrice syna Františka (* 1854, sign. 711, sn. 188), kde je uveden jako manželský syn již zesnulého kovářského mistra Josefa Holánka ze Starého Ranska čp. 53 a Barbory roz. Slámové ze Starého Ranska čp. 33."),

    89: dict(n="Johanna Hlaváčková", y="", st="doc",

             f=["× Jan Holánek", "dcera mistra zámečnického Vojtěcha Hlaváčka a Barbory Haislerové"],

             bydl="Staré Ransko čp. 49",

             r=["ransko_krest_frantisek_holanek_1854"],

             note="Doložena v křestní matrice syna Františka (* 1854, sign. 711, sn. 188). Manželská dcera zámečnického mistra Vojtěcha Hlaváčka ze Starého Ranska čp. 49 a Barbory roz. Haislerové z Hamrů čp. 9 (u Hlinska)."),

    90: dict(n="Matěj Šíma", y="", st="fam",

             f=["× Františka Benová"],

             zam="horník / horolezec", bydl="Staré Ransko čp. 2", r=[],

             note="Údaje z rodinného stromu PDF (v PDF uvedeno 'horolezec' – ověřit v matrice, zda nešlo o horníka / havíře v železárnách v Ransku)."),

    91: dict(n="Františka Benová", y="", st="fam",

             f=["× Matěj Šíma"], bydl="Staré Ransko čp. 41", r=[], note="Údaje z rodinného stromu PDF."),

    92: dict(n="Václav Henzl", y="* 1844", st="fam",

             f=["* 6. 8. 1844 Hluboká čp. 15", "× Marie Procházková"],

             zam="čtvrtláník", r=[],

             note="Údaje z rodinného stromu PDF."),

    93: dict(n="Marie Procházková", y="", st="fam",

             f=["× Václav Henzl"], bydl="Hluboká čp. 7", r=[], note="Údaje z rodinného stromu PDF."),



    112: dict(n="Jan Krejsek", y="1796 – po 1867", st="doc",
              f=["* 17. 5. 1796 Blažkov čp. 26", "× 8. 2. 1825 Josefsdorf Anna Procházková", "† po 1867",
                 "křest 23. 5. 1796 pastorem Aaronem Štettinou (evangelický sbor Nové Město na Moravě)",
                 "syn sedláka Václava Krejska st. († 1832 na choleru) a Anny rozené Stehlíkové ze Zvole"],
              zam="sedlák a rolník v Blažkově čp. 26",
              bydl="Blažkov čp. 26", puvod="Blažkov čp. 26",
              r=["blazkov_krest_jan_krejsek_1796", "josefsdorf_oddani_jan_krejsek_1825", "blazkov_oddani_vaclav_krejsek_1867"],
              note="Evangelický sedlák v Blažkově na gruntu čp. 26. Narozen 17. 5. 1796 v Blažkově čp. 26 jako syn sedláka Václava Krejska a Anny roz. Stehlíkové ze Zvole (pokřtěn 23. 5. 1796 pastorem Aaronem Štettinou). Dne 8. února 1825 byl evangelickým pastorem Gedeonem Šlachtou ze sboru ve Veselí oddán s Annou Procházkovou z familiantského Josefsdorfu (Storfu) čp. 5. Otec Václava Krejska a dědeček bystřického mistra kolářského Otakara Krejska."),

    113: dict(n="Anna Krejsková", y="* cca 1800 – po 1867", st="doc",
              f=["* cca 1800–1801 Josefsdorf (Storf) čp. 5", "× 8. 2. 1825 Jan Krejsek", "† po 1867",
                 "dcera Václava Procházky, sedláka v Josefsdorfu a Terezie rozené Zubánkové z Domanínku"],
              roz="Procházková", bydl="Blažkov čp. 26", puvod="Josefsdorf (Storf) čp. 5 (fara Rožná)",
              r=["josefsdorf_oddani_jan_krejsek_1825", "blazkov_oddani_vaclav_krejsek_1867"],
              note="Narozena kolem roku 1800 v Josefsdorfu (Storfu) čp. 5 v rodině sedláka Václava Procházky a Terezie rozené Zubánkové z Domanínku. Dne 8. února 1825 se provdala za Jana Krejska z Blažkova čp. 26."),

    114: dict(n="František Hamřík", y="* cca 1826 – po 1877", st="doc",
              f=["* cca 1826–1827 Blažkov čp. 14", "× 10. 2. 1847 Zvole Anna Falská", "† po 1877",
                 "syn svobodníka Františka Hamříka st. a Augustiny Josefy rozené Valouškové, dcery mlynářského mistra ve Zvoli čp. 65"],
              zam="svobodník a rolník v Blažkově čp. 14",
              bydl="Blažkov čp. 14", puvod="Blažkov čp. 14",
              r=["zvole_oddani_frantisek_hamrik_1847", "blazkov_krest_marianna_hamrikova_1849"],
              note="Evangelický svobodník (Freysaß) v Blažkově na rodovém dvoře čp. 14. Dne 10. února 1847 byl ve Zvoli oddán se sedmnáctiletou Annou Falskou z Blažkova čp. 28 / Zvole čp. 10. Otec Marie Krejskové roz. Hamříkové a dědeček bystřického mistra kolářského Otakara Krejska."),

    115: dict(n="Anna Hamříková", y="* cca 1829 – po 1867", st="doc",
              f=["* cca 1829–1830 Blažkov čp. 28 / Zvole čp. 10", "× 10. 2. 1847 František Hamřík", "† po 1867",
                 "dcera Františka Falského, svobodníka v Blažkově čp. 28 a hostinského ve Zvoli čp. 10, a Kateřiny rozené Mišníčkové"],
              roz="Falská", bydl="Blažkov čp. 14", puvod="Blažkov čp. 28 / Zvole čp. 10",
              r=["zvole_oddani_frantisek_hamrik_1847", "blazkov_krest_marianna_hamrikova_1849"],
              note="Dcera ze starého svobodnického rodu Falských z Blažkova čp. 28 a hostinského ve Zvoli čp. 10 Františka Falského a Kateřiny rozené Mišníčkové. V únoru 1847 se provdala za svobodníka Františka Hamříka do Blažkova čp. 14."),

    120: dict(n="František Černý", y="asi 1829 – před 1885", st="doc",
              f=["* asi 1829", "× 21. 1. 1856 Vlkov čp. 13 Kateřina Michlová", "† před 1885"],
              zam="mistr kovářský v Dobšicích čp. 27 a Malém Zboží čp. 15",
              bydl="Dobšice čp. 27, později Malé Zboží čp. 15", puvod="Dobšice čp. 27",
              r=["vlkov_oddani_frantisek_cerny_1856", "dobsice_krest_jan_cerny_1860", "podebrady_oddani_jan_cerny_1885"],
              note="Mistr kovářský v Dobšicích čp. 27 a v Malém Zboží čp. 15, manželský syn kováře Václava Černého z Dobšic čp. 27 a Anny roz. Šiškové z kovářské usedlosti v Žiželicích čp. 119. Dne 21. 1. 1856 se ve Vlkově čp. 13 oženil se sedmnáctiletou dcerou místního kováře Kateřinou Michlovou. Otec mistra kovářského Jana Černého (* 1860)."),

    121: dict(n="Kateřina Černá", y="* asi 1838", st="doc",
              f=["* asi 1838 Vlkov čp. 13", "× 21. 1. 1856 Vlkov čp. 13 František Černý"],
              roz="Michlová", bydl="Vlkov čp. 13, Dobšice čp. 27, Malé Zboží čp. 15", puvod="Vlkov čp. 13",
              r=["vlkov_oddani_frantisek_cerny_1856", "dobsice_krest_jan_cerny_1860", "podebrady_oddani_jan_cerny_1885"],
              note="Pocházela z kovářské chalupy ve Vlkově čp. 13 jako manželská dcera již zemřelého kováře Josefa Michla a Anny roz. Fialové z Lužan čp. 19. Dne 21. 1. 1856 se po vrchnoporučenském svolení provdala za kováře Františka Černého z Dobšic. Matka mistra kovářského Jana Černého (* 1860)."),

    122: dict(n="Václav Hromada", y="* 1832 · † před 1885", st="doc",
              f=["* 31. 8. 1832 Vyšehořovice čp. 22", "× 12. 4. 1853 Chvalovice čp. 21 Anna Kováříková", "† před 1885"],
              zam="gruntovník a rolník v Chvalovicích čp. 21 a 4",
              bydl="Chvalovice čp. 21 a 4", puvod="Vyšehořovice čp. 22",
              r=["kovanice_oddani_vaclav_hromada_1853", "chvalovice_krest_anna_hromadova_1864", "podebrady_oddani_jan_cerny_1885"],
              note="Gruntovník v Chvalovicích čp. 21 a rolník v čp. 4. Narozen 31. 8. 1832 ve Vyšehořovicích čp. 22 jako manželský syn gruntovníka Václava Hromady st. a Alžběty roz. Jirkovské z čp. 25. Dne 12. 4. 1853 se ještě jako nezletilý (20 1/2 let) po vrchnoporučenském svolení soudu v Českém Brodě oženil v Chvalovicích s Annou Kováříkovou a převzal zdejší grunt čp. 21. Otec Anny Černé roz. Hromadové (* 1864)."),

    123: dict(n="Anna Hromadová", y="* 1831", st="doc",
              f=["* 1831 Chvalovice čp. 21", "× 12. 4. 1853 Chvalovice čp. 21 Václav Hromada"],
              roz="Kováříková", bydl="Chvalovice čp. 21 a 4", puvod="Chvalovice čp. 21",
              r=["kovanice_oddani_vaclav_hromada_1853", "chvalovice_krest_anna_hromadova_1864", "podebrady_oddani_jan_cerny_1885"],
              note="Manželka gruntovníka Václava Hromady, narozená roku 1831 v Chvalovicích čp. 21 jako dcera hospodáře Josefa Kováříka a Anny roz. Homolové z Chrástu na Českobrodsku. Dne 12. 4. 1853 se provdala za Václava Hromadu za písemného souhlasu otce Josefa Kováříka, který odešel na výminek. Matka Anny Černé roz. Hromadové (* 1864)."),

    124: dict(n="Václav Měšťánek", y="* cca 1830", st="doc",
              f=["* cca 1830 Dvory", "× 4. 10. 1858 Pečky (farnost Nebovidy) Barbora Kosová"],
              zam="tovaryš tesařský v Bojišti čp. 10, záložník c. k. 6. pluku polního dělostřelectva, tkalec",
              bydl="Bojiště čp. 10 (okres Kolín)", puvod="Dvory čp. 2",
              r=["bojiste_oddani_vaclav_mestanek_1858", "bojiste_krest_josef_mestanek_1859", "koncice_oddani_josef_mestanek_1883", "koncice_krest_marie_mestankova_1885"],
              note="Tovaryš tesařský v Bojišti čp. 10 a tkalec. Sloužil u c. k. 6. pluku polního dělostřelectva (Artillerie-Regiment Nr. 6, majitel generálmajor rytíř von Fitz). Narozen kolem roku 1830 ve Dvorech čp. 2 jako manželský syn nádeníka Antonína Měšťánka a Barbory roz. Šafáříkové z Peček. Dne 4. 10. 1858 se v Pečkách po doručení vojenského povolení z Pešti a ohláškách u dělostřelecké jednotky v Uhrách oženil s Barborou Kosovou z Bojiště čp. 10. Otec mistra tesařského Josefa Měšťánka (* 1859)."),

    125: dict(n="Barbora Měšťánková", y="* cca 1835", st="doc",
              f=["* cca 1835 Bojiště čp. 10", "× 4. 10. 1858 Pečky (farnost Nebovidy) Václav Měšťánek"],
              roz="Kosová", bydl="Bojiště čp. 10", puvod="Bojiště čp. 10",
              r=["bojiste_oddani_vaclav_mestanek_1858", "bojiste_krest_josef_mestanek_1859", "koncice_oddani_josef_mestanek_1883", "koncice_krest_marie_mestankova_1885"],
              note="Narozena kolem roku 1835 v Bojišti čp. 10 jako manželská dcera domkáře a tesaře Václava Kosa a Marie roz. Kollářové z Peček čp. 55. Dne 4. 10. 1858 se za přítomnosti svého otce v Pečkách provdala za tesaře a dělostřeleckého záložníka Václava Měšťánka. Matka Josefa Měšťánka (* 1859)."),

    127: dict(n="Kateřina Ouzká", y="", st="doc",
              f=[], bydl="Končice čp. 14", puvod="Končice",
              r=["koncice_krest_katerina_ouzka_1862", "koncice_oddani_josef_mestanek_1883", "koncice_krest_marie_mestankova_1885"],
              note="Svobodná matka v Končicích čp. 14, dcera domkaře a baráčníka Jiřího Ouzkého z Končic čp. 14 a Barbory roz. Daníčkové z Končic čp. 12. Matka Kateřiny provdané Měšťánkové (* 1862)."),



    # 7. generace (128–143, 170–175, 242–255)

    128: dict(n="František Menšík", y="", st="doc",

              f=["× Anna Dvořáková"],

              zam="řezník v Jistebnici", puvod="Jistebnice",

              r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1865"],

              note="Řezník v Jistebnici, otec pekaře Josefa Menšíka z čp. 156. V křtu syna Josefa 1832 zapsán Faustin Menšík, v oddací matrice 1865 František."),

    129: dict(n="Anna Menšíková", y="", st="doc",

              f=["× František Menšík"],

              roz="Dvořáková", puvod="Jistebnice",

              r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1865"],

              note="Manželka řezníka Františka Menšíka z Jistebnice."),

    130: dict(n="František Horych", y="", st="doc",

              f=["× 18. 1. 1791 Jistebnice Barbora Dědová"],

              zam="mistr zednický a měšťan v Jistebnici", puvod="Jistebnice",

              r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1828", "jistebnice_oddani_josef_mensik_1865"],

              note="Mistr zednický a měšťan v Jistebnici (čp. 136 a 86), otec Barbory Menšíkové roz. Horychové. Oddán 18. 1. 1791 v Jistebnici s Barborou Dědovou."),

    131: dict(n="Barbora Horychová", y="", st="doc",

              f=["× 18. 1. 1791 Jistebnice František Horych"],

              roz="Dědová", puvod="Jistebnice",

              r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1828", "jistebnice_oddani_josef_mensik_1865"],

              note="Manželka zednického mistra Františka Horycha z Jistebnice, rozená Dědová. Oddána 18. 1. 1791 v Jistebnici."),

    132: dict(n="Antonín Šmedla st.", y="", st="doc",

              f=["× Anna Kostková"],

              zam="punčochář v Jistebnici", puvod="Jistebnice",

              r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

              note="Punčochář v Jistebnici, otec kostelníka Antonína Šmedly."),

    133: dict(n="Anna Šmedlová", y="", st="doc",

              f=["× Antonín Šmedla"],

              roz="Kostková", puvod="Jistebnice",

              r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

              note="Manželka punčocháře Antonína Šmedly z Jistebnice, rozená Kostková."),

    134: dict(n="Václav Šebele", y="", st="doc",

              f=["× Apolonie Šebelová"],

              zam="správčí ve Vlasenicích", puvod="Vlasenice",

              r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

              note="Správčí ve Vlasenicích, otec Františky Šmedlové roz. Šebelové."),

    135: dict(n="Apolonie Šebelová", y="", st="doc",

              f=["× Václav Šebele"],

              puvod="Vlasenice",

              r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

              note="Manželka správčího Václava Šebeleho ve Vlasenicích."),

    136: dict(n="Václav Jirkovský", y="", st="doc",

              f=["× Anna Pilzová"],

              zam="patentinvalida (vysloužilý voják) v Čáslavi", puvod="Kutná Hora", bydl="Čáslav",

              r=["hastal_krest_alois_jirkovsky_1859"],

              note="Patentinvalida v Čáslavi, původem z Kutné Hory. Otec hrnčířského tovaryše Františka Jirkovského v Praze."),

    137: dict(n="Anna Jirkovská", y="", st="doc",

              f=["× Václav Jirkovský"],

              roz="Pilzová", puvod="Kutná Hora",

              r=["hastal_krest_alois_jirkovsky_1859"],

              note="Manželka Václava Jirkovského, rozená Pilzová (Pílcová) z Kutné Hory. Matka Františka Jirkovského."),

    139: dict(n="Barbora Franzová", y="", st="doc",

              f=[], zam="pradlena v Praze", puvod="Praha", bydl="Praha",

              r=["hastal_krest_alois_jirkovsky_1859"],

              note="Pradlena v Praze, matka Aloisie Jirkovské roz. Franzové."),

    140: dict(n="Josef Tichý", y="", st="doc",

              f=["× Anna Satrová"],

              zam="vrchnostenský poddaný v Březnici", puvod="Březnice", bydl="Březnice",

              r=["apolinar_krest_aloisie_ticha_1858"],

              note="Vrchnostenský poddaný v Březnici, otec pražského mistra krejčovského Františka Tichého."),

    141: dict(n="Anna Tichá", y="", st="doc",

              f=["× Josef Tichý"],

              roz="Satrová", puvod="Koupě", bydl="Březnice / Koupě",

              r=["apolinar_krest_aloisie_ticha_1858"],

              note="Manželka Josefa Tichého, rozená Satrová (Šatrová) z Koupě u Březnice. Matka Františka Tichého."),

    142: dict(n="Václav Svoboda", y="", st="doc",

              f=["× Anna Schneiderová"],

              zam="komisionář od policie v Praze", puvod="Praha", bydl="Praha Nové Město čp. 501-II",

              r=["apolinar_krest_aloisie_ticha_1858"],

              note="Komisionář od policie v Praze na Novém Městě čp. 501-II. Otec Anny Tiché roz. Svobodové."),

    143: dict(n="Anna Svobodová", y="", st="doc",

              f=["× Václav Svoboda"],

              roz="Schneiderová", puvod="Praha", bydl="Praha Nové Město čp. 501-II",

              r=["apolinar_krest_aloisie_ticha_1858"],

              note="Manželka pražského policejního komisionáře Václava Svobody, rozená Schneiderová. Matka Anny Tiché roz. Svobodové."),

    170: dict(n="Josef Jarolím", y="", st="doc",

              f=["× Kateřina Táborská"],

              zam="obuvník", bydl="Žleby čp. 126",

              r=["zleby_krest_jan_jarolim_1863", "zleby_krest_emilie_jarolimova_1899"],

              note="Otec Barbory Jarolímové, obuvník ve Žlebech čp. 126; doložen v křestních zápisech dcery, vnuka Jana i pravnučky Emilie."),

    171: dict(n="Kateřina Táborská", y="", st="doc",

              f=["× Josef Jarolím", "dcera Josefa Táborského"],

              bydl="Žleby čp. 7 / čp. 126",

              r=["zleby_krest_jan_jarolim_1863", "zleby_krest_emilie_jarolimova_1899"],

              note="Matka Barbory Jarolímové, dcera Josefa Táborského ze Žlebů."),

    172: dict(n="Martin Havel", y="† před 1857", st="doc",

              f=["× Magdalena Dolanská", "† před 13. 1. 1857"],

              zam="domkař", bydl="Dolní Krupá čp. 42",

              r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888"],

              note="Domkař v Dolní Krupé čp. 42, otec mistra krejčovského Jana Havla. Doložen v křestní matrice vnučky Antonie."),

    173: dict(n="Magdalena Dolanská", y="† před 1857", st="doc",

              f=["× Martin Havel", "† před 13. 1. 1857"],

              bydl="Dolní Krupá čp. 22",

              r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888"],

              note="Matka krejčího Jana Havla, rodem z Dolní Krupé čp. 22. Doložena v křestní matrice vnučky Antonie."),

    174: dict(n="Ignác Jeřábek", y="† po 1864", st="doc",

              f=["× Josefa Hoffmannová", "† po 1864"],

              zam="učitel", bydl="Čachotín čp. 15, Jiříkov čp. 4 a Dolní Krupá čp. 42",

              r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888", "zleby_krest_emilie_jarolimova_1899"],

              note="Učitel v Čachotíně čp. 15, k roku 1857 žil v Jiříkově čp. 4, k roku 1864 na odpočinku v Dolní Krupé čp. 42. Otec Anny Jeřábkové. Doložen v křestních matrikách dcery i vnuček."),

    175: dict(n="Josefa Hoffmannová", y="† před 1864", st="doc",

              f=["× Ignác Jeřábek", "† před 9. 7. 1864"],

              bydl="Frauenthal (Pohled) čp. 5",

              r=["krupa_krest_antonie_havlova_1857"],

              note="Manželka učitele Ignáce Jeřábka, rodem z Frauenthalu (Pohledu) čp. 5. Matka Anny Jeřábkové. Doložena v křestní matrice dcery Antonie."),

    176: dict(n="Josef Holánek", y="† před 1854", st="doc",

              f=["× Barbora Slámová", "† před 4. 8. 1854"],

              zam="mistr kovářský", bydl="Staré Ransko čp. 53",

              r=["ransko_krest_frantisek_holanek_1854"],

              note="Mistr kovářský ve Starém Ransku čp. 53. Doložen v křestní matrice vnuka Františka (* 1854), kde je uveden jako již zesnulý mistr kovářský. Manželka Barbora roz. Slámová z čp. 33."),

    177: dict(n="Barbora Slámová", y="", st="doc",

              f=["× Josef Holánek"],

              bydl="Staré Ransko čp. 33",

              r=["ransko_krest_frantisek_holanek_1854"],

              note="V rodinném stromu PDF byla uvedena s křestním jménem Filipina; v křestní matrice vnuka Františka (* 1854) je však jednoznačně doložena jako Barbora rozená Sláma ze Starého Ranska čp. 33."),

    178: dict(n="Vojtěch Hlaváček", y="", st="doc",

              f=["× Barbora Haislerová"],

              zam="mistr zámečnický", bydl="Staré Ransko čp. 49",

              r=["ransko_krest_frantisek_holanek_1854"],

              note="Mistr zámečnický ve Starém Ransku čp. 49 (v rodinném stromu PDF byl chybně označen za uhlíře). Doložen v křestní matrice vnuka Františka Holánka (* 1854)."),

    179: dict(n="Barbora Haislerová", y="", st="doc",

              f=["× Vojtěch Hlaváček"],

              bydl="Hamry čp. 9 (panství Hlinecké)",

              r=["ransko_krest_frantisek_holanek_1854"],

              note="Pocházela z Hamrů čp. 9 na hlineckém panství (panství Hlinsko, Chrudimský kraj). Doložena v křestním zápise vnuka Františka Holánka (* 1854)."),

    180: dict(n="Tomáš Šíma", y="", st="fam",

              f=["× Marie Halíková"], zam="dráb", bydl="Staré Ransko čp. 2", r=[], note="Údaje z rodinného stromu PDF."),

    181: dict(n="Marie Halíková", y="", st="fam",

              f=["× Tomáš Šíma"], bydl="Olešná (Volešná)", r=[], note="Údaje z rodinného stromu PDF."),

    182: dict(n="František Ben", y="", st="fam",

              f=["× Karolina Králíčková"], zam="hamernický mistr", bydl="Staré Ransko čp. 41", r=[], note="Údaje z rodinného stromu PDF."),

    183: dict(n="Karolina Králíčková", y="", st="fam",

              f=["× František Ben"], bydl="Česká Kamenice", r=[], note="Údaje z rodinného stromu PDF."),

    184: dict(n="Jan Henzl", y="† před 1872", st="fam",

              f=["× Anna Nováková", "† před 1872"], zam="kovář a zámečník", bydl="Hluboká čp. 15", r=[], note="Údaje z rodinného stromu PDF."),

    185: dict(n="Anna Nováková", y="", st="fam",

              f=["× Jan Henzl"], bydl="Chlumětín", r=[], note="Údaje z rodinného stromu PDF (psána Anna Nowak)."),



    224: dict(n="Václav Krejsek", y="* před 1775 – † 1832", st="doc",
              f=["* před 1775 Blažkov", "× Anna Stehlíková (ze Zvole)", "† 1832 Blažkov čp. 26 (na choleru)",
                 "otec sedláka Jana Krejska (* 1796)", "pradědeček mistra kolářského Otakara Krejska"],
              zam="sedlák v Blažkově čp. 26", bydl="Blažkov čp. 26", puvod="Blažkov",
              r=["blazkov_krest_jan_krejsek_1796", "josefsdorf_oddani_jan_krejsek_1825", "blazkov_umrti_vaclav_krejsek_1832"],
              note="Evangelický sedlák v Blažkově na rodovém gruntu čp. 26. Manžel Anny rozené Stehlíkové ze Zvole a otec sedláka Jana Krejska (* 1796). Zemřel v roce 1832 v Blažkově čp. 26 na epidemii asijské cholery (zápis v evangelické matrice zemřelých Nové Město na Moravě sv. 16719, detail 7380, sn. 118, pag. 233, č. 1)."),

    225: dict(n="Anna Krejsková", y="* před 1780", st="doc",
              f=["* před 1780 Zvole", "dcera sedláka ze Zvole", "matka Jana Krejska (* cca 1799)"],
              roz="Stehlíková", bydl="Blažkov čp. 26", puvod="Zvole",
              r=["josefsdorf_oddani_jan_krejsek_1825"],
              note="Dcera sedláka Stehlíka ze Zvole, manželka sedláka Václava Krejska v Blažkově."),

    226: dict(n="Václav Procházka", y="* před 1780", st="doc",
              f=["* před 1780", "otec Anny Procházkové (* cca 1800)"],
              zam="sedlák v Josefsdorfu (Storfu) čp. 5", bydl="Josefsdorf čp. 5", puvod="Josefsdorf",
              r=["josefsdorf_oddani_jan_krejsek_1825"],
              note="Sedlák ve familiantské vsi Josefsdorf (Storf) čp. 5 na pernštejnském panství (fara Rožná)."),

    227: dict(n="Terezie Procházková", y="* před 1780", st="doc",
              f=["* před 1780 Domanínek", "dcera sedláka Zubánka z Domanínku", "matka Anny Procházkové (* cca 1800)"],
              roz="Zubánková", bydl="Josefsdorf čp. 5", puvod="Domanínek (fara Bystřice n/P.)",
              r=["josefsdorf_oddani_jan_krejsek_1825"],
              note="Pocházela z rodiny sedláka Zubánka z Domanínku u Bystřice nad Pernštejnem."),

    228: dict(n="František Hamřík st.", y="† před 1847", st="doc",
              f=["* cca 1790–1800 Blažkov", "† před 10. 2. 1847 Blažkov čp. 14", "otec svobodníka Františka Hamříka ml."],
              zam="svobodník v Blažkově čp. 14", bydl="Blažkov čp. 14", puvod="Blažkov čp. 14",
              r=["zvole_oddani_frantisek_hamrik_1847"],
              note="Svobodník (Freysaß) v Blažkově na usedlosti čp. 14. Manžel Augustiny Josefy Valouškové."),

    229: dict(n="Augustina Josefa Hamříková", y="* před 1805", st="doc",
              f=["* před 1805 Zvole", "dcera Václava Valouška, mlynářského mistra ve Zvoli čp. 65", "matka svobodníka Františka Hamříka ml."],
              roz="Valoušková", bydl="Blažkov čp. 14", puvod="Zvole čp. 65",
              r=["zvole_oddani_frantisek_hamrik_1847"],
              note="Dcera Václava Valouška, mlynářského mistra na mlýně ve Zvoli čp. 65."),

    230: dict(n="František Falský", y="* cca 1795–1805 – po 1867", st="doc",
              f=["* cca 1795–1805 Blažkov", "otec Anny Hamříkové roz. Falské", "svědek na svatbě vnuka Václava Krejska 1867"],
              zam="svobodník v Blažkově čp. 28, hostinský a majitel usedlosti ve Zvoli čp. 10",
              bydl="Zvole čp. 10 a Blažkov čp. 28", puvod="Blažkov čp. 28",
              r=["zvole_oddani_frantisek_hamrik_1847", "blazkov_krest_marianna_hamrikova_1849", "blazkov_oddani_vaclav_krejsek_1867"],
              note="Významná osobnost regionu: svobodník v Blažkově čp. 28 a zároveň hostinský a gruntovník ve Zvoli čp. 10. Vlastnoručně podepsán na svatebním zápise dcery Anny v únoru 1847."),

    231: dict(n="Kateřina Falská", y="† před 1847", st="doc",
              f=["* cca 1800 Blažkov", "† před 10. 2. 1847", "dcera Františka Mišníčka, svobodníka v Blažkově čp. 28", "matka Anny Hamříkové roz. Falské"],
              roz="Mišníčková", bydl="Blažkov čp. 28 / Zvole čp. 10", puvod="Blažkov čp. 28",
              r=["zvole_oddani_frantisek_hamrik_1847"],
              note="Pocházela ze svobodnického rodu Mišníčků z Blažkova čp. 28; první manželka svobodníka a hostinského Františka Falského."),

    240: dict(n="Václav Černý", y="", st="doc",
              f=["× Anna Šišková"],
              zam="mistr kovářský v Dobšicích čp. 27", bydl="Dobšice čp. 27", puvod="Dobšice",
              r=["vlkov_oddani_frantisek_cerny_1856", "dobsice_krest_jan_cerny_1860"],
              note="Mistr kovářský v Dobšicích čp. 27 (fara Žehuň), manžel Anny roz. Šiškové z kovářského rodu v Žiželicích čp. 119. Otec kováře Františka Černého a dědeček kováře Jana Černého (* 1860)."),

    241: dict(n="Anna Černá", y="", st="doc",
              f=["× Václav Černý"],
              roz="Šišková", bydl="Dobšice čp. 27", puvod="Žiželice čp. 119",
              r=["vlkov_oddani_frantisek_cerny_1856", "dobsice_krest_jan_cerny_1860"],
              note="Pocházela z kovářské usedlosti v Žiželicích čp. 119 jako dcera mistra kovářského Jana Šišky. Manželka kováře Václava Černého z Dobšic čp. 27 a matka Františka Černého."),

    242: dict(n="Josef Michl", y="† před 1856", st="doc",
              f=["† před 1856", "× Anna Fialová"],
              zam="mistr kovářský ve Vlkově čp. 13", bydl="Vlkov čp. 13", puvod="Vlkov",
              r=["vlkov_oddani_frantisek_cerny_1856", "dobsice_krest_jan_cerny_1860", "podebrady_oddani_jan_cerny_1885"],
              note="Mistr kovářský ve Vlkově čp. 13, zemřel před 21. lednem 1856. Manžel Anny roz. Fialové z Lužan čp. 19. Otec Kateřiny provdané Černé a dědeček kováře Jana Černého."),

    243: dict(n="Anna Michlová", y="", st="doc",
              f=["× Josef Michl"],
              roz="Fialová", bydl="Vlkov čp. 13", puvod="Lužany čp. 19",
              r=["vlkov_oddani_frantisek_cerny_1856", "dobsice_krest_jan_cerny_1860"],
              note="Pocházela ze vsi Lužany čp. 19 jako dcera Jana Fialy. Manželka mistra kovářského Josefa Michla z kovářské chalupy ve Vlkově čp. 13, matka Kateřiny provdané Černé a babička kováře Jana Černého."),

    244: dict(n="Václav Hromada st.", y="† před 1853", st="doc",
              f=["† před 1853", "× Alžběta Jirkovská"],
              zam="gruntovník ve Vyšehořovicích čp. 22", bydl="Vyšehořovice čp. 22", puvod="Vyšehořovice",
              r=["kovanice_oddani_vaclav_hromada_1853", "chvalovice_krest_anna_hromadova_1864"],
              note="Gruntovník ve Vyšehořovicích čp. 22 na Českobrodsku, manžel Alžběty roz. Jirkovské z usedlosti čp. 25. Zemřel před 12. dubnem 1853. Otec gruntovníka Václava Hromady ml. z Chvalovic."),

    245: dict(n="Alžběta Hromadová", y="", st="doc",
              f=["× Václav Hromada"],
              roz="Jirkovská", bydl="Vyšehořovice čp. 22", puvod="Vyšehořovice čp. 25",
              r=["kovanice_oddani_vaclav_hromada_1853", "chvalovice_krest_anna_hromadova_1864"],
              note="Pocházela ze selského rodu Jirkovských z Vyšehořovic čp. 25 na Českobrodsku. Manželka gruntovníka Václava Hromady st. z čp. 22 a matka Václava Hromady ml. z Chvalovic."),

    246: dict(n="Josef Kovářík", y="", st="doc",
              f=["× Anna Homolová"],
              zam="výminkář a dříve gruntovník v Chvalovicích čp. 21", bydl="Chvalovice čp. 21", puvod="Chvalovice",
              r=["kovanice_oddani_vaclav_hromada_1853", "chvalovice_krest_anna_hromadova_1864"],
              note="Hospodář a gruntovník v Chvalovicích čp. 21, který roku 1853 předal grunt mladému zeti Václavu Hromadovi a dceři Anně a odešel na výminek. Dne 12. 4. 1853 vlastnoručně podepsal v matrice souhlas se sňatkem své dcery Anny. Manžel Anny roz. Homolové z Chrástu."),

    247: dict(n="Anna Kováříková", y="", st="doc",
              f=["× Josef Kovářík"],
              roz="Homolová", bydl="Chvalovice čp. 21", puvod="Chrást (okres Český Brod)",
              r=["kovanice_oddani_vaclav_hromada_1853", "chvalovice_krest_anna_hromadova_1864"],
              note="Pocházela z Chrástu na Českobrodsku, manželka výminkáře Josefa Kováříka v Chvalovicích čp. 21 a matka Anny provdané Hromadové."),

    248: dict(n="Antonín Měšťánek", y="† před 1858", st="doc",
              f=["† před 1858", "× Barbora Šafáříková"],
              zam="domkář a nádeník ve Dvorech čp. 2", bydl="Dvory čp. 2 (okres Kouřimský)", puvod="Dvory",
              r=["bojiste_oddani_vaclav_mestanek_1858", "bojiste_krest_josef_mestanek_1859"],
              note="Domkář a nádeník ve Dvorech čp. 2 na Kouřimsku. Manžel Barbory roz. Šafáříkové. Zemřel před říjnem 1858. Otec tesaře a dělostřeleckého záložníka Václava Měšťánka a dědeček Josefa Měšťánka (* 1859)."),

    249: dict(n="Barbora Měšťánková", y="", st="doc",
              f=["× Antonín Měšťánek"],
              roz="Šafáříková", bydl="Dvory čp. 2", puvod="Pečky (okres Kolín)",
              r=["bojiste_oddani_vaclav_mestanek_1858", "bojiste_krest_josef_mestanek_1859"],
              note="Pocházela z Peček na Kolínsku, manželka domkáře Antonína Měšťánka ze Dvorů čp. 2. Matka tesaře Václava Měšťánka a babička Josefa Měšťánka (* 1859)."),

    250: dict(n="Václav Kos", y="", st="doc",
              f=["× Marie Kollářová"],
              zam="domkář a tesař v Bojišti čp. 10", bydl="Bojiště čp. 10", puvod="Bojiště",
              r=["bojiste_oddani_vaclav_mestanek_1858", "bojiste_krest_josef_mestanek_1859", "koncice_oddani_josef_mestanek_1883", "koncice_krest_marie_mestankova_1885"],
              note="Domkář a tesař v Bojišti čp. 10 na Kolínsku. Manžel Marie roz. Kollářové z Peček čp. 55. Dne 4. 10. 1858 byl přítomen na svatbě své dcery Barbory s Václavem Měšťánkem v Pečkách a připojil svůj otcovský souhlas. Dědeček Josefa Měšťánka (* 1859)."),

    251: dict(n="Marie Kosová", y="", st="doc",
              f=["× Václav Kos"],
              roz="Kollářová", bydl="Bojiště čp. 10", puvod="Pečky čp. 55",
              r=["bojiste_oddani_vaclav_mestanek_1858", "bojiste_krest_josef_mestanek_1859"],
              note="Pocházela ze stavení čp. 55 v Pečkách na Kolínsku. Manželka domkáře a tesaře Václava Kosa z Bojiště čp. 10 a matka Barbory provdané Měšťánkové."),

    254: dict(n="Jiří Ouzký", y="† před 1862", st="doc",
              f=["† před 1862", "× Barbora Daníčková"],
              zam="domkař a baráčník v Končicích čp. 14", bydl="Končice čp. 14", puvod="Končice",
              r=["koncice_krest_katerina_ouzka_1862", "koncice_oddani_josef_mestanek_1883", "koncice_krest_marie_mestankova_1885"],
              note="Domkař a baráčník v Končicích čp. 14, zemřel před dubnem 1862. Manžel Barbory roz. Daníčkové z Končic čp. 12. Dědeček Kateřiny provdané Měšťánkové."),

    255: dict(n="Barbora Ouzká", y="", st="doc",
              f=["× Jiří Ouzký"],
              roz="Daníčková", bydl="Končice čp. 14", puvod="Končice čp. 12",
              r=["koncice_oddani_josef_mestanek_1883", "koncice_krest_marie_mestankova_1885"],
              note="Dcera Jiřího Daníčka z Končic čp. 12, manželka domkaře Jiřího Ouzkého z Končic čp. 14."),



    # 8. generace (144–147, 342, 352–363, 510)

    342: dict(n="Josef Táborský", y="", st="doc",

              f=[], bydl="Žleby čp. 7 / čp. 126",

              r=["zleby_krest_jan_jarolim_1863", "zleby_krest_emilie_jarolimova_1899"],

              note="Otec Kateřiny Táborské ze Žlebů; doložen v křestních zápisech vnuka Jana a pravnučky Emilie Jarolímových."),

    352: dict(n="František Holánek", y="", st="fam",

              f=[], bydl="Křižanov", r=[], note="Údaje z rodinného stromu PDF."),

    354: dict(n="Jan Sláma", y="", st="fam",

              f=["× Alžběta Dymáčková"], zam="tesař", bydl="Staré Ransko čp. 33", r=[], note="Údaje z rodinného stromu PDF."),

    355: dict(n="Alžběta Dymáčková", y="", st="fam",

              f=["× Jan Sláma"], r=[], note="Údaje z rodinného stromu PDF."),

    358: dict(n="Josef Haisler", y="", st="fam",

              f=[], bydl="Františkodol (Fraunsthal)", r=[], note="Údaje z rodinného stromu PDF."),

    360: dict(n="Vojtěch Šíma", y="", st="fam",

              f=[], bydl="Staré Ransko", r=[], note="Údaje z rodinného stromu PDF."),

    362: dict(n="Ondřej Halík", y="", st="fam",

              f=["× Kateřina Dušková"], r=[], note="Údaje z rodinného stromu PDF."),

    363: dict(n="Kateřina Dušková", y="", st="fam",

              f=["× Ondřej Halík"], r=[], note="Údaje z rodinného stromu PDF."),

    # 8. generace – doplněno z GEDCOM (353)

    353: dict(n='Mariana Žundálková', y='1764–1802', st='mh',

             f=['* 13. 8. 1764 Kundratice', '× 1. 2. 1791 Křižanov 37 František Holánek', '† 19. 10. 1802 Křižanov 37'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),



    510: dict(n="Jiří Daníček", y="† před 1885", st="doc",
              f=["† před 1885"],
              zam="domkař v Končicích čp. 12", bydl="Končice čp. 12", puvod="Končice",
              r=["koncice_oddani_josef_mestanek_1883", "koncice_krest_marie_mestankova_1885"],
              note="Domkař v Končicích čp. 12, otec Barbory provdané Ouzké a pradědeček Kateřiny provdané Měšťánkové."),



    # 9. generace (704–711)

    704: dict(n='Václav Holánek', y='1726–1787', st='mh',

             f=['* 23. 9. 1726 Křižanov', '× 10. 11. 1754 Křižanov Judita Holánková', '† 23. 11. 1787 Křižanov 37'],

             zam='kovář', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    705: dict(n='Judita Holánková', y='1734–1809', st='mh',

             f=['* 19. 10. 1734 Jívoví', '× 10. 11. 1754 Křižanov Václav Holánek', '† 18. 3. 1809 Křižanov 37'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    706: dict(n='Matěj Žundálek', y='1735–1800', st='mh',

             f=['* 2. 2. 1735', '× asi 1755 Alžběta Žundálková', '† 2. 4. 1800'],

             zam='sedlák', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    707: dict(n='Alžběta Žundálková', y='1738–1806', st='mh',

             f=['* 1738', '× asi 1755 Matěj Žundálek', '† 13. 5. 1806 Kundratice 24'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    708: dict(n='Jan Sláma', y='1715–1772', st='mh',

             f=['* 30. 3. 1715', '× 2. 2. 1744 Sopoty Rozálie Pokorná', '† 19. 6. 1772 Sopoty 12'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    709: dict(n='Rozálie Pokorná', y='1722–1773', st='mh',

             f=['* 1722', '× 2. 2. 1744 Sopoty Jan Sláma', '† 8. 4. 1773 Sopoty 12'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    710: dict(n='Karel Dymáček', y='1718–1772', st='mh',

             f=['* 11. 7. 1718 Ransko', '× 17. 9. 1752 Ransko Anna Dobrovolná', '† 6. 5. 1772 Ransko 9'],

             zam='slévač', pohreb='Krucemburk, sv. Mikuláš', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    711: dict(n='Anna Dobrovolná', y='1728–1780', st='mh',

             f=['* 1. 7. 1728', '× 17. 9. 1752 Ransko Karel Dymáček', '† 1780'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),



    # 10. generace (1408–1423)

    1408: dict(n='Vít Holánek', y='1680–1756', st='mh',

             f=['* asi 1680', '× 22. 7. 1720 Mariana Vodičková Škodová', '† 24. 5. 1756'],

             zam='kovář', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1409: dict(n='Mariana Vodičková Škodová', y='1681–1742', st='mh',

             f=['* 19. 5. 1681', '× 22. 7. 1720 Vít Holánek', '† 9. 7. 1742'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1410: dict(n='Josef Holánek', y='1701–1789', st='mh',

             f=['* 13. 3. 1701', '× 10. 2. 1726 Jívoví a Kundratice Barbora Havelková', '† 30. 7. 1789 Jívoví 1'],

             zam='sedlák', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1411: dict(n='Barbora Havelková', y='1704–1783', st='mh',

             f=['* 4. 12. 1704', '× 10. 2. 1726 Jívoví a Kundratice Josef Holánek', '† 19. 2. 1783 Jívoví 1'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1412: dict(n='Antonín Žundálek', y='1710–1750', st='mh',

             f=['* asi 1710', '× 24. 2. 1734 Margareta Cziczálková', '† asi 1750'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1413: dict(n='Margareta Cziczálková', y='1711–1741', st='mh',

             f=['* 15. 6. 1711', '× 24. 2. 1734 Antonín Žundálek', '† 30. 10. 1741'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1416: dict(n='Josef Sláma', y='1672–1732', st='mh',

             f=['* 1672', '× 18. 12. 1703 Alžběta Dymáčková', '† 4. 10. 1732 Sopoty'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1417: dict(n='Alžběta Dymáčková', y='1683–1751', st='mh',

             f=['* 1683', '× 18. 12. 1703 Josef Sláma', '† 14. 9. 1751 Sopoty'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1418: dict(n='František Pokorný', y='1700–1744', st='mh',

             f=['* asi 1700', '† asi 1744'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1420: dict(n='Tobiáš Dymáček', y='1686–1762', st='mh',

             f=['* 13. 6. 1686 Sobiňovská huť', '× 8. 11. 1711 Mariana Chlebečková', '† 2. 6. 1762 Ransko'],

             pohreb='Krucemburk, sv. Mikuláš', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1421: dict(n='Mariana Chlebečková', y='1694–1748', st='mh',

             f=['* 25. 8. 1694 Sobíňov', '× 8. 11. 1711 Tobiáš Dymáček', '† 26. 1. 1748 Ransko'],

             pohreb='Krucemburk, sv. Mikuláš', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1422: dict(n='Martin Dobrovolný', y='1697–1773', st='mh',

             f=['* 11. 11. 1697', '× 28. 1. 1725 Apolena Zrzavá', '† 5. 1. 1773 Krucemburk 102'],

             zam='sedlák', pohreb='Krucemburk, sv. Mikuláš', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1423: dict(n='Apolena Zrzavá', y='1704–1763', st='mh',

             f=['* 11. 3. 1704', '× 28. 1. 1725 Martin Dobrovolný', '† 30. 11. 1763 Krucemburk'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),



    # 11. generace (2816–2847)

    2816: dict(n='Jiří Holánek', y='1630–1706', st='mh',

             f=['* asi 1630', '× asi 1655 Dorota Holánková', '† 13. 10. 1706'],

             pohreb='Křižanov, sv. Václav', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2817: dict(n='Dorota Holánková', y='1635–1704', st='mh',

             f=['* asi 1635', '× asi 1655 Jiří Holánek', '† 6. 2. 1704'],

             pohreb='Křižanov, sv. Václav', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2818: dict(n='Řehoř Škoda', y='1643–1726', st='mh',

             f=['* asi 1643 Dolní Bory', '× 13. 2. 1678 Sklené Salomena Šebková', '† 1. 7. 1726 Dolní Bory'],

             zam='mlynář', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2819: dict(n='Salomena Šebková', y='1650–1715', st='mh',

             f=['* asi 1650', '× 13. 2. 1678 Sklené Řehoř Škoda', '† 5. 3. 1715'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2820: dict(n='Šebestian Holánek', y='1666–1747', st='mh',

             f=['* asi 1666', '× 3. 2. 1686 Mariana Skřípalová', '† 6. 8. 1747'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2821: dict(n='Mariana Skřípalová', y='1666–1748', st='mh',

             f=['* asi 1666 Sviny', '× 3. 2. 1686 Šebestian Holánek', '† 22. 8. 1748'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2822: dict(n='Jan Havelka', y='1672–1727', st='mh',

             f=['* 19. 5. 1672', '× 28. 1. 1703 Margita Pávková', '† 28. 8. 1727'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2823: dict(n='Margita Pávková', y='1680–1730', st='mh',

             f=['* 14. 3. 1680', '× 28. 1. 1703 Jan Havelka', '† asi 1730'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2824: dict(n='Jan Žundálek', y='1677–1727', st='mh',

             f=['* asi 1677', '× 13. 7. 1704 Jívoví a pernštejnské panství Mariana Karásková', '† 25. 1. 1727'],

             zam='šafář', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2825: dict(n='Mariana Karásková', y='1685–1733', st='mh',

             f=['* 2. 8. 1685', '× 13. 7. 1704 Jívoví a pernštejnské panství Jan Žundálek', '† 14. 9. 1733'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2826: dict(n='Jakub Cziczálek', y='1669–1737', st='mh',

             f=['* 7. 6. 1669', '× asi 1690 Magdalena Cziczálková', '† 25. 12. 1737'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2827: dict(n='Magdalena Cziczálková', y='1670–1736', st='mh',

             f=['* asi 1670', '× asi 1690 Jakub Cziczálek', '† 11. 5. 1736'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2834: dict(n='Jan Dymáček', y='1660–1705', st='mh',

             f=['* asi 1660 Sobíňov', '† asi 1705'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2840: dict(n='Tomáš Dymáček', y='1664–1710', st='mh',

             f=['* asi 1664', '× 11. 6. 1684 Sobíňov a Horní Studenec Dorota Jeigerová', '† asi 1710'],

             zam='slévač, správce v huti', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2841: dict(n='Dorota Jeigerová', y='1664–1710', st='mh',

             f=['* asi 1664 Horní Studenec', '× 11. 6. 1684 Sobíňov a Horní Studenec Tomáš Dymáček', '† asi 1710 Sobíňov'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2842: dict(n='Matěj Chlebeček', y='1662–1706', st='mh',

             f=['* 24. 2. 1662', '× 1. 10. 1685 Sopoty a pila pod Bílkem Alžběta Ambrožová', '† 7. 12. 1706 Sobíňov'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2843: dict(n='Alžběta Ambrožová', y='1665–1710', st='mh',

             f=['* asi 1665', '× 1. 10. 1685 Sopoty a pila pod Bílkem Matěj Chlebeček', '† asi 1710'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2844: dict(n='Jan Dobrovolný', y='1665–1725', st='mh',

             f=['* 1665 Benátky', '× 21. 10. 1685 Kateřina Pátková', '† 25. 11. 1725'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2845: dict(n='Kateřina Pátková', y='1665–1737', st='mh',

             f=['* 1665', '× 21. 10. 1685 Jan Dobrovolný', '† 27. 12. 1737'],

             pohreb='Krucemburk, sv. Mikuláš', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2846: dict(n='Martin Zrzavý', y='1668–1720', st='mh',

             f=['* 5. 12. 1668', '× 19. 1. 1698 Alžběta Fejtková', '† asi 1720'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2847: dict(n='Alžběta Fejtková', y='1678–1720', st='mh',

             f=['* asi 1678', '× 19. 1. 1698 Martin Zrzavý', '† asi 1720'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),



}



LINES = {
    8: ("Menšíkovi a Jirkovští", "Jihočeská a pražská větev – pradědeček František Xaver Menšík (* 1873 Jistebnice), pekaři v Jistebnici a hrdinové protinacistického odboje Linhartovi."),
    9: ("Pivničkovi a Tomíčkovi", "Pražská a kadaňská větev – babička MUDr. Ludmila Menšíková roz. Pivničková (1909–2007), učitel Jan Emanuel Pivnička a železniční přednosta Antonín Tomíček z Hauenštejnu."),
    10: ("Jarolímovi a Hůlkovi", "Obuvníci ze Žlebů, krejčí z Dolní Krupé a lesníci; dědeček Richard Jarolím (1927–2012)."),
    11: ("Holánkovi a Henzlovi", "Zámečníci a hamerníci ze Starého Ranska a truhláři z Hluboké; babička Zdenka Jarolímová roz. Holánková (* 1928)."),
    12: ("Čákiovi", "Slovenská řeckokatolická větev – pradědeček Juraj (Jiří) Čáki (* 13. 4. 1919 Dúbrava čp. 42), roľník Andrej Čáki (* 1891) a babička Júlia (* 1868) ze Zemplína."),
    13: ("Bubancovi", "Východoslovenská větev – prababička Marie Čákiová roz. Bubancová z podhorské obce Šmigovec pod Vihorlatem (okres Snina)."),
    14: ("Krejzkovi a Sýsovi", "Vysočinská větev – pradědeček MUDr. Miroslav Krejzek (1914–1978, Bystřice nad Pernštejnem / Žamberk), mistr kolářský Otakar Krejzek a hajný Leopold Sýs z Borovníka."),
    15: ("Černí a Měšťánkovi", "Polabská větev – prababička MUDr. Věra Krejzková roz. Černá (1917–2005), mistři kovářští Černí z Poděbrad a mistři tesařští Měšťánkovi z Končic."),
}



# Boční příbuzní: n = „Jméno (roky)“, t = text na stránce předka (plná data sem), vetev = karta ve stromu

# se stejnými poli jako osoba v P (n, y, f, roz, zam, bydl, puvod, pohreb, vztah) + manzel a deti.

SIDE = [

    dict(k=2, n="Jakub Menšík (* 1977)", t="Bratr Jana, * 8. 2. / 10. 2. 1977 Praha, bytem Praha 6 - Dejvice.", r=[],

         vetev=dict(n="Jakub Menšík", y="* 1977", f=["* 8. 2. 1977 Praha (v rodinném stromu též 10. 2. 1977)"], bydl="Praha 6 - Dejvice (Mozambická)", vztah="bratr Jana")),

    dict(k=3, n="Mgr. Lucie Černíková roz. Čákiová", t="Sestra Julie, Mgr., roz. Čákiová (manžel Aleš Černík, CIO v C.S.CARGO; děti David Černík * asi 2004 a Lenka Černíková * asi 2008).", r=[],

         vetev=dict(n="Mgr. Lucie Černíková", y="", roz="Čákiová", bydl="Praha (Stodůlky)", vztah="sestra Julie",

                    manzel=dict(n="Aleš Černík", y="", zam="ředitel IT (CIO)", bydl="Praha"),

                    deti=[dict(n="David Černík", y="* asi 2004", f=["* asi 2004 Praha"], bydl="Praha"),

                          dict(n="Lenka Černíková", y="* asi 2008", f=["* asi 2008 Praha"], bydl="Praha")])),

    dict(k=4, n="Ivan Menšík (asi 1942–2012)", t="Starší bratr Radima Menšíka (strýc Jana), syn Miroslava a Ludmily, * asi 1942 Praha, † 2012 Praha, pohřben v Čtyřkolech.", r=[],

         vetev=dict(n="Ivan Menšík", y="asi 1942–2012", f=["* asi 1942 Praha", "† 2012 Praha"], bydl="Praha",

                    pohreb="Čtyřkoly", vztah="bratr Radima")),

    dict(k=5, n="Lenka Hájková roz. Jarolímová (* 1962)", t="Mladší sestra Zdeňky (teta Jana), * 21. / 24. 4. 1962 Hradec Králové; manžel Ing. arch. Martin Hájek (* 1960 Smiřice, architekt), syn Ing. arch. Václav Hájek (* 17. 1. / 20. 2. 1983 Hradec Králové, architekt).", r=[],

         vetev=dict(n="Lenka Hájková", y="* 1962", f=["* 24. 4. 1962 Hradec Králové (v rodinném stromu též 21. 4. 1962)"], roz="Jarolímová", bydl="Hradec Králové (Františka Žaloudka 422)", vztah="sestra Zdeňky",

                    manzel=dict(n="Ing. arch. Martin Hájek", y="* 1960", zam="architekt", bydl="Smiřice"),

                    deti=[dict(n="Ing. arch. Václav Hájek", y="* 1983", f=["* 20. 2. 1983 Hradec Králové (v rodinném stromu též 17. 1. 1983)"], zam="architekt", bydl="Hradec Králové (Horova 1184)")])),

    dict(k=7, n="MUDr. Iva Gajdošová († 2013)", t="Lékařka (MUDr.), sestra Evy Čákiové (teta Julie), roz. Krejzková, † 2013 Hradec Králové; dcera Barbora Gajdošová (partner René Štefec, dcera Evelína Štefcová * 2013) a syn Marek Gajdoš.", r=[],

         vetev=dict(n="MUDr. Iva Gajdošová", y="† 2013", f=["† 2013 Hradec Králové"], roz="Krejzková", zam="lékařka", pohreb="Hradec Králové",

                    bydl="Hradec Králové", vztah="sestra Evy",

                    manzel=dict(n="MUDr. Gajdoš", y="", zam="lékař", bydl="Hradec Králové"),

                    deti=[dict(n="Barbora Gajdošová", y="", bydl="Hradec Králové / Praha",

                               manzel=dict(n="René Štefec", y="", zam="kominík", bydl="Praha"),

                               deti=[dict(n="Evelína Štefcová", y="* 2013", bydl="Praha", vztah="dcera")]),

                          dict(n="Marek Gajdoš", y="", bydl="Hradec Králové / Praha", manzel=dict(n="Valadez", y="", puvod="Mexiko", bydl="Praha"))])),

    dict(k=8, n="František Pavel Menšík (* 1901)", t="Starší bratr doc. Miroslava Menšíka (prastrýc Jana), * 1901 Praha, † v dětství Praha. Doložen v policejní konskripci karton 388, obraz 88.", r=[],

         vetev=dict(n="František Pavel Menšík", y="* 1901", f=["* 1901 Praha", "† v dětství Praha"], vztah="bratr Miroslava")),

    dict(k=8, n="Vlastimila Menšíková (* 1902)", t="Sestra doc. Miroslava Menšíka (prateta Jana), * 1902 Praha, dcera Františka a Pavlíny. Doložena v policejní konskripci karton 388, obraz 88.", r=[],

         vetev=dict(n="Vlastimila Menšíková", y="* 1902", f=["* 1902 Praha"], vztah="sestra Miroslava")),

    dict(k=34, n="Pavlína Berta Linhartová roz. Jirkovská (1854–1927)", t="Sestra Aloise Jirkovského, teta Pavlíny Menšíkové roz. Jirkovské a kmotra při jejím křtu. Narozena 24. 8. 1854 v Praze u křižovníků, oddána 20. 5. 1883 u Týna s Janem Linhartem (* 16. 4. 1854 Velké Číčovice, mlynářský chasník a záložník vozatajského pluku). Zemřela 27. 2. 1927 na Král. Vinohradech. Matka slavné odbojové rodiny bratří Linhartových.", r=["tyn_oddani_jan_linhart_1883"],
         vetev=dict(n="Pavlína Berta Linhartová", y="1854–1927", f=["* 24. 8. 1854 Praha (křest u sv. Františka)", "× 20. 5. 1883 Praha (Týnský chrám) Jan Linhart (* 1854 Číčovice)", "† 27. 2. 1927 Praha-Vinohrady"], roz="Jirkovská", vztah="sestra Aloise, teta Pavlíny")),

    dict(k=17, n="Bedřich Linhart (1886–1944)", t="Vlastní bratranec Pavlíny Menšíkové roz. Jirkovské. Narozen 9. 4. 1886 v Michli čp. 14, vrchní kriminální inspektor pražské policie, ruský legionář a klíčový představitel protinacistického odboje (krycí jméno „Polda“; spolupráce s Obranou národa, skupinou Tří králů a sítí ÚVOD). V letech 1939–1941 jako tlumočník v Petschkově paláci varoval ohrožené osoby a vynášel zprávy gestapa; v garáži a autě ukrýval vysílačku Sparta Ic. Zatčen v červenci 1942 a dne 20. 10. 1944 v 16:00 popraven gilotinou v pankrácké sekyrárně.", r=["tyn_oddani_jan_linhart_1883"],
         vetev=dict(n="Bedřich Linhart", y="1886–1944", f=["* 9. 4. 1886 Praha-Michle", "† 20. 10. 1944 Praha-Pankrác (popraven v sekyrárně)"], zam="vrchní kriminální inspektor policie, ruský legionář, protinacistický odbojář (Polda)", vztah="bratranec Pavlíny Menšíkové roz. Jirkovské")),

    dict(k=17, n="Otto Linhart (1895–1980)", t="Vlastní bratranec Pavlíny Menšíkové roz. Jirkovské. Narozen 24. 9. 1895 v Praze u sv. Františka, ruský legionář, poštovní revident na Hlavní poště v Praze a legendární radiotelegrafista ilegální vysílačky Sparta I (ÚVOD). Jako jediný ze čtyř bratří přežil protektorátní pronásledování gestapem v hluboké ilegalitě.", r=[],
         vetev=dict(n="Otto Linhart", y="1895–1980", f=["* 24. 9. 1895 Praha", "† 29. 3. 1980 Praha"], zam="poštovní úředník, ruský legionář, radiotelegrafista vysílačky Sparta I", vztah="bratranec Pavlíny Menšíkové roz. Jirkovské")),

    dict(k=17, n="Václav a Zdeněk Linhartovi", t="Bratři Bedřicha a Otto Linharta, bratranci Pavlíny Menšíkové roz. Jirkovské. Zdeněk Linhart (* 12. 5. 1888 Praha, † 17. 1. 1943 KT Stutthof), řidič tramvaje, poskytoval byt pro vysílání Jindřicha Klečky. Václav Linhart (* 21. 7. 1892 Praha, † 4. 7. 1942 Praha), kamenotiskař a odbojář, při zatýkání gestapem požil cyankáli. Sestry Marie a Ludmila přežily věznění v KT Ravensbrück.", r=[],
         vetev=dict(n="Václav a Zdeněk Linhartovi", y="† 1942, † 1943", f=["Václav: * 21. 7. 1892, † 4. 7. 1942 Praha (cyankáli při zatýkání)", "Zdeněk: * 12. 5. 1888, † 17. 1. 1943 KT Stutthof"], zam="odbojáři (Sparta I)", vztah="bratranci Pavlíny Menšíkové roz. Jirkovské")),

    dict(k=65, n="Václav Horych (* 1795)", t="Bratr Barbory Menšíkové roz. Horychové, měšťan v Jistebnici čp. 86. Narozen 4. 8. 1795 v čp. 136, oddán 18. 2. 1828 v Jistebnici s Marií Šmedlovou (čp. 197). V roce 1865 byl svědkem na svatbě svého synovce Josefa Menšíka ml. a Marie Šmedlové.", r=["jistebnice_oddani_josef_mensik_1828", "jistebnice_oddani_josef_mensik_1865"],

         vetev=dict(n="Václav Horych", y="* 1795", f=["* 4. 8. 1795 Jistebnice čp. 136", "× 18. 2. 1828 Jistebnice Mariana Šmedlová"], zam="měšťan v Jistebnici čp. 86", vztah="bratr Barbory")),

    dict(k=12, n="Miroslav Čáky", t="Bratr Juraje Čákiho, původem ze Slovenska (Zemplín / Snina).", r=[],

         vetev=dict(n="Miroslav Čáky", y="", puvod="Slovensko (Zemplín / Snina)", vztah="bratr Juraje (psán Čáky)")),

    dict(k=14, n="Ladislav Krejzek (* 1905)", t="Nejstarší bratr primáře MUDr. Miroslava Krejzka, syn mistra kolářského Otakara Krejzka a Františky roz. Sýsové. Narozen roku 1905, odborný učitel v Bystřici nad Pernštejnem č. p. 451 (učitelské zkoušky v Brně 1925 a 1928). Dne 12. 6. 1943 byl svědkem na svatbě bratra MUDr. Emila Krejzka v Bystřici nad Pernštejnem.", r=["bystrice_oddani_emil_krejzek_1943"],

         vetev=dict(n="Ladislav Krejzek", y="* 1905", f=["* 1905"], zam="odborný učitel v Bystřici nad Pernštejnem č. p. 451", bydl="Bystřice nad Pernštejnem č. p. 451", vztah="nejstarší bratr Miroslava")),

    dict(k=14, n="Otakar Krejzek ml. (* cca 1908–1909)", t="Starší bratr primáře MUDr. Miroslava Krejzka z Bystřice nad Pernštejnem č. p. 147 / 433, syn mistra kolářského Otakara Krejzka a Františky roz. Sýsové. V letech 1928–1930 student učitelského ústavu v Brně, později poručík pěšího pluku 31 v Jihlavě (1935–1937).", r=[],

         vetev=dict(n="Otakar Krejzek ml.", y="* cca 1908–1909", f=["* cca 1908–1909 Bystřice nad Pernštejnem č. p. 147"], zam="učitel, poručík pěšího pluku 31 v Jihlavě", bydl="Bystřice nad Pernštejnem / Jihlava", vztah="bratr Miroslava")),

    dict(k=14, n="Bedřich Krejzek (* cca 1909–1910)", t="Starší bratr primáře MUDr. Miroslava Krejzka z Bystřice nad Pernštejnem č. p. 147 / 433, syn mistra kolářského Otakara Krejzka a Františky roz. Sýsové. V letech 1928–1930 student učitelského ústavu v Brně.", r=[],

         vetev=dict(n="Bedřich Krejzek", y="* cca 1909–1910", f=["* cca 1909–1910 Bystřice nad Pernštejnem č. p. 147"], zam="student učitelského ústavu v Brně (1928–1930)", bydl="Bystřice nad Pernštejnem", vztah="bratr Miroslava")),

    dict(k=14, n="MUDr. Emil Krejzek (* 1910)", t="Starší bratr primáře MUDr. Miroslava Krejzka, syn mistra kolářského Otakara Krejzka a Františky roz. Sýsové. Narozen 11. 10. 1910 v Bystřici nad Pernštejnem (křestní matrika tom. XIII, pag. 106), absolvent reálného gymnázia v Tišnově (1925–1929), praktický lékař (MUDr.) v Bystřici nad Pernštejnem č. p. 433 a č. p. 404. Dne 12. 6. 1943 oddán v Bystřici nad Pernštejnem s Miroslavou (Miladou) Šípkovou-Křížovou (* 20. 1. 1914 Olomouc – Nová Ulice). Dne 7. 4. 1949 šel spolu s bratrem MUDr. Miroslavem Krejzkem za svědka na svatbě nejmladšího bratra Václava.", r=["bystrice_oddani_emil_krejzek_1943", "bystrice_oddani_vaclav_krejzek_1949"],

         vetev=dict(n="MUDr. Emil Krejzek", y="* 1910", f=["* 11. 10. 1910 Bystřice nad Pernštejnem č. p. 147", "× 12. 6. 1943 Bystřice nad Pernštejnem Miroslava (Milada) Šípková-Křížová"], zam="praktický lékař (MUDr.) v Bystřici nad Pernštejnem", bydl="Bystřice nad Pernštejnem č. p. 433 a č. p. 404", vztah="bratr Miroslava",
                    manzel=dict(n="Miroslava (Milada) Šípková-Křížová", y="* 1914", f=["* 20. 1. 1914 Olomouc – Nová Ulice"], zam="soukromá úřednice", bydl="Brno / Bystřice nad Pernštejnem"))),

    dict(k=14, n="MUDr. Václav Krejzek (* 1919)", t="Nejmladší bratr primáře MUDr. Miroslava Krejzka, syn mistra kolářského Otakara Krejzka a Františky roz. Sýsové. Narozen 25. 3. 1919 v Bystřici nad Pernštejnem (křestní matrika tom. XII, pag. 224), v letech 1933–1938 student reálného gymnázia v Tišnově, absolvent medicíny a lékař (MUC. / MUDr.) v Bystřici nad Pernštejnem č. p. 433. Dne 7. 4. 1949 oddán na Starém Brně s poštovní úřednicí Naděždou Smetanovou (* 3. 10. 1926 Svitavy) za svědectví bratrů MUDr. Emila Krejzka a MUDr. Miroslava Krejzka.", r=["bystrice_oddani_vaclav_krejzek_1949"],

         vetev=dict(n="MUDr. Václav Krejzek", y="* 1919", f=["* 25. 3. 1919 Bystřice nad Pernštejnem č. p. 147", "× 7. 4. 1949 Staré Brno Naděžda Smetanová"], zam="lékař (MUC. / MUDr.)", bydl="Bystřice nad Pernštejnem č. p. 433", vztah="bratr Miroslava",
                    manzel=dict(n="Naděžda Smetanová", y="* 1926", f=["* 3. 10. 1926 Svitavy"], zam="poštovní úřednice", bydl="Brno"))),

    dict(k=15, n="bratr Věry Černé", t="Bratr Věry Krejzkové roz. Černé, syn Josefa Černého.", r=[],

         vetev=dict(n="bratr Černý", y="", vztah="bratr Věry, syn Josefa")),

    dict(k=21, n="Josefa Haňavcová roz. Jarolímová", t="Sestra Emilie, Žleby čp. 37. Manžel Rudolf Haňavec (* 22. 10. 1896 Žleby čp. 190), dcera Hana Hrachová roz. Haňavcová (Žleby / Rumburk, manžel Jan Hrach, † Rumburk).", r=[],

         vetev=dict(n="Josefa Haňavcová", y="", roz="Jarolímová", bydl="Žleby čp. 37", vztah="sestra Emilie",

                    manzel=dict(n="Rudolf Haňavec", y="* 1896", f=["* 22. 10. 1896 Žleby čp. 190"]),

                    deti=[dict(n="Hana Hrachová", y="", roz="Haňavcová", bydl="Žleby / Rumburk",

                               manzel=dict(n="Jan Hrach", y="", f=["† Rumburk"], bydl="Rumburk"))])),

    dict(k=21, n="Rudolf Jarolím (* 1903)", t="Bratr Emilie, * 1. 10. 1903 Žleby čp. 37. Syn Jaroslav Jarolím (* 10. 6. 1927 Žleby – † 10. 5. 2012 New York).", r=[],

         vetev=dict(n="Rudolf Jarolím", y="* 1903", f=["* 1. 10. 1903 Žleby čp. 37"], vztah="bratr Emilie",

                    deti=[dict(n="Jaroslav Jarolím", y="1927–2012", f=["* 10. 6. 1927 Žleby", "† 10. 5. 2012 New York"],

                               bydl="New York (ze Žlebů)")])),

    dict(k=22, n="Helena Měřínská roz. Holánková (1896–1982)", t="Sestra Julia, * 1896 Staré Ransko čp. 55. Manžel František Měřínský (* 4. 6. 1890 Staré Ransko – † 1951), syn Miloš Měřínský (1924–1998, architekt; manželka Jitka Měřínská * 1942, učitelka), vnučka Jitka Měřínská (* 1979, Brno).", r=[],

         vetev=dict(n="Helena Měřínská", y="1896–1982", f=["* 1896 Staré Ransko čp. 55", "† 1982"], roz="Holánková", vztah="sestra Julia",

                    manzel=dict(n="František Měřínský", y="1890–1951", f=["* 4. 6. 1890 Staré Ransko", "† 1951"]),

                    deti=[dict(n="Miloš Měřínský", y="1924–1998", zam="architekt",

                               manzel=dict(n="Jitka Měřínská", y="* 1942", zam="učitelka"),

                               deti=[dict(n="Jitka Měřínská", y="* 1979", bydl="Brno")])])),

    dict(k=43, n="Ignác Havel (* 1864)", t="Bratr Antonie Havlové, * 9. 7. 1864 Dolní Krupá čp. 42, syn mistra krejčovského Jana Havla a Anny Jeřábkové.", r=[],

         vetev=dict(n="Ignác Havel", y="* 1864", f=["* 9. 7. 1864 Dolní Krupá čp. 42"], vztah="bratr Antonie")),

    dict(k=43, n="Otilie Havlová (* 1876)", t="Sestra Antonie Havlové, * 12. 12. 1876 Slatina nad Úpou, v domácnosti.", r=[],

         vetev=dict(n="Otilie Havlová", y="* 1876", f=["* 12. 12. 1876 Slatina nad Úpou"], zam="v domácnosti", vztah="sestra Antonie")),

]



ISSUES = [

    ("Otcovská větev Menšíků – narození a rodiče doc. RNDr. Miroslava Vladimíra Menšíka (* 3. 8. 1906 Praha, č. 8)", "Vyřešeno z primárních matrik: Miroslav Vladimír Menšík se narodil 3. 8. 1906 v Praze čp. 1717-II a byl pokřtěn 9. 8. 1906 v kostele Nejsv. Trojice v Podskalí (TRP N15, sn. 56). Rodiče František Xaver Menšík (* 8. 7. 1873 Jistebnice) a Pavlína Rosalie roz. Jirkovská (* 2. 11. 1882 Praha) oddáni 8. 5. 1902 u Týna."),

        ("Otcovská větev Menšíků – rodné příjmení a rodiče babičky MUDr. Ludmily Menšíkové (č. 9)", "Vyřešeno z primárních matrik, archiválií a evidence SPH: babička MUDr. Ludmila Menšíková byla rozená Pivničková (1909–2007), dětská lékařka, dcera měšťanského učitele na Hradčanech Jana Emanuela Pivničky (1872–po 1921) a Emmy Marie roz. Tomíčkové (* 1886 Warta). Doloženi i prarodiče Josef Pivnička (* 1844 Čechtice) & Antonie roz. Grubnerová (* 1843 Dobříš) a přednosta stanice Antonín Tomíček & Anna roz. Halíková z Lobče."),

    ("Větev manželky Julie Menšík Čákiové (prarodiče dětí č. 12–15)", "Vyřešeno z rodinných údajů: všichni 4 prarodiče Julie jsou identifikováni – Juraj (Jiří) Čáki (* asi 1921, č. 12) & Marie roz. Bubancová (č. 13) z otcovy strany, Miroslav Krejzek (1914–1978, č. 14) & Věra roz. Černá (1917–2005, č. 15) z matčiny strany."),

    ("Původ pradědečka Fridricha Hůlka (č. 20)", "Otevřené: v PDF je uveden jako lesní inženýr s fotografií, ale bez data a místa narození; jeho syn Richard (* 1927 Žleby čp. 17) nesl příjmení matky Jarolím."),

    ("Povolání Matěje Šímy (č. 90) ze Starého Ranska čp. 2", "Otevřené: v PDF je uvedeno 'horolezec' – v matrice Starého Ranska ověřit, zda nešlo o čtení slova 'horník' / 'havíř' u železáren."),

    ("Původ a narození pradědečka Otakara Krejzka st. (* cca 1880–1885) a prababičky Františky roz. Sýsové", "Plně vyřešeno z evangelických matrik Nového Města na Moravě (svazek 16712, detail 11619, sn. 16, č. 20): pradědeček se narodil 6. 5. 1877 v Blažkově čp. 20 jako Otakar Jan Krejzek v rodině evangelického rolníka Václava Krejska a Marie roz. Hamříkové. Následně dohledána celá rodová linie: sňatek rodičů 1867, sňatek prarodičů Františka Hamříka a Anny Falské 1847 (svobodníci v Blažkově čp. 14 a 28) a sňatek Jana Krejska a Anny Procházkové 1825 (oddáni pastorem Gedeonem Šlachtou z Veselí). (1943 a 1949): prababička Františka Krejzková byla rozená Sýsová, dcera hajného Leopolda Sýse z Borovníka (č. 58), a všichni šest synů Otakara a Františky Krejzkových jsou jmenovitě doloženi (Ladislav * 1905, Otakar ml., Bedřich, MUDr. Emil * 1910, MUDr. Miroslav * 1914, MUDr. Václav * 1919). V indexu narozených Bystřice (1834–1883) ani Nového Města žádný Otakar Krejzek zapsán není; hypotéza o otcovství nadučitele Augustina Korejzla byla archivně vyvrácena. Kolářská rodina Krejzků má své nejhlubší kořeny v sousední farnosti Strážek (čp. 21 a 23, Tomáš a František Krejzek). Hajný Leopold Sýs sloužil v Borovníku na panské hájovně dočasně a sňatek Otakara Krejzka s Františkou Sýsovou (před r. 1905) se konal mimo farnosti Bystřice, Březí a Heřmanov."),
]



HYPOTEZY = [

]



SAME = {}

