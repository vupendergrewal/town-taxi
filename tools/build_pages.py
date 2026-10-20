from pathlib import Path

ROOT = Path(r"C:\Users\grewa\Downloads\town-taxi")

ICONS = {
    "car": '<path d="M4 15h16l-1.4-4.2A2 2 0 0 0 16.7 9H7.3a2 2 0 0 0-1.9 1.4L4 15z"/><path d="M7 15v2M17 15v2"/><circle cx="7.5" cy="16.5" r="1"/><circle cx="16.5" cy="16.5" r="1"/>',
    "calendar": '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M8 3v4M16 3v4M4 10h16"/>',
    "people": '<path d="M9 11a3 3 0 1 0-3-3 3 3 0 0 0 3 3zM16 11a2.5 2.5 0 1 0-2.5-2.5A2.5 2.5 0 0 0 16 11z"/><path d="M3.5 19c.4-2.4 2.4-4 5.5-4s5.1 1.6 5.5 4M14 15c1.8 0 3.6.8 4.2 3"/>',
    "plane": '<path d="M3 12l18-6-6 16-2.5-6.2L3 12z"/>',
    "person": '<circle cx="12" cy="8" r="3"/><path d="M6 19c.8-3 2.8-4.5 6-4.5S17.2 16 18 19"/>',
    "wheel": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2"/><path d="M12 4v6M12 14v6M4 12h6M14 12h6"/>',
    "case": '<rect x="3" y="7" width="18" height="12" rx="2"/><path d="M8 7V6a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v1M3 12h18"/>',
    "access": '<circle cx="8" cy="6" r="2"/><path d="M8 9v5h4l2 5"/><path d="M6 14h6"/><circle cx="17" cy="17" r="3"/><path d="M17 14v-3h3"/>',
    "box": '<path d="M3 8l9-4 9 4-9 4-9-4z"/><path d="M3 8v8l9 4 9-4V8M12 12v8"/>',
    "bolt": '<path d="M13 3L5 14h7l-1 7 8-11h-7l1-7z"/>',
    "snow": '<path d="M12 3v18M5 7l14 10M19 7L5 17"/><path d="M12 7l2-1M12 7l-2-1M12 17l2 1M12 17l-2 1"/>',
    "phone": '<path d="M8 3h3l1 4-2 1a12 12 0 0 0 6 6l1-2 4 1v3a2 2 0 0 1-2 2A16 16 0 0 1 6 5a2 2 0 0 1 2-2z"/>',
}

