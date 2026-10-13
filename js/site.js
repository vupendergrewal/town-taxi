document.documentElement.classList.add("js");

const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");
let menuAnchor = 0;
function closeMenus() {
  navLinks?.classList.remove("open");
  navToggle?.setAttribute("aria-expanded", "false");
  document.querySelectorAll(".drop.open").forEach((drop) => {
    drop.classList.remove("open");
    drop.querySelector(".drop-btn")?.setAttribute("aria-expanded", "false");
  });
}
navToggle?.addEventListener("click", () => {
  const open = navLinks.classList.toggle("open");
  navToggle.setAttribute("aria-expanded", String(open));
  if (!open) {
    closeMenus();
    return;
  }
  if (touch && window.lenis) window.lenis.reset();
  menuAnchor = window.scrollY;
});
window.addEventListener("scroll", () => {
  if (!touch || !navLinks?.classList.contains("open")) return;
  if (Math.abs(window.scrollY - menuAnchor) > 28) closeMenus();
}, { passive: true });

document.querySelectorAll(".drop-btn").forEach((button) => {
  button.addEventListener("click", (event) => {
    event.stopPropagation();
    const drop = button.closest(".drop");
    const willOpen = !drop.classList.contains("open");
    document.querySelectorAll(".drop.open").forEach((other) => {
      other.classList.remove("open");
      other.querySelector(".drop-btn")?.setAttribute("aria-expanded", "false");
    });
    drop.classList.toggle("open", willOpen);
    button.setAttribute("aria-expanded", String(willOpen));
  });
});
document.addEventListener("click", (event) => {
  if (event.target.closest(".drop")) return;
  document.querySelectorAll(".drop.open").forEach((drop) => {
    drop.classList.remove("open");
    drop.querySelector(".drop-btn")?.setAttribute("aria-expanded", "false");
  });
});

const header = document.querySelector(".site-header");
let navShown = 0;
let navTarget = 0;
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const touch = window.matchMedia("(pointer: coarse), (max-width: 980px)").matches;
const navRange = touch ? 220 : 460;
let lenis = null;
if (window.Lenis) {
  lenis = new Lenis({
    lerp: touch ? 0.1 : 0.065,
    smoothWheel: true,
    syncTouch: true,
    syncTouchLerp: 0.08,
    touchInertiaMultiplier: 34,
    wheelMultiplier: 0.72,
    touchMultiplier: 1.15,
    virtualScroll() {
      return !document.documentElement.classList.contains("is-typing");
    },
  });
  window.lenis = lenis;
  const fieldSelector = "input, textarea, select";
  const typingNow = () => document.activeElement?.matches?.(fieldSelector) ?? false;
  const releaseScroll = () => {
    const typing = typingNow();
    document.documentElement.classList.toggle("is-typing", typing);
    if (typing) {
      lenis.options.syncTouch = false;
      lenis.reset();
    } else if (touch) {
      lenis.options.syncTouch = true;
    }
  };
  document.addEventListener("focusin", (event) => {
    if (event.target.matches(fieldSelector)) releaseScroll();
  });
  document.addEventListener("focusout", () => {
    setTimeout(releaseScroll, 60);
  });
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (event) => {
      const id = link.getAttribute("href");
      const target = id && id.length > 1 ? document.querySelector(id) : null;
      if (!target) return;
      event.preventDefault();
      lenis.scrollTo(target, { offset: -90 });
    });
  });
}

function frame(time) {
  if (lenis) lenis.raf(time);
  const y = lenis ? lenis.scroll : window.scrollY;
  const moved = Math.abs(window.scrollY - menuAnchor) > 28 || Math.abs(y - menuAnchor) > 28;
  if (touch && navLinks?.classList.contains("open") && moved) closeMenus();
  navTarget = Math.min(1, Math.max(0, y / navRange));
  const follow = 0.06;
  navShown += (navTarget - navShown) * follow;
  if (Math.abs(navTarget - navShown) < 0.0004) navShown = navTarget;
  header?.style.setProperty("--nav-p", navShown.toFixed(4));
  const line = document.querySelector("#scrollLine");
  if (line) {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const progress = max > 0 ? Math.min(1, Math.max(0, y / max)) : 0;
    line.style.transform = `scaleX(${progress})`;
  }
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);

