"""Bygger takskottning.html ur index.html: samma stil, sidhuvud, sidfot och skript, nytt innehåll.

    python bygg_takskottning.py

Kör om efter ändringar i index.html så att sidorna hålls i takt.
"""
import re
from pathlib import Path

HÄR = Path(__file__).parent
s = (HÄR / "index.html").read_text(encoding="utf-8")

TITEL = "Takskottning i Stockholm – säsongsavtal och jour | Hammarby ByggXpert AB"
BESKR = ("Takskottning och borttagning av istappar i Stockholm. Säsongsavtal för bostadsrättsföreningar och "
         "fastighetsägare, utryckning inom 24 timmar, licens enligt Skotta säkert, avspärrning och vakt.")

EXTRA_CSS = """
  .faktakort{background:var(--ink);color:var(--bone);padding:2.2rem 2rem;align-self:center}
  .faktakort h3{font-family:'Archivo',sans-serif;color:var(--gold);font-size:1.05rem;letter-spacing:.06em;
    text-transform:uppercase;margin:0 0 1.1rem}
  .faktakort ul{list-style:none;margin:0;padding:0}
  .faktakort li{padding:.55rem 0;border-bottom:1px solid rgba(255,255,255,.12);display:flex;gap:.7rem}
  .faktakort li:last-child{border-bottom:0}
  .faktakort li::before{content:"✓";color:var(--gold);font-weight:700}
  .pris{width:100%;border-collapse:collapse;margin-top:1rem;font-size:.98rem}
  .pris th{text-align:left;background:var(--ink);color:var(--bone);padding:.75rem .9rem;font-weight:600}
  .pris td{padding:.75rem .9rem;border-bottom:1px solid #DDD8CF;vertical-align:top}
  .pris td:nth-child(2){white-space:nowrap;font-weight:600}
  .pris-not{font-size:.88rem;color:var(--steel);margin-top:.8rem}
  .faq details{border-bottom:1px solid #DDD8CF;padding:1rem 0}
  .faq summary{cursor:pointer;font-weight:600;font-size:1.05rem}
  .faq details p{margin:.7rem 0 0;color:var(--steel)}
  .wrap-smal{max-width:62rem}
"""

