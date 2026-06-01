import { useEffect, useMemo, useState } from "react";
import "./OrganizerDashboard.css";

type DescribedEntity = {
  id: number;
  name: string;
  description?: string | null;
};
type OrganizerEntity = DescribedEntity & { user?: number | { id?: number } };
type LocationEntity = DescribedEntity & {
  address?: string;
  building?: string | null;
  room?: string | null;
};
type SponsorEntity = {
  id: number;
  name: string;
  description?: string | null;
  link?: string | null;
};
type RegistrationItem = {
  id: number;
  user?:
    | number
    | {
        id?: number;
        username?: string;
        email?: string;
        first_name?: string;
        last_name?: string;
      };
  username?: string;
  email?: string;
  status?: DescribedEntity;
  status_name?: string;
  created_at?: string;
};

type EventItem = {
  id: number;
  name: string;
  description: string;
  registration_link?: string | null;
  online_link?: string | null;
  organizer: OrganizerEntity;
  location: LocationEntity;
  category: DescribedEntity;
  participation_type: DescribedEntity;
  status: DescribedEntity;
  start_date: string;
  end_date: string;
  capacity?: number | null;
  registered_count?: number;
  registration_deadline?: string | null;
  pricing_type?: string;
  access_policy?: string;
  is_free_entry?: boolean;
  requires_registration?: boolean;
  requires_ticket?: boolean;
  qr_code?: string | null;
  created_at?: string;
  updated_at?: string;
};

type EventForm = {
  name: string;
  description: string;
  registration_link: string;
  online_link: string;
  organizer_id: string;
  location_id: string;
  category_id: string;
  participation_type_id: string;
  status_id: string;
  start_date: string;
  end_date: string;
  capacity: string;
  registration_deadline: string;
  pricing_type: "free" | "paid";
  access_policy: "open" | "registration" | "ticket" | "registration_ticket";
  max_files: string;
  max_file_size_mb: string;
};

const emptyForm: EventForm = {
  name: "",
  description: "",
  registration_link: "",
  online_link: "",
  organizer_id: "",
  location_id: "",
  category_id: "",
  participation_type_id: "",
  status_id: "",
  start_date: "",
  end_date: "",
  capacity: "",
  registration_deadline: "",
  pricing_type: "free",
  access_policy: "open",
  max_files: "",
  max_file_size_mb: "",
};

const authHeaders = () => {
  const token = localStorage.getItem("access");
  return token ? { Authorization: `Bearer ${token}` } : {};
};

const toDateTimeLocal = (value?: string | null) => {
  if (!value) return "";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "";
  const offsetDate = new Date(
    date.getTime() - date.getTimezoneOffset() * 60000,
  );
  return offsetDate.toISOString().slice(0, 16);
};