const riseItems = document.querySelectorAll(".reason, .svc, .fact, .split > div, .split > figure, .card");
const riseObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add("is-in");
    riseObserver.unobserve(entry.target);
  });
}, { threshold: 0.2 });
riseItems.forEach((item, index) => {
  item.classList.add("rise");
  item.style.setProperty("--d", `${(index % 4) * 80}ms`);
  riseObserver.observe(item);
});

const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
if (finePointer && !reduceMotion) {
  document.body.classList.add("has-cursor");
  const dot = document.querySelector(".cursor-dot");
  const ring = document.querySelector(".cursor-ring");
  let x = 0;
  let y = 0;
  let rx = 0;
  let ry = 0;
  window.addEventListener("pointermove", (event) => {
    x = event.clientX;
    y = event.clientY;
    if (dot) dot.style.transform = `translate(${x}px, ${y}px)`;
    const hot = event.target.closest("a, button");
    document.body.classList.toggle("cursor-hot", Boolean(hot));
  });
  const follow = () => {
    rx += (x - rx) * 0.18;
    ry += (y - ry) * 0.18;
    if (ring) ring.style.transform = `translate(${rx}px, ${ry}px)`;
    requestAnimationFrame(follow);
  };
  follow();
}

const toast = document.querySelector(".toast");
function showToast(message) {
  if (!toast) return;
  toast.textContent = message;
  toast.classList.add("show");
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => toast.classList.remove("show"), 2600);
}

document.querySelectorAll("[data-copy]").forEach((link) => {
  link.addEventListener("click", async () => {
    const value = link.getAttribute("data-copy");
    try {
      await navigator.clipboard.writeText(value);
      showToast("Number copied. Your phone should open with it filled in.");
    } catch {
      showToast(value);
    }
  });
});

const form = document.querySelector("#bookingForm");
const nowChip = document.querySelector("[data-when='now']");
const laterChip = document.querySelector("[data-when='later']");
const timeInput = document.querySelector("#pickupTime");
const dateInput = document.querySelector("#pickupDate");
const timeMode = document.querySelector("#timeMode");

function nzParts() {
  const parts = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Pacific/Auckland",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    hourCycle: "h23",
  }).formatToParts(new Date());
  const get = (type) => parts.find((part) => part.type === type)?.value || "00";
  return { date: `${get("year")}-${get("month")}-${get("day")}`, time: `${get("hour")}:${get("minute")}` };
}
function setWhen(mode) {
  if (!timeInput || !timeMode) return;
  const nz = nzParts();
  timeMode.value = mode;
  nowChip?.classList.toggle("is-on", mode === "now");
  laterChip?.classList.toggle("is-on", mode === "later");
  if (dateInput && !dateInput.value) dateInput.value = nz.date;
  if (mode === "now") {
    if (dateInput) dateInput.value = nz.date;
    timeInput.value = nz.time;
  }
  timeInput.readOnly = mode === "now";
}
nowChip?.addEventListener("click", () => setWhen("now"));
laterChip?.addEventListener("click", () => setWhen("later"));
setWhen("now");

const clock = document.querySelector("#nzClock");
function dunHour() {
  return Number(new Intl.DateTimeFormat("en-GB", {
    timeZone: "Pacific/Auckland",
    hour: "2-digit",
    hourCycle: "h23",
  }).format(new Date()));
}
function dayPart(hour) {
  if (hour < 5 || hour >= 21) return "Late night";
  if (hour < 12) return "Morning";
  if (hour < 17) return "Afternoon";
  return "Evening";
}
function paintClock() {
  if (!clock) return;
  const label = new Intl.DateTimeFormat("en-NZ", {
    timeZone: "Pacific/Auckland",
    weekday: "long",
    hour: "numeric",
    minute: "2-digit",
  }).format(new Date());
  clock.textContent = `${dayPart(dunHour())} in Dunedin · ${label} · open`;
}
paintClock();
setInterval(paintClock, 30000);