MAIN = """
<main>

  <section class="hero">
    <div class="hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">Takskottning · Istappar · Snöras · Stockholm</p>
        <h1>Snöfria tak.<br>Säkra trottoarer.<br><em>Inga överraskningar.</em></h1>
        <p class="hero-lead">
          Som fastighetsägare ansvarar ni för att snö och is på taket inte rasar ner på någon.
          Med ett säsongsavtal håller vi koll på era tak hela vintern och skottar när det behövs –
          med licensierad personal, avspärrning och vakt på marken.
        </p>
        <div class="hero-actions">
          <a href="#kontakt" class="btn">Begär offert</a>
          <a href="tel:+46708997312" class="btn btn-ghost">Ring 070-899 73 12</a>
        </div>
      </div>
      <div class="faktakort">
        <h3>Säsongsavtal 2026/27</h3>
        <ul>
          <li>Tillsyn efter snöfall och töväder</li>
          <li>Utryckning inom 24 timmar</li>
          <li>Även kvällar, helger och röda dagar</li>
          <li>Licens enligt Skotta säkert</li>
          <li>Avspärrning och vakt på marken</li>
          <li>Ansvars- och entreprenadförsäkring</li>
          <li>Arbetsrapport efter varje tillfälle</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="varfor">
    <div class="sec-head reveal">
      <div class="dim"><span class="dim-label">01 — Ert ansvar</span><span class="dim-rule"></span></div>
      <h2>Snö på taket är<br>fastighetsägarens sak</h2>
      <p class="sec-intro">
        Enligt ordningslagen ska fastighetsägaren se till att snö och is på taket inte orsakar skada
        för den som går förbi. Rasar ett snöras eller en istapp ner på en person eller en bil är det
        föreningen eller fastighetsägaren som står för följderna. Ett säsongsavtal gör att ni slipper
        jaga en entreprenör samma morgon som alla andra.
      </p>
    </div>
  </section>

  <section id="ingar" class="ram">
    <div class="sec-head reveal">
      <div class="dim"><span class="dim-label">02 — Det här ingår</span><span class="dim-rule"></span></div>
      <h2>Hela vintern,<br>en kontakt</h2>
    </div>
    <div class="ram-grid reveal">
      <div class="ram-list">
        <div class="ram-item">
          <h3>Tillsyn och bedömning</h3>
          <p>Vi tittar till taken efter snöfall och vid töväder och bedömer när skottning behövs. Vi hör alltid av oss innan vi skottar.</p>
        </div>
        <div class="ram-item">
          <h3>Prioriterad utryckning</h3>
          <p>Arbetet påbörjas inom 24 timmar från beställning eller vår bedömning – vid akut rasrisk så snart som möjligt.</p>
        </div>
        <div class="ram-item">
          <h3>Skottning, istappar och isvallar</h3>
          <p>Snö på tak och takfot, istappar och isvallar över entréer och trottoar, samt rensning runt takbrunnar, ventilationshuvar och takfönster.</p>
        </div>
        <div class="ram-item">
          <h3>Rapport efter varje tillfälle</h3>
          <p>Datum, tider, antal personer och utfört arbete. Brister vi ser på tak eller taksäkerhet får ni skriftligt.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="priser">
    <div class="sec-head reveal">
      <div class="dim"><span class="dim-label">03 — Priser</span><span class="dim-rule"></span></div>
      <h2>Öppna priser</h2>
      <p class="sec-intro">Säsongsavgiften täcker tillsyn, beredskap och prioriterad utryckning. Själva skottningen debiteras per timme.</p>
    </div>
    <div class="reveal wrap-smal">
      <table class="pris">
        <tr><th>Post</th><th>Pris exkl. moms</th><th>Kommentar</th></tr>
        <tr><td>Säsongsavtal 1 nov – 15 apr</td><td>5 900 kr</td><td>Tillsyn, beredskap och prioriterad utryckning</td></tr>
        <tr><td>Timpris vardagar 07–16</td><td>595 kr/tim</td><td>Per person: takskottare, vakt och arbetsledare</td></tr>
        <tr><td>Timpris 16–07, helger och röda dagar</td><td>850 kr/tim</td><td>Per person</td></tr>
        <tr><td>Framkörning</td><td>495 kr</td><td>Per tillfälle. Restid debiteras inte</td></tr>
        <tr><td>Minimidebitering</td><td>2 tim</td><td>Per person och tillfälle, därefter per påbörjad halvtimme</td></tr>
      </table>
      <p class="pris-not">Exempel: tre personer i fyra timmar en vardag kostar cirka 7 635 kr exkl. moms. Faktisk tid beror på snömängd, is, taklutning och trafik nedanför. Moms 25 % tillkommer.</p>
    </div>
  </section>

  <section id="kvarter" class="process">
    <div class="sec-head reveal">
      <div class="dim"><span class="dim-label">04 — Kvartersavtal</span><span class="dim-rule"></span></div>
      <h2>Granne med<br>en kund?</h2>
      <p class="sec-intro">
        Ligger flera föreningar på samma gata eller i samma kvarter skottar vi taken i samma tur.
        Det ger kortare väntetid för alla och delad framkörning. Fråga oss om ett kvartersavtal
        tillsammans med era grannar.
      </p>
    </div>
    <div class="steps reveal">
      <div class="step"><p class="num">01</p><h3>Kontakt</h3><p>Ring eller skicka formuläret. Vi svarar samma dag.</p></div>
      <div class="step"><p class="num">02</p><h3>Genomgång</h3><p>Vi går igenom taken, taksäkerheten och gränsen mot grannfastigheter.</p></div>
      <div class="step"><p class="num">03</p><h3>Avtal</h3><p>Ett tydligt säsongsavtal med fasta priser för hela vintern.</p></div>
      <div class="step"><p class="num">04</p><h3>Beredskap</h3><p>Vi håller koll, hör av oss och skottar när det behövs.</p></div>
    </div>
  </section>

  <section id="sakerhet">
    <div class="sec-head reveal">
      <div class="dim"><span class="dim-label">05 — Säkerhet</span><span class="dim-rule"></span></div>
      <h2>Säkert för de<br>på taket – och nedanför</h2>
    </div>
    <div class="kma-grid reveal">
      <div class="kma-item"><h3>Skotta säkert</h3><p>Alla som arbetar åt oss med takskottning har licens enligt Skotta säkert och arbetar alltid med personligt fallskydd.</p></div>
      <div class="kma-item"><h3>Licensierad handledare</h3><p>Varje tillfälle leds av en handledare som gör riskbedömning på plats innan arbetet börjar.</p></div>
      <div class="kma-item"><h3>Avspärrning och vakt</h3><p>Riskområdet spärras av med band och skyltar, och en vakt på marken håller gående och bilar borta.</p></div>
      <div class="kma-item"><h3>Varsamt med taket</h3><p>Vi skottar så att takbeläggning, rännor, snörasskydd och huvar inte skadas. Vi har ansvars- och entreprenadförsäkring.</p></div>
    </div>
  </section>

  <section id="fragor">
    <div class="sec-head reveal">
      <div class="dim"><span class="dim-label">06 — Vanliga frågor</span><span class="dim-rule"></span></div>
      <h2>Frågor och svar</h2>
    </div>
    <div class="faq reveal wrap-smal">
      <details><summary>När behövs takskottning?</summary>
        <p>I Stockholm oftast från slutet av december till mars, men ett tidigt snöfall i november förekommer. Därför börjar säsongsavtalet den 1 november.</p></details>
      <details><summary>Vad händer om det knappt snöar?</summary>
        <p>Då betalar ni bara säsongsavgiften för tillsyn och beredskap. Timmar debiteras bara när vi faktiskt skottar.</p></details>
      <details><summary>Vilka områden täcker ni?</summary>
        <p>Stockholms innerstad, söderort, västerort, Solna, Sundbyberg, Nacka och närliggande kommuner. Vi utgår från Gröndalsvägen.</p></details>
      <details><summary>Vår byggnad sitter ihop med grannens. Hur gör vi?</summary>
        <p>Vi går igenom gränsen på taket vid avtalsstart och skottar bara era taksektioner, om inte grannen också tecknar avtal.</p></details>
      <details><summary>Vad behöver föreningen göra?</summary>
        <p>Se till att taksäkerheten (takstegar, glidskenor, förankringspunkter) fungerar, ge oss tillgång till vind och takluckor och avisera boende om att flytta bilar när vi kommer.</p></details>
    </div>
  </section>

  <section id="kontakt" class="contact">
    <div class="sec-head reveal">
      <div class="dim"><span class="dim-label">07 — Kontakt</span><span class="dim-rule"></span></div>
      <h2>Begär offert på<br>takskottning</h2>
    </div>
    <div class="contact-grid reveal">
      <div class="contact-info">
        <p>Berätta vilken fastighet det gäller, ungefär hur många huskroppar och om taken vetter mot gata eller gård. Vi återkommer samma dag.</p>
        <dl>
          <dt>Telefon</dt><dd><a href="tel:+46708997312">070-899 73 12</a></dd>
          <dt>E-post</dt><dd><a href="mailto:niklas@hammarbybyggxpert.se">niklas@hammarbybyggxpert.se</a></dd>
          <dt>Adress</dt><dd>Gröndalsvägen 196, 117 69 Stockholm</dd>
          <dt>Org.nr</dt><dd>556299-3690 · F-skatt</dd>
        </dl>
      </div>
      <form id="offert" novalidate>
        <div class="row">
          <div><label for="namn">Namn</label><input id="namn" name="namn" type="text" autocomplete="name" required></div>
          <div><label for="foretag">Förening eller företag</label><input id="foretag" name="foretag" type="text" autocomplete="organization"></div>
        </div>
        <div class="row">
          <div><label for="epost">E-post</label><input id="epost" name="epost" type="email" autocomplete="email" required></div>
          <div><label for="telefon">Telefon</label><input id="telefon" name="telefon" type="tel" autocomplete="tel"></div>
        </div>
        <div>
          <label for="typ">Typ av uppdrag</label>
          <select id="typ" name="typ">
            <option>Snöskottning av tak</option>
            <option>Kvartersavtal tillsammans med grannar</option>
            <option>Akut: snöras eller istappar nu</option>
          </select>
        </div>
        <div>
          <label for="beskrivning">Fastighet och tak</label>
          <textarea id="beskrivning" name="beskrivning" placeholder="Adress, antal huskroppar, taktyp och om taken vetter mot gata eller gård."></textarea>
        </div>
        <div class="form-msg" id="formMsg" role="status"></div>
        <div><button class="btn" type="submit">Skicka förfrågan</button></div>
        <p class="form-note">Vi använder uppgifterna bara för att svara på förfrågan.</p>
      </form>
    </div>
  </section>
</main>
"""

