# Rodokmen – skill a plugin pro Gemini & Antigravity

![Rodokmen z matrik a rodinný web – vějíř předků, mapa a zajímavosti](docs/banner.jpg)

Gemini v aplikaci **Google Antigravity** (nebo **Gemini CLI**) vás provede tvorbou rodokmenu **od rodinných vzpomínek přes digitalizované matriky až k hezkému rodinnému webu**
s vějířem předků, mapou, příběhem rodu a výřezy původních zápisů s přepisem a překladem.
Je určený pro lidi, kteří genealogii nikdy nedělali a neprogramují – technickou práci dělá Gemini, vy dodáváte
znalost rodiny a rozhodujete.

Tento repozitář je **fork projektu [sarsonj/rodokmen-skill](https://github.com/sarsonj/rodokmen-skill)** od Jindřicha Šaršona, přetransformovaný a upravený pro **Gemini** a **Google Antigravity** (`plugin.json`, `gemini-extension.json`, `GEMINI.md`, podpora subagentů přes `invoke_subagent`, PowerShell relací na Windows a multimodálního čtení snímků).

> **Než začnete**
>
> Tento skill **nenahrazuje genealoga** ani zkušeného badatele. Je to pomůcka, která umí rychle projít hodně matrik.
> Umělá inteligence ale dělá chyby: špatně přečte jméno, splete si dva Jany ze stejné vsi nebo spojí rodiny, které
> k sobě nepatří. Skill se tomu snaží bránit – u každého údaje je zdroj a výřez původního zápisu, údaje se navzájem
> kontrolují a nejisté věci jsou označené. Za správnost rodokmenu ale ručíte vy. Používáte ho na vlastní odpovědnost.
>
> Kdo potřebuje rodokmen, na který se dá spolehnout (dědictví, publikace, sporné případy), nebo se zasekne na místě,
> kam matriky nestačí, ať se obrátí na genealoga. Začít můžete u
> [České genealogické a heraldické společnosti](https://www.genealogie.cz) (Praha a pobočky po Čechách) nebo
> u [Moravské genealogické a heraldické společnosti](https://www.mghs.cz) (Brno). Obě pořádají kurzy a přednášky
> a mají knihovnu. Rodokmen ze skillu, kde je u každého údaje zdroj a snímek, může genealogovi posloužit jako dobrý
> podklad.

## Jak vypadá web
Ukázkový web s vymyšlenou rodinou Novákových (260 předků v 11 generacích) má na úvodní stránce příběh rodu, zajímavosti,
mapu, kde předci žili, osm rodů a vějíř předků. Další stránky: rodokmen po rodinách, karty osob, výřezy zápisů
s přepisem a překladem, „Co hledáme“ a deník hledání. **[Podívejte se na celou úvodní stránku ukázky →](docs/ukazka-web.png)**

## Co budete potřebovat
- **Google Antigravity** (aplikace nebo CLI `agy`) případně **Gemini CLI**.
- **Počítač s Windows nebo macOS** (na Windows 11 s Pythonem z python.org a Git Bashem).
- Programy **Python 3, Node.js, ImageMagick a git**. Nemusíte je instalovat předem – Gemini zkontroluje, co chybí,
  a pomůže s instalací (na Macu přes [Homebrew](https://brew.sh), na Windows přes `winget`).
- Volitelně účet na [Netlify](https://www.netlify.com) (zdarma), pokud chcete web zveřejnit pro rodinu.

## Jak pracují modely v Antigravity
- **Hlavní model (Gemini Pro):** vede rozhovor, ověřuje každé čtení přímo na výřezu matriky v plném rozlišení (`read_file`), zapisuje do dat projektu a píše příběhy.
- **Pomocníci / subagenti (Gemini Flash):** při procházení větších svazků matrik spouští hlavní agent 2–4 paralelní pomocníky (`invoke_subagent` s `TypeName: "self"` a `Model: "flash"`), kteří vyhledají kandidátní zápisy do složky `pracovni/`. Každý nález pak hlavní model ověří na snímku (princip čtyř očí).

## Instalace v Antigravity a Gemini

### Varianta A – jako plugin v Antigravity (doporučeno)
Naklonujte tento repozitář a nainstalujte ho přes `agy` CLI nebo zkopírováním do složky pluginů:
```bash
git clone <url-tohoto-repozitare> rodokmen-skill
agy plugin install ./rodokmen-skill
```
Případně naklonujte repozitář přímo do globální složky pluginů Antigravity:
- **Windows:** `C:\Users\<jméno>\.gemini\config\plugins\rodokmen`
- **macOS / Linux:** `~/.gemini/config/plugins/rodokmen`

Po instalaci restartujte Antigravity.

### Varianta B – jako samostatný skill
Zkopírujte složku `skills/rodokmen` do globální složky skillů:
- **Windows:** `C:\Users\<jméno>\.gemini\config\skills\rodokmen`
- **macOS / Linux:** `~/.gemini/config/skills/rodokmen`

(Výsledek: `~/.gemini/config/skills/rodokmen/SKILL.md`.)

### Varianta C – přímo v otevřeném workspace
Repozitář obsahuje `.agents/skills.json`, takže pokud otevřete samotnou složku tohoto repozitáře jako workspace v Antigravity, skill `rodokmen` se načte automaticky.

## První spuštění
1. Otevřete Antigravity (nebo spusťte `agy`) a napište:
   > Chci udělat rodokmen své rodiny.
2. Gemini zkontroluje potřebné programy, založí složku projektu (např. `~/Rodokmen`) se souborem pravidel `GEMINI.md` a začne se ptát na rodinu.
   Připravte si, co víte o rodičích, prarodičích a pradědečcích, a rodinné dokumenty (rodné a oddací listy, parte,
   fotky, kroniky) – stačí vyfotit mobilem.
3. **Příště otevírejte v Antigravity přímo složku projektu** (např. `~/Rodokmen`). Díky souboru `GEMINI.md` a `data/STAV.md` si Gemini automaticky přečte, kde jste skončili, a plynule naváže.

Chcete nejdřív vidět, jak web vypadá? Řekněte: *„Ukaž mi ukázkový web.“* Gemini založí ukázkový projekt
s vymyšlenou rodinou a spustí náhled na pozadí.

## Jak to probíhá
| Fáze | Co děláte vy | Co dělá Gemini v Antigravity |
|---|---|---|
| 0. Příprava | potvrdíte instalaci programů | založí projekt (`GEMINI.md`, `data/`, `web/`, `tools/`) |
| 1. Rozhovor | vyprávíte, dodáte dokumenty, zeptáte se příbuzných | zapisuje, čte dokumenty, navrhuje otázky |
| 2. Matriky | rozhodujete sporná místa | hledá svazky, stahuje a čte zápisy, dělá výřezy, přepisy a překlady, vede deník hledání |
| 3. Příběhy | doplníte rodinné historky, schválíte texty | průběžně sbírá zajímavosti, napíše „Příběh <vašeho rodu>“ |
| 4. Web | díváte se a říkáte, co upravit | staví web a spouští živý náhled na pozadí |
| 5. Zveřejnění | založíte účet na Netlify, schválíte obsah | nasadí web s přihlášením rodinnou otázkou |

Matriky jsou online jen do určitého data: narození starší než 100 let, sňatky 75 a úmrtí 30 let.
O mladší údaje se žádá na matričním úřadě. Gemini vám řekne, kdy to je potřeba.

## Co je v repozitáři
```
plugin.json             manifest pluginu pro Google Antigravity
gemini-extension.json   manifest rozšíření pro Gemini CLI
.agents/skills.json     automatické načtení skillu při otevření repozitáře v Antigravity
skills/rodokmen/
  SKILL.md              průvodce pro Gemini (fáze, pravidla, subagenti)
  reference/            podrobné návody: čtení matrik, portály archivů, formát dat, web, soukromí,
                        metodická příručka (playbook, anglicky)
  tools/                nástroje v Pythonu (ARON, výřezy, rámečky, mapa, kontrola dat, export do webu, vějíř)
  template/             šablona projektu: GEMINI.md, prázdná data, ukázková rodina, web (Astro)
```

## Co umí a co ne
- **Hotové nástroje** (bez prohlížeče) mají: východní Čechy (SOA Zámrsk, ARON), jižní Čechy (SOA Třeboň,
  včetně dobrovolnických rejstříků), západní Čechy (SOA Plzeň, Porta fontium), střední Čechy (SOA Praha, eBadatelna –
  i urbáře a gruntovní knihy) a Prahu (AHMP a policejní přihlášky 1850–1914). Pro severní Čechy (SOA Litoměřice)
  stahuje snímky nástrojem, knihu ale najde přes prohlížeč. Pro Rakousko je postup přes Matriculu.
- Ostatní archivy (Brno, Opava) obsluhuje obecným postupem přes integrovaný prohlížeč v Antigravity (`chrome-devtools-mcp`).
  Funguje to, ale je to pomalejší.
- U úředníků, vojáků a lékařů hledá i v **dobových novinách** (ANNO, Kramerius) – kariéra, vyznamenání, parte.
- Umí načíst **rodinný strom z MyHeritage** a dalších služeb (export GEDCOM, z MyHeritage i zálohu stromu z programu
  Family Tree Builder) a udělat z něj plán hledání.
- Průběžně sbírá **zajímavosti** (svatby na poslední chvíli, rod sto let v jednom domě…) a s vámi napíše
  **Příběh vašeho rodu** – hlavní článek webu.
- Ke každému zápisu ukládá výřez s vyznačeným místem, aby se to dalo zkontrolovat, a nejistá místa označuje otazníkem.
- Placené služby (MyHeritage, Ancestry) hromadně neprochází – vede to k zablokování účtu.

## Soukromí
Projekt obsahuje osobní údaje vaší rodiny. Zůstává na vašem počítači. Web je chráněný rodinnou otázkou
a není indexovaný vyhledávači; bez nastavené otázky ho nástroj nenasadí. Je to lehká ochrana proti náhodným
návštěvníkům, ne trezor: kdo zná odpověď, vidí všechno, co na web dáte. Gemini má pokyn psát o žijících lidech
jen jméno a rok narození a před zveřejněním s vámi projít, co o nich web říká – kód to ale nevynucuje,
rozhodnutí je na vás.
Pokud projekt chcete zálohovat na GitHub, použijte **soukromý** repozitář.

## Bezpečnost
Skill je obyčejný text (návod pro Gemini) a sada skriptů v Pythonu. Všechno si můžete před instalací prohlédnout
tady v repozitáři.
- **Žádný automaticky spouštěný kód.** Plugin nemá hooky ani vlastní MCP servery. Skripty spouští jen Gemini, když je
  při práci potřebuje.
- **Kam skripty sahají:** zapisují do složky projektu rodokmenu (stažené snímky, mezivýsledky, web).
  Výjimkou jsou dočasné soubory systému, npm při instalaci webu a přihlášení nástroje pro nasazení (Netlify,
  CapRover), pokud web zveřejňujete. Mimo projekt nic nemažou ani nepřepisují.
- **Na které servery chodí:** archivní portály (ARON SOA Zámrsk, SOA Třeboň, SOA Plzeň – Porta fontium, SOA Praha –
  eBadatelna, AHMP, Národní archiv, SOA Litoměřice, Matricula), noviny (ANNO, Kramerius), OpenStreetMap (mapa
  a souřadnice obcí) a při instalaci webu registr npm.
  Na Netlify jen tehdy, když web sami zveřejníte. Nikam jinam nic neposílají, ani vaše data, ani poznámky.

## Původní autor a licence
Původní projekt [sarsonj/rodokmen-skill](https://github.com/sarsonj/rodokmen-skill) vytvořil **Jindřich Šaršon**.
Skill je pod licencí [MIT](LICENSE): smíte ho volně používat, upravovat a šířit dál, jen zachovejte uvedení autora.
Výjimkou je metodická příručka `skills/rodokmen/reference/playbook.md`. Je to převzatá rešeršní zpráva bez uvedeného
autora, licence MIT se na ni nevztahuje (podrobnosti na začátku souboru).
