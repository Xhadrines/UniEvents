import { useEffect, useMemo, useState } from "react";
import "./AdminDashboard.css";

type Entity = Record<string, any> & { id?: number | string };

type CrudResource = {
  key: string;
  label: string;
  endpoint: string;
  readonly?: boolean;
};

type ForeignKeyConfig = {
  resourceKey: string;
  label?: string;
};

const FK_FIELDS: Record<string, ForeignKeyConfig> = {
  role: { resourceKey: "roles", label: "Rol" },
  role_id: { resourceKey: "roles", label: "Rol" },

  status: { resourceKey: "statuses", label: "Status" },
  status_id: { resourceKey: "statuses", label: "Status" },

  faculty: { resourceKey: "faculties", label: "Facultate" },
  faculty_id: { resourceKey: "faculties", label: "Facultate" },

  specialization: { resourceKey: "specializations", label: "Specializare" },
  specialization_id: { resourceKey: "specializations", label: "Specializare" },

  organizer_type: { resourceKey: "organizerTypes", label: "Tip organizator" },
  organizer_type_id: {
    resourceKey: "organizerTypes",
    label: "Tip organizator",
  },

  organizer: { resourceKey: "organizers", label: "Organizator" },
  organizer_id: { resourceKey: "organizers", label: "Organizator" },

  category: { resourceKey: "categories", label: "Categorie" },
  category_id: { resourceKey: "categories", label: "Categorie" },

  participation_type: {
    resourceKey: "participationTypes",
    label: "Tip participare",
  },
  participation_type_id: {
    resourceKey: "participationTypes",
    label: "Tip participare",
  },

  location: { resourceKey: "locations", label: "Locație" },
  location_id: { resourceKey: "locations", label: "Locație" },

  user: { resourceKey: "users", label: "Utilizator" },
  user_id: { resourceKey: "users", label: "Utilizator" },

  event: { resourceKey: "events", label: "Eveniment" },
  event_id: { resourceKey: "events", label: "Eveniment" },

  sponsor: { resourceKey: "sponsors", label: "Sponsor" },
  sponsor_id: { resourceKey: "sponsors", label: "Sponsor" },

  material_type: { resourceKey: "materialTypes", label: "Tip material" },
  material_type_id: { resourceKey: "materialTypes", label: "Tip material" },

  notification_type: {
    resourceKey: "notificationTypes",
    label: "Tip notificare",
  },
  notification_type_id: {
    resourceKey: "notificationTypes",
    label: "Tip notificare",
  },

  uploaded_by: { resourceKey: "users", label: "Încărcat de" },
  uploaded_by_id: { resourceKey: "users", label: "Încărcat de" },

  created_by: { resourceKey: "users", label: "Creat de" },
  created_by_id: { resourceKey: "users", label: "Creat de" },
};