SERVICES = [
    {
        "slug": "taxi",
        "name": "Taxi",
        "icon": "car",
        "line": "Point to point across Dunedin.",
        "image": "assets/images/sedan-b.jpg",
        "alt": "Black sedan on the road",
        "intro": "For the everyday jobs: the Octagon, the hospital, campus, St Clair, Mosgiel, Port Chalmers.",
        "copy": "Town Taxi is a private car from the door you name to the door you need. No rank, no shared ride, no extra stop on the way. Book it for right now or lock it in for later in the day. If the pickup is a hotel, a hall or the university, put that in the notes and the driver will come to the entrance you give us.",
    },
    {
        "slug": "event-management",
        "name": "Event Management",
        "icon": "calendar",
        "line": "Guest cars for functions and weddings.",
        "image": "assets/images/1511578314322-379afb476865.jpg",
        "alt": "A set table at an evening function",
        "intro": "Weddings, race days, graduations and private functions.",
        "copy": "Moving guests is the part of an event that fails in public. We take the timetable — who leaves the hotel, who needs to be at the venue, who goes home after — and run the cars against that list. One person on your side can deal with us, instead of every guest booking their own taxi at midnight.",
    },
    {
        "slug": "conference-booking",
        "name": "Conference Booking",
        "icon": "people",
        "line": "Timed runs for delegates.",
        "image": "assets/images/1505373877841-8d25f7d46678.jpg",
        "alt": "A speaker at a conference",
        "intro": "Hotels, the airport and the venue, on a schedule.",
        "copy": "A conference day is a stack of small pickups that all matter. We take the delegate list, the hotel names and the session times, and we put cars on those runs. Tell us the day before if a flight lands late. We would rather change one booking than have someone standing outside arrivals with no car.",
    },
    {
        "slug": "group-transport",
        "name": "Group Transport",
        "icon": "people",
        "line": "One vehicle for the whole party.",
        "image": "assets/images/1469854523086-cc02fe5d8800.jpg",
        "alt": "A van on an open road",
        "intro": "Families, teams and tour groups who want to travel together.",
        "copy": "If you are more than four, or you have a pile of bags, say so when you book and we will send a larger vehicle. The group stays in one car. That is the point — nobody is split across two taxis that arrive ten minutes apart. Sports kits, instruments and extra cases can go in the notes.",
    },
    {
        "slug": "airport-transfer",
        "name": "Airport Transfer",
        "icon": "plane",
        "line": "Dunedin Airport, timed properly.",
        "image": "assets/images/1436491865332-7a61a109cc05.jpg",
        "alt": "An aircraft wing above the clouds",
        "intro": "Meet at arrivals, or a drop-off that leaves room to check in.",
        "copy": "Dunedin Airport is a short run until it is an early flight or a late landing. For departures we work backwards from the time you need to be at the terminal, not from a guess. For arrivals, give us the flight in the notes if you want the driver watching the landing. Flight number is optional. The pickup time is not.",
    },
    {
        "slug": "companion-service",
        "name": "Companion Service",
        "icon": "person",
        "line": "A driver who stays with the passenger.",
        "image": "assets/images/1566073771259-6a8506099945.jpg",
        "alt": "A quiet hotel entrance",
        "intro": "Appointments, shopping, or a passenger who needs a steady hand.",
        "copy": "Some trips are not just a drop at the kerb. A companion booking means the driver waits, helps with the door and the bags, and takes the passenger on to the next stop. Tell us if there is a walking frame, a clinic time, or someone who should not be left outside. We will allow the extra time instead of rushing the meter.",
    },
    {
        "slug": "private-drivers",
        "name": "Private Drivers",
        "icon": "wheel",
        "line": "A car and driver by the hour.",
        "image": "assets/images/dunedin-roslyn.jpg",
        "alt": "Dunedin city and harbour from the hills",
        "credit": 'Dunedin from Roslyn. Photo: <a href="https://commons.wikimedia.org/wiki/File:Dunedin_City_Centre_from_Roslyn.jpg">Lord A.Nelson</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>',
        "intro": "Useful for visitors who do not want a rental car.",
        "copy": "Hire the driver for a few hours or the day. Peninsula, the station, Baldwin Street, a run out to the coast — you set the stops, the car stays with you. This is also how longer South Island trips start: Dunedin to Queenstown, Wanaka or Christchurch, quoted before anyone leaves.",
    },
    {
        "slug": "corporate-vehicle",
        "name": "Corporate Vehicle",
        "icon": "case",
        "line": "Client pickups and staff travel.",
        "image": "assets/images/van-b.jpg",
        "alt": "A grey sedan parked in a city",
        "intro": "A clean car and a driver who is on time.",
        "copy": "If you are collecting a client from the airport or moving staff between sites, the car should not be the thing people talk about afterwards. We keep it simple: a confirmed time, a named pickup, and a driver who knows the address. Accounts that book often can deal with one phone number rather than a new driver every trip.",
    },
    {
        "slug": "package-delivery",
        "name": "Urgent Package Delivery",
        "icon": "box",
        "line": "Same-day documents and parcels.",
        "image": "assets/images/1566576721346-d4a3b4eaeb55.jpg",
        "alt": "A sealed parcel",
        "intro": "Across Dunedin, when a courier is too slow.",
        "copy": "A signed envelope, a small parcel, a set of keys. Give us the pickup, the drop-off and who will receive it. We treat it as a direct run, not a loop of other stops. If the item is large, heavy or needs two people, say that in the notes so we send the right vehicle.",
    },
    {
        "slug": "jump-start",
        "name": "Jump Start",
        "icon": "bolt",
        "line": "A flat battery, not a tow.",
        "image": "assets/images/1486262715619-67b85e0b08d3.jpg",
        "alt": "A car engine bay",
        "intro": "Driveway, carpark or the side of a quiet street.",
        "copy": "If the car will not start and you think it is the battery, call us and tell us where it is sitting. We will come out and try a jump start. This is not a breakdown truck. If the car needs a tow, or it is in a live lane, we will tell you and you can call a recovery service. Have the keys and the bonnet release ready.",
    },
    {
        "slug": "ski-transfers",
        "name": "Ski Transfers",
        "icon": "snow",
        "line": "Dunedin to the South Island fields.",
        "image": "assets/images/1551698618-1dfe5d97d256.jpg",
        "alt": "A skier on a snowy slope",
        "intro": "Coronet Peak, the Remarkables, Cardrona, Treble Cone.",
        "copy": "These are long, early runs, so they are pre-booked. We pick up from your house or hotel in Dunedin, fit the skis or boards in the vehicle, and drive you to the field. The same car can bring you back on the day you choose. Tell us how many people and how many sets of gear. A sedan is the wrong tool for four people and four boards — we would rather send the bigger vehicle the night before than find out at 5am.",
    },
]