const formatDateTime = (value?: string | null) => {
  if (!value) return "N/A";
  return new Intl.DateTimeFormat("ro-RO", {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(new Date(value));
};

const currentUserId = () => {
  try {
    const user = JSON.parse(localStorage.getItem("user") || "{}");
    return Number(user.user_id ?? user.id ?? user.profile?.user ?? 0);
  } catch {
    return 0;
  }
};

const userOwnsOrganizer = (organizer: OrganizerEntity) => {
  const userId = currentUserId();
  const organizerUser = organizer.user;
  if (typeof organizerUser === "number") return organizerUser === userId;
  if (organizerUser && typeof organizerUser === "object")
    return Number(organizerUser.id) === userId;
  return false;
};

export const OrganizerDashboard = () => {
  const [events, setEvents] = useState<EventItem[]>([]);
  const [organizers, setOrganizers] = useState<OrganizerEntity[]>([]);
  const [locations, setLocations] = useState<LocationEntity[]>([]);
  const [categories, setCategories] = useState<DescribedEntity[]>([]);
  const [participationTypes, setParticipationTypes] = useState<
    DescribedEntity[]
  >([]);
  const [statuses, setStatuses] = useState<DescribedEntity[]>([]);
  const [sponsors, setSponsors] = useState<SponsorEntity[]>([]);
  const [eventSponsors, setEventSponsors] = useState<any[]>([]);
  const [registrations, setRegistrations] = useState<RegistrationItem[]>([]);
  const [selectedEvent, setSelectedEvent] = useState<EventItem | null>(null);
  const [mode, setMode] = useState<"list" | "create" | "edit" | "view">("list");
  const modalOpen = mode === "create" || mode === "edit" || mode === "view";
  const [form, setForm] = useState<EventForm>(emptyForm);
  const [selectedSponsorIds, setSelectedSponsorIds] = useState<number[]>([]);
  const [sponsorSearch, setSponsorSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState("");

  const myOrganizers = useMemo(() => {
    const mine = organizers.filter(userOwnsOrganizer);
    return mine.length > 0 ? mine : organizers;
  }, [organizers]);

  const myOrganizerIds = useMemo(
    () => new Set(myOrganizers.map((o) => o.id)),
    [myOrganizers],
  );
  const myEvents = useMemo(
    () => events.filter((event) => myOrganizerIds.has(event.organizer?.id)),
    [events, myOrganizerIds],
  );

  const selectedEventSponsors = useMemo(() => {
    if (!selectedEvent) return [];
    return eventSponsors
      .filter(
        (item) => Number(item.event?.id ?? item.event) === selectedEvent.id,
      )
      .map((item) =>
        item.sponsor && typeof item.sponsor === "object"
          ? item.sponsor
          : sponsors.find((s) => s.id === Number(item.sponsor)),
      )
      .filter(Boolean) as SponsorEntity[];
  }, [eventSponsors, selectedEvent, sponsors]);

  const filteredSponsors = useMemo(() => {
    const search = sponsorSearch.trim().toLowerCase();

    if (!search) return sponsors;

    return sponsors.filter((sponsor) =>
      sponsor.name.toLowerCase().includes(search),
    );
  }, [sponsors, sponsorSearch]);

  const loadData = async () => {
    setLoading(true);
    setMessage("");
    try {
      const base = import.meta.env.VITE_API;
      const headers = authHeaders();
      const [
        eventsData,
        organizersData,
        locationsData,
        categoriesData,
        participationData,
        statusesData,
        sponsorsData,
        eventSponsorsData,
      ] = await Promise.all([
        fetch(`${base}/api/events/`, { headers }).then((r) =>
          r.ok ? r.json() : [],
        ),
        fetch(`${base}/api/organizers/`, { headers }).then((r) =>
          r.ok ? r.json() : [],
        ),
        fetch(`${base}/api/locations/`, { headers }).then((r) =>
          r.ok ? r.json() : [],
        ),
        fetch(`${base}/api/categories/`, { headers }).then((r) =>
          r.ok ? r.json() : [],
        ),
        fetch(`${base}/api/participation-types/`, { headers }).then((r) =>
          r.ok ? r.json() : [],
        ),
        fetch(`${base}/api/statuses/`, { headers }).then((r) =>
          r.ok ? r.json() : [],
        ),
        fetch(`${base}/api/sponsors/`, { headers }).then((r) =>
          r.ok ? r.json() : [],
        ),
        fetch(`${base}/api/event-sponsors/`, { headers }).then((r) =>
          r.ok ? r.json() : [],
        ),
      ]);
      setEvents(Array.isArray(eventsData) ? eventsData : []);
      setOrganizers(Array.isArray(organizersData) ? organizersData : []);
      setLocations(Array.isArray(locationsData) ? locationsData : []);
      setCategories(Array.isArray(categoriesData) ? categoriesData : []);
      setParticipationTypes(
        Array.isArray(participationData) ? participationData : [],
      );
      setStatuses(Array.isArray(statusesData) ? statusesData : []);
      setSponsors(Array.isArray(sponsorsData) ? sponsorsData : []);
      setEventSponsors(
        Array.isArray(eventSponsorsData) ? eventSponsorsData : [],
      );
    } catch (err) {
      console.error(err);
      setMessage("Nu s-au putut încărca datele dashboard-ului.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  useEffect(() => {
    if (myOrganizers.length > 0 && !form.organizer_id) {
      setForm((previous) => ({
        ...previous,
        organizer_id: String(myOrganizers[0].id),
      }));
    }
  }, [myOrganizers, form.organizer_id]);

  const openCreate = () => {
    setSelectedEvent(null);
    setSelectedSponsorIds([]);
    setForm({
      ...emptyForm,
      organizer_id: myOrganizers[0] ? String(myOrganizers[0].id) : "",
    });
    setMode("create");
  };

  const openEdit = (event: EventItem) => {
    setSelectedEvent(event);
    setForm({
      name: event.name ?? "",
      description: event.description ?? "",
      registration_link: event.registration_link ?? "",
      online_link: event.online_link ?? "",
      organizer_id: String(event.organizer?.id ?? myOrganizers[0]?.id ?? ""),
      location_id: String(event.location?.id ?? ""),
      category_id: String(event.category?.id ?? ""),
      participation_type_id: String(event.participation_type?.id ?? ""),
      status_id: String(event.status?.id ?? ""),
      start_date: toDateTimeLocal(event.start_date),
      end_date: toDateTimeLocal(event.end_date),
      capacity: event.capacity ? String(event.capacity) : "",
      registration_deadline: toDateTimeLocal(event.registration_deadline),
      pricing_type: event.pricing_type === "paid" ? "paid" : "free",
      access_policy:
        (event.access_policy as EventForm["access_policy"]) ?? "open",
      max_files: event.max_files ? String(event.max_files) : "",
      max_file_size_mb: event.max_file_size_mb
        ? String(event.max_file_size_mb)
        : "",
    });
    setSelectedSponsorIds(
      eventSponsors
        .filter((item) => Number(item.event?.id ?? item.event) === event.id)
        .map((item) => Number(item.sponsor?.id ?? item.sponsor))
        .filter(Boolean),
    );
    setMode("edit");
  };

  const openView = async (event: EventItem) => {
    setSelectedEvent(event);
    setMode("view");
    try {
      const res = await fetch(
        `${import.meta.env.VITE_API}/api/registrations/?event=${event.id}`,
        { headers: authHeaders() },
      );
      const data = res.ok ? await res.json() : [];
      const list = Array.isArray(data) ? data : [];
      setRegistrations(
        list.filter(
          (reg: any) => Number(reg.event?.id ?? reg.event) === event.id,
        ),
      );
    } catch {
      setRegistrations([]);
    }
  };

  const changeForm = (field: keyof EventForm, value: string) =>
    setForm((previous) => ({ ...previous, [field]: value }));

  const payloadFromForm = () => ({
    name: form.name,
    description: form.description,
    registration_link: form.registration_link || null,
    online_link: form.online_link || null,
    organizer_id: Number(form.organizer_id),
    location_id: Number(form.location_id),
    category_id: Number(form.category_id),
    participation_type_id: Number(form.participation_type_id),
    start_date: new Date(form.start_date).toISOString(),
    end_date: new Date(form.end_date).toISOString(),
    capacity: form.capacity ? Number(form.capacity) : null,
    registration_deadline: form.registration_deadline
      ? new Date(form.registration_deadline).toISOString()
      : null,
    pricing_type: form.pricing_type,
    access_policy: form.access_policy,
  });

  const syncSponsors = async (eventId: number) => {
    const currentLinks = eventSponsors.filter(
      (item) => Number(item.event?.id ?? item.event) === eventId,
    );
    await Promise.all(
      currentLinks.map((item) =>
        fetch(`${import.meta.env.VITE_API}/api/event-sponsors/${item.id}/`, {
          method: "DELETE",
          headers: authHeaders(),
        }),
      ),
    );
    await Promise.all(
      selectedSponsorIds.map((sponsorId) =>
        fetch(`${import.meta.env.VITE_API}/api/event-sponsors/`, {
          method: "POST",
          headers: { "Content-Type": "application/json", ...authHeaders() },
          body: JSON.stringify({ event_id: eventId, sponsor_id: sponsorId }),
        }),
      ),
    );
  };

  const submitForm = async () => {
    setMessage("");
    try {
      const isEdit = mode === "edit" && selectedEvent;
      const url = isEdit
        ? `${import.meta.env.VITE_API}/api/events/${selectedEvent.id}/`
        : `${import.meta.env.VITE_API}/api/events/`;
      const res = await fetch(url, {
        method: isEdit ? "PUT" : "POST",
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify(payloadFromForm()),
      });
      const data = await res.json();
      if (!res.ok) {
        setMessage(typeof data === "string" ? data : JSON.stringify(data));
        return;
      }
      await syncSponsors(data.id);
      setMessage(isEdit ? "Eveniment actualizat." : "Eveniment creat.");
      closeModal();
      await loadData();
    } catch (err) {
      console.error(err);
      setMessage("A apărut o eroare la salvare.");
    }
  };

  const deleteEvent = async (event: EventItem) => {
    const confirmed = window.confirm(`Ștergi evenimentul „${event.name}”?`);
    if (!confirmed) return;
    const res = await fetch(
      `${import.meta.env.VITE_API}/api/events/${event.id}/`,
      { method: "DELETE", headers: authHeaders() },
    );
    if (res.ok || res.status === 204) {
      setMessage("Eveniment șters.");
      await loadData();
    } else {
      setMessage("Nu s-a putut șterge evenimentul.");
    }
  };

  const toggleSponsor = (id: number) => {
    setSelectedSponsorIds((previous) =>
      previous.includes(id)
        ? previous.filter((item) => item !== id)
        : [...previous, id],
    );
  };

  const closeModal = () => {
    setMode("list");
    setSelectedEvent(null);
    setRegistrations([]);
    setSelectedSponsorIds([]);
  };

  return (
    <main className="organizer-dashboard-shell">
      <section className="dashboard-panel dashboard-hero">
        <div>
          <span className="dashboard-kicker">Organizator</span>
          <h1>Panou de control evenimente</h1>
        </div>
        <button
          className="dashboard-primary"
          type="button"
          onClick={openCreate}
        >
          + Creează eveniment
        </button>
      </section>

      {message && <p className="dashboard-message">{message}</p>}

      <section className="dashboard-panel events-panel">
        <div className="dashboard-section-head">
          <h2>Evenimentele mele</h2>
          <span>{myEvents.length} evenimente</span>
        </div>
        {loading ? (
          <p>Se încarcă...</p>
        ) : (
          <div className="organizer-event-list">
            {myEvents.map((event) => (
              <article key={event.id} className="organizer-event-card">
                <div>
                  <h3>{event.name}</h3>
                  <p>
                    {event.location?.name} · {formatDateTime(event.start_date)}
                  </p>
                  <small>
                    {event.registered_count ?? 0}
                    {event.capacity ? ` / ${event.capacity}` : ""} participanți
                  </small>
                </div>
                <div className="dashboard-actions">
                  <button type="button" onClick={() => openView(event)}>
                    Vizualizare
                  </button>
                  <button type="button" onClick={() => openEdit(event)}>
                    Editare
                  </button>
                  <button
                    type="button"
                    className="danger"
                    onClick={() => deleteEvent(event)}
                  >
                    Ștergere
                  </button>
                </div>
              </article>
            ))}
            {myEvents.length === 0 && (
              <p>Nu există evenimente create pentru organizația ta.</p>
            )}
          </div>
        )}
      </section>

      {modalOpen && (
        <div className="dashboard-modal-backdrop" onClick={closeModal}>
          <div
            className="dashboard-modal"
            onClick={(event) => event.stopPropagation()}
          >
            {(mode === "create" || mode === "edit") && (
              <>
                <div className="dashboard-modal-header">
                  <div>
                    <span className="dashboard-kicker">Eveniment</span>
                    <h2>
                      {mode === "create"
                        ? "Creează eveniment"
                        : "Editează eveniment"}
                    </h2>
                  </div>
                  <button
                    type="button"
                    className="dashboard-modal-close"
                    onClick={closeModal}
                  >
                    ×
                  </button>
                </div>

                <div className="dashboard-form-grid">
                  <label>
                    Nume
                    <input
                      value={form.name}
                      onChange={(e) => changeForm("name", e.target.value)}
                    />
                  </label>
                  <label>
                    Începe
                    <input
                      type="datetime-local"
                      value={form.start_date}
                      onChange={(e) => changeForm("start_date", e.target.value)}
                    />
                  </label>
                  <label>
                    Se termină
                    <input
                      type="datetime-local"
                      value={form.end_date}
                      onChange={(e) => changeForm("end_date", e.target.value)}
                    />
                  </label>
                  <label>
                    Locație
                    <select
                      value={form.location_id}
                      onChange={(e) =>
                        changeForm("location_id", e.target.value)
                      }
                    >
                      <option value="">Alege locația</option>
                      {locations.map((l) => (
                        <option key={l.id} value={l.id}>
                          {l.name}
                        </option>
                      ))}
                    </select>
                  </label>
                  <label>
                    Categorie
                    <select
                      value={form.category_id}
                      onChange={(e) =>
                        changeForm("category_id", e.target.value)
                      }
                    >
                      <option value="">Alege categoria</option>
                      {categories.map((c) => (
                        <option key={c.id} value={c.id}>
                          {c.name}
                        </option>
                      ))}
                    </select>
                  </label>
                  <label>
                    Participare
                    <select
                      value={form.participation_type_id}
                      onChange={(e) =>
                        changeForm("participation_type_id", e.target.value)
                      }
                    >
                      <option value="">Alege tipul</option>
                      {participationTypes.map((p) => (
                        <option key={p.id} value={p.id}>
                          {p.name}
                        </option>
                      ))}
                    </select>
                  </label>
                  <label>
                    Capacitate
                    <input
                      type="number"
                      value={form.capacity}
                      onChange={(e) => changeForm("capacity", e.target.value)}
                    />
                  </label>
                  <label>
                    Termen înscriere
                    <input
                      type="datetime-local"
                      value={form.registration_deadline}
                      onChange={(e) =>
                        changeForm("registration_deadline", e.target.value)
                      }
                    />
                  </label>
                  <label>
                    Tip preț
                    <select
                      value={form.pricing_type}
                      onChange={(e) =>
                        changeForm("pricing_type", e.target.value)
                      }
                    >
                      <option value="free">Gratuit</option>
                      <option value="paid">Plătit</option>
                    </select>
                  </label>
                  <label>
                    Acces
                    <select
                      value={form.access_policy}
                      onChange={(e) =>
                        changeForm("access_policy", e.target.value)
                      }
                    >
                      <option value="open">Acces deschis</option>
                      <option value="registration">Necesită înscriere</option>
                      <option value="ticket">Necesită bilet</option>
                      <option value="registration_ticket">
                        Înscriere și bilet
                      </option>
                    </select>
                  </label>
                  <label>
                    Link înscriere
                    <input
                      value={form.registration_link}
                      onChange={(e) =>
                        changeForm("registration_link", e.target.value)
                      }
                    />
                  </label>
                  <label>
                    Link online
                    <input
                      value={form.online_link}
                      onChange={(e) =>
                        changeForm("online_link", e.target.value)
                      }
                    />
                  </label>
                  <label className="full">
                    Descriere
                    <textarea
                      rows={5}
                      value={form.description}
                      onChange={(e) =>
                        changeForm("description", e.target.value)
                      }
                    />
                  </label>
                </div>

                <div className="sponsor-picker">
                  <div className="sponsor-picker-head">
                    <div>
                      <span className="dashboard-kicker">Sponsori</span>
                      <h3>Selectează sponsorii evenimentului</h3>
                    </div>
                    <span>{selectedSponsorIds.length} selectați</span>
                  </div>

                  <input
                    className="sponsor-search"
                    type="search"
                    value={sponsorSearch}
                    onChange={(e) => setSponsorSearch(e.target.value)}
                    placeholder="Caută sponsor..."
                  />

                  <div className="sponsor-grid">
                    {filteredSponsors.map((sponsor) => {
                      const selected = selectedSponsorIds.includes(sponsor.id);

                      return (
                        <button
                          key={sponsor.id}
                          type="button"
                          className={
                            selected ? "sponsor-card selected" : "sponsor-card"
                          }
                          onClick={() => toggleSponsor(sponsor.id)}
                        >
                          <span>{sponsor.name}</span>
                          <strong>{selected ? "✓" : "+"}</strong>
                        </button>
                      );
                    })}

                    {filteredSponsors.length === 0 && (
                      <p className="sponsor-empty">
                        Nu există sponsori găsiți.
                      </p>
                    )}
                  </div>
                </div>

                <div className="dashboard-modal-actions">
                  <button
                    className="dashboard-primary"
                    type="button"
                    onClick={submitForm}
                  >
                    {mode === "create" ? "Creează" : "Salvează modificările"}
                  </button>
                  <button
                    type="button"
                    className="dashboard-secondary"
                    onClick={closeModal}
                  >
                    Anulează
                  </button>
                </div>
              </>
            )}

            {mode === "view" && selectedEvent && (
              <>
                <div className="dashboard-modal-header">
                  <div>
                    <span className="dashboard-kicker">Detalii eveniment</span>
                    <h2>{selectedEvent.name}</h2>
                  </div>
                  <button
                    type="button"
                    className="dashboard-modal-close"
                    onClick={closeModal}
                  >
                    ×
                  </button>
                </div>
                <div className="dashboard-details-grid">
                  <div>
                    <span>Descriere</span>
                    <strong>{selectedEvent.description}</strong>
                  </div>
                  <div>
                    <span>Perioadă</span>
                    <strong>
                      {formatDateTime(selectedEvent.start_date)} -{" "}
                      {formatDateTime(selectedEvent.end_date)}
                    </strong>
                  </div>
                  <div>
                    <span>Locație</span>
                    <strong>{selectedEvent.location?.name}</strong>
                  </div>
                  <div>
                    <span>Categorie</span>
                    <strong>{selectedEvent.category?.name}</strong>
                  </div>
                  <div>
                    <span>Participare</span>
                    <strong>{selectedEvent.participation_type?.name}</strong>
                  </div>
                  <div>
                    <span>Status</span>
                    <strong>{selectedEvent.status?.name}</strong>
                  </div>
                  <div>
                    <span>Sponsori</span>
                    <strong>
                      {selectedEventSponsors.length
                        ? selectedEventSponsors.map((s) => s.name).join(", ")
                        : "Fără sponsori"}
                    </strong>
                  </div>
                </div>

                <div className="dashboard-subsection">
                  <h3>Persoane înscrise</h3>
                  <div className="registration-list">
                    {registrations.map((registration) => {
                      const user =
                        registration.user &&
                        typeof registration.user === "object"
                          ? registration.user
                          : null;
                      const name =
                        registration.username ||
                        user?.username ||
                        `${user?.first_name ?? ""} ${user?.last_name ?? ""}`.trim() ||
                        "Utilizator";
                      return (
                        <article
                          key={registration.id}
                          className="registration-card"
                        >
                          <strong>{name}</strong>
                          <span>
                            {registration.email ||
                              user?.email ||
                              "Email indisponibil"}
                          </span>
                          <small>
                            {registration.status?.name ||
                              registration.status_name ||
                              "Status necunoscut"}
                          </small>
                        </article>
                      );
                    })}
                    {registrations.length === 0 && (
                      <p>Nu există înscrieri pentru acest eveniment.</p>
                    )}
                  </div>
                </div>
              </>
            )}
          </div>
        </div>
      )}
    </main>
  );
};
