"""Bygger om-oss.html ur index.html: samma stil, sidhuvud, sidfot och skript, nytt innehåll.

    python bygg_omoss.py

Lägger också till länken "Om oss" i menyn på startsidan.
"""
import json
import re
from pathlib import Path

HÄR = Path(__file__).parent
s = (HÄR / "index.html").read_text(encoding="utf-8")

TITEL = "Om oss – Hammarby ByggXpert AB, byggföretag i Stockholm"
BESKR = ("Hammarby ByggXpert AB (org.nr 556299-3690) är ett byggföretag på Gröndalsvägen 196 i Stockholm. "
         "Bygg, renovering, entreprenad, fastighetsunderhåll och takskottning. Godkänd för F-skatt.")

TEAM = [
    ("Niklas Markusson", "Arbetschef / Delägare", "070-899 73 12", "+46708997312", "niklas@hammarbybyggxpert.se"),
    ("Robert Lähteenmäki", "Projektchef", "073-651 03 62", "+46736510362", "robert@hammarbybyggxpert.se"),
    ("Mitch Camara", "Projektledare / Delägare", "073-527 11 45", "+46735271145", "alex@hammarbybyggxpert.se"),
    ("Christer Gartmon", "Affärsutvecklare / Projektansvarig", "073-961 53 35", "+46739615335",
     "christer@hammarbybyggxpert.se"),
]

EXTRA_CSS = """
  .fakta{width:100%;max-width:62rem;border-collapse:collapse;font-size:1rem}
  .fakta th{text-align:left;width:34%;padding:.8rem 1rem;background:#EFEBE4;font-weight:600;vertical-align:top}
  .fakta td{padding:.8rem 1rem;border-bottom:1px solid #DDD8CF}
  .team{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:1.4rem;max-width:72rem}
  .person{background:var(--paper);border-left:3px solid var(--gold);padding:1.4rem 1.4rem 1.3rem}
  .initialer{width:3.2rem;height:3.2rem;border-radius:50%;background:var(--ink);color:var(--gold);display:flex;
    align-items:center;justify-content:center;font-family:'Archivo',sans-serif;font-weight:800;margin-bottom:.9rem}
  .person h3{margin:0 0 .2rem;font-size:1.1rem}
  .person .roll{color:var(--steel);margin:0 0 .8rem;font-size:.95rem}
  .person a{display:block;font-size:.95rem;margin:.15rem 0;word-break:break-all}
  .lead-text{max-width:52rem;font-size:1.12rem;line-height:1.7}
"""


def initialer(namn):
    return "".join(d[0] for d in namn.split()[:2]).upper()


team_html = "\n".join(
    f"""      <div class="person">
        <div class="initialer">{initialer(n)}</div>
        <h3>{n}</h3>
        <p class="roll">{r}</p>
        <a href="tel:{tl}">{t}</a>
        <a href="mailto:{e}">{e}</a>
      </div>""" for n, r, t, tl, e in TEAM)