def icon(name):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


def services_menu(prefix):
    links = []
    for svc in SERVICES:
        links.append(
            f'<a href="{prefix}services/{svc["slug"]}.html">{icon(svc["icon"])}{svc["name"]}</a>'
        )
    return "\n".join(links)


def shell(title, description, body, prefix="", current=""):
    def current_attr(key):
        return ' aria-current="page"' if current == key else ""

    return f"""<!doctype html>
<html lang="en-NZ">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="{prefix}assets/logo-tile.png">
  <link rel="stylesheet" href="{prefix}css/lenis.css">
  <link rel="stylesheet" href="{prefix}css/styles.css?v=25">
  <script>
    (function () {{
      try {{
        var saved = localStorage.getItem("townTaxiTheme");
        var night = saved === "night";
        if (saved !== "day" && saved !== "night") {{
          var parts = new Intl.DateTimeFormat("en-GB", {{ timeZone: "Pacific/Auckland", month: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23" }}).formatToParts(new Date());
          var pick = function (type) {{ return Number((parts.find(function (part) {{ return part.type === type; }}) || {{}}).value || 0); }};
          var now = pick("hour") * 60 + pick("minute");
          var table = {{ 1: [360, 1275], 2: [400, 1240], 3: [440, 1180], 4: [410, 1090], 5: [450, 1040], 6: [480, 1020], 7: [470, 1035], 8: [435, 1070], 9: [390, 1100], 10: [380, 1190], 11: [340, 1240], 12: [330, 1280] }};
          var pair = table[pick("month")] || [390, 1170];
          night = now < pair[0] || now >= pair[1];
        }}
        if (night) document.documentElement.classList.add("is-night");
      }} catch (error) {{}}
    }})();
  </script>
</head>
<body>
  <div class="scroll-line" aria-hidden="true"><span id="scrollLine"></span></div>
  <div class="cursor-dot" aria-hidden="true"></div>
  <div class="cursor-ring" aria-hidden="true"></div>
  <header class="site-header">
    <div class="nav">
      <a class="brand" href="{prefix}index.html">
        <img src="{prefix}assets/logo-mark.png" alt="">
        <span>Town Taxi<small>Dunedin</small></span>
      </a>
      <nav class="nav-links" data-lenis-prevent-touch>
        <a href="{prefix}index.html"{current_attr("home")}>Home</a>
        <div class="drop">
          <button class="drop-btn" type="button" aria-expanded="false"{current_attr("services")}>Services</button>
          <div class="drop-panel">
            {services_menu(prefix)}
          </div>
        </div>
        <a href="{prefix}about.html"{current_attr("about")}>About</a>
        <a href="{prefix}areas.html"{current_attr("areas")}>Areas</a>
        <a href="{prefix}contact.html"{current_attr("contact")}>Contact</a>
        <a class="btn btn-yellow menu-book" href="{prefix}index.html#book">Book a cab</a>
      </nav>
      <button class="theme-btn" type="button" aria-pressed="false" aria-label="Switch to night">
        <svg class="icon-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M16.2 13.4A6.4 6.4 0 0 1 9.6 4.3 7 7 0 1 0 19.7 14.2a6.4 6.4 0 0 1-3.5-.8z"/></svg>
        <svg class="icon-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.4"/><path d="M12 3.2v2.2M12 18.6v2.2M3.2 12h2.2M18.6 12h2.2M5.8 5.8l1.5 1.5M16.7 16.7l1.5 1.5M18.2 5.8l-1.5 1.5M7.3 16.7l-1.5 1.5"/></svg>
      </button>
      <a class="btn btn-yellow desk-book" href="{prefix}index.html#book">Book a cab</a>
      <button class="nav-toggle" type="button" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
    </div>
  </header>
  {body}
  <footer class="site-footer">
    <div class="horizon-car" aria-hidden="true">
      <div class="car3d">
        <div class="car3d-shadow"></div>
        <div class="car3d-shell">
          <div class="car3d-roof"></div>
          <div class="car3d-glass"></div>
          <div class="car3d-sign">Taxi</div>
          <div class="car3d-lamp"></div>
        </div>
        <div class="car3d-wheel back"><i></i></div>
        <div class="car3d-wheel front"><i></i></div>
      </div>
    </div>
    <div class="wrap foot">
      <div>
        <img class="foot-logo" src="{prefix}assets/logo-mark.png" alt="">
        <p>Town Taxi is a Dunedin service for locals, visitors, airport travellers and businesses. Open 24 hours.</p>
      </div>
      <div>
        <h3>Visit</h3>
        <a href="{prefix}index.html">Home</a>
        <a href="{prefix}about.html">About</a>
        <a href="{prefix}areas.html">Areas</a>
        <a href="{prefix}contact.html">Contact</a>
      </div>
      <div>
        <h3>Desk</h3>
        <a href="tel:+64204522958">+64 20 452 2958</a>
        <a href="https://wa.me/64204522958" target="_blank" rel="noreferrer">WhatsApp</a>
        <a href="mailto:hitowntaxi@gmail.com">hitowntaxi@gmail.com</a>
      </div>
      <div>
        <h3>Hours</h3>
        <p>24 hours, 7 days<br>Dunedin, New Zealand</p>
        <a href="https://www.facebook.com/share/18od8Xp4LX/" target="_blank" rel="noreferrer">Facebook</a>
        <a href="https://www.instagram.com/towntaxidunedin/" target="_blank" rel="noreferrer">Instagram</a>
      </div>
    </div>
    <div class="wrap legal">© 2026 Town Taxi · towntaxi.co.nz</div>
  </footer>
  <a class="call-fab" href="tel:+64204522958" data-copy="+64 20 452 2958" aria-label="Call Town Taxi">
    {icon("phone")}
  </a>
  <div class="phone-bar">
    <a class="btn btn-ghost" href="tel:+64204522958">Call</a>
    <a class="btn btn-yellow" href="{prefix}index.html#book">Book</a>
  </div>
  <div class="driver-card" id="driverCard" hidden>
    <div class="driver-sheet" role="dialog" aria-modal="true" aria-labelledby="driverWhen">
      <p class="eyebrow">With the desk</p>
      <p class="driver-when" id="driverWhen"></p>
      <div class="driver-ends">
        <span id="driverFrom"></span>
        <span class="driver-via" id="driverVia" hidden></span>
        <span id="driverTo"></span>
      </div>
      <p id="driverWho"></p>
      <p class="driver-phone">Town Taxi · +64 20 452 2958</p>
      <button class="btn btn-ink" id="driverClose" type="button">Close</button>
    </div>
  </div>
  <div class="toast" role="status"></div>
  <script src="{prefix}js/lenis.min.js"></script>
  <script src="{prefix}js/site.js?v=28"></script>
</body>
</html>
"""