const tripLine = document.querySelector("#tripLine");
function viaValue() {
  return document.querySelector("#via")?.value.trim() || "";
}
function paintTrip() {
  if (!tripLine) return;
  const pickup = document.querySelector("#pickup")?.value.trim();
  const dropoff = document.querySelector("#dropoff")?.value.trim();
  const via = viaValue();
  const people = document.querySelector("#passengers")?.value || "1";
  const when = timeMode?.value === "now" ? "leaving now" : "booked ahead";
  const route = pickup && dropoff
    ? (via ? `${pickup} to ${dropoff}, via ${via}` : `${pickup} to ${dropoff}`)
    : pickup ? `From ${pickup}` : dropoff ? `To ${dropoff}` : "Tell us the pickup and drop-off";
  tripLine.textContent = `${route} · ${people} passengers · ${when}`;
  const sketch = document.querySelector("#routeSketch");
  const ends = document.querySelector("#routeEnds");
  if (!sketch) return;
  const ready = Boolean(pickup && dropoff);
  const was = sketch.classList.contains("is-ready");
  sketch.hidden = !ready;
  if (!ready) {
    sketch.classList.remove("is-ready");
    if (ends) ends.textContent = "";
  } else if (!was) sketch.classList.add("is-ready");
  const viaDot = sketch.querySelector(".route-via");
  if (viaDot) viaDot.hidden = !(ready && via);
  if (ends && ready) ends.textContent = via ? `${pickup}  →  ${via}  →  ${dropoff}` : `${pickup}  →  ${dropoff}`;
}
const nameInput = document.querySelector("#name");
const phoneInput = document.querySelector("#phone");
const pickupInput = document.querySelector("#pickup");
const liveWhats = document.querySelector("#liveWhats");
if (nameInput && localStorage.getItem("townTaxiName")) nameInput.value = localStorage.getItem("townTaxiName");
if (phoneInput && localStorage.getItem("townTaxiPhone")) phoneInput.value = localStorage.getItem("townTaxiPhone");
function rememberPassenger() {
  if (nameInput) localStorage.setItem("townTaxiName", nameInput.value);
  if (phoneInput) localStorage.setItem("townTaxiPhone", phoneInput.value);
}
function tripMessage({ name, pickup, via, dropoff, when, passengers, service }) {
  const stop = via ? `, via ${via}` : "";
  return `Hi Town Taxi, this is ${name || "a passenger"}. Pickup ${pickup}${stop}, drop-off ${dropoff}, ${when}, ${passengers} passengers, ${service}.`;
}
function paintWhats() {
  if (!liveWhats) return;
  const pickup = pickupInput?.value.trim() || "";
  const dropoff = document.querySelector("#dropoff")?.value.trim() || "";
  const via = viaValue();
  const people = document.querySelector("#passengers")?.value || "1";
  const serviceName = document.querySelector("#service")?.selectedOptions?.[0]?.textContent || "Taxi";
  const when = timeMode?.value === "now" ? "now" : `${document.querySelector("#pickupDate")?.value || ""} ${document.querySelector("#pickupTime")?.value || ""}`.trim();
  const who = nameInput?.value.trim() || "a passenger";
  const message = tripMessage({
    name: who,
    pickup: pickup || "a pickup",
    via,
    dropoff: dropoff || "a drop-off",
    when,
    passengers: people,
    service: serviceName,
  });
  liveWhats.href = `https://wa.me/64204522958?text=${encodeURIComponent(message)}`;
  const maps = document.querySelector("#routeMaps");
  if (maps) maps.href = mapsHref(pickup, dropoff, via);
}
function inDunedin(place) {
  const clean = place.trim();
  return /dunedin/i.test(clean) ? clean : `${clean}, Dunedin`;
}
function mapsHref(pickup, dropoff, via) {
  if (pickup && dropoff) {
    const stop = via ? `&waypoints=${encodeURIComponent(inDunedin(via))}` : "";
    return `https://www.google.com/maps/dir/?api=1&origin=${encodeURIComponent(inDunedin(pickup))}&destination=${encodeURIComponent(inDunedin(dropoff))}${stop}&travelmode=driving`;
  }
  const place = pickup || dropoff;
  if (!place) return "https://www.google.com/maps/search/?api=1&query=Dunedin%2C%20New%20Zealand";
  return `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(inDunedin(place))}`;
}
function savedTrip() {
  try {
    return JSON.parse(localStorage.getItem("townTaxiLastTrip") || "null");
  } catch {
    return null;
  }
}
function showSame() {
  const button = document.querySelector("#sameTrip");
  if (button) button.hidden = !savedTrip()?.pickup;
}
function slimTrip(trip) {
  return {
    pickup: trip.pickup,
    dropoff: trip.dropoff,
    via: trip.via || "",
    passengers: trip.passengers || "1",
    service: trip.service || "Taxi",
    notes: trip.notes || "",
  };
}
function samePlace(a, b) {
  return a.pickup === b.pickup && a.dropoff === b.dropoff && (a.via || "") === (b.via || "");
}
function readTrips() {
  try {
    const list = JSON.parse(localStorage.getItem("townTaxiTrips") || "[]");
    if (Array.isArray(list) && list.length) return list.filter((item) => item?.pickup && item?.dropoff);
  } catch { /* fall through to the last saved trip */ }
  const last = savedTrip();
  return last?.pickup && last?.dropoff ? [last] : [];
}
function paintRecent() {
  const row = document.querySelector("#recentTrips");
  if (!row) return;
  const trips = readTrips().slice(0, 3);
  row.replaceChildren();
  row.hidden = trips.length === 0;
  trips.forEach((trip) => {
    const button = document.createElement("button");
    button.type = "button";
    const stop = trip.via ? ` via ${trip.via}` : "";
    button.textContent = `${trip.pickup} → ${trip.dropoff}${stop}`;
    button.title = button.textContent;
    button.addEventListener("click", () => fillTrip(trip));
    row.appendChild(button);
  });
}
function storeTrip(trip) {
  if (!trip?.pickup || !trip?.dropoff) return;
  const slim = slimTrip(trip);
  const previous = readTrips();
  localStorage.setItem("townTaxiLastTrip", JSON.stringify(slim));
  const next = [slim, ...previous.filter((item) => !samePlace(item, slim))].slice(0, 3);
  localStorage.setItem("townTaxiTrips", JSON.stringify(next));
  showSame();
  paintRecent();
}
function currentTrip() {
  return {
    pickup: pickupInput?.value.trim() || "",
    dropoff: document.querySelector("#dropoff")?.value.trim() || "",
    via: viaValue(),
    passengers: document.querySelector("#passengers")?.value || "1",
    service: document.querySelector("#service")?.value || "Taxi",
    notes: document.querySelector("#notes")?.value || "",
  };
}
function fillTrip(trip) {
  const dropoff = document.querySelector("#dropoff");
  const via = document.querySelector("#via");
  if (!trip || !pickupInput || !dropoff) return;
  pickupInput.value = trip.pickup || "";
  dropoff.value = trip.dropoff || "";
  if (via) via.value = trip.via || "";
  const passengers = document.querySelector("#passengers");
  const service = document.querySelector("#service");
  const notes = document.querySelector("#notes");
  if (passengers && trip.passengers) passengers.value = trip.passengers;
  if (service && trip.service && (!service.options || [...service.options].some((option) => option.value === trip.service))) service.value = trip.service;
  if (notes) notes.value = trip.notes || "";
  document.querySelectorAll("[data-place]").forEach((button) => button.classList.remove("is-on"));
  paintTrip();
  paintWhats();
}
function applySharedLink() {
  const query = new URLSearchParams(window.location.search);
  const service = document.querySelector("#service");
  const named = query.get("service");
  if (service && named && (!service.options || [...service.options].some((option) => option.value === named))) service.value = named;
  const pickup = query.get("pickup") || "";
  const dropoff = query.get("dropoff") || "";
  const via = query.get("via") || "";
  const notes = query.get("notes") || "";
  const passengers = query.get("passengers") || "";
  const hasTrip = Boolean(pickup || dropoff || via || notes || passengers || query.get("when") === "later");
  if (!hasTrip) return;
  const dropoffInput = document.querySelector("#dropoff");
  const viaInput = document.querySelector("#via");
  const notesInput = document.querySelector("#notes");
  const passengersInput = document.querySelector("#passengers");
  if (pickupInput && pickup) pickupInput.value = pickup;
  if (dropoffInput && dropoff) dropoffInput.value = dropoff;
  if (viaInput && via) viaInput.value = via;
  if (notesInput && notes) notesInput.value = notes;
  if (passengersInput && [...passengersInput.options].some((option) => option.value === passengers)) passengersInput.value = passengers;
  if (query.get("when") === "later") {
    setWhen("later");
    const date = query.get("date");
    const time = query.get("time");
    if (dateInput && date) dateInput.value = date;
    if (timeInput && time) timeInput.value = time;
  }
  document.querySelectorAll("[data-place]").forEach((button) => {
    button.classList.toggle("is-on", button.getAttribute("data-place") === dropoff);
  });
}
showSame();
paintRecent();
document.querySelector("#sameTrip")?.addEventListener("click", () => fillTrip(savedTrip()));
document.querySelector("#swapTrip")?.addEventListener("click", () => {
  const dropoff = document.querySelector("#dropoff");
  if (!pickupInput || !dropoff) return;
  const next = dropoff.value;
  dropoff.value = pickupInput.value;
  pickupInput.value = next;
  document.querySelectorAll("[data-place]").forEach((button) => button.classList.remove("is-on"));
  paintTrip();
  paintWhats();
});
liveWhats?.addEventListener("click", () => storeTrip(currentTrip()));
document.querySelectorAll("[data-place]").forEach((button) => {
  button.addEventListener("click", () => {
    const dropoff = document.querySelector("#dropoff");
    if (!dropoff) return;
    dropoff.value = button.getAttribute("data-place") || "";
    document.querySelectorAll("[data-place]").forEach((other) => other.classList.toggle("is-on", other === button));
    paintTrip();
    paintWhats();
  });
});
form?.addEventListener("input", () => {
  rememberPassenger();
  paintTrip();
  paintWhats();
});
form?.addEventListener("change", () => {
  paintTrip();
  paintWhats();
});
applySharedLink();
paintTrip();
paintWhats();