MAIN = f"""
<main>

  <section class="hero">
    <div class="hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">Om oss · Gröndalsvägen 196 · Stockholm</p>
        <h1>Byggföretag<br>i Stockholm.<br><em>En kontakt.</em></h1>
        <p class="hero-lead">
          Hammarby ByggXpert AB bygger, renoverar och underhåller fastigheter åt bostadsrättsföreningar,
          fastighetsägare, förvaltare och entreprenörer i Stockholmsregionen. Vintertid håller vi taken
          fria från snö och is.
        </p>
        <div class="hero-actions">
          <a href="./#kontakt" class="btn">Kontakta oss</a>
          <a href="takskottning.html" class="btn btn-ghost">Takskottning</a>
        </div>
      </div>
      <div class="faktakort">
        <h3>I korthet</h3>
        <ul>
          <li>Org.nr 556299-3690</li>
          <li>Registrerat 1987</li>
          <li>Godkänd för F-skatt</li>
          <li>26 års branscherfarenhet i arbetsledningen</li>
          <li>Fullt försäkrade: ansvars- och entreprenadförsäkring</li>
          <li>Anslutna till ID06</li>
          <li>Licens enligt Skotta säkert</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="vilka">
    <div class="sec-head reveal">
      <div class="dim"><span class="dim-label">01 — Vilka vi är</span><span class="dim-rule"></span></div>
      <h2>Ett lokalt<br>byggföretag</h2>
    </div>
    <div class="reveal">
      <p class="lead-text">
        Vi är ett Stockholmsbaserat byggföretag med kontor på Gröndalsvägen. Vi tar hand om hela kedjan –
        planering, bemanning, genomförande och uppföljning – från mindre service- och underhållsarbeten till
        kompletta entreprenader. Som kund har du en namngiven kontaktperson genom hela uppdraget, och det
        är samma personal som återkommer till fastigheten.
      </p>
      <p class="lead-text">
        Vi växer snabbt och arbetar i dag både som huvudentreprenör och som underentreprenör åt andra
        byggföretag, förvaltare och fastighetsbolag.
      </p>
    </div>
  </section>


  <section id="fakta">
    <div class="sec-head reveal">
      <div class="dim"><span class="dim-label">02 — Företagsfakta</span><span class="dim-rule"></span></div>
      <h2>Uppgifter för<br>beställare</h2>
      <p class="sec-intro">Vi är fullt försäkrade och anslutna till ID06. Försäkringsbevis, licenser och utdrag ur bokföringen lämnas på begäran.</p>
    </div>
    <div class="reveal">
      <table class="fakta">
        <tr><th>Företag</th><td>Hammarby ByggXpert AB</td></tr>
        <tr><th>Organisationsnummer</th><td>556299-3690</td></tr>
        <tr><th>Momsregistreringsnummer</th><td>SE556299369001</td></tr>
        <tr><th>Skatt</th><td>Godkänd för F-skatt</td></tr>
        <tr><th>Adress</th><td>Gröndalsvägen 196, 117 69 Stockholm</td></tr>
        <tr><th>Telefon</th><td><a href="tel:+46708997312">070-899 73 12</a></td></tr>
        <tr><th>E-post</th><td><a href="mailto:info@hammarbybyggxpert.se">info@hammarbybyggxpert.se</a></td></tr>
        <tr><th>Verksamhet</th><td>Bygg, renovering, entreprenad, fastighetsunderhåll och takskottning</td></tr>
        <tr><th>Verksamhetsområde</th><td>Stockholm, Solna, Sundbyberg, Nacka och Lidingö</td></tr>
        <tr><th>Försäkringar</th><td>Fullt försäkrade, med ansvarsförsäkring och entreprenadförsäkring</td></tr>
        <tr><th>ID06</th><td>Anslutna till ID06. Vår personal bär ID06-kort på arbetsplatsen.</td></tr>
      </table>
    </div>
  </section>

  <section id="sakerhet" class="process">
    <div class="sec-head reveal">
      <div class="dim"><span class="dim-label">03 — Så arbetar vi</span><span class="dim-rule"></span></div>
      <h2>Ordning och<br>säkerhet</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><p class="num">01</p><h3>En kontakt</h3><p>En namngiven ansvarig som har mandat att prissätta och boka in arbetet.</p></div>
      <div class="step"><p class="num">02</p><h3>Säkert arbete</h3><p>Riskbedömning före start, fallskydd vid arbete på höjd och avspärrning mot allmänheten.</p></div>
      <div class="step"><p class="num">03</p><h3>Dokumentation</h3><p>Egenkontroll under arbetet och skriftlig rapport efter utfört uppdrag.</p></div>
      <div class="step"><p class="num">04</p><h3>Ordning</h3><p>Vi städar efter oss varje dag och lämnar fastigheten i det skick vi fick den.</p></div>
    </div>
  </section>
</main>
"""

NAV = """    <nav>
      <a href="./">Startsida</a>
      <a href="#fakta">Företagsfakta</a>
      <a href="takskottning.html">Takskottning</a>
    </nav>"""

FAKTAKORT_CSS = re.search(r"  \.faktakort\{.*?\n(?=  \.pris\{)", (HÄR / "bygg_takskottning.py").read_text(encoding="utf-8"),
                          re.S)
ut = s
ut = re.sub(r"<title>.*?</title>", f"<title>{TITEL}</title>", ut, count=1, flags=re.S)
ut = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{BESKR}">', ut, count=1)
ut = ut.replace("</style>", (FAKTAKORT_CSS.group(0) if FAKTAKORT_CSS else "") + EXTRA_CSS + "</style>", 1)
ut = re.sub(r"    <nav>.*?</nav>", NAV, ut, count=1, flags=re.S)
ut = ut.replace('<a href="#top"><img', '<a href="./"><img', 1)
ut = ut.replace('href="#kontakt" class="btn">Kontakta oss</a>', 'href="./#kontakt" class="btn">Kontakta oss</a>', 1)
ut = re.sub(r"<main>.*?</main>", lambda m: MAIN.strip(), ut, count=1, flags=re.S)
ut = ut.replace("form.addEventListener('submit'", "form && form.addEventListener('submit'")
om = {"@context": "https://schema.org", "@type": "AboutPage", "url": "https://hammarbybyggxpert.se/om-oss.html",
      "about": {"@id": "https://hammarbybyggxpert.se/#foretag"}}
ut = ut.replace("</head>", '<script type="application/ld+json">\n' + json.dumps(om, ensure_ascii=False, indent=1)
                + "\n</script>\n</head>", 1)
(HÄR / "om-oss.html").write_text(ut, encoding="utf-8", newline="")

idx = s
if 'href="om-oss.html"' not in idx:
    idx = idx.replace('<a href="takskottning.html">Takskottning</a>',
                      '<a href="takskottning.html">Takskottning</a>\n      <a href="om-oss.html">Om oss</a>', 1)
    (HÄR / "index.html").write_text(idx, encoding="utf-8", newline="")
print("om-oss.html", len(ut) // 1024, "kB")
