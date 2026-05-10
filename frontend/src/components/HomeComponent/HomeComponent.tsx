import { useEffect, useMemo, useState } from "react";
import {
  Calendar,
  momentLocalizer,
  Views,
  type View,
} from "react-big-calendar";
import moment from "moment";

import "react-big-calendar/lib/css/react-big-calendar.css";
import "./HomeComponent.css";

moment.locale("ro", {
  week: {
    dow: 1,
  },
});

const localizer = momentLocalizer(moment);

type EventStatus = "Active" | "Inactive" | "Pending" | "Cancelled";
type ParticipationType = "Fizic" | "Online" | "Hibrid";
type FilterMode = "and" | "or";

type EventItem = {
  id: number;
  name: string;
  description: string;
  faculty: {
    id: number;
    name: string;
  };
  category: {
    id: number;
    name: string;
  };
  organizer: {
    id: number;
    name: string;
    type: string;
  };
  location: {
    id: number;
    name: string;
    address: string;
    building?: string;
    room?: string;
  };
  participationType: ParticipationType;
  startDate: Date;
  endDate: Date;
  registrationLink?: string;
  onlineLink?: string;
  capacity: number;
  registeredCount: number;
  isFreeEntry: boolean;
  requiresRegistration: boolean;
  requiresTicket: boolean;
  qrCode?: string;
  status: {
    id: number;
    name: EventStatus;
  };
};

const eventData: EventItem[] = [
  {
    id: 1,
    name: "Workshop React pentru studenți",
    description:
      "Sesiune practică despre componente, stare locală și integrarea cu API-ul aplicației UniEvents.",
    faculty: { id: 1, name: "Inginerie Electrică și Știința Calculatoarelor" },
    category: { id: 1, name: "Academic" },
    organizer: { id: 1, name: "Tech Club USV", type: "Club Studențesc" },
    location: {
      id: 1,
      name: "Sala A101",
      address: "Campus Rectorat",
      building: "A",
      room: "101",
    },
    participationType: "Hibrid",
    startDate: new Date(2026, 5, 25, 10, 0),
    endDate: new Date(2026, 5, 25, 12, 0),
    registrationLink: "https://unievents.usv.ro/register/react-workshop",
    onlineLink: "https://meet.google.com/abc-defg-hij",
    capacity: 60,
    registeredCount: 41,
    isFreeEntry: true,
    requiresRegistration: true,
    requiresTicket: false,
    qrCode: "UE-REACT-2026-01",
    status: { id: 1, name: "Active" },
  },
  {
    id: 2,
    name: "Conferință despre inteligență artificială",
    description:
      "Prezentări despre modele moderne, aplicații universitare și analiză de feedback.",
    faculty: { id: 2, name: "Automatică și Calculatoare" },
    category: { id: 2, name: "Cercetare" },
    organizer: { id: 2, name: "AI Lab USV", type: "Laborator" },
    location: {
      id: 2,
      name: "Aula Mare",
      address: "Campus Rectorat",
      building: "Aula",
    },
    participationType: "Fizic",
    startDate: new Date(2026, 5, 26, 14, 0),
    endDate: new Date(2026, 5, 26, 16, 30),
    registrationLink: "https://unievents.usv.ro/register/ai-conference",
    capacity: 180,
    registeredCount: 142,
    isFreeEntry: false,
    requiresRegistration: true,
    requiresTicket: true,
    qrCode: "UE-AI-2026-02",
    status: { id: 1, name: "Active" },
  },
  {
    id: 3,
    name: "Târg de voluntariat și carieră",
    description:
      "Organizații și companii locale prezintă oportunități de practică, voluntariat și internship.",
    faculty: { id: 3, name: "Toate facultățile" },
    category: { id: 3, name: "Carieră" },
    organizer: { id: 3, name: "Asociația Studenților USV", type: "Asociație" },
    location: { id: 3, name: "Holul principal", address: "Campus Rectorat" },
    participationType: "Fizic",
    startDate: new Date(2026, 6, 5, 9, 0),
    endDate: new Date(2026, 6, 5, 17, 0),
    registrationLink: "https://unievents.usv.ro/register/career-fair",
    capacity: 300,
    registeredCount: 198,
    isFreeEntry: true,
    requiresRegistration: false,
    requiresTicket: false,
    status: { id: 1, name: "Active" },
  },
  {
    id: 4,
    name: "Workshop de design și comunicare",
    description:
      "Activitate despre identitate vizuală, materiale publicate și colaborarea cu organizatorii.",
    faculty: { id: 4, name: "Științe și Litere" },
    category: { id: 4, name: "Voluntariat" },
    organizer: { id: 4, name: "Design Club", type: "Club Studențesc" },
    location: {
      id: 4,
      name: "Sala B205",
      address: "Campus Rectorat",
      building: "B",
      room: "205",
    },
    participationType: "Online",
    startDate: new Date(2026, 6, 28, 18, 0),
    endDate: new Date(2026, 6, 28, 19, 30),
    registrationLink: "https://unievents.usv.ro/register/design-workshop",
    onlineLink: "https://meet.google.com/xyz-uvwx-yz",
    capacity: 45,
    registeredCount: 36,
    isFreeEntry: true,
    requiresRegistration: true,
    requiresTicket: false,
    status: { id: 1, name: "Active" },
  },
  {
    id: 5,
    name: "Hackathon interdisciplinar",
    description:
      "48 de ore de lucru pentru prototipuri, prezentări și validare în fața juriului.",
    faculty: { id: 1, name: "Inginerie Electrică și Știința Calculatoarelor" },
    category: { id: 5, name: "Competiție" },
    organizer: {
      id: 5,
      name: "USV Innovation Hub",
      type: "Centru de Inovație",
    },
    location: {
      id: 5,
      name: "Centrul de Inovație",
      address: "Campus Rectorat",
    },
    participationType: "Hibrid",
    startDate: new Date(2026, 7, 12, 9, 0),
    endDate: new Date(2026, 7, 14, 18, 0),
    registrationLink: "https://unievents.usv.ro/register/hackathon",
    capacity: 120,
    registeredCount: 96,
    isFreeEntry: false,
    requiresRegistration: true,
    requiresTicket: true,
    qrCode: "UE-HACK-2026-05",
    status: { id: 1, name: "Active" },
  },
];