function aucklandClock() {
  const parts = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Pacific/Auckland",
    month: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    hourCycle: "h23",
  }).formatToParts(new Date());
  const get = (type) => Number(parts.find((item) => item.type === type)?.value || "0");
  return { month: get("month"), minutes: get("hour") * 60 + get("minute") };
}
function dunIsNight() {
  const { month, minutes: now } = aucklandClock();
  const table = {
    1: [360, 1275], 2: [400, 1240], 3: [440, 1180], 4: [410, 1090],
    5: [450, 1040], 6: [480, 1020], 7: [470, 1035], 8: [435, 1070],
    9: [390, 1100], 10: [380, 1190], 11: [340, 1240], 12: [330, 1280],
  };
  const [rise, set] = table[month] || [390, 1170];
  return now < rise || now >= set;
}
function applyTheme() {
  const saved = localStorage.getItem("townTaxiTheme");
  const night = saved === "night" || (saved !== "day" && dunIsNight());
  document.documentElement.classList.toggle("is-night", night);
  const button = document.querySelector(".theme-btn");
  if (!button) return;
  button.setAttribute("aria-pressed", String(night));
  button.setAttribute("aria-label", night ? "Switch to day" : "Switch to night");
}
document.querySelector(".theme-btn")?.addEventListener("click", () => {
  const night = document.documentElement.classList.contains("is-night");
  localStorage.setItem("townTaxiTheme", night ? "day" : "night");
  applyTheme();
});
applyTheme();
setInterval(applyTheme, 60000);