def booking_form():
    return f"""
        <form class="glass book" id="bookingForm">
          <h2 class="serif">Book a cab</h2>
          <p class="trip-line" id="tripLine">Tell us the pickup and drop-off.</p>
          <div class="route-sketch" id="routeSketch" hidden>
            <svg viewBox="0 0 280 28" aria-hidden="true">
              <path class="route-path" d="M8 16 H272"/>
              <circle cx="8" cy="16" r="3.5"/>
              <circle class="route-via" cx="140" cy="16" r="3" hidden/>
              <circle class="route-end" cx="272" cy="16" r="3.5"/>
            </svg>
            <span id="routeEnds"></span>
          </div>
          <div class="fields">
            <div class="field"><label for="name">Name</label><input id="name" name="name" required autocomplete="name"></div>
            <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" required autocomplete="tel"></div>
            <div class="field full"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" placeholder="Optional"></div>
            <div class="field"><label for="pickup">Pickup</label><input id="pickup" name="pickup" required placeholder="Address, hotel or airport"></div>
            <div class="field"><label for="dropoff">Drop-off</label><input id="dropoff" name="dropoff" required></div>
            <div class="field full"><label for="via">Stop on the way</label><input id="via" name="via" placeholder="Optional, one extra stop"></div>
            <div class="field full">
              <div class="trip-tools">
                <button type="button" id="sameTrip" hidden>Same as last time</button>
                <button type="button" id="swapTrip" aria-label="Swap pickup and drop-off">Swap ends</button>
              </div>
              <div class="recent-trips" id="recentTrips" hidden aria-label="Recent trips"></div>
              <p class="place-note">These buttons fill the drop-off.</p>
              <div class="place-picks" aria-label="Common Dunedin drop-offs">
                <button type="button" data-place="Dunedin Airport">Airport</button>
                <button type="button" data-place="The Octagon">Octagon</button>
                <button type="button" data-place="Dunedin Hospital">Hospital</button>
                <button type="button" data-place="Mosgiel">Mosgiel</button>
                <button type="button" data-place="Larnach Castle">Larnach Castle</button>
                <button type="button" data-place="Tunnel Beach">Tunnel Beach</button>
                <button type="button" data-place="Portobello Beach">Portobello Beach</button>
              </div>
            </div>
            <div class="field"><label for="pickupDate">Date</label><input id="pickupDate" name="pickupDate" type="date" required></div>
            <div class="field">
              <label for="pickupTime">Pickup time</label>
              <div class="time-picks">
                <button class="chip is-on" type="button" data-when="now">Now</button>
                <button class="chip" type="button" data-when="later">Later</button>
              </div>
              <input id="pickupTime" name="pickupTime" type="time" required>
              <input type="hidden" id="timeMode" name="timeMode" value="now">
            </div>
            <div class="field"><label for="passengers">Passengers</label>
              <select id="passengers" name="passengers" required>
                <option selected>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7</option><option>8</option>
              </select>
            </div>
            <input type="hidden" id="service" name="service" value="Taxi">
            <div class="field full"><label for="notes">Notes</label><textarea id="notes" name="notes" placeholder="Bags, child seat, hotel entrance, access needs"></textarea></div>
            <input class="full" type="text" name="_honey" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
          </div>
          <div class="send-row">
            <button class="btn btn-ink" type="submit">Send booking</button>
            <a class="btn btn-ghost" id="liveWhats" href="https://wa.me/64204522958" target="_blank" rel="noreferrer">Send this on WhatsApp</a>
            <a class="btn btn-ghost" id="routeMaps" href="https://www.google.com/maps/dir/?api=1&amp;travelmode=driving" target="_blank" rel="noreferrer">See the route</a>
          </div>
          <p class="form-status" id="formStatus"></p>
          <div class="slip" id="tripSlip" hidden>
            <p class="eyebrow">With the desk</p>
            <h3 id="slipTitle"></h3>
            <p id="slipBody"></p>
            <div class="slip-actions">
              <a class="btn btn-yellow" id="slipWhats" href="https://wa.me/64204522958" target="_blank" rel="noreferrer">Send it on WhatsApp too</a>
              <a class="btn btn-ghost" id="slipMaps" href="https://www.google.com/maps/dir/?api=1&amp;travelmode=driving" target="_blank" rel="noreferrer">Open in Maps</a>
              <button class="btn btn-ghost" id="slipCopy" type="button">Copy details</button>
              <button class="btn btn-ghost" id="slipDriver" type="button">Show the driver</button>
              <button class="btn btn-ghost" id="slipCal" type="button" hidden>Add to calendar</button>
            </div>
          </div>
          <p class="fine">Each booking is emailed to hitowntaxi@gmail.com. Add an email and a copy comes back to you too.</p>
        </form>
    """