const faculties = [
  "Toate",
  ...Array.from(new Set(eventData.map((e) => e.faculty.name))),
];
const categories = [
  "Toate",
  ...Array.from(new Set(eventData.map((e) => e.category.name))),
];
const locations = [
  "Toate",
  ...Array.from(new Set(eventData.map((e) => e.location.name))),
];
const organizers = [
  "Toți",
  ...Array.from(new Set(eventData.map((e) => e.organizer.name))),
];
const participations = [
  "Toate",
  ...Array.from(new Set(eventData.map((e) => e.participationType))),
];

const formatDateTime = (value: Date) =>
  new Intl.DateTimeFormat("ro-RO", {
    dateStyle: "full",
    timeStyle: "short",
  }).format(value);
const formatShortDate = (value: Date) =>
  new Intl.DateTimeFormat("ro-RO", { day: "2-digit", month: "short" }).format(
    value,
  );

const createIcsLink = (event: EventItem) => {
  const pad = (input: number) => String(input).padStart(2, "0");
  const toIcsStamp = (value: Date) =>
    `${value.getFullYear()}${pad(value.getMonth() + 1)}${pad(value.getDate())}T${pad(value.getHours())}${pad(value.getMinutes())}00`;

  const locationStr = event.location.room
    ? `${event.location.name}, Room ${event.location.room}`
    : `${event.location.name}, ${event.location.address}`;

  const payload = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//UniEvents//Home//RO",
    "BEGIN:VEVENT",
    `SUMMARY:${event.name}`,
    `DESCRIPTION:${event.description}`,
    `LOCATION:${locationStr}`,
    `DTSTART:${toIcsStamp(event.startDate)}`,
    `DTEND:${toIcsStamp(event.endDate)}`,
    `UID:unievents-${event.id}@usv.ro`,
    "END:VEVENT",
    "END:VCALENDAR",
  ].join("\n");

  return `data:text/calendar;charset=utf-8,${encodeURIComponent(payload)}`;
};

