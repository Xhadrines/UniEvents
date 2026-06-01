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
type EventSponsorLink = {
  id: number;
  event?: number | { id?: number };
  sponsor?: number | SponsorEntity | { id?: number };
};
type MaterialEntity = {
  id: number;
  title: string;
  file?: string | null;
  is_public?: boolean;
  material_type?: DescribedEntity;
  uploaded_by?: DescribedEntity | null;
  created_at?: string;
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

type RegistrationWithEvent = RegistrationItem & {
  event?: number | { id?: number };
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
  max_files?: number | null;
  max_file_size_mb?: number | null;
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
  start_time: string;
  end_time: string;
  capacity: string;
  registration_deadline: string;
  registration_deadline_time: string;
  pricing_type: "free" | "paid";
  access_policy: "open" | "registration" | "ticket" | "registration_ticket";
  is_free_entry: boolean;
  requires_registration: boolean;
  requires_ticket: boolean;
  max_files: string;
  max_file_size_mb: string;
};

type MaterialForm = {
  title: string;
  material_type_id: string;
  file: File | null;
  is_public: boolean;
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
  start_time: "",
  end_time: "",
  capacity: "",
  registration_deadline: "",
  registration_deadline_time: "",
  pricing_type: "free",
  access_policy: "open",
  is_free_entry: true,
  requires_registration: false,
  requires_ticket: false,
  max_files: "",
  max_file_size_mb: "",
};

const EVENT_EDITABLE_FIELDS = [
  "name",
  "description",
  "registration_link",
  "online_link",
  "location_id",
  "category_id",
  "participation_type_id",
  "start_date",
  "end_date",
  "capacity",
  "registration_deadline",
  "pricing_type",
  "is_free_entry",
  "requires_registration",
  "requires_ticket",
  "max_files",
  "max_file_size_mb",
] as const;

const EVENT_READONLY_FIELDS = [
  "organizer",
  "status",
  "access_policy",
  "qr_code",
  "validated_by",
  "validated_at",
  "created_at",
  "updated_at",
] as const;

const emptyMaterialForm: MaterialForm = {
  title: "",
  material_type_id: "",
  file: null,
  is_public: true,
};

const deriveAccessPolicy = (form: EventForm) => {
  if (form.requires_registration && form.requires_ticket)
    return "registration_ticket";
  if (form.requires_registration) return "registration";
  if (form.requires_ticket) return "ticket";
  return "open";
};

const authHeaders = (): Record<string, string> => {
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

const splitDateTime = (value?: string | null) => {
  if (!value) {
    return {
      date: "",
      time: "",
    };
  }

  const local = toDateTimeLocal(value);

  return {
    date: local.slice(0, 10),
    time: local.slice(11, 16),
  };
};

const formatDateTime = (value?: string | null) => {
  if (!value) return "N/A";
  return new Intl.DateTimeFormat("ro-RO", {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(new Date(value));
};

const isRejectedEvent = (event?: EventItem | null) =>
  event?.status?.name?.toLowerCase().includes("respins");

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
  const [materialTypes, setMaterialTypes] = useState<DescribedEntity[]>([]);
  const [sponsors, setSponsors] = useState<SponsorEntity[]>([]);
  const [eventSponsors, setEventSponsors] = useState<EventSponsorLink[]>([]);
  const [registrations, setRegistrations] = useState<RegistrationItem[]>([]);
  const [eventMaterials, setEventMaterials] = useState<MaterialEntity[]>([]);
  const [selectedEvent, setSelectedEvent] = useState<EventItem | null>(null);
  const [mode, setMode] = useState<"list" | "create" | "edit" | "view">("list");
  const modalOpen = mode === "create" || mode === "edit" || mode === "view";
  const [form, setForm] = useState<EventForm>(emptyForm);
  const [materialForm, setMaterialForm] =
    useState<MaterialForm>(emptyMaterialForm);
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
      .filter((item) => {
        const linkedEvent =
          typeof item.event === "object" && item.event
            ? item.event.id
            : item.event;
        return Number(linkedEvent) === selectedEvent.id;
      })
      .map((item) =>
        typeof item.sponsor === "object" && item.sponsor
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

  const loadEventMaterials = async (eventId: number) => {
    try {
      const base = import.meta.env.VITE_API;
      const response = await fetch(`${base}/api/events/${eventId}/materials/`, {
        headers: authHeaders(),
      });
      const data = response.ok ? await response.json() : [];
      setEventMaterials(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error(error);
      setEventMaterials([]);
    }
  };

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
        materialTypesData,
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
        fetch(`${base}/api/material-types/`, { headers }).then((r) =>
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
      setMaterialTypes(
        Array.isArray(materialTypesData) ? materialTypesData : [],
      );
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
      start_date: splitDateTime(event.start_date).date,
      start_time: splitDateTime(event.start_date).time,
      end_date: splitDateTime(event.end_date).date,
      end_time: splitDateTime(event.end_date).time,
      capacity: event.capacity ? String(event.capacity) : "",
      registration_deadline: splitDateTime(event.registration_deadline).date,
      registration_deadline_time: splitDateTime(event.registration_deadline)
        .time,
      pricing_type: event.pricing_type === "paid" ? "paid" : "free",
      access_policy:
        (event.access_policy as EventForm["access_policy"]) ?? "open",
      is_free_entry: Boolean(event.is_free_entry ?? true),
      requires_registration: Boolean(event.requires_registration ?? false),
      requires_ticket: Boolean(event.requires_ticket ?? false),
      max_files: event.max_files ? String(event.max_files) : "",
      max_file_size_mb: event.max_file_size_mb
        ? String(event.max_file_size_mb)
        : "",
    });
    setSelectedSponsorIds(
      eventSponsors
        .filter((item) => {
          const linkedEvent =
            typeof item.event === "object" && item.event
              ? item.event.id
              : item.event;
          return Number(linkedEvent) === event.id;
        })
        .map((item) =>
          Number(
            typeof item.sponsor === "object" && item.sponsor
              ? item.sponsor.id
              : item.sponsor,
          ),
        )
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
          (reg: RegistrationWithEvent) =>
            Number(
              typeof reg.event === "object" && reg.event
                ? reg.event.id
                : reg.event,
            ) === event.id,
        ),
      );
      await loadEventMaterials(event.id);
    } catch {
      setRegistrations([]);
      setEventMaterials([]);
    }
  };

  const changeForm = (field: keyof EventForm, value: string | boolean) =>
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
    start_date: new Date(`${form.start_date}T${form.start_time}`).toISOString(),
    end_date: new Date(`${form.end_date}T${form.end_time}`).toISOString(),
    capacity: form.capacity ? Number(form.capacity) : null,
    registration_deadline:
      form.registration_deadline && form.registration_deadline_time
        ? new Date(
            `${form.registration_deadline}T${form.registration_deadline_time}`,
          ).toISOString()
        : null,
    pricing_type: form.pricing_type,
    is_free_entry: form.is_free_entry,
    requires_registration: form.requires_registration,
    requires_ticket: form.requires_ticket,
    access_policy: deriveAccessPolicy(form),
    max_files: form.max_files ? Number(form.max_files) : null,
    max_file_size_mb: form.max_file_size_mb
      ? Number(form.max_file_size_mb)
      : null,
  });

  const syncSponsors = async (eventId: number) => {
    const currentLinks = eventSponsors.filter((item) => {
      const linkedEvent =
        typeof item.event === "object" && item.event
          ? item.event.id
          : item.event;
      return Number(linkedEvent) === eventId;
    });
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

  const changeMaterialForm = <K extends keyof MaterialForm>(
    field: K,
    value: MaterialForm[K],
  ) => setMaterialForm((previous) => ({ ...previous, [field]: value }));

  const updateMaterialVisibility = async (
    material: MaterialEntity,
    isPublic: boolean,
  ) => {
    try {
      const response = await fetch(
        `${import.meta.env.VITE_API}/api/event-materials/${material.id}/`,
        {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            ...authHeaders(),
          },
          body: JSON.stringify({ is_public: isPublic }),
        },
      );

      if (!response.ok) {
        setMessage("Nu s-a putut modifica vizibilitatea materialului.");
        return;
      }

      if (selectedEvent) {
        await loadEventMaterials(selectedEvent.id);
      }
    } catch {
      setMessage("A apărut o eroare la modificarea vizibilității.");
    }
  };

  const uploadMaterial = async () => {
    if (!selectedEvent || !materialForm.file) return;

    if (isRejectedEvent(selectedEvent)) {
      setMessage("Evenimentul respins nu permite încărcarea materialelor.");
      return;
    }

    if (
      selectedEvent.max_files !== null &&
      selectedEvent.max_files !== undefined &&
      eventMaterials.length >= selectedEvent.max_files
    ) {
      setMessage("Evenimentul a atins numărul maxim de fișiere permis.");
      return;
    }

    if (
      selectedEvent.max_file_size_mb !== null &&
      selectedEvent.max_file_size_mb !== undefined
    ) {
      const maxBytes = selectedEvent.max_file_size_mb * 1024 * 1024;
      if (materialForm.file.size > maxBytes) {
        setMessage(
          `Fișierul depășește limita de ${selectedEvent.max_file_size_mb} MB.`,
        );
        return;
      }
    }

    try {
      setMessage("");
      const base = import.meta.env.VITE_API;
      const body = new FormData();
      body.append("title", materialForm.title);
      body.append("material_type", materialForm.material_type_id);
      body.append("file", materialForm.file);
      body.append("is_public", materialForm.is_public ? "True" : "False");

      const response = await fetch(
        `${base}/api/events/${selectedEvent.id}/materials/upload/`,
        {
          method: "POST",
          headers: authHeaders(),
          body,
        },
      );
      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        setMessage(data.error || "Nu s-a putut încărca materialul.");
        return;
      }

      setMessage("Materialul a fost încărcat.");
      setMaterialForm(emptyMaterialForm);
      await loadEventMaterials(selectedEvent.id);
    } catch (error) {
      console.error(error);
      setMessage("Nu s-a putut încărca materialul.");
    }
  };

  const closeModal = () => {
    setMode("list");
    setSelectedEvent(null);
    setRegistrations([]);
    setEventMaterials([]);
    setSelectedSponsorIds([]);
    setMaterialForm(emptyMaterialForm);
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
                  <label className="full">
                    Nume eveniment
                    <input
                      value={form.name}
                      onChange={(e) => changeForm("name", e.target.value)}
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

                  <label>
                    Data început
                    <input
                      type="date"
                      lang="ro"
                      value={form.start_date}
                      onChange={(e) => changeForm("start_date", e.target.value)}
                    />
                  </label>

                  <label>
                    Ora început
                    <input
                      type="time"
                      step="300"
                      value={form.start_time}
                      onChange={(e) => changeForm("start_time", e.target.value)}
                    />
                  </label>

                  <label>
                    Data final
                    <input
                      type="date"
                      lang="ro"
                      value={form.end_date}
                      onChange={(e) => changeForm("end_date", e.target.value)}
                    />
                  </label>

                  <label>
                    Ora final
                    <input
                      type="time"
                      step="300"
                      value={form.end_time}
                      onChange={(e) => changeForm("end_time", e.target.value)}
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
                    Număr maxim fișiere
                    <input
                      type="number"
                      min="0"
                      value={form.max_files}
                      onChange={(e) => changeForm("max_files", e.target.value)}
                    />
                  </label>

                  <label>
                    Dimensiune maximă fișier MB
                    <input
                      type="number"
                      min="0"
                      value={form.max_file_size_mb}
                      onChange={(e) =>
                        changeForm("max_file_size_mb", e.target.value)
                      }
                    />
                  </label>

                  <label>
                    Data limită înscriere
                    <input
                      type="date"
                      lang="ro"
                      value={form.registration_deadline}
                      onChange={(e) =>
                        changeForm("registration_deadline", e.target.value)
                      }
                    />
                  </label>

                  <label>
                    Ora limită înscriere
                    <input
                      type="time"
                      step="300"
                      value={form.registration_deadline_time}
                      onChange={(e) =>
                        changeForm("registration_deadline_time", e.target.value)
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
                    Intrare gratuită
                    <select
                      value={String(form.is_free_entry)}
                      onChange={(e) =>
                        changeForm("is_free_entry", e.target.value === "true")
                      }
                    >
                      <option value="true">Da</option>
                      <option value="false">Nu</option>
                    </select>
                  </label>

                  <label>
                    Necesită înscriere
                    <select
                      value={String(form.requires_registration)}
                      onChange={(e) =>
                        changeForm(
                          "requires_registration",
                          e.target.value === "true",
                        )
                      }
                    >
                      <option value="false">Nu</option>
                      <option value="true">Da</option>
                    </select>
                  </label>

                  <label>
                    Necesită bilet
                    <select
                      value={String(form.requires_ticket)}
                      onChange={(e) =>
                        changeForm("requires_ticket", e.target.value === "true")
                      }
                    >
                      <option value="false">Nu</option>
                      <option value="true">Da</option>
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
                </div>

                <div className="dashboard-details-grid dashboard-subsection">
                  <div>
                    <span>Organizator</span>
                    <strong>
                      {myOrganizers.find(
                        (organizer) =>
                          String(organizer.id) === form.organizer_id,
                      )?.name || "Se completează automat"}
                    </strong>
                  </div>
                  <div>
                    <span>Status</span>
                    <strong>În așteptare</strong>
                  </div>
                  <div>
                    <span>Politică acces</span>
                    <strong>
                      {deriveAccessPolicy(form) === "registration_ticket"
                        ? "Necesită înscriere și bilet"
                        : deriveAccessPolicy(form) === "registration"
                          ? "Necesită înscriere"
                          : deriveAccessPolicy(form) === "ticket"
                            ? "Necesită bilet"
                            : "Acces deschis"}
                    </strong>
                  </div>
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
                  <div className="full">
                    <span>Descriere</span>
                    <strong>{selectedEvent.description || "N/A"}</strong>
                  </div>

                  <div>
                    <span>Începe</span>
                    <strong>{formatDateTime(selectedEvent.start_date)}</strong>
                  </div>

                  <div>
                    <span>Se termină</span>
                    <strong>{formatDateTime(selectedEvent.end_date)}</strong>
                  </div>

                  <div>
                    <span>Locație</span>
                    <strong>
                      {selectedEvent.location?.name || "N/A"}
                      {selectedEvent.location?.address
                        ? `, ${selectedEvent.location.address}`
                        : ""}
                      {selectedEvent.location?.building
                        ? `, Corp ${selectedEvent.location.building}`
                        : ""}
                      {selectedEvent.location?.room
                        ? `, Sala ${selectedEvent.location.room}`
                        : ""}
                    </strong>
                  </div>

                  <div>
                    <span>Organizator</span>
                    <strong>{selectedEvent.organizer?.name || "N/A"}</strong>
                  </div>

                  <div>
                    <span>Categorie</span>
                    <strong>{selectedEvent.category?.name || "N/A"}</strong>
                  </div>

                  <div>
                    <span>Participare</span>
                    <strong>
                      {selectedEvent.participation_type?.name || "N/A"}
                    </strong>
                  </div>

                  <div>
                    <span>Status</span>
                    <strong>{selectedEvent.status?.name || "N/A"}</strong>
                  </div>

                  <div>
                    <span>Capacitate</span>
                    <strong>
                      {selectedEvent.registered_count ?? 0}
                      {selectedEvent.capacity
                        ? ` / ${selectedEvent.capacity}`
                        : " / Nelimitat"}
                    </strong>
                  </div>

                  <div>
                    <span>Număr maxim fișiere</span>
                    <strong>{selectedEvent.max_files ?? "Nelimitat"}</strong>
                  </div>

                  <div>
                    <span>Dimensiune maximă fișier</span>
                    <strong>
                      {selectedEvent.max_file_size_mb
                        ? `${selectedEvent.max_file_size_mb} MB`
                        : "Fără limită"}
                    </strong>
                  </div>

                  <div>
                    <span>Termen înscriere</span>
                    <strong>
                      {formatDateTime(selectedEvent.registration_deadline)}
                    </strong>
                  </div>

                  <div>
                    <span>Tip preț</span>
                    <strong>
                      {selectedEvent.pricing_type === "paid"
                        ? "Plătit"
                        : "Gratuit"}
                    </strong>
                  </div>

                  <div>
                    <span>Intrare gratuită</span>
                    <strong>{selectedEvent.is_free_entry ? "Da" : "Nu"}</strong>
                  </div>

                  <div>
                    <span>Necesită înscriere</span>
                    <strong>
                      {selectedEvent.requires_registration ? "Da" : "Nu"}
                    </strong>
                  </div>

                  <div>
                    <span>Necesită bilet</span>
                    <strong>
                      {selectedEvent.requires_ticket ? "Da" : "Nu"}
                    </strong>
                  </div>

                  <div>
                    <span>Politică acces</span>
                    <strong>{selectedEvent.access_policy || "N/A"}</strong>
                  </div>

                  <div>
                    <span>Link înscriere</span>
                    <strong>{selectedEvent.registration_link || "N/A"}</strong>
                  </div>

                  <div>
                    <span>Link online</span>
                    <strong>{selectedEvent.online_link || "N/A"}</strong>
                  </div>

                  <div>
                    <span>Cod QR</span>
                    <strong>
                      {selectedEvent.qr_code ? "Disponibil" : "N/A"}
                    </strong>
                  </div>

                  <div>
                    <span>Limite fișiere</span>
                    <strong>
                      {selectedEvent.max_files ?? "Nelimitat"} fișiere,{" "}
                      {selectedEvent.max_file_size_mb ?? "fără limită"} MB /
                      fișier
                    </strong>
                  </div>

                  <div>
                    <span>Creat la</span>
                    <strong>{formatDateTime(selectedEvent.created_at)}</strong>
                  </div>

                  <div>
                    <span>Actualizat la</span>
                    <strong>{formatDateTime(selectedEvent.updated_at)}</strong>
                  </div>

                  <div className="full">
                    <span>Sponsori</span>
                    <strong>
                      {selectedEventSponsors.length
                        ? selectedEventSponsors.map((s) => s.name).join(", ")
                        : "Fără sponsori"}
                    </strong>
                  </div>
                </div>

                <div className="dashboard-subsection">
                  <div className="sponsor-picker-head">
                    <div>
                      <span className="dashboard-kicker">Materiale</span>
                      <h3>Încărcare materiale eveniment</h3>
                    </div>
                    <span>
                      {eventMaterials.length}
                      {selectedEvent.max_files
                        ? ` / ${selectedEvent.max_files}`
                        : ""}
                    </span>
                  </div>

                  {isRejectedEvent(selectedEvent) ? (
                    <p className="dashboard-message">
                      Evenimentul a fost respins. Nu mai poți încărca materiale
                      pentru acest eveniment.
                    </p>
                  ) : (
                    <>
                      <div className="dashboard-form-grid">
                        <label>
                          Titlu
                          <input
                            value={materialForm.title}
                            onChange={(event) =>
                              changeMaterialForm("title", event.target.value)
                            }
                          />
                        </label>

                        <label>
                          Tip material
                          <select
                            value={materialForm.material_type_id}
                            onChange={(event) =>
                              changeMaterialForm(
                                "material_type_id",
                                event.target.value,
                              )
                            }
                          >
                            <option value="">Alege tipul</option>

                            {materialTypes.map((type) => (
                              <option key={type.id} value={type.id}>
                                {type.name}
                              </option>
                            ))}
                          </select>
                        </label>

                        <label>
                          Fișier
                          <label className="custom-file-upload">
                            <input
                              type="file"
                              hidden
                              onChange={(event) =>
                                changeMaterialForm(
                                  "file",
                                  event.target.files?.[0] ?? null,
                                )
                              }
                            />

                            <span>
                              {materialForm.file
                                ? materialForm.file.name
                                : "Selectează fișier"}
                            </span>
                          </label>
                        </label>

                        <label>
                          Vizibilitate
                          <select
                            value={String(materialForm.is_public)}
                            onChange={(event) =>
                              changeMaterialForm(
                                "is_public",
                                event.target.value === "true",
                              )
                            }
                          >
                            <option value="true">Da</option>
                            <option value="false">Nu</option>
                          </select>
                        </label>
                      </div>

                      <div className="dashboard-modal-actions">
                        <button
                          className="dashboard-primary"
                          type="button"
                          onClick={uploadMaterial}
                          disabled={
                            !materialForm.file ||
                            !materialForm.title ||
                            !materialForm.material_type_id ||
                            (selectedEvent.max_files !== null &&
                              selectedEvent.max_files !== undefined &&
                              eventMaterials.length >= selectedEvent.max_files)
                          }
                        >
                          Încarcă material
                        </button>
                      </div>
                    </>
                  )}

                  <div className="registration-list">
                    {eventMaterials.map((material) => {
                      const fileName = material.file
                        ? material.file.split("/").pop()
                        : "Fără fișier";

                      const fileUrl = material.file
                        ? material.file.startsWith("http")
                          ? material.file
                          : `${import.meta.env.VITE_API}${material.file}`
                        : "";

                      return (
                        <article
                          key={material.id}
                          className="registration-card"
                        >
                          <strong>{material.title}</strong>

                          <span>
                            {material.material_type?.name || "Tip necunoscut"}
                          </span>

                          <small>
                            {material.is_public ? "Public" : "Privat"}
                            {material.created_at
                              ? ` · ${formatDateTime(material.created_at)}`
                              : ""}
                          </small>

                          {material.is_public && fileUrl ? (
                            <a
                              className="material-download-link"
                              href={fileUrl}
                              target="_blank"
                              rel="noreferrer"
                              download
                            >
                              Descarcă: {fileName}
                            </a>
                          ) : (
                            <small>{fileName}</small>
                          )}

                          {!isRejectedEvent(selectedEvent) && (
                            <label className="material-visibility-toggle">
                              <span>Vizibil pentru utilizatori</span>

                              <select
                                className="material-visibility-select"
                                value={String(material.is_public)}
                                onChange={(event) =>
                                  updateMaterialVisibility(
                                    material,
                                    event.target.value === "true",
                                  )
                                }
                              >
                                <option value="true">Da</option>
                                <option value="false">Nu</option>
                              </select>
                            </label>
                          )}
                        </article>
                      );
                    })}
                    {eventMaterials.length === 0 && (
                      <p>
                        Nu există materiale încărcate pentru acest eveniment.
                      </p>
                    )}
                  </div>

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