def story(prefix, image, alt, title, text, credit=""):
    caption = f"\n          <figcaption>{credit}</figcaption>" if credit else ""
    return f"""
    <section class="section">
      <div class="wrap split">
        <div>
          <div class="rule"></div>
          <h2>{title}</h2>
          <p>{text}</p>
        </div>
        <figure class="frame">
          <div class="frame-photo">
            <img src="{prefix}{image}" alt="{alt}">
          </div>{caption}
        </figure>
      </div>
    </section>
    """


home = shell(
    "Town Taxi Dunedin | 24 hour cabs",
    "Town Taxi is a 24 hour Dunedin taxi for airport transfers, local trips, corporate travel and longer South Island runs.",
    f"""
    <main>
      <section class="hero">
        <video class="hero-video" autoplay muted loop playsinline poster="assets/images/dunedin-roslyn.jpg">
          <source src="assets/video/hero.mp4" type="video/mp4">
        </video>
        <div class="hero-veil"></div>
        <div class="hero-grid">
          <div class="reveal">
            <p class="eyebrow" id="nzClock">Dunedin · Open 24 hours</p>
            <h1>Your trip, your way.</h1>
            <p class="hero-actions">
              <a class="btn btn-yellow" href="https://wa.me/64204522958" target="_blank" rel="noreferrer">WhatsApp</a>
              <a class="btn btn-ghost" href="tel:+64204522958" data-copy="+64 20 452 2958">Call +64 20 452 2958</a>
            </p>
          </div>
          <div id="book" class="reveal">{booking_form()}</div>
        </div>
        <div class="hero-drive" aria-hidden="true">
          <div class="horizon-car is-driving">
            <div class="car3d">
              <div class="car3d-shadow"></div>
              <div class="car3d-shell">
                <div class="car3d-roof"></div>
                <div class="car3d-glass"></div>
                <div class="car3d-sign">Taxi</div>
                <div class="car3d-lamp"></div>
              </div>
              <div class="car3d-wheel back"><i></i></div>
              <div class="car3d-wheel front"><i></i></div>
            </div>
          </div>
        </div>
      </section>
      <div class="places" aria-hidden="true">
        <div class="places-track">
          <span>The Octagon</span><span>Dunedin Airport</span><span>Larnach Castle</span><span>The hospital</span><span>Tunnel Beach</span><span>Portobello Beach</span><span>Mosgiel</span><span>Port Chalmers</span>
          <span>The Octagon</span><span>Dunedin Airport</span><span>Larnach Castle</span><span>The hospital</span><span>Tunnel Beach</span><span>Portobello Beach</span><span>Mosgiel</span><span>Port Chalmers</span>
        </div>
      </div>
      <section class="section" style="padding-top:28px">
        <div class="wrap reasons">
          <article class="glass reason"><strong>24 hours</strong><p>Early flights and late finishes use the same number.</p></article>
          <article class="glass reason"><strong>Private car</strong><p>Your booking is not shared with other passengers.</p></article>
          <article class="glass reason"><strong>Door to door</strong><p>House, hotel, hospital, campus or the airport.</p></article>
          <article class="glass reason"><strong>Confirmed first</strong><p>We call you back before the car is on the way.</p></article>
        </div>
      </section>
      <section class="section" style="padding-top:10px">
        <div class="wrap">
          <p class="eyebrow">Services</p>
          <h2>What the car is for.</h2>
          <div class="directory" style="margin-top:28px">
            {''.join(f'<a class="svc" href="services/{s["slug"]}.html">{icon(s["icon"])}<span><b>{s["name"]}</b>{s["line"]}</span><i>→</i></a>' for s in SERVICES)}
          </div>
        </div>
      </section>
      {story("", "assets/images/dunedin-roslyn.jpg", "Dunedin city and harbour from the hills", "Based in Dunedin. The longer trips are booked, not waved down.", "Local work stays in the city. Airport, corporate and South Island runs are arranged ahead, with the price talked through before you travel. If you only remember one thing: call +64 20 452 2958. Someone answers, day or night.", 'Dunedin from Roslyn. Photo: <a href="https://commons.wikimedia.org/wiki/File:Dunedin_City_Centre_from_Roslyn.jpg">Lord A.Nelson</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>')}
    </main>
    """,
    current="home",
)