const CRUD_RESOURCES: CrudResource[] = [
  { key: "users", label: "Utilizatori", endpoint: "/api/users/" },
  {
    key: "userProfiles",
    label: "Profiluri utilizatori",
    endpoint: "/api/user-profiles/",
  },
  { key: "roles", label: "Roluri", endpoint: "/api/roles/" },
  { key: "statuses", label: "Statusuri", endpoint: "/api/statuses/" },
  { key: "faculties", label: "Facultăți", endpoint: "/api/faculties/" },
  {
    key: "specializations",
    label: "Specializări",
    endpoint: "/api/specializations/",
  },
  {
    key: "organizerTypes",
    label: "Tipuri organizatori",
    endpoint: "/api/organizer-types/",
  },
  { key: "organizers", label: "Organizatori", endpoint: "/api/organizers/" },
  { key: "categories", label: "Categorii", endpoint: "/api/categories/" },
  {
    key: "participationTypes",
    label: "Tipuri participare",
    endpoint: "/api/participation-types/",
  },
  { key: "locations", label: "Locații", endpoint: "/api/locations/" },
  { key: "events", label: "Evenimente", endpoint: "/api/events/" },
  { key: "sponsors", label: "Sponsori", endpoint: "/api/sponsors/" },
  {
    key: "eventSponsors",
    label: "Eveniment - Sponsor",
    endpoint: "/api/event-sponsors/",
  },
  { key: "registrations", label: "Înscrieri", endpoint: "/api/registrations/" },
  { key: "feedbacks", label: "Feedback", endpoint: "/api/feedbacks/" },
  {
    key: "materialTypes",
    label: "Tipuri materiale",
    endpoint: "/api/material-types/",
  },
  {
    key: "eventMaterials",
    label: "Materiale evenimente",
    endpoint: "/api/event-materials/",
  },
  {
    key: "favoriteEvents",
    label: "Evenimente favorite",
    endpoint: "/api/favorite-events/",
  },
  {
    key: "notificationTypes",
    label: "Tipuri notificări",
    endpoint: "/api/notification-types/",
  },
  {
    key: "notifications",
    label: "Notificări",
    endpoint: "/api/notifications/",
  },
  { key: "reports", label: "Rapoarte", endpoint: "/api/reports/" },
];

const HIDDEN_FORM_FIELDS = [
  "id",
  "created_at",
  "updated_at",
  "date_joined",
  "qr_code",
  "last_login",
  "password",
  "is_staff",
  "is_superuser",
  "groups",
  "user_permissions",
];

const authHeaders = () => {
  const token = localStorage.getItem("access");
  return token ? { Authorization: `Bearer ${token}` } : {};
};

const apiBase = () => import.meta.env.VITE_API || "";