const tripPlans = {
  now: { service: "Taxi", mode: "now" },
  airport: { service: "Airport Transfer", pickup: "Dunedin Airport", mode: "later" },
  town: { service: "Taxi", mode: "now" },
  ski: { service: "Ski Transfers", mode: "later" },
  event: { service: "Event Management", mode: "later" },
};
document.querySelectorAll("[data-trip]").forEach((button) => {
  button.addEventListener("click", () => {
    const plan = tripPlans[button.getAttribute("data-trip")];
    if (!plan) return;
    document.querySelectorAll("[data-trip]").forEach((other) => other.classList.toggle("is-on", other === button));
    const service = document.querySelector("#service");
    const pickup = document.querySelector("#pickup");
    if (service && plan.service && (!service.options || [...service.options].some((option) => option.value === plan.service))) service.value = plan.service;
    if (pickup && plan.pickup && !pickup.value.trim()) pickup.value = plan.pickup;
    setWhen(plan.mode);
    paintTrip();
    const book = document.querySelector("#book");
    if (window.lenis && book) window.lenis.scrollTo(book, { offset: -90 });
    else book?.scrollIntoView({ behavior: "smooth", block: "start" });
    document.querySelector("#name")?.focus();
  });
});

function openDriverCard(data, when) {
  const card = document.querySelector("#driverCard");
  if (!card) return;
  const whenLine = document.querySelector("#driverWhen");
  const from = document.querySelector("#driverFrom");
  const via = document.querySelector("#driverVia");
  const to = document.querySelector("#driverTo");
  const who = document.querySelector("#driverWho");
  if (whenLine) whenLine.textContent = when;
  if (from) from.textContent = data.pickup;
  if (via) {
    via.hidden = !data.via;
    via.textContent = data.via ? `via ${data.via}` : "";
  }
  if (to) to.textContent = data.dropoff;
  if (who) {
    const dateBit = data.timeMode === "later" && data.pickupDate ? `${data.pickupDate} · ` : "";
    who.textContent = `${data.name} · ${dateBit}${data.passengers} passengers · ${data.service}`;
  }
  card.hidden = false;
  document.querySelector("#driverClose")?.focus();
}
function closeDriverCard() {
  const card = document.querySelector("#driverCard");
  if (card) card.hidden = true;
}
document.querySelector("#driverClose")?.addEventListener("click", closeDriverCard);
document.querySelector("#driverCard")?.addEventListener("click", (event) => {
  if (event.target.id === "driverCard") closeDriverCard();
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") closeDriverCard();
});