about = shell(
    "About Town Taxi | Dunedin",
    "Town Taxi is a reliable 24 hour taxi service based in Dunedin, New Zealand.",
    f"""
    <main>
      <section class="page-hero">
        <img src="assets/images/1566073771259-6a8506099945.jpg" alt="">
        <div class="veil"></div>
        <div class="wrap">
          <div class="rule"></div>
          <h1>A Dunedin taxi desk that picks up the phone.</h1>
          <p class="lede">Town Taxi is a reliable and professional taxi service based in Dunedin, providing safe, comfortable and convenient transportation for local customers, visitors, airport travellers and businesses.</p>
        </div>
      </section>
      {story("", "assets/images/sedan-b.jpg", "Town Taxi style sedan", "The job is the pickup, not the website.", "People book us because a flight is early, a guest is waiting at a motel, or a meeting cannot start late. The site is here so you can send the details without dictating them down the phone. The car still has to be where we said it would be.")}
    </main>
    """,
    current="about",
)

contact = shell(
    "Contact Town Taxi | Dunedin",
    "Call, WhatsApp or email Town Taxi in Dunedin. Open 24 hours.",
    f"""
    <main>
      <section class="section">
        <div class="wrap">
          <p class="eyebrow">Contact</p>
          <h1>Call, or send the booking through.</h1>
          <div class="contact-grid" style="margin-top:28px">
            <div>
              <article class="glass card"><h3>Phone</h3><p><a href="tel:+64204522958" data-copy="+64 20 452 2958">+64 20 452 2958</a></p><p>Same number on WhatsApp.<br><a href="https://wa.me/64204522958">Open WhatsApp</a></p></article>
              <article class="glass card"><h3>Email</h3><p><a href="mailto:hitowntaxi@gmail.com">hitowntaxi@gmail.com</a></p></article>
              <article class="glass card"><h3>Base</h3><p>Dunedin, New Zealand<br>Open 24 hours, 7 days.</p><p><a href="https://www.facebook.com/share/18od8Xp4LX/" target="_blank" rel="noreferrer">Facebook</a><br><a href="https://www.instagram.com/towntaxidunedin/" target="_blank" rel="noreferrer">Instagram</a></p></article>
            </div>
            <div class="map-frame">
              <iframe title="Map of Dunedin, New Zealand" src="https://www.openstreetmap.org/export/embed.html?bbox=170.45%2C-45.95%2C170.62%2C-45.82&amp;layer=mapnik&amp;marker=-45.8742%2C170.5036"></iframe>
            </div>
          </div>
          <p class="fine" style="margin-top:10px">Map by OpenStreetMap. It does not use a paid key, so it will not expire.</p>
        </div>
      </section>
      <section class="section" style="padding-top:0">
        <div class="wrap" style="max-width:760px" id="book">{booking_form()}</div>
      </section>
    </main>
    """,
    current="contact",
)

