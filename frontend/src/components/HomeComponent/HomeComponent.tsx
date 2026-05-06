import { Calendar, momentLocalizer, Views } from "react-big-calendar";
import moment from "moment";
import { useState } from "react";

import "react-big-calendar/lib/css/react-big-calendar.css";
import "./HomeComponent.css";

moment.locale("ro", {
  week: {
    dow: 1,
  },
});

const localizer = momentLocalizer(moment);

const mockEvents = [
  {
    id: 1,
    title: "Workshop React",
    start: new Date(2026, 2, 25, 10, 0),
    end: new Date(2026, 2, 25, 12, 0),
    resource: {
      categorie: "Tehnologie",
      locatie: "Sala A101",
      organizator: "Tech Club",
      capacitate: 50,
      participanti: 28,
    },
  },
  {
    id: 2,
    title: "Conferință despre AI",
    start: new Date(2026, 2, 26, 14, 0),
    end: new Date(2026, 2, 26, 16, 30),
    resource: {
      categorie: "Seminare",
      locatie: "Aula Mare",
      organizator: "AI Lab",
      capacitate: 200,
      participanti: 145,
    },
  },
  {
    id: 3,
    title: "Meetup Design",
    start: new Date(2026, 2, 28, 18, 0),
    end: new Date(2026, 2, 28, 19, 30),
    resource: {
      categorie: "Design",
      locatie: "Sala B205",
      organizator: "Design Club",
      capacitate: 40,
      participanti: 32,
    },
  },
  {
    id: 4,
    title: "Hackathon",
    start: new Date(2026, 3, 5, 9, 0),
    end: new Date(2026, 3, 6, 18, 0),
    resource: {
      categorie: "Competiție",
      locatie: "Centrul de Inovație",
      organizator: "Student Association",
      capacitate: 150,
      participanti: 87,
    },
  },
];

const MyDateHeader = ({ date }: any) => {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: "4px 0",
      }}
    >
      {/* Numele zilei */}
      <span style={{ fontWeight: 600, color: "#fff", marginBottom: "4px" }}>
        {moment(date).format("dddd")}
      </span>

      {/* Linia separator */}
      <span
        style={{
          width: "80%",
          height: "1px",
          backgroundColor: "#444",
          margin: "2px 0",
        }}
      ></span>

      {/* Numărul zilei */}
      <span style={{ fontSize: "12px", color: "#ccc", marginTop: "2px" }}>
        {moment(date).format("D")}
      </span>
    </div>
  );
};

export const HomeComponent = () => {
  const [currentView, setCurrentView] = useState<string>(Views.MONTH);
  const [selectedEvent, setSelectedEvent] = useState<any>(null);
  const [currentDate, setCurrentDate] = useState<Date>(new Date());

  const handleViewChange = (newView: string) => {
    setCurrentView(newView);
  };

  const handleSelectEvent = (event: any) => {
    setSelectedEvent(event);
  };

  const handlePrevMonth = () => {
    setCurrentDate(
      new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1),
    );
  };

  const handleTodayMonth = () => {
    setCurrentDate(new Date());
  };

  const handleNextMonth = () => {
    setCurrentDate(
      new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1),
    );
  };

  const monthName = moment(currentDate).format("MMMM YYYY");

  return (
    <main className="home-main">
      <aside className="home-sidebar">
        <div className="sidebar-header">
          <h3>Detalii Eveniment</h3>
        </div>

        <div className="sidebar-content">
          {selectedEvent ? (
            <div className="event-details">
              <h4>{selectedEvent.title}</h4>

              <div className="event-info">
                <p>
                  <strong>Categorie:</strong> {selectedEvent.resource.categorie}
                </p>
                <p>
                  <strong>Locație:</strong> {selectedEvent.resource.locatie}
                </p>
                <p>
                  <strong>Organizator:</strong>{" "}
                  {selectedEvent.resource.organizator}
                </p>
              </div>

              <div className="event-stats">
                <div className="stat">
                  <span className="stat-label">Capacitate</span>
                  <span className="stat-value">
                    {selectedEvent.resource.participanti}/
                    {selectedEvent.resource.capacitate}
                  </span>
                </div>
              </div>

              <div className="event-time">
                <p>
                  <strong>Inceput:</strong>{" "}
                  {selectedEvent.start.toLocaleString("ro-RO")}
                </p>
                <p>
                  <strong>Încheiere:</strong>{" "}
                  {selectedEvent.end.toLocaleString("ro-RO")}
                </p>
              </div>

              <button className="btn-primary">Înscrie-te</button>
            </div>
          ) : (
            <div className="sidebar-placeholder">
              <p>
                Selectează un eveniment din calendar pentru a vedea detaliile
              </p>
            </div>
          )}
        </div>
      </aside>

      <section className="home-calendar-container">
        <div className="calendar-toolbar-custom">
          <div className="toolbar-content">
            <div className="month-nav-buttons">
              <button className="nav-btn" onClick={handlePrevMonth}>
                ← Anterior
              </button>
              <button className="nav-btn active" onClick={handleTodayMonth}>
                Azi
              </button>
              <button className="nav-btn" onClick={handleNextMonth}>
                Următor →
              </button>
            </div>

            <div className="month-title">
              <h2>{monthName}</h2>
            </div>

            <div className="view-buttons">
              <button
                className={`view-btn ${currentView === Views.DAY ? "active" : ""}`}
                onClick={() => handleViewChange(Views.DAY)}
              >
                Zile
              </button>
              <button
                className={`view-btn ${currentView === Views.WEEK ? "active" : ""}`}
                onClick={() => handleViewChange(Views.WEEK)}
              >
                Săptămână
              </button>
              <button
                className={`view-btn ${currentView === Views.MONTH ? "active" : ""}`}
                onClick={() => handleViewChange(Views.MONTH)}
              >
                Lună
              </button>
            </div>
          </div>
        </div>

        <div className="calendar-wrapper">
          <Calendar
            localizer={localizer}
            events={mockEvents}
            defaultView={Views.MONTH}
            view={currentView}
            onView={handleViewChange}
            date={currentDate}
            onNavigate={setCurrentDate}
            views={[Views.DAY, Views.WEEK, Views.MONTH]}
            onSelectEvent={handleSelectEvent}
            style={{ height: "100%" }}
            popup
            selectable
            defaultDate={currentDate}
            formats={{
              dayFormat: "D",
              weekdayFormat: "dddd",
              dayHeaderFormat: "dddd",
              dayFormat: "dddd",
              weekFormat: "dddd",
              dateFormat: "D",
            }}
          />
        </div>
      </section>
    </main>
  );
};