const normalize = (value: unknown) =>
  String(value ?? "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase();

const isPendingEvent = (event: Entity) => {
  const statusName = normalize(
    event.status?.name ?? event.status_name ?? event.status,
  );
  return (
    statusName.includes("asteptare") ||
    statusName.includes("pending") ||
    statusName.includes("in asteptare")
  );
};

const displayValue = (value: any): string => {
  if (value === null || value === undefined || value === "") return "—";
  if (typeof value === "boolean") return value ? "Da" : "Nu";
  if (typeof value === "object") {
    return (
      value.name ||
      value.title ||
      value.username ||
      value.email ||
      value.id ||
      JSON.stringify(value)
    );
  }
  if (typeof value === "string" && /^\d{4}-\d{2}-\d{2}T/.test(value)) {
    return new Intl.DateTimeFormat("ro-RO", {
      dateStyle: "medium",
      timeStyle: "short",
    }).format(new Date(value));
  }
  return String(value);
};

const searchableText = (item: Entity) =>
  Object.values(item)
    .map((value) => displayValue(value))
    .join(" ")
    .toLowerCase();

const optionLabel = (item: Entity) =>
  item.name ||
  item.title ||
  item.username ||
  item.email ||
  (item.first_name && item.last_name
    ? `${item.first_name} ${item.last_name}`
    : undefined) ||
  `#${item.id}`;

const selectedRelationId = (value: any) => {
  if (value === null || value === undefined || value === "") return "";
  if (typeof value === "object") return value.id ?? "";
  return value;
};

const getColumns = (items: Entity[]) => {
  const preferred = [
    "id",
    "name",
    "title",
    "username",
    "email",
    "status",
    "role",
    "event",
    "user",
    "created_at",
  ];
  const keys = Array.from(new Set(items.flatMap((item) => Object.keys(item))));
  const ordered = [
    ...preferred.filter((key) => keys.includes(key)),
    ...keys.filter((key) => !preferred.includes(key)),
  ];
  return ordered.slice(0, 7);
};

const toEditablePayload = (form: Record<string, any>) => {
  const payload: Record<string, any> = {};

  Object.entries(form).forEach(([key, value]) => {
    if (
      ["id", "created_at", "updated_at", "date_joined", "qr_code"].includes(key)
    )
      return;

    if (value === "") {
      payload[key] = null;
      return;
    }

    if (typeof value === "object" && value !== null) {
      if (value.id !== undefined) payload[`${key}_id`] = value.id;
      return;
    }

    if (key.endsWith("_id")) {
      const numericValue = Number(value);
      payload[key] = Number.isNaN(numericValue) ? value : numericValue;
      return;
    }

    if (typeof value === "object" && value !== null && "id" in value) {
      payload[key] = value.id;
    } else {
      payload[key] = value;
    }
  });

  return payload;
};

export const AdminDashboard = () => {
  const [mainTab, setMainTab] = useState<"pending" | "crud">("pending");
  const [activeResourceKey, setActiveResourceKey] = useState(
    CRUD_RESOURCES[0].key,
  );
  const [data, setData] = useState<Record<string, Entity[]>>({});
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [search, setSearch] = useState("");
  const [modalMode, setModalMode] = useState<"view" | "create" | "edit" | null>(
    null,
  );
  const [selectedItem, setSelectedItem] = useState<Entity | null>(null);
  const [form, setForm] = useState<Record<string, any>>({});

  const activeResource =
    CRUD_RESOURCES.find((item) => item.key === activeResourceKey) ||
    CRUD_RESOURCES[0];
  const events = data.events || [];
  const pendingEvents = useMemo(() => events.filter(isPendingEvent), [events]);
  const activeItems = data[activeResource.key] || [];

  const getRelationOptions = (fieldKey: string) => {
    const relation = FK_FIELDS[fieldKey];
    return relation ? data[relation.resourceKey] || [] : [];
  };

  const displayTableValue = (fieldKey: string, value: any) => {
    const relation = FK_FIELDS[fieldKey];

    if (!relation) {
      return displayValue(value);
    }

    const relationId =
      typeof value === "object" && value !== null ? value.id : value;

    const relatedItem = (data[relation.resourceKey] || []).find(
      (item) => String(item.id) === String(relationId),
    );

    return relatedItem ? optionLabel(relatedItem) : displayValue(value);
  };

  const displayViewValue = (fieldKey: string, value: any) => {
    const relation = FK_FIELDS[fieldKey];

    if (!relation) {
      return displayValue(value);
    }

    const relationId =
      typeof value === "object" && value !== null ? value.id : value;

    const relatedItem = (data[relation.resourceKey] || []).find(
      (item) => String(item.id) === String(relationId),
    );

    const label = relatedItem ? optionLabel(relatedItem) : displayValue(value);

    return relationId ? `#${relationId} — ${label}` : label;
  };

  const updateRelationField = (fieldKey: string, selectedId: string) => {
    setForm((previous) => ({
      ...previous,
      [fieldKey]: selectedId ? Number(selectedId) : "",
    }));
  };

  const filteredItems = useMemo(() => {
    const term = search.trim().toLowerCase();
    if (!term) return activeItems;
    return activeItems.filter((item) => searchableText(item).includes(term));
  }, [activeItems, search]);

  const columns = useMemo(
    () => getColumns(filteredItems.length ? filteredItems : activeItems),
    [filteredItems, activeItems],
  );

  const request = async (endpoint: string, options: RequestInit = {}) => {
    const headers = {
      ...(options.body instanceof FormData
        ? {}
        : { "Content-Type": "application/json" }),
      ...authHeaders(),
      ...(options.headers || {}),
    };

    const response = await fetch(`${apiBase()}${endpoint}`, {
      ...options,
      headers,
    });
    const hasBody = response.status !== 204;
    const body = hasBody ? await response.json().catch(() => null) : null;

    if (!response.ok) {
      throw new Error(
        body?.error || JSON.stringify(body) || "Cererea a eșuat.",
      );
    }

    return body;
  };

  const loadResource = async (resource: CrudResource) => {
    const result = await request(resource.endpoint, { method: "GET" });
    setData((previous) => ({
      ...previous,
      [resource.key]: Array.isArray(result) ? result : [],
    }));
  };

  const loadAll = async () => {
    setLoading(true);
    setMessage("");
    try {
      await Promise.all(CRUD_RESOURCES.map(loadResource));
    } catch (error) {
      console.error(error);
      setMessage(
        error instanceof Error
          ? error.message
          : "Nu s-au putut încărca datele.",
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadAll();
  }, []);

  const openCreate = () => {
    const template = activeItems[0] || {};
    const nextForm = Object.fromEntries(
      Object.keys(template)
        .filter((key) => !HIDDEN_FORM_FIELDS.includes(key))
        .map((key) => [key, ""]),
    );

    setSelectedItem(null);
    setForm(nextForm);
    setModalMode("create");
  };

  const openView = (item: Entity) => {
    setSelectedItem(item);
    setForm(item);
    setModalMode("view");
  };

  const openEdit = (item: Entity) => {
    const editableForm = Object.fromEntries(
      Object.entries(item).filter(([key]) => !HIDDEN_FORM_FIELDS.includes(key)),
    );

    setSelectedItem(item);
    setForm(editableForm);
    setModalMode("edit");
  };

  const closeModal = () => {
    setModalMode(null);
    setSelectedItem(null);
    setForm({});
  };

  const saveItem = async () => {
    setMessage("");
    try {
      const payload = toEditablePayload(form);
      const isEdit = modalMode === "edit" && selectedItem?.id;
      const endpoint = isEdit
        ? `${activeResource.endpoint}${selectedItem.id}/`
        : activeResource.endpoint;

      await request(endpoint, {
        method: isEdit ? "PATCH" : "POST",
        body: JSON.stringify(payload),
      });

      setMessage(
        isEdit
          ? "Înregistrarea a fost actualizată."
          : "Înregistrarea a fost creată.",
      );
      closeModal();
      await loadResource(activeResource);
      if (activeResource.key === "events")
        await loadResource(CRUD_RESOURCES.find((r) => r.key === "events")!);
    } catch (error) {
      console.error(error);
      setMessage(
        error instanceof Error
          ? error.message
          : "Nu s-a putut salva înregistrarea.",
      );
    }
  };

  const deleteItem = async (item: Entity) => {
    if (!item.id) return;
    const confirmed = window.confirm(`Ștergi înregistrarea #${item.id}?`);
    if (!confirmed) return;

    try {
      await request(`${activeResource.endpoint}${item.id}/`, {
        method: "DELETE",
      });
      setMessage("Înregistrarea a fost ștearsă.");
      await loadResource(activeResource);
    } catch (error) {
      console.error(error);
      setMessage(
        error instanceof Error
          ? error.message
          : "Nu s-a putut șterge înregistrarea.",
      );
    }
  };

  const approveEvent = async (event: Entity) => {
    if (!event.id) return;
    try {
      await request(`/api/events/${event.id}/validate/`, { method: "POST" });
      setMessage(`Evenimentul „${event.name || event.id}” a fost acceptat.`);
      await loadResource(CRUD_RESOURCES.find((r) => r.key === "events")!);
    } catch (error) {
      console.error(error);
      setMessage(
        error instanceof Error
          ? error.message
          : "Nu s-a putut accepta evenimentul.",
      );
    }
  };

  const rejectEvent = async (event: Entity) => {
    if (!event.id) return;
    const confirmed = window.confirm(
      `Respingi/anulezi evenimentul „${event.name || event.id}”?`,
    );
    if (!confirmed) return;

    try {
      await request(`/api/events/${event.id}/cancel/`, { method: "POST" });
      setMessage(`Evenimentul „${event.name || event.id}” a fost anulat.`);
      await loadResource(CRUD_RESOURCES.find((r) => r.key === "events")!);
    } catch (error) {
      console.error(error);
      setMessage(
        error instanceof Error
          ? error.message
          : "Nu s-a putut anula evenimentul.",
      );
    }
  };

  return (
    <main className="admin-dashboard-shell">
      <section className="dashboard-panel dashboard-hero">
        <div>
          <span className="dashboard-kicker">Administrator</span>
          <h1>Panou administrare UniEvents</h1>
          <p>
            Validare evenimente și administrare rapidă pentru toate tabelele.
          </p>
        </div>
        <button className="dashboard-secondary" type="button" onClick={loadAll}>
          Reîncarcă datele
        </button>
      </section>

      <section className="dashboard-panel admin-mode-tabs">
        <button
          className={mainTab === "pending" ? "active" : ""}
          onClick={() => setMainTab("pending")}
        >
          Evenimente în așteptare ({pendingEvents.length})
        </button>
        <button
          className={mainTab === "crud" ? "active" : ""}
          onClick={() => setMainTab("crud")}
        >
          Panou CRUD / MVC
        </button>
      </section>

      {message && <p className="dashboard-message">{message}</p>}

      {mainTab === "pending" && (
        <section className="dashboard-panel events-panel">
          <div className="dashboard-section-head">
            <h2>Evenimente care așteaptă aprobare</h2>
            <span>
              {loading ? "Se încarcă..." : `${pendingEvents.length} evenimente`}
            </span>
          </div>

          <div className="organizer-event-list">
            {pendingEvents.map((event) => (
              <article key={event.id} className="organizer-event-card">
                <div>
                  <h3>{event.name || `Eveniment #${event.id}`}</h3>
                  <p>
                    {displayValue(event.location)} ·{" "}
                    {displayValue(event.start_date)}
                  </p>
                  <small>Status: {displayValue(event.status)}</small>
                </div>
                <div className="dashboard-actions">
                  <button type="button" onClick={() => openView(event)}>
                    Vizualizare
                  </button>
                  <button type="button" onClick={() => approveEvent(event)}>
                    Acceptă
                  </button>
                  <button
                    type="button"
                    className="danger"
                    onClick={() => rejectEvent(event)}
                  >
                    Respinge
                  </button>
                </div>
              </article>
            ))}
            {!loading && pendingEvents.length === 0 && (
              <p>Nu există evenimente în așteptare.</p>
            )}
          </div>
        </section>
      )}

      {mainTab === "crud" && (
        <section className="dashboard-panel admin-crud-layout">
          <aside className="admin-resource-tabs">
            {CRUD_RESOURCES.map((resource) => (
              <button
                key={resource.key}
                className={resource.key === activeResource.key ? "active" : ""}
                type="button"
                onClick={() => {
                  setActiveResourceKey(resource.key);
                  setSearch("");
                }}
              >
                {resource.label}
                <span>{data[resource.key]?.length ?? 0}</span>
              </button>
            ))}
          </aside>

          <div className="admin-table-panel">
            <div className="dashboard-section-head admin-table-head">
              <div>
                <h2>{activeResource.label}</h2>
                <span>{filteredItems.length} înregistrări afișate</span>
              </div>
              <button
                className="dashboard-primary"
                type="button"
                onClick={openCreate}
              >
                + Adaugă
              </button>
            </div>

            <input
              className="admin-search"
              type="search"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder={`Caută în ${activeResource.label.toLowerCase()}...`}
            />

            <div className="admin-table-wrap">
              <table className="admin-table">
                <thead>
                  <tr>
                    {columns.map((column) => (
                      <th key={column}>{column}</th>
                    ))}
                    <th>Acțiuni</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredItems.map((item, index) => (
                    <tr key={item.id || index}>
                      {columns.map((column) => (
                        <td key={column}>
                          {displayTableValue(column, item[column])}
                        </td>
                      ))}
                      <td>
                        <div className="dashboard-actions table-actions">
                          <button type="button" onClick={() => openView(item)}>
                            Vizualizare
                          </button>
                          <button type="button" onClick={() => openEdit(item)}>
                            Editare
                          </button>
                          <button
                            type="button"
                            className="danger"
                            onClick={() => deleteItem(item)}
                          >
                            Delete
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
              {!loading && filteredItems.length === 0 && (
                <p className="admin-empty">
                  Nu există date pentru acest tabel.
                </p>
              )}
            </div>
          </div>
        </section>
      )}

      {modalMode && (
        <div className="dashboard-modal-backdrop" onClick={closeModal}>
          <div
            className="dashboard-modal"
            onClick={(event) => event.stopPropagation()}
          >
            <div className="dashboard-modal-header">
              <div>
                <span className="dashboard-kicker">{activeResource.label}</span>
                <h2>
                  {modalMode === "view"
                    ? "Vizualizare"
                    : modalMode === "create"
                      ? "Adăugare"
                      : "Editare"}
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

            {modalMode === "view" ? (
              <div className="dashboard-details-grid">
                {Object.entries(selectedItem || form).map(([key, value]) => (
                  <div key={key}>
                    <span>{key}</span>
                    <strong>{displayViewValue(key, value)}</strong>
                  </div>
                ))}
              </div>
            ) : (
              <>
                <div className="dashboard-form-grid">
                  {Object.entries(form).map(([key, value]) => {
                    const isLong =
                      key.includes("description") ||
                      key.includes("message") ||
                      key.includes("comment");
                    const isDate =
                      typeof value === "string" &&
                      /^\d{4}-\d{2}-\d{2}T/.test(value);
                    const relation = FK_FIELDS[key];
                    const relationOptions = relation
                      ? getRelationOptions(key)
                      : [];

                    const isBoolean =
                      typeof value === "boolean" ||
                      value === "true" ||
                      value === "false";

                    return (
                      <label key={key} className={isLong ? "full" : ""}>
                        {relation?.label || key}

                        {relation ? (
                          <select
                            value={String(selectedRelationId(value))}
                            onChange={(event) =>
                              updateRelationField(key, event.target.value)
                            }
                          >
                            <option value="">
                              Alege {relation.label?.toLowerCase() || key}
                            </option>
                            {relationOptions.map((option) => (
                              <option key={option.id} value={option.id}>
                                {optionLabel(option)}
                              </option>
                            ))}
                          </select>
                        ) : isBoolean ? (
                          <select
                            value={String(value)}
                            onChange={(event) =>
                              setForm((previous) => ({
                                ...previous,
                                [key]: event.target.value === "true",
                              }))
                            }
                          >
                            <option value="true">True</option>
                            <option value="false">False</option>
                          </select>
                        ) : isLong ? (
                          <textarea
                            rows={4}
                            value={
                              typeof value === "object"
                                ? JSON.stringify(value)
                                : (value ?? "")
                            }
                            onChange={(event) =>
                              setForm((previous) => ({
                                ...previous,
                                [key]: event.target.value,
                              }))
                            }
                          />
                        ) : (
                          <input
                            type={isDate ? "datetime-local" : "text"}
                            value={
                              typeof value === "object"
                                ? displayValue(value)
                                : (value ?? "")
                            }
                            onChange={(event) =>
                              setForm((previous) => ({
                                ...previous,
                                [key]: event.target.value,
                              }))
                            }
                          />
                        )}
                      </label>
                    );
                  })}
                </div>

                <div className="dashboard-modal-actions">
                  <button
                    className="dashboard-primary"
                    type="button"
                    onClick={saveItem}
                  >
                    Salvează
                  </button>
                  <button
                    className="dashboard-secondary"
                    type="button"
                    onClick={closeModal}
                  >
                    Anulează
                  </button>
                </div>
              </>
            )}
          </div>
        </div>
      )}
    </main>
  );
};