areas = shell(
    "Areas | Town Taxi Dunedin",
    "Town Taxi covers Dunedin, the airport, Mosgiel, Port Chalmers and booked ski runs.",
    """
    <main>
      <section class="section">
        <div class="wrap">
          <p class="eyebrow">Areas</p>
          <h1>Where the car goes.</h1>
          <p class="lede">Local work stays around Dunedin. Longer runs, including the ski fields, are booked ahead and the price is talked through before you travel.</p>
          <div class="areas" style="margin-top:28px">
            <article class="glass card"><h3>Dunedin</h3><p>The Octagon, the hospital, the university, St Clair, South Dunedin and the hill suburbs. Book it now or for later.</p></article>
            <article class="glass card"><h3>Dunedin Airport</h3><p>Momona, for arrivals and early departures. Tell us the time you need to be there. We do not ask for a flight number.</p></article>
            <article class="glass card"><h3>Mosgiel</h3><p>A booked run out of the city, not a car you wave down on the street.</p></article>
            <article class="glass card"><h3>Port Chalmers</h3><p>The port and cruise days. Say which gate or ship entrance in the notes.</p></article>
            <article class="glass card"><h3>Ski runs</h3><p>Dunedin to the South Island fields. These are arranged ahead, with the timing and the price agreed before the car leaves.</p></article>
          </div>
          <div class="map-frame" style="margin-top:22px">
            <iframe title="Map of Dunedin, the airport, Mosgiel and Port Chalmers" src="https://www.openstreetmap.org/export/embed.html?bbox=170.15%2C-45.98%2C170.72%2C-45.78&amp;layer=mapnik&amp;marker=-45.8742%2C170.5036"></iframe>
          </div>
          <p class="fine" style="margin-top:10px">Map by OpenStreetMap. The ski fields sit further inland, so they are not on this city map.</p>
          <p style="margin-top:18px"><a class="btn btn-yellow" href="index.html#book">Book a cab</a></p>
        </div>
      </section>
    </main>
    """,
    current="areas",
)