function aucklandInstant(dateStr, timeStr) {
  for (const offset of ["+12:00", "+13:00"]) {
    const instant = new Date(`${dateStr}T${timeStr}:00${offset}`);
    const shown = new Intl.DateTimeFormat("en-GB", {
      timeZone: "Pacific/Auckland",
      hour: "2-digit",
      minute: "2-digit",
      hourCycle: "h23",
    }).format(instant);
    if (shown === timeStr) return instant;
  }
  return new Date(`${dateStr}T${timeStr}:00+12:00`);
}
function downloadCalendar(data, when) {
  const start = aucklandInstant(data.pickupDate, data.pickupTime);
  const end = new Date(start.getTime() + 60 * 60 * 1000);
  const stamp = (date) => date.toISOString().replace(/[-:]/g, "").replace(/\.\d{3}/, "");
  const clean = (value) => String(value).replace(/[\r\n,;]/g, " ");
  const body = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//Town Taxi//Booking//EN",
    "BEGIN:VEVENT",
    `DTSTART:${stamp(start)}`,
    `DTEND:${stamp(end)}`,
    `SUMMARY:Town Taxi pickup - ${clean(data.pickup)}`,
    `DESCRIPTION:${clean(data.pickup)} to ${clean(data.dropoff)}${data.via ? `, via ${clean(data.via)}` : ""}. ${clean(when)}. ${clean(data.passengers)} passengers. ${clean(data.service)}.`,
    "END:VEVENT",
    "END:VCALENDAR",
  ].join("\r\n");
  const file = new Blob([body], { type: "text/calendar" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(file);
  link.download = "town-taxi.ics";
  link.click();
  URL.revokeObjectURL(link.href);
}

form?.addEventListener("submit", async (event) => {
  event.preventDefault();
  const status = document.querySelector("#formStatus");
  const submit = form.querySelector("[type='submit']");
  const data = Object.fromEntries(new FormData(form).entries());
  data.via = String(data.via || "").trim();
  if (data._honey) return;
  const when = data.timeMode === "now" ? `Now (${data.pickupDate} ${data.pickupTime})` : `${data.pickupDate} at ${data.pickupTime}`;
  submit.disabled = true;
  if (status) {
    status.className = "form-status";
    status.textContent = "Sending…";
  }
  const customerEmail = String(data.email || "").trim();
  const hasCustomerEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(customerEmail);
  const payload = {
    name: data.name,
    phone: data.phone,
    email: hasCustomerEmail ? customerEmail : "Not given",
    pickup: data.pickup,
    via: data.via || "None",
    dropoff: data.dropoff,
    when,
    passengers: data.passengers,
    service: data.service,
    notes: data.notes || "None",
    _subject: "New Town Taxi booking",
    _template: "table",
    _captcha: "false",
  };
  if (hasCustomerEmail) {
    payload._replyto = customerEmail;
    payload._autoresponse = "Town Taxi has your booking. We will call you on the number you gave to confirm the car.";
  }
  try {
    const desks = ["hitowntaxi@gmail.com"];
    const results = await Promise.all(desks.map(async (address) => {
      const response = await fetch(`https://formsubmit.co/ajax/${address}`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(payload),
      });
      const body = await response.json().catch(() => ({}));
      return { address, ok: response.ok && String(body.success) === "true", message: body.message || "" };
    }));
    const delivered = results.filter((item) => item.ok);
    if (!delivered.length) {
      const waiting = results.some((item) => /activ/i.test(item.message));
      throw new Error(waiting ? "activation" : "send failed");
    }
    const slip = document.querySelector("#tripSlip");
    const slipTitle = document.querySelector("#slipTitle");
    const slipBody = document.querySelector("#slipBody");
    const slipWhats = document.querySelector("#slipWhats");
    const slipCal = document.querySelector("#slipCal");
    const slipMaps = document.querySelector("#slipMaps");
    const slipCopy = document.querySelector("#slipCopy");
    storeTrip(data);
    if (slip && slipTitle && slipBody) {
      slipTitle.textContent = `${data.pickup} to ${data.dropoff}`;
      slipBody.textContent = `${data.name}${data.via ? ` · via ${data.via}` : ""} · ${when} · ${data.passengers} passengers · ${data.service}`;
      const message = tripMessage({ ...data, when });
      if (slipWhats) slipWhats.href = `https://wa.me/64204522958?text=${encodeURIComponent(message)}`;
      if (slipMaps) slipMaps.href = mapsHref(data.pickup, data.dropoff, data.via);
      if (slipCopy) {
        slipCopy.onclick = async () => {
          const stop = data.via ? `, via ${data.via}` : "";
          const text = `${data.pickup} to ${data.dropoff}${stop}. ${data.name}, ${when}, ${data.passengers} passengers, ${data.service}. Town Taxi +64 20 452 2958`;
          try {
            await navigator.clipboard.writeText(text);
            showToast("Trip copied");
          } catch {
            showToast("Couldn’t copy. The trip is written above.");
          }
        };
      }
      if (slipCal) {
        slipCal.hidden = data.timeMode !== "later";
        slipCal.onclick = () => downloadCalendar(data, when);
      }
      slip.hidden = false;
      slip.classList.add("is-shown");
      const cardWhen = data.timeMode === "now" ? "Now" : (data.pickupTime || when);
      const slipDriver = document.querySelector("#slipDriver");
      if (slipDriver) slipDriver.onclick = () => openDriverCard(data, cardWhen);
      openDriverCard(data, cardWhen);
    }
    form.reset();
    setWhen("now");
    document.querySelectorAll("[data-place], [data-trip]").forEach((button) => button.classList.remove("is-on"));
    paintTrip();
    if (status) {
      status.className = "form-status ok";
      const copy = hasCustomerEmail ? " A copy is also going to the email on the form." : "";
      status.textContent = `Sent to ${delivered.map((item) => item.address).join(" and ")}.${copy}`;
    }
  } catch (error) {
    if (status) {
      status.className = "form-status bad";
      status.textContent = error.message === "activation"
        ? "Check hitowntaxi@gmail.com, including spam, for an email called Activate Form. Click that link once, then send the booking again."
        : "That didn’t send. Call +64 20 452 2958 or email hitowntaxi@gmail.com.";
    }
  } finally {
    submit.disabled = false;
  }
});
