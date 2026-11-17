import json, os, pathlib
SRC = pathlib.Path(__file__).parent
OUT = SRC.parent / "site"
OUT.mkdir(exist_ok=True)
CSS = (SRC / "styles.css").read_text()
JS = (SRC / "site.js").read_text()

PHONE = "0448 741 813"
TEL = "tel:+61448741813"
IG = "https://www.instagram.com/multileaseexcavation/"
BIZ = "Multilease Excavation"

I_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
I_ARROW = '<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
I_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg>'
I_X = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
I_PREV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg>'
I_NEXT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>'
DIGGER = '<svg class="dig" viewBox="0 0 54 34" aria-hidden="true"><rect x="2" y="26" width="30" height="7" rx="3.5" fill="currentColor"/><rect x="6" y="15" width="21" height="11" rx="2" fill="currentColor"/><rect x="15" y="6" width="10" height="10" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M26 17 L39 5 L50 16" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 16 l-6 8 h8 z" fill="currentColor"/></svg>'

SERVICES = [
  ("demolition-sydney.html", "Demolition"),
  ("excavation-sydney.html", "Excavation"),
  ("tight-access-excavation-sydney.html", "Tight access"),
  ("hook-bins-sydney.html", "Hook bins"),
]

def schema_business():
    return {
      "@context": "https://schema.org",
      "@type": "GeneralContractor",
      "name": "Multilease Excavation Pty Ltd",
      "alternateName": BIZ,
      "description": "Sydney demolition and excavation contractor with its own fleet: house and commercial demolition, strip outs, bulk and tight access excavation, site clean up and hook bins.",
      "telephone": "+61 448 741 813",
      "image": "media/sh125-loading.webp",
      "logo": "media/logo-square.png",
      "address": {"@type": "PostalAddress", "streetAddress": "32 Mulgoa Road", "addressLocality": "Regentville", "addressRegion": "NSW", "postalCode": "2745", "addressCountry": "AU"},
      "areaServed": [{"@type": "City", "name": "Sydney"}, "Penrith", "Western Sydney", "Inner West", "North Shore", "South West Sydney"],
      "identifier": {"@type": "PropertyValue", "propertyID": "ABN", "value": "56 664 948 501"},
      "sameAs": [IG],
      "knowsAbout": ["Demolition", "Excavation", "Tight access excavation", "Strip outs", "Site clean up", "Hook bins", "OSD tank excavation"]
    }