pages = {
    "index.html": home,
    "about.html": about,
    "areas.html": areas,
    "contact.html": contact,
}

(ROOT / "services").mkdir(exist_ok=True)
for name, html in pages.items():
    (ROOT / name).write_text(html, encoding="utf-8")

for svc in SERVICES:
    page = shell(
        f"{svc['name']} | Town Taxi Dunedin",
        svc["intro"],
        f"""
        <main>
          <section class="page-hero">
            <img src="../{svc['image']}" alt="">
            <div class="veil"></div>
            <div class="wrap">
              <p class="eyebrow">Service</p>
              <h1>{svc['name']}</h1>
              <p class="lede">{svc['intro']}</p>
            </div>
          </section>
          <section class="section">
            <div class="wrap facts">
              <article class="glass fact"><h3>When</h3><p>Now, or a time you set. Early and late jobs are the same desk.</p></article>
              <article class="glass fact"><h3>What we need</h3><p>Name, phone, pickup, drop-off, date, time and how many passengers.</p></article>
              <article class="glass fact"><h3>What you get</h3><p>A private car, and a call back before we dispatch.</p></article>
            </div>
          </section>
          {story("../", svc["image"], svc["alt"], svc["name"], svc["copy"], svc.get("credit", ""))}
          <section class="section" style="padding-top:0">
            <div class="wrap">
              <a class="btn btn-yellow" href="../index.html?service={svc['name'].replace(' ', '%20')}#book">Book {svc['name']}</a>
            </div>
          </section>
        </main>
        """,
        prefix="../",
        current="services",
    )
    (ROOT / "services" / f"{svc['slug']}.html").write_text(page, encoding="utf-8")

print("wrote", len(pages) + len(SERVICES), "pages")