const toCalendarEvent = (event: EventItem) => ({
  ...event,
  start: event.startDate,
  end: event.endDate,
});

export const HomeComponent = () => {
  const [view, setView] = useState<View>(Views.MONTH);
  const [currentDate, setCurrentDate] = useState(() => new Date());
  const [selectedFaculty, setSelectedFaculty] = useState("Toate");
  const [selectedCategory, setSelectedCategory] = useState("Toate");
  const [selectedLocation, setSelectedLocation] = useState("Toate");
  const [selectedOrganizer, setSelectedOrganizer] = useState("Toți");
  const [selectedParticipation, setSelectedParticipation] = useState("Toate");
  const [filterMode, setFilterMode] = useState<FilterMode>("and");
  const [selectedEventId, setSelectedEventId] = useState<number | null>(
    eventData[0].id,
  );
  const [modalOpen, setModalOpen] = useState(false);

  const filteredEvents = useMemo(() => {
    return eventData.filter((event) => {
      const checks = [
        selectedFaculty === "Toate" || event.faculty.name === selectedFaculty,
        selectedCategory === "Toate" ||
          event.category.name === selectedCategory,
        selectedLocation === "Toate" ||
          event.location.name === selectedLocation,
        selectedOrganizer === "Toți" ||
          event.organizer.name === selectedOrganizer,
        selectedParticipation === "Toate" ||
          event.participationType === selectedParticipation,
      ];

      return filterMode === "and"
        ? checks.every(Boolean)
        : checks.some(Boolean);
    });
  }, [
    filterMode,
    selectedCategory,
    selectedFaculty,
    selectedLocation,
    selectedOrganizer,
    selectedParticipation,
  ]);

  const calendarEvents = useMemo(
    () => filteredEvents.map(toCalendarEvent),
    [filteredEvents],
  );
  const selectedEvent = useMemo(
    () => eventData.find((event) => event.id === selectedEventId) ?? null,
    [selectedEventId],
  );

  const openDetails = (event: EventItem) => {
    setSelectedEventId(event.id);
    setModalOpen(true);
  };

  const closeDetails = () => setModalOpen(false);

  useEffect(() => {
    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === "Escape") closeDetails();
    };

    window.addEventListener("keydown", handleEscape);
    return () => window.removeEventListener("keydown", handleEscape);
  }, []);

  return (
    <main className="home-shell">
      <aside className="home-sidebar">
        <div className="sidebar-section">
          <div className="sidebar-section-head">
            <h2>Filtre</h2>
            <span>Combinație {filterMode.toUpperCase()}</span>
          </div>

          <div className="filter-stack">
            <label>
              Facultate
              <select
                value={selectedFaculty}
                onChange={(event) => setSelectedFaculty(event.target.value)}
              >
                {faculties.map((option) => (
                  <option key={option} value={option}>
                    {option}
                  </option>
                ))}
              </select>
            </label>
            <label>
              Categorie
              <select
                value={selectedCategory}
                onChange={(event) => setSelectedCategory(event.target.value)}
              >
                {categories.map((option) => (
                  <option key={option} value={option}>
                    {option}
                  </option>
                ))}
              </select>
            </label>
            <label>
              Locație
              <select
                value={selectedLocation}
                onChange={(event) => setSelectedLocation(event.target.value)}
              >
                {locations.map((option) => (
                  <option key={option} value={option}>
                    {option}
                  </option>
                ))}
              </select>
            </label>
            <label>
              Organizator
              <select
                value={selectedOrganizer}
                onChange={(event) => setSelectedOrganizer(event.target.value)}
              >
                {organizers.map((option) => (
                  <option key={option} value={option}>
                    {option}
                  </option>
                ))}
              </select>
            </label>
            <label>
              Participare
              <select
                value={selectedParticipation}
                onChange={(event) =>
                  setSelectedParticipation(event.target.value)
                }
              >
                {participations.map((option) => (
                  <option key={option} value={option}>
                    {option}
                  </option>
                ))}
              </select>
            </label>

            <div className="filter-mode-row">
              <span>Combinare</span>
              <div className="mode-buttons">
                <button
                  type="button"
                  className={
                    filterMode === "and" ? "mode-btn active" : "mode-btn"
                  }
                  onClick={() => setFilterMode("and")}
                >
                  AND
                </button>
                <button
                  type="button"
                  className={
                    filterMode === "or" ? "mode-btn active" : "mode-btn"
                  }
                  onClick={() => setFilterMode("or")}
                >
                  OR
                </button>
              </div>
            </div>

            <div className="view-buttons-sidebar">
              <span>Vizualizare</span>
              <div className="mode-buttons">
                <button
                  type="button"
                  className={
                    view === Views.MONTH ? "mode-btn active" : "mode-btn"
                  }
                  onClick={() => setView(Views.MONTH)}
                >
                  Lună
                </button>
                <button
                  type="button"
                  className={
                    view === Views.WEEK ? "mode-btn active" : "mode-btn"
                  }
                  onClick={() => setView(Views.WEEK)}
                >
                  Săptămână
                </button>
                <button
                  type="button"
                  className={
                    view === Views.DAY ? "mode-btn active" : "mode-btn"
                  }
                  onClick={() => setView(Views.DAY)}
                >
                  Zi
                </button>
              </div>
            </div>
          </div>
        </div>

        <div className="sidebar-section sidebar-list">
          <div className="sidebar-section-head">
            <h2>Lista evenimentelor</h2>
            <span>{filteredEvents.length} rezultate</span>
          </div>

          <div className="event-list">
            {filteredEvents.map((event) => (
              <button
                key={event.id}
                type="button"
                className={
                  selectedEventId === event.id && modalOpen
                    ? "event-list-item active"
                    : "event-list-item"
                }
                onClick={() => openDetails(event)}
              >
                <div className="event-list-top">
                  <strong>{event.name}</strong>
                  <span>{formatShortDate(event.startDate)}</span>
                </div>
                <p>{event.location.name}</p>
                <div className="event-list-bottom">
                  <span>{event.category.name}</span>
                  <span>{event.participationType}</span>
                </div>
              </button>
            ))}
          </div>
        </div>
      </aside>

      <section className="home-calendar-area">
        <div className="calendar-frame">
          <Calendar
            localizer={localizer}
            events={calendarEvents}
            view={view}
            onView={setView}
            date={currentDate}
            onNavigate={setCurrentDate}
            popup
            selectable
            onSelectEvent={(event) => openDetails(event as EventItem)}
            startAccessor="start"
            endAccessor="end"
            titleAccessor="name"
            style={{ height: "100%" }}
            views={[Views.MONTH, Views.WEEK, Views.DAY]}
            messages={{
              today: "Azi",
              previous: "Înapoi",
              next: "Înainte",
              month: "Lună",
              week: "Săptămână",
              day: "Zi",
              agenda: "Agendă",
              date: "Dată",
              time: "Oră",
              event: "Eveniment",
              noEventsInRange: "Nu există evenimente în acest interval.",
            }}
            formats={{
              dayFormat: "D",
              weekdayFormat: (date) => moment(date).format("ddd"),
              monthHeaderFormat: (date) => moment(date).format("MMMM YYYY"),
              dayHeaderFormat: (date) => moment(date).format("dddd, D MMMM"),
              eventTimeRangeFormat: ({
                start,
                end,
              }: {
                start: Date;
                end: Date;
              }) =>
                `${moment(start).format("HH:mm")} - ${moment(end).format("HH:mm")}`,
            }}
          />
        </div>
      </section>

      {modalOpen && selectedEvent && (
        <div className="event-modal-backdrop" onClick={closeDetails}>
          <div
            className="event-modal"
            onClick={(event) => event.stopPropagation()}
          >
            <div className="event-modal-header">
              <div>
                <span className="modal-kicker">Detalii eveniment</span>
                <h2>{selectedEvent.name}</h2>
              </div>
              <button
                type="button"
                className="modal-close"
                onClick={closeDetails}
              >
                ×
              </button>
            </div>

            <p className="modal-description">{selectedEvent.description}</p>

            <div className="modal-grid">
              <div>
                <span>Data și ora</span>
                <strong>
                  {formatDateTime(selectedEvent.startDate)} -{" "}
                  {moment(selectedEvent.endDate).format("HH:mm")}
                </strong>
              </div>
              <div>
                <span>Locație</span>
                <strong>
                  {selectedEvent.location.name}
                  {selectedEvent.location.room &&
                    `, Sala ${selectedEvent.location.room}`}
                </strong>
              </div>
              <div>
                <span>Organizator</span>
                <strong>{selectedEvent.organizer.name}</strong>
              </div>
              <div>
                <span>Tip participare</span>
                <strong>{selectedEvent.participationType}</strong>
              </div>
              <div>
                <span>Facultate</span>
                <strong>{selectedEvent.faculty.name}</strong>
              </div>
              <div>
                <span>Locuri</span>
                <strong>
                  {selectedEvent.registeredCount}/{selectedEvent.capacity}
                </strong>
              </div>
            </div>

            <div className="modal-tags">
              <span>{selectedEvent.status.name}</span>
              <span>
                {selectedEvent.isFreeEntry
                  ? "Intrare liberă"
                  : "Taxă de participare"}
              </span>
              <span>
                {selectedEvent.requiresRegistration
                  ? "Necesită înscriere"
                  : "Acces direct"}
              </span>
              <span>{selectedEvent.qrCode ? "Are cod QR" : "Fără cod QR"}</span>
            </div>

            <div className="modal-actions">
              {selectedEvent.registrationLink && (
                <a
                  className="modal-primary"
                  href={selectedEvent.registrationLink}
                  target="_blank"
                  rel="noreferrer"
                >
                  Înscriere
                </a>
              )}
              <a
                className="modal-secondary"
                href={`https://calendar.google.com/calendar/render?action=TEMPLATE&text=${encodeURIComponent(selectedEvent.name)}&dates=${moment(selectedEvent.startDate).format("YYYYMMDDTHHmmss")}/${moment(selectedEvent.endDate).format("YYYYMMDDTHHmmss")}&details=${encodeURIComponent(selectedEvent.description)}&location=${encodeURIComponent(selectedEvent.location.name)}`}
                target="_blank"
                rel="noreferrer"
              >
                Google Calendar
              </a>
              <a
                className="modal-secondary"
                href={createIcsLink(selectedEvent)}
                download={`${selectedEvent.name}.ics`}
              >
                Descarcă .ics
              </a>
            </div>

            <div className="modal-footer">
              <div>
                <strong>Cod QR</strong>
                <p>{selectedEvent.qrCode || "N/A"}</p>
              </div>
              <div>
                <strong>Tip bilet</strong>
                <p>
                  {selectedEvent.requiresTicket
                    ? "Bilet obligatoriu"
                    : "Fără bilet"}
                </p>
              </div>
              <div>
                <strong>Înscriți</strong>
                <p>{selectedEvent.registeredCount} persoane</p>
              </div>
              <div>
                <strong>Capacitate</strong>
                <p>{selectedEvent.capacity} locuri</p>
              </div>
            </div>
          </div>
        </div>
      )}
    </main>
  );
};