def head(title, desc, extra_schema=None):
    blocks = [schema_business()] + (extra_schema or [])
    sch = "\n".join('<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False) + '</script>' for b in blocks)
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#2a1d16">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="media/sh125-loading.webp">
<meta property="og:locale" content="en_AU">
<link rel="icon" href="media/apple-touch-icon.png">
<link rel="apple-touch-icon" href="media/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<script>document.documentElement.classList.add('js')</script>
{sch}
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-banner" role="note">Concept website prepared for <strong>Multilease Excavation</strong> by Mago Labs. Not the live site.</div>
'''

def header(home=True):
    p = "" if home else "index.html"
    return f'''<header class="header">
  <nav class="nav" aria-label="Main">
    <a class="brand" href="index.html" aria-label="Multilease Excavation home"><img src="media/logo-wordmark-white.png" alt="Multilease Excavation" width="898" height="106"></a>
    <ul class="nav-links" id="nav-links">
      <li><a href="{p}#services">Services</a></li>
      <li><a href="{p}#fleet">Fleet</a></li>
      <li><a href="{p}#jobs">Recent jobs</a></li>
      <li><a href="{p}#how">How we work</a></li>
      <li><a href="{p}#quote">Get a quote</a></li>
    </ul>
    <a class="nav-call" href="{TEL}">{I_PHONE}<span class="t">{PHONE}</span><span class="sr">Call {PHONE}</span></a>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
  </nav>
</header>
<div class="gauge" data-max="6" aria-hidden="true"><span class="val">Depth 0.0 m</span><span class="bar"><span class="lvl"></span></span></div>
'''

def cta(home=True):
    jobs = ["House demolition", "Commercial demolition", "Strip out / partial demolition", "Bulk excavation", "Tight access excavation", "Footings, OSD tank or pool dig", "Site clean up", "Hook bin", "Not sure yet"]
    opts = "".join(f"<option>{j}</option>" for j in jobs)
    return f'''<section class="cta" id="quote" aria-labelledby="cta-h">
  <div class="wrap cta-grid">
    <div data-reveal>
      <span class="label">Free quote</span>
      <h2 id="cta-h">Got a block that needs clearing?</h2>
      <p class="lede">Send the address and a few photos. We will check access, scope the job and come back with a clear, fixed quote. No obligation, no runaround.</p>
      <a class="cta-phone" href="{TEL}">{I_PHONE}{PHONE}</a>
      <p class="mono" style="margin-top:14px;color:#fbe1d5">Based in Regentville. Working Sydney wide.</p>
    </div>
    <form class="quote" data-reveal data-delay="120" novalidate>
      <div><label for="q-name">Your name</label><input id="q-name" name="name" autocomplete="name" required></div>
      <div><label for="q-phone">Phone</label><input id="q-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
      <div><label for="q-sub">Site suburb</label><input id="q-sub" name="suburb" autocomplete="address-level2" required></div>
      <div><label for="q-job">Job type</label><select id="q-job" name="job">{opts}</select></div>
      <div class="full"><label for="q-msg">Tell us about the site (optional)</label><textarea id="q-msg" name="message" placeholder="e.g. Single storey double brick house, pool out the back, side access about 1.2 m"></textarea></div>
      <div class="full"><label for="q-file">Photos or plans (optional)</label><input id="q-file" name="files" type="file" accept="image/*,.pdf" multiple></div>
      <div class="full"><button class="btn btn-primary" type="submit">Get my free quote {I_ARROW}</button></div>
      <p class="full fine">Your details are only used to quote your job. Prefer to talk? Call {PHONE}.</p>
      <p class="full ok" tabindex="-1" role="status">Thanks. On the live site this goes straight to the Multilease inbox. This is a concept demo, so nothing was sent.</p>
    </form>
  </div>
</section>
'''

def footer():
    svc = "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in SERVICES)
    return f'''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="foot-logo" href="index.html" aria-label="Multilease Excavation home"><img src="media/logo-wordmark-white.png" alt="Multilease Excavation" width="898" height="106" loading="lazy"></a>
        <p>Demolition, excavation and civil contractors. Transforming visions into reality, one site at a time, right across Sydney.</p>
      </div>
      <div><h4>Services</h4><ul>{svc}<li><a href="index.html#fleet">Our fleet</a></li></ul></div>
      <div><h4>Contact</h4><ul>
        <li><a href="{TEL}">{PHONE}</a></li>
        <li><a href="{IG}" rel="noopener" target="_blank">Instagram @multileaseexcavation</a></li>
        <li><a href="index.html#quote">Request a quote</a></li></ul></div>
      <div><h4>Business</h4><ul>
        <li>32 Mulgoa Road, Regentville NSW 2745</li>
        <li>Multilease Excavation Pty Ltd</li>
        <li>ABN 56 664 948 501</li>
        <li>Registered Buy NSW supplier</li>
        <li><span class="ph-note">Licence no. to confirm</span></li></ul></div>
    </div>
    <div class="giant" aria-hidden="true">KNOCK IT DOWN. DIG IT OUT.</div>
    <div class="legal">
      <span>&copy; 2026 Multilease Excavation Pty Ltd. Servicing Greater Sydney from Regentville.</span>
      <span class="credit">Concept website by <a href="https://magolabs.in" target="_blank" rel="noopener">Mago Labs</a> <span class="beat" aria-hidden="true">&#9829;</span></span>
    </div>
  </div>
</footer>
<div class="mbar"><a class="btn btn-ghost" href="{TEL}">{I_PHONE}Call</a><a class="btn btn-primary" href="#quote">Free quote</a></div>
<script>{JS}</script>
</body>
</html>
'''

def vid(name, label="", cls=""):
    return f'<video class="{cls}" muted loop playsinline preload="none" poster="media/{name}.webp" data-src="media/{name}.mp4" aria-label="{label}"></video>'

# ---------------- HOME ----------------
FAQ_HOME = [
  ("How much does house demolition cost in Sydney?", "It depends on the size of the house, what it is built from (double brick, fibro or weatherboard), the access, and whether there is asbestos, a pool, a garage or a slab to come out as well. The fastest way to a real number is to send us the address and a few photos. We will come back with a fixed quote, not a range."),
  ("Do you handle the council side of a demolition?", "Most demolitions in NSW need an approval first, either a DA or a complying development certificate. We work alongside your builder or certifier, follow the conditions on the approval and provide the paperwork they need from us, including waste dockets."),
  ("How narrow can your machines get in?", "Our Yanmar ViO17 mini excavator works through access of about one metre, so side passages and backyards are no problem. If your access is tighter than that, ask us about a micro excavator from around 0.7 m. Send a photo of the narrowest point and we will tell you straight."),
  ("What happens if there is asbestos on site?", "Asbestos is removed by a licensed removalist under NSW rules before the main knock down, with clearance paperwork for your certifier. We have done jobs with asbestos garages and sheds, and we plan the sequence so the site keeps moving."),
  ("Do you recycle demolition waste?", "Yes. Brick, concrete, steel, timber and green waste are separated on site wherever we can, so more of your old house goes to recycling and less goes to landfill. Every load is docketed."),
  ("Can you supply bins and trucks as well?", "Yes. We run hook bins for soil, concrete, brick, vegetation and household waste, and tippers for bigger cart away. One crew, one booking, one invoice."),
]

def faq_html(items):
    return "".join(f'<details><summary>{q}<i aria-hidden="true"></i></summary><div class="a"><p>{a}</p></div></details>' for q, a in items)

def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

STEPS = [
  ("01", "Set up and strip out", "Fencing up, services checked and the inside stripped first. Steel, timber and brick are separated before the big machine touches a wall.", '<img src="media/site-fence.webp" alt="Multilease Excavation site fence with demolition work in progress signage" loading="lazy" width="825" height="1100">'),
  ("02", "Knock it down", "Our Sumitomo SH125 brings the building down in sections while a hose keeps the dust on the ground and off your neighbours' cars.", vid("knockdown", "Sumitomo excavator demolishing a brick building with water spray for dust")),
  ("03", "Load and cart away", "Brick, concrete and soil go straight into tippers and bins. Sorted for recycling wherever we can, docketed every load.", vid("loadout", "Excavator loading demolition rubble into a bin")),
  ("04", "Dig it out", "Footings, OSD tanks, basements and pools. Bulk or detailed, with the machine matched to the access.", '<img src="media/deep-cut.webp" alt="Yanmar mini excavator in a deep excavation beside a new home" loading="lazy" width="880" height="1100">'),
  ("05", "Site ready", "A clean, level block and a builder who can start on day one. That is the job done properly.", '<img src="media/wahroonga-cleared.webp" alt="Cleared and excavated house site in Wahroonga ready for footings" loading="lazy" width="825" height="1100">'),
]

def story():
    steps = "".join(f'''<li class="step"><div class="copy"><span class="n">Stage {n} / 05</span><h3>{t}</h3><p>{p}</p></div><div class="media">{m}</div></li>''' for n, t, p, m in STEPS)
    layers = "".join(f'<div class="layer" aria-hidden="true">{m}</div>' for *_, m in STEPS)
    ticks = "".join(f"<span>{t.split()[0] if i<4 else 'Ready'}</span>" for i,(n,t,p,m) in enumerate(STEPS))
    return f'''<section class="band story" id="process-story" aria-labelledby="story-h">
  <div class="story-scroller">
    <div class="story-sticky wrap">
      <div class="story-left">
        <div class="head" data-reveal><span class="label">How a job comes down</span><h2 id="story-h">From standing <span class="soft">to site ready.</span></h2></div>
        <ol class="story-steps">{steps}</ol>
      </div>
      <div class="story-stage">{layers}</div>
      <div class="rail" aria-hidden="true"><div class="track"></div><div class="fill"></div>{DIGGER}<div class="ticks">{ticks}</div></div>
    </div>
  </div>
</section>'''

FLEET = [
  ("Yanmar ViO17", "1.7 t mini", 1.0, "~1.0 m", "Side passages, backyards and under house digs. Runs a hammer, grab and sieve bucket.", "vio17-hammer", "Red Yanmar ViO17 mini excavator with RH-20 hydraulic hammer"),
  ("Yanmar ViO55", "5.5 t", 2.0, "~2.0 m", "Trenching, footings and mid size digs where a mini is too slow.", "vio55-trench", "Yellow Yanmar ViO55 excavator trenching on a house site"),
  ("CAT 305", "5 t, our newest", 2.0, "~2.0 m", "Just delivered by WesTrac. Detailed excavation with a full set of buckets.", "cat305-farm", "New CAT 305 excavator with buckets and quick hitch"),
  ("Sumitomo SH125", "12.5 t short tail", 2.6, "~2.5 m", "The demolition and bulk dig muscle. Short tail swing for tight streets.", "sh125-rubble", "Yellow Sumitomo SH125 excavator on a commercial demolition"),
  ("Tippers and hook bins", "Same day cart away", 3.0, "~3.0 m", "Soil, brick, concrete and green waste out the gate the same day.", "sh125-truck-overhead", "Excavator loading bricks into a yellow tipper truck"),
]

def fleet():
    items = "".join(f'''<li class="mach" data-needs="{need}" data-name="{n}"><div class="ph"><img src="media/{img}.webp" alt="{alt}" loading="lazy" width="825" height="1100"><span class="fit">Fits</span></div><div class="bd"><h3>{n}</h3><span class="meta">{w} / needs {wd}</span><p>{p}</p></div></li>''' for n, w, need, wd, p, img, alt in FLEET)
    return f'''<section class="sec" id="fleet" aria-labelledby="fleet-h">
  <div class="wrap">
    <div class="fleet-top">
      <div class="head" data-reveal><span class="label">The fleet</span><h2 id="fleet-h">Our own machines. <span class="soft">Sized to your gate.</span></h2>
      <p class="lede">We own our gear, so we turn up when we say we will. Slide to the narrowest point on your site and see what we can get in.</p></div>
      <div class="gate" data-reveal data-delay="100">
        <label for="gate">Narrowest access <output id="gate-out" for="gate">1.2 m</output></label>
        <input type="range" id="gate" min="0.7" max="3.2" step="0.1" value="1.2" aria-describedby="gate-verdict">
        <div class="scale" aria-hidden="true"><span>0.7 m</span><span>Side passage</span><span>Driveway</span><span>3.2 m</span></div>
        <p class="verdict" id="gate-verdict" aria-live="polite">At 1.2 m we can bring in: Yanmar ViO17.</p>
      </div>
    </div>
    <ul class="fleet">{items}</ul>
    <p class="foot-note">Access widths are approximate and include a little clearance. Every job gets a proper access check before we quote. Fleet details to be confirmed by Multilease.</p>
  </div>
</section>'''

PROJECTS = [
  ("vid", "crane-lift", "Lindfield", "OSD tank", "700+ t", "Removed to make way for an OSD tank", "Mini excavators craned in over the building, rock hammered and dug out to depth.", "Mini excavator lifted by tower crane onto an excavation site in Lindfield"),
  ("vid", "tight-access", "Wahroonga", "Tight access", "1 m", "Backyard demolition and dig", "Yanmar ViO17 through a garden side passage. Footings dug, waste sorted for recycling.", "Yanmar mini excavator working in a Wahroonga backyard"),
  ("txt", "", "Concord", "Full demolition", "3 in 1", "Double brick house, asbestos garage and pool", "Kicked off the year by taking a whole block back to dirt, ready for the new build."),
  ("vid", "water-suppression", "Sydney", "Commercial", "Dust down", "Brick building down, dust kept down", "Water spray on the bucket the whole way through. Neighbours kept happy, site kept moving.", "Excavator demolishing a white brick building with a water hose for dust control"),
  ("txt", "", "Birrong", "Site clean up", "13", "Truckloads of mixed soil removed", "A builder's side passage cleared back to clean ground with the ViO17."),
  ("vid", "stormwater-pit", "Sydney", "Drainage", "Pit in", "Stormwater pit installed", "Dug, set and backfilled with the mini, footpath left tidy.", "Crew installing a concrete stormwater pit with a mini excavator"),
  ("img", "cat305-handover", "Casula", "New gear", "CAT 305", "Another addition to the fleet", "Thanks to Michael and the team at WesTrac for the quick delivery.", "Multilease crew taking delivery of a new CAT 305 at WesTrac Casula"),
]

def projects():
    cards = []
    for kind, media, sub, tag, big, h, p, *alt in PROJECTS:
        top = f'<div class="top"><span>{sub}</span><span>{tag}</span></div>'
        if kind == "txt":
            cards.append(f'<article class="prj text"><div class="pm">{top}<span class="big">{big}</span></div><div class="bt"><h3>{h}</h3><p>{p}</p></div></article>')
        else:
            m = vid(media, alt[0]) if kind == "vid" else f'<img src="media/{media}.webp" alt="{alt[0]}" loading="lazy" width="825" height="1100">'
            cards.append(f'<article class="prj"><div class="pm">{m}{top}</div><div class="bt"><span class="big">{big}</span><h3>{h}</h3><p>{p}</p></div></article>')
    return f'''<section class="band sec" id="jobs" aria-labelledby="jobs-h">
  <div class="wrap head-row">
    <div class="head" data-reveal><span class="label">Recent jobs</span><h2 id="jobs-h">Real sites. <span class="soft">Real tonnes.</span></h2></div>
    <div class="rail-btns" data-reveal><button type="button" data-rail="prj-rail" data-dir="prev" aria-label="Previous jobs">{I_PREV}</button><button type="button" data-rail="prj-rail" data-dir="next" aria-label="More jobs">{I_NEXT}</button></div>
  </div>
  <div class="rail-wrap"><div class="prj-rail" id="prj-rail" tabindex="0" aria-label="Recent jobs, scroll sideways">{"".join(cards)}</div></div>
</section>'''

def home():
    title = "Demolition & Excavation Sydney | Multilease Excavation"
    desc = "Sydney demolition and excavation crew with its own fleet. House knock downs, strip outs, bulk and tight access digs, site clean up and hook bins. Call 0448 741 813."
    svcs = [
      ("01", "demolition-sydney.html", "House and commercial demolition", "Full knock downs, partial demos and strip outs. Houses, garages, pools, sheds and warehouses.", "sh125-loading", "feature", "Demolition services"),
      ("02", "excavation-sydney.html", "Excavation and earthworks", "Bulk and detailed digs, footings, OSD tanks, pools and basements, cut to level.", "vio55-trench", "", "Excavation services"),
      ("03", "tight-access-excavation-sydney.html", "Tight access excavation", "No room? No worries. Our ViO17 works through about a metre of side access.", "vio17-wall", "", "Tight access digs"),
      ("04", "demolition-sydney.html#strip-out", "Site clean up and strip outs", "Mixed soil, rubble and green waste loaded and gone. Interiors stripped back to the frame.", "breaker-rubble", "", "Strip outs and clean ups"),
      ("05", "hook-bins-sydney.html", "Hook bins and waste removal", "Bins for soil, concrete, brick, vegetation and household waste. Sorted for recycling.", "sh125-dirt", "", "Book a hook bin"),
    ]
    sv = "".join(f'''<a class="svc {c}" href="{h}" data-reveal data-delay="{i*70}"><span class="thumb"><img src="media/{img}.webp" alt="" loading="lazy" width="150" height="150"></span><span class="num">{n}</span><h3>{t}</h3><p>{p}</p><span class="go">{g} {I_ARROW}</span></a>''' for i,(n,h,t,p,img,c,g) in enumerate(svcs))
    layers = [
      ("topsoil","Topsoil","0 to 0.3 m","Wahroonga","Tight access backyard demolition and dig","Yanmar ViO17 through a garden side passage. Footings dug, waste sorted for recycling.","1 m","access"),
      ("clay","Clay","0.3 to 1.2 m","Birrong","Site clean up","A builder's side passage cleared back to clean ground.","13","truckloads"),
      ("shale","Shale","1.2 to 2.5 m","Concord","Full demolition","Double brick house, asbestos garage and swimming pool, taken back to dirt.","3 in 1","structures down"),
      ("sandstone","Sandstone","2.5 to 4.0 m","Lindfield","OSD tank excavation","Rock hammered and dug out to depth, mini excavators craned in over the building.","700+","tonnes out"),
      ("bedrock","Bedrock","4.0 m +","The fleet","What every job sits on","Our own machines, from a 1.7 t mini to a 12.5 t Sumitomo, run by one crew.","5","machines"),
    ]
    STRATA = "".join(f'''<article class="stratum {k}" data-reveal data-delay="{i*90}"><div class="depth"><span class="mono">{n}</span><span class="m">{d}</span></div><div class="job"><h3><span>{s}</span> {t}</h3><p>{p}</p></div><div class="num"><b>{big}</b><span class="mono">{u}</span></div></article>''' for i,(k,n,d,s,t,p,big,u) in enumerate(layers))
    body = f'''{head(title, desc, [faq_schema(FAQ_HOME)])}{header()}
<main id="main">
<section class="hero" aria-labelledby="hero-h">
  <div class="hero-grid">
    <div>
      <h1 id="hero-h"><span class="kicker"><i></i>Demolition &amp; Excavation, Sydney</span><span class="ln"><span>Knock it down.</span></span><span class="ln y"><span>Dig it out.</span></span></h1>
      <p class="lede">Multilease Excavation is a Sydney demolition and civil crew with its own fleet. House knock downs, strip outs, bulk digs and tight access excavation, from the first brick to a clean, level block your builder can start on.</p>
      <div class="hero-ctas"><a class="btn btn-primary" href="#quote">Get my free quote {I_ARROW}</a><a class="btn btn-ghost" href="{TEL}">{I_PHONE}Call {PHONE}</a></div>
      <ul class="chips"><li>Own fleet, 1.7 t to 12.5 t</li><li>Registered NSW Gov supplier</li><li>Hook bins on hand</li></ul>
    </div>
    <div class="hero-media">
      <div class="vcard"><img src="media/hero-demolition.webp" alt="" width="540" height="720" fetchpriority="high" style="position:absolute;inset:0"><video muted loop playsinline preload="none" poster="media/hero-demolition.webp" data-src="media/hero-demolition.mp4" aria-label="Sumitomo excavator demolishing a brick house in Sydney" style="position:relative"></video><span class="tag"><i></i>On site, Sydney</span></div>
      <div class="mini"><img src="media/vio17-hammer.webp" alt="Yanmar ViO17 mini excavator with hydraulic hammer" width="880" height="1100"></div>
      <div class="spec"><b>12.5 t</b>Sumitomo SH125<br>on the knock down</div>
    </div>
  </div>
</section>

<section class="strata-sec" aria-labelledby="strata-h">
  <div class="wrap">
    <div class="head-row" data-reveal><div class="head"><span class="label">Proof in the ground</span><h2 id="strata-h">Real jobs. <span class="soft">Layer by layer.</span></h2></div>
    <p class="lede" style="max-width:40ch">Every layer of Sydney ground has a job of ours in it. Scroll down and dig through a few.</p></div>
    <div class="strata">
      <div class="grass" aria-hidden="true"></div>
      {STRATA}
    </div>
  </div>
</section>

<section class="sec" id="problem" aria-labelledby="prob-h">
  <div class="wrap problem-grid">
    <div class="head" data-reveal>
      <span class="label">The headache</span>
      <h2 id="prob-h">The builder is booked. <span class="soft">The old house is still standing.</span></h2>
      <p class="lede">You have the approval, a builder waiting and a house, pool or garage in the way. Chasing a demo crew, an excavator hire, a tipper and a bin company eats weeks. Then one of them runs late and the whole build slides.</p>
      <p class="answer">We take the whole lot off your plate. <mark>One crew, one quote, start to finish.</mark></p>
    </div>
    <div class="quote-stack" aria-label="What our customers tell us before they call">
      <div class="qbubble" data-reveal>"Three quotes, three different scopes, and nobody will commit to a date."<small>Owner builder, Inner West</small></div>
      <div class="qbubble" data-reveal data-delay="100">"Side access is barely a metre. Every big outfit says it can't be done."<small>Homeowner, North Shore</small></div>
      <div class="qbubble" data-reveal data-delay="200">"I need the site clean and level before my slab crew turns up Monday."<small>Builder, Western Sydney</small></div>
      <p class="ph-note" style="margin-top:6px">Example situations, not customer reviews</p>
    </div>
  </div>
</section>

<section class="sec" id="services" aria-labelledby="svc-h" style="padding-top:0">
  <div class="wrap">
    <div class="head" data-reveal><span class="label">What we do</span><h2 id="svc-h">Demolition and excavation <span class="soft">across Sydney.</span></h2>
    <p class="lede">From a backyard dig to a full commercial knock down, it is all done with our own machines and our own crew.</p></div>
    <div class="svc-grid">{sv}</div>
  </div>
</section>

{story()}

{fleet()}

{projects()}

<section class="sec" id="why" aria-labelledby="why-h">
  <div class="wrap">
    <div class="head" data-reveal><span class="label">Why Multilease</span><h2 id="why-h">One crew. <span class="soft">Start to finish.</span></h2>
    <p class="lede">A crew that owns the job, not a hire company with a phone number.</p></div>
    <div class="compare">
      <div class="col them" data-reveal><h3>Juggling four contractors</h3><ul>
        <li>{I_X}<span>A demo crew, a dig crew, a tipper and a bin company, all on different days</span></li>
        <li>{I_X}<span>Every handover is a gap where your job sits idle</span></li>
        <li>{I_X}<span>Hired machines that may not fit your access</span></li>
        <li>{I_X}<span>When it runs late, everyone points at someone else</span></li></ul></div>
      <div class="col us" data-reveal data-delay="120"><h3>Multilease Excavation</h3><ul>
        <li>{I_CHECK}<span>Knock down, dig, cart away and bins in one booking</span></li>
        <li>{I_CHECK}<span>Our own fleet from 1.7 t to 12.5 t, picked for your site</span></li>
        <li>{I_CHECK}<span>Dust and noise managed, neighbours kept in the loop</span></li>
        <li>{I_CHECK}<span>One number to call, and we answer it</span></li></ul></div>
    </div>
    <p class="dont" data-reveal>What we don't do: we don't build houses. We get the site ready for the people who do, and we get it right.</p>
  </div>
</section>

<section class="sec" id="how" aria-labelledby="how-h" style="padding-top:0">
  <div class="wrap">
    <div class="head" data-reveal><span class="label">How we work</span><h2 id="how-h">Four steps. <span class="soft">No surprises.</span></h2></div>
    <ol class="steps4">
      <li data-reveal><h3>Call or send photos</h3><p>Tell us the address and what is coming down or coming out. Photos and plans speed things up.</p></li>
      <li data-reveal data-delay="80"><h3>Site check and fixed quote</h3><p>We check access, services and your approval conditions, then give you a fixed price and a start date.</p></li>
      <li data-reveal data-delay="160"><h3>Knock down and dig</h3><p>Fenced, safe and tidy. Dust kept down, waste sorted, neighbours kept in the loop.</p></li>
      <li data-reveal data-delay="240"><h3>Clean, level handover</h3><p>Site cleared, dockets handed over, ready for your builder to start the next stage.</p></li>
    </ol>
  </div>
</section>

<section class="sec" id="reviews" aria-labelledby="rev-h" style="padding-top:0">
  <div class="wrap">
    <div class="head" data-reveal><span class="label">Word on site</span><h2 id="rev-h">Builders call us back. <span class="soft">That says enough.</span></h2></div>
    <div class="split">
      <div class="review" data-reveal><div class="stars" aria-label="5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote>Your best Google review goes here, with the customer's name and suburb.</blockquote><span class="ph-note">Placeholder on this concept site. Real reviews link to your Google Business Profile.</span></div>
      <div class="area" data-reveal data-delay="120"><h3>Based in Regentville. Working right across Sydney.</h3>
        <ul><li class="base">Regentville / Penrith</li><li>Western Sydney</li><li>Inner West</li><li>Upper North Shore</li><li>South West Sydney</li><li>Wahroonga</li><li>Lindfield</li><li>Concord</li><li>Croydon</li><li>Birrong</li></ul>
        <p>Not on the list? If it is in Greater Sydney, give us a call. We go where the job is.</p></div>
    </div>
  </div>
</section>

<section class="sec" id="faq" aria-labelledby="faq-h" style="padding-top:0">
  <div class="wrap">
    <div class="head" data-reveal><span class="label">Questions</span><h2 id="faq-h">Demolition and excavation <span class="soft">questions, answered.</span></h2></div>
    <div class="faq">{faq_html(FAQ_HOME)}</div>
  </div>
</section>

{cta()}
</main>
{footer()}'''
    (OUT / "index.html").write_text(body)

if __name__ == "__main__":
    home()
    import services
    services.build(globals())
    print("built")
