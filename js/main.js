const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");
if (menuToggle && navLinks) {
  menuToggle.addEventListener("click", () => {
    navLinks.classList.toggle("open");
  });
}

const nowChip = document.querySelector("[data-time='now']");
const laterChip = document.querySelector("[data-time='later']");
const timeInput = document.querySelector("#pickupTime");
const timeMode = document.querySelector("#timeMode");

function setTimeMode(mode) {
  if (!timeInput || !timeMode) return;
  timeMode.value = mode;
  nowChip?.classList.toggle("active", mode === "now");
  laterChip?.classList.toggle("active", mode === "later");
  if (mode === "now") {
    const now = new Date();
    timeInput.value = now.toTimeString().slice(0, 5);
    const dateInput = document.querySelector("#pickupDate");
    if (dateInput) dateInput.valueAsDate = now;
  }
  timeInput.disabled = mode === "now";
}

nowChip?.addEventListener("click", () => setTimeMode("now"));
laterChip?.addEventListener("click", () => setTimeMode("later"));
setTimeMode("now");

const form = document.querySelector("#bookingForm");
const toast = document.querySelector("#toast");

function showToast(message) {
  if (!toast) return;
  toast.textContent = message;
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 3200);
}

form?.addEventListener("submit", (event) => {
  event.preventDefault();
  const data = Object.fromEntries(new FormData(form).entries());
  const when = data.timeMode === "now" ? "Now" : `${data.pickupDate} at ${data.pickupTime}`;
  const message = [
    "New Town Taxi booking request",
    `Name: ${data.name}`,
    `Phone: ${data.phone}`,
    data.email ? `Email: ${data.email}` : null,
    `Pickup: ${data.pickup}`,
    `Drop-off: ${data.dropoff}`,
    `When: ${when}`,
    `Passengers: ${data.passengers}`,
    data.vehicle ? `Vehicle: ${data.vehicle}` : null,
    data.notes ? `Notes: ${data.notes}` : null,
  ]
    .filter(Boolean)
    .join("%0A");

  window.open(`https://wa.me/64204522958?text=${message}`, "_blank");
  showToast("Opening WhatsApp with your booking details.");
  form.reset();
  setTimeMode("now");
});