NAV = """    <nav>
      <a href="./">Startsida</a>
      <a href="#ingar">Det här ingår</a>
      <a href="#priser">Priser</a>
      <a href="#kvarter">Kvartersavtal</a>
      <a href="#sakerhet">Säkerhet</a>
    </nav>"""

ut = s
ut = re.sub(r"<title>.*?</title>", f"<title>{TITEL}</title>", ut, count=1, flags=re.S)
ut = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{BESKR}">', ut, count=1)
ut = ut.replace("</style>", EXTRA_CSS + "</style>", 1)
ut = re.sub(r"    <nav>.*?</nav>", NAV, ut, count=1, flags=re.S)
ut = ut.replace('<a href="#top"><img', '<a href="./"><img', 1)
ut = re.sub(r"<main>.*?</main>", lambda m: MAIN.strip(), ut, count=1, flags=re.S)
ut = ut.replace("'Förfrågan via hemsidan: '", "'Takskottning via hemsidan: '")
(HÄR / "takskottning.html").write_text(ut, encoding="utf-8", newline="")

# Länk från startsidan: menyn och texten under Fastighetsunderhåll
idx = s
if 'href="takskottning.html"' not in idx:
    idx = idx.replace('<a href="#kvalitet">Kvalitet</a>',
                      '<a href="#kvalitet">Kvalitet</a>\n      <a href="takskottning.html">Takskottning</a>', 1)
    idx = idx.replace("Alla som arbetar åt oss har licens enligt Skotta säkert.</p>",
                      "Alla som arbetar åt oss har licens enligt Skotta säkert. "
                      '<a href="takskottning.html">Läs mer om takskottning →</a></p>', 1)
    (HÄR / "index.html").write_text(idx, encoding="utf-8", newline="")
print("takskottning.html", len(ut) // 1024, "kB")
