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

type FilterMode = "and" | "or";
type FilterKey =
  | "category"
  | "location"
  | "organizer"
  | "participation"
  | "date"
  | "extra"
  | "sort";

type DescribedEntity = {
  id: number;
  name: string;
  description?: string | null;
};

type OrganizerEntity = DescribedEntity & {
  link?: string | null;
  organizer_type?: DescribedEntity | null;
};

type LocationEntity = DescribedEntity & {
  address: string;
  building?: string | null;
  room?: string | null;
};

type RawEventRecord = Record<string, unknown>;

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
  start_date: Date;
  end_date: Date;
  registered_count?: number;
  user_registration_status?: string | null;
  capacity?: number | null;
  registration_deadline?: Date;
  pricing_type?: string;
  access_policy?: string;
  is_free_entry: boolean;
  requires_registration: boolean;
  requires_ticket: boolean;
  qr_code?: string | null;
  max_files?: number | null;
  max_file_size_mb?: number | null;
  validated_by?: string | number | null;
  validated_at?: Date;
  created_at?: Date;
  updated_at?: Date;
  is_favorite?: boolean;
};

type FeedbackItem = {
  id: number;
  user?: number;
  username?: string;
  event?: number;
  rating: number;
  comment: string;
  created_at?: string;
  updated_at?: string;
};

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
    `DTSTART:${toIcsStamp(event.start_date)}`,
    `DTEND:${toIcsStamp(event.end_date)}`,
    `UID:unievents-${event.id}@usv.ro`,
    "END:VEVENT",
    "END:VCALENDAR",
  ].join("\n");

  return `data:text/calendar;charset=utf-8,${encodeURIComponent(payload)}`;
};

const toCalendarEvent = (event: EventItem) => ({
  ...event,
  start: event.start_date,
  end: event.end_date,
});

const withDescriptionTitle = (entity?: { description?: string | null }) =>
  entity?.description ? { title: entity.description } : {};

const formatOptionalDateTime = (value?: Date) =>
  value ? formatDateTime(value) : "N/A";

const formatPricingType = (value?: string) =>
  value === "paid" ? "Plătit" : "Gratuit";

const formatAccessPolicy = (value?: string) => {
  switch (value) {
    case "registration":
      return "Necesită înscriere";
    case "ticket":
      return "Necesită bilet";
    case "registration_ticket":
      return "Necesită înscriere și bilet";
    default:
      return "Acces deschis";
  }
};

const formatLinkText = (value: string) => {
  try {
    return new URL(value).hostname.replace(/^www\./, "");
  } catch {
    return value;
  }
};

const getMediaUrl = (value?: string | null) => {
  if (!value) return "";

  if (value.startsWith("http")) {
    return value;
  }

  if (value.startsWith("/media/")) {
    return `${import.meta.env.VITE_API}${value}`;
  }

  return `${import.meta.env.VITE_API}/media/${value}`;
};

export const HomeComponent = () => {
  const [view, setView] = useState<View>(Views.MONTH);
  const [currentDate, setCurrentDate] = useState(() => new Date());
  const [selectedCategory, setSelectedCategory] = useState("Toate");
  const [selectedLocation, setSelectedLocation] = useState("Toate");
  const [selectedOrganizer, setSelectedOrganizer] = useState("Toți");
  const [selectedParticipation, setSelectedParticipation] = useState("Toate");
  const [selectedDateFilter, setSelectedDateFilter] = useState("Toate");
  const [selectedExtraFilter, setSelectedExtraFilter] = useState("Toate");
  const [sortOption, setSortOption] = useState("Data apropiată");
  const [filterMode, setFilterMode] = useState<FilterMode>("and");
  const [events, setEvents] = useState<EventItem[]>([]);
  const [selectedEventId, setSelectedEventId] = useState<number | null>(null);
  const [modalOpen, setModalOpen] = useState(false);
  const [categoriesList, setCategoriesList] = useState<DescribedEntity[]>([]);
  const [locationsList, setLocationsList] = useState<
    { id: number; name: string }[]
  >([]);
  const [organizersList, setOrganizersList] = useState<
    { id: number; name: string }[]
  >([]);
  const [participationTypesList, setParticipationTypesList] = useState<
    DescribedEntity[]
  >([]);
  const [activeFilter, setActiveFilter] = useState<FilterKey | null>(null);
  const [filterSearch, setFilterSearch] = useState("");
  const [feedbacks, setFeedbacks] = useState<FeedbackItem[]>([]);
  const [feedbackRating, setFeedbackRating] = useState(5);
  const [feedbackComment, setFeedbackComment] = useState("");
  const [feedbackLoading, setFeedbackLoading] = useState(false);
  const [feedbackMessage, setFeedbackMessage] = useState("");
  const [registrationLoading, setRegistrationLoading] = useState(false);
  const [registrationMessage, setRegistrationMessage] = useState("");
  const [favoriteEventIds, setFavoriteEventIds] = useState<Set<number>>(
    () => new Set(),
  );
  const [favoriteLoading, setFavoriteLoading] = useState(false);
  const [favoriteMessage, setFavoriteMessage] = useState("");

  const categories = ["Toate", ...categoriesList.map((c) => c.name)];
  const locations = ["Toate", ...locationsList.map((l) => l.name)];
  const organizers = ["Toți", ...organizersList.map((o) => o.name)];
  const participations = [
    "Toate",
    ...participationTypesList.map((p) => p.name),
  ];
  const dateFilters = ["Toate", "Azi", "Săptămâna aceasta", "Luna aceasta"];
  const extraFilters = [
    "Toate",
    "Intrare liberă",
    "Necesită înscriere",
    "Are cod QR",
  ];
  const sortOptions = [
    "Data apropiată",
    "Data îndepărtată",
    "Alfabetic A-Z",
    "Alfabetic Z-A",
  ];

  const filterConfigs: Record<
    FilterKey,
    {
      title: string;
      label: string;
      value: string;
      options: string[];
      onSelect: (value: string) => void;
    }
  > = {
    category: {
      title: "Alege categoria",
      label: "Categorie",
      value: selectedCategory,
      options: categories,
      onSelect: setSelectedCategory,
    },
    location: {
      title: "Alege locația",
      label: "Locație",
      value: selectedLocation,
      options: locations,
      onSelect: setSelectedLocation,
    },
    organizer: {
      title: "Alege organizatorul",
      label: "Organizator",
      value: selectedOrganizer,
      options: organizers,
      onSelect: setSelectedOrganizer,
    },
    participation: {
      title: "Alege tipul de participare",
      label: "Participare",
      value: selectedParticipation,
      options: participations,
      onSelect: setSelectedParticipation,
    },
    date: {
      title: "Alege perioada",
      label: "Perioada",
      value: selectedDateFilter,
      options: dateFilters,
      onSelect: setSelectedDateFilter,
    },
    extra: {
      title: "Alege filtrul suplimentar",
      label: "Filtru suplimentar",
      value: selectedExtraFilter,
      options: extraFilters,
      onSelect: setSelectedExtraFilter,
    },
    sort: {
      title: "Alege sortarea",
      label: "Sortare",
      value: sortOption,
      options: sortOptions,
      onSelect: setSortOption,
    },
  };

  const currentFilterConfig = activeFilter ? filterConfigs[activeFilter] : null;
  const visibleFilterOptions = currentFilterConfig
    ? currentFilterConfig.options.filter((option) =>
        option.toLowerCase().includes(filterSearch.trim().toLowerCase()),
      )
    : [];

  const openFilterModal = (filter: FilterKey) => {
    setActiveFilter(filter);
    setFilterSearch("");
  };

  const closeFilterModal = () => {
    setActiveFilter(null);
    setFilterSearch("");
  };

  const selectFilterOption = (value: string) => {
    currentFilterConfig?.onSelect(value);
    closeFilterModal();
  };

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const token = localStorage.getItem("access");

        const res = await fetch(`${import.meta.env.VITE_API}/api/events/`, {
          headers: token
            ? {
                Authorization: `Bearer ${token}`,
              }
            : {},
        });

        if (!res.ok) {
          console.error("Failed to fetch events", res.status);
          return;
        }
        const data = (await res.json()) as RawEventRecord[];
        const normalizeEntity = (value: unknown, fallbackName = "N/A") =>
          value && typeof value === "object"
            ? value
            : { id: value ?? 0, name: fallbackName };

        const mapped: EventItem[] = data.map((e: RawEventRecord) => ({
          id: Number(e.id ?? 0),
          name: String(e.name ?? ""),
          description: String(e.description ?? ""),
          registration_link:
            typeof e.registration_link === "string"
              ? e.registration_link
              : null,
          online_link: typeof e.online_link === "string" ? e.online_link : null,
          organizer: normalizeEntity(
            e.organizer,
            String(e.organizer_name ?? "N/A"),
          ) as OrganizerEntity,
          location:
            e.location && typeof e.location === "object"
              ? (e.location as LocationEntity)
              : {
                  id: Number(e.location ?? 0),
                  name: String(e.location_name ?? "N/A"),
                  address: String(e.location_address ?? "N/A"),
                },
          category: normalizeEntity(
            e.category,
            String(e.category_name ?? "N/A"),
          ) as DescribedEntity,
          participation_type: normalizeEntity(
            e.participation_type,
            String(e.participation_type_name ?? "N/A"),
          ) as DescribedEntity,
          status: normalizeEntity(
            e.status,
            String(e.status_name ?? "N/A"),
          ) as DescribedEntity,
          start_date: new Date(String(e.start_date)),
          end_date: new Date(String(e.end_date)),
          capacity: typeof e.capacity === "number" ? e.capacity : null,
          registered_count:
            typeof e.registered_count === "number" ? e.registered_count : 0,
          user_registration_status:
            typeof e.user_registration_status === "string"
              ? e.user_registration_status
              : null,
          registration_deadline: e.registration_deadline
            ? new Date(String(e.registration_deadline))
            : undefined,
          pricing_type:
            typeof e.pricing_type === "string" ? e.pricing_type : undefined,
          access_policy:
            typeof e.access_policy === "string" ? e.access_policy : undefined,
          is_free_entry: Boolean(e.is_free_entry ?? true),
          requires_registration: Boolean(e.requires_registration ?? false),
          requires_ticket: Boolean(e.requires_ticket ?? false),
          qr_code: typeof e.qr_code === "string" ? e.qr_code : null,
          max_files: typeof e.max_files === "number" ? e.max_files : undefined,
          max_file_size_mb:
            typeof e.max_file_size_mb === "number"
              ? e.max_file_size_mb
              : undefined,
          validated_by:
            e.validated_by && typeof e.validated_by === "object"
              ? ((e.validated_by as { username?: string }).username ??
                undefined)
              : typeof e.validated_by === "string" ||
                  typeof e.validated_by === "number"
                ? e.validated_by
                : undefined,
          validated_at: e.validated_at
            ? new Date(String(e.validated_at))
            : undefined,
          created_at: e.created_at ? new Date(String(e.created_at)) : undefined,
          updated_at: e.updated_at ? new Date(String(e.updated_at)) : undefined,
        }));

        setEvents(mapped);
        if (mapped.length > 0) setSelectedEventId((id) => id ?? mapped[0].id);
      } catch (err) {
        console.error(err);
      }
    };

    fetchEvents();
  }, []);

  useEffect(() => {
    const fetchLists = async () => {
      try {
        const base = import.meta.env.VITE_API;
        const endpoints = [
          `${base}/api/categories/`,
          `${base}/api/locations/`,
          `${base}/api/organizers/`,
          `${base}/api/participation-types/`,
        ];

        const results = await Promise.all(
          endpoints
            .map((url) => fetch(url).then((r) => (r.ok ? r.json() : [])))
            .map((p) => p.catch(() => [] as RawEventRecord[])),
        );

        const [cat, loc, org, part] = results;

        setCategoriesList(Array.isArray(cat) ? cat : []);
        setLocationsList(Array.isArray(loc) ? loc : []);
        setOrganizersList(Array.isArray(org) ? org : []);
        setParticipationTypesList(Array.isArray(part) ? part : []);
      } catch (err) {
        console.error("Failed to fetch filter lists", err);
      }
    };

    fetchLists();
  }, []);

  useEffect(() => {
    const fetchFavoriteEvents = async () => {
      try {
        const token = localStorage.getItem("access");

        const res = await fetch(
          `${import.meta.env.VITE_API}/api/my-favorite-events/`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          },
        );

        if (!res.ok) {
          console.error("Failed to fetch favorite events", res.status);
          return;
        }

        const data = await res.json();

        const ids = new Set<number>(
          data
            .map((favorite: any) => favorite.event?.id)
            .filter((id: unknown): id is number => typeof id === "number"),
        );

        setFavoriteEventIds(ids);
      } catch (err) {
        console.error(err);
      }
    };

    fetchFavoriteEvents();
  }, []);

  const filteredEvents = useMemo(() => {
    return events.filter((event) => {
      const now = new Date();

      const isToday = event.start_date.toDateString() === now.toDateString();

      const startOfWeek = moment().startOf("week");
      const endOfWeek = moment().endOf("week");

      const isThisWeek = moment(event.start_date).isBetween(
        startOfWeek,
        endOfWeek,
        undefined,
        "[]",
      );

      const isThisMonth =
        event.start_date.getMonth() === now.getMonth() &&
        event.start_date.getFullYear() === now.getFullYear();

      const matchesDate =
        selectedDateFilter === "Toate" ||
        (selectedDateFilter === "Azi" && isToday) ||
        (selectedDateFilter === "Săptămâna aceasta" && isThisWeek) ||
        (selectedDateFilter === "Luna aceasta" && isThisMonth);

      const matchesExtra =
        selectedExtraFilter === "Toate" ||
        (selectedExtraFilter === "Intrare liberă" && event.is_free_entry) ||
        (selectedExtraFilter === "Necesită înscriere" &&
          event.requires_registration) ||
        (selectedExtraFilter === "Are cod QR" && Boolean(event.qr_code));

      const checks = [
        selectedCategory === "Toate" ||
          event.category?.name === selectedCategory,
        selectedLocation === "Toate" ||
          event.location?.name === selectedLocation,
        selectedOrganizer === "Toți" ||
          event.organizer?.name === selectedOrganizer,
        selectedParticipation === "Toate" ||
          event.participation_type.name === selectedParticipation,
        matchesDate,
        matchesExtra,
      ];

      return filterMode === "and"
        ? checks.every(Boolean)
        : checks.some(Boolean);
    });
  }, [
    filterMode,
    selectedCategory,
    selectedLocation,
    selectedOrganizer,
    selectedParticipation,
    selectedDateFilter,
    selectedExtraFilter,
    events,
  ]);

  const sortedEvents = useMemo(() => {
    const sorted = [...filteredEvents];

    switch (sortOption) {
      case "Data îndepărtată":
        sorted.sort((a, b) => b.start_date.getTime() - a.start_date.getTime());
        break;

      case "Alfabetic A-Z":
        sorted.sort((a, b) => a.name.localeCompare(b.name));
        break;

      case "Alfabetic Z-A":
        sorted.sort((a, b) => b.name.localeCompare(a.name));
        break;

      default:
        sorted.sort((a, b) => a.start_date.getTime() - b.start_date.getTime());
    }

    return sorted;
  }, [filteredEvents, sortOption]);

  const calendarEvents = useMemo(
    () => sortedEvents.map(toCalendarEvent),
    [sortedEvents],
  );

  const selectedEvent = useMemo(
    () => events.find((event) => event.id === selectedEventId) ?? null,
    [selectedEventId, events],
  );

  const canLeaveFeedback = selectedEvent
    ? new Date() >= selectedEvent.end_date
    : false;

  const averageRating =
    feedbacks.length > 0
      ? feedbacks.reduce((sum, feedback) => sum + feedback.rating, 0) /
        feedbacks.length
      : 0;

  const isRegistered = selectedEvent?.user_registration_status === "Acceptat";

  const isWaiting =
    selectedEvent?.user_registration_status === "Lista de asteptare";

  const openDetails = (event: EventItem) => {
    setSelectedEventId(event.id);
    setModalOpen(true);
  };

  const closeDetails = () => setModalOpen(false);

  const fetchFeedbacks = async (eventId: number) => {
    try {
      const token = localStorage.getItem("access");

      const res = await fetch(
        `${import.meta.env.VITE_API}/api/events/${eventId}/feedbacks/`,
        {
          headers: token
            ? {
                Authorization: `Bearer ${token}`,
              }
            : {},
        },
      );

      if (!res.ok) {
        console.error("Failed to fetch feedbacks", res.status);
        return;
      }

      const data = (await res.json()) as FeedbackItem[];
      setFeedbacks(data);
    } catch (err) {
      console.error(err);
    }
  };

  const submitFeedback = async () => {
    if (!selectedEvent) return;

    setFeedbackLoading(true);
    setFeedbackMessage("");

    try {
      const token = localStorage.getItem("access");

      const res = await fetch(
        `${import.meta.env.VITE_API}/api/events/${selectedEvent.id}/feedback/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            ...(token ? { Authorization: `Bearer ${token}` } : {}),
          },
          body: JSON.stringify({
            rating: feedbackRating,
            comment: feedbackComment.trim(),
          }),
        },
      );

      const data = await res.json();

      if (!res.ok) {
        setFeedbackMessage(data.error || "Nu s-a putut trimite feedback-ul.");
        return;
      }

      setFeedbackMessage("Feedback trimis cu succes.");
      setFeedbackComment("");
      setFeedbackRating(5);
      await fetchFeedbacks(selectedEvent.id);
    } catch (err) {
      console.error(err);
      setFeedbackMessage("A apărut o eroare la trimiterea feedback-ului.");
    } finally {
      setFeedbackLoading(false);
    }
  };

  const registerToEvent = async () => {
    if (!selectedEvent) return;

    setRegistrationLoading(true);
    setRegistrationMessage("");

    try {
      const token = localStorage.getItem("access");

      const res = await fetch(
        `${import.meta.env.VITE_API}/api/events/${selectedEvent.id}/register/`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      const data = await res.json();

      const newStatus = data.status_name;

      if (!res.ok) {
        setRegistrationMessage(
          data.error || "Nu s-a putut realiza înscrierea.",
        );
        return;
      }

      const updatedEvents = events.map((event) => {
        if (event.id !== selectedEvent.id) return event;

        return {
          ...event,
          user_registration_status: newStatus,
          registered_count:
            newStatus === "Acceptat"
              ? (event.registered_count ?? 0) + 1
              : event.registered_count,
        };
      });

      setEvents(updatedEvents);

      setRegistrationMessage(
        newStatus === "Lista de asteptare"
          ? "Ai fost adăugat în lista de așteptare."
          : "Înscriere realizată cu succes.",
      );
    } catch (err) {
      console.error(err);
      setRegistrationMessage("A apărut o eroare.");
    } finally {
      setRegistrationLoading(false);
    }
  };

  const cancelRegistration = async () => {
    if (!selectedEvent) return;

    setRegistrationLoading(true);
    setRegistrationMessage("");

    try {
      const token = localStorage.getItem("access");

      const res = await fetch(
        `${import.meta.env.VITE_API}/api/events/${selectedEvent.id}/cancel-registration/`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      const data = await res.json();

      if (!res.ok) {
        setRegistrationMessage(data.error || "Nu s-a putut anula înscrierea.");
        return;
      }

      const updatedEvents = events.map((event) => {
        if (event.id !== selectedEvent.id) return event;

        return {
          ...event,
          user_registration_status: "Anulat",
          registered_count: Math.max((event.registered_count ?? 1) - 1, 0),
        };
      });

      setEvents(updatedEvents);

      setRegistrationMessage("Înscriere anulată.");
    } catch (err) {
      console.error(err);
      setRegistrationMessage("A apărut o eroare.");
    } finally {
      setRegistrationLoading(false);
    }
  };

  const toggleFavorite = async () => {
    if (!selectedEvent) return;

    setFavoriteLoading(true);
    setFavoriteMessage("");

    const token = localStorage.getItem("access");
    const isFavorite = favoriteEventIds.has(selectedEvent.id);

    try {
      const res = await fetch(
        isFavorite
          ? `${import.meta.env.VITE_API}/api/events/${selectedEvent.id}/favorite/remove/`
          : `${import.meta.env.VITE_API}/api/events/${selectedEvent.id}/favorite/`,
        {
          method: isFavorite ? "DELETE" : "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      if (!res.ok && res.status !== 204) {
        setFavoriteMessage("Nu s-a putut actualiza lista de favorite.");
        return;
      }

      setFavoriteEventIds((previous) => {
        const next = new Set(previous);

        if (isFavorite) {
          next.delete(selectedEvent.id);
        } else {
          next.add(selectedEvent.id);
        }

        return next;
      });

      setFavoriteMessage(
        isFavorite
          ? "Eveniment eliminat de la favorite."
          : "Eveniment adăugat la favorite. Ai primit și un email de confirmare.",
      );
    } catch (err) {
      console.error(err);
      setFavoriteMessage("A apărut o eroare.");
    } finally {
      setFavoriteLoading(false);
    }
  };

  useEffect(() => {
    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        closeDetails();
        closeFilterModal();
      }
    };

    window.addEventListener("keydown", handleEscape);
    return () => window.removeEventListener("keydown", handleEscape);
  }, []);

  useEffect(() => {
    if (!modalOpen || !selectedEvent) return;

    fetchFeedbacks(selectedEvent.id);
    setFeedbackMessage("");
    setFeedbackComment("");
    setFeedbackRating(5);
  }, [modalOpen, selectedEvent]);

  return (
    <main className="home-shell">
      <aside className="home-sidebar">
        <div className="sidebar-section">
          <div className="sidebar-section-head">
            <h2>Filtre</h2>
            <span>Combinație {filterMode.toUpperCase()}</span>
          </div>

          <div className="filter-stack">
            <div className="filter-picker-field">
              <span>Categorie</span>
              <button
                type="button"
                className="filter-picker-button"
                onClick={() => openFilterModal("category")}
              >
                <span>{selectedCategory}</span>
                <span aria-hidden="true">⌄</span>
              </button>
            </div>

            <div className="filter-picker-field">
              <span>Locație</span>
              <button
                type="button"
                className="filter-picker-button"
                onClick={() => openFilterModal("location")}
              >
                <span>{selectedLocation}</span>
                <span aria-hidden="true">⌄</span>
              </button>
            </div>

            <div className="filter-picker-field">
              <span>Organizator</span>
              <button
                type="button"
                className="filter-picker-button"
                onClick={() => openFilterModal("organizer")}
              >
                <span>{selectedOrganizer}</span>
                <span aria-hidden="true">⌄</span>
              </button>
            </div>

            <div className="filter-picker-field">
              <span>Participare</span>
              <button
                type="button"
                className="filter-picker-button"
                onClick={() => openFilterModal("participation")}
              >
                <span>{selectedParticipation}</span>
                <span aria-hidden="true">⌄</span>
              </button>
            </div>

            <div className="filter-picker-field">
              <span>Perioada</span>

              <button
                type="button"
                className="filter-picker-button"
                onClick={() => openFilterModal("date")}
              >
                <span>{selectedDateFilter}</span>
                <span aria-hidden="true">⌄</span>
              </button>
            </div>

            <div className="filter-picker-field">
              <span>Filtru suplimentar</span>

              <button
                type="button"
                className="filter-picker-button"
                onClick={() => openFilterModal("extra")}
              >
                <span>{selectedExtraFilter}</span>
                <span aria-hidden="true">⌄</span>
              </button>
            </div>

            <div className="filter-picker-field">
              <span>Sortare</span>

              <button
                type="button"
                className="filter-picker-button"
                onClick={() => openFilterModal("sort")}
              >
                <span>{sortOption}</span>
                <span aria-hidden="true">⌄</span>
              </button>
            </div>

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
            <span>{sortedEvents.length} rezultate</span>
          </div>

          <div className="event-list">
            {sortedEvents.map((event) => (
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
                  <span>{formatShortDate(event.start_date)}</span>
                </div>
                <p>{event.location.name}</p>
                <div className="event-list-bottom">
                  <span>{event.category.name}</span>
                  <span>{event.participation_type.name}</span>
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

      {currentFilterConfig && (
        <div className="filter-modal-backdrop" onClick={closeFilterModal}>
          <div
            className="filter-modal"
            onClick={(event) => event.stopPropagation()}
          >
            <div className="filter-modal-header">
              <div>
                <span className="modal-kicker">Filtrare</span>
                <h2>{currentFilterConfig.title}</h2>
              </div>
              <button
                type="button"
                className="modal-close"
                onClick={closeFilterModal}
              >
                ×
              </button>
            </div>

            <input
              className="filter-modal-search"
              type="search"
              value={filterSearch}
              onChange={(event) => setFilterSearch(event.target.value)}
              placeholder={`Caută în ${currentFilterConfig.label.toLowerCase()}...`}
              autoFocus
            />

            <div className="filter-modal-list">
              {visibleFilterOptions.length > 0 ? (
                visibleFilterOptions.map((option) => (
                  <button
                    key={option}
                    type="button"
                    className={
                      option === currentFilterConfig.value
                        ? "filter-modal-option active"
                        : "filter-modal-option"
                    }
                    onClick={() => selectFilterOption(option)}
                  >
                    <span>{option}</span>
                    {option === currentFilterConfig.value && <strong>✓</strong>}
                  </button>
                ))
              ) : (
                <p className="filter-modal-empty">Nu există rezultate.</p>
              )}
            </div>
          </div>
        </div>
      )}

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

                <button
                  type="button"
                  className={
                    favoriteEventIds.has(selectedEvent.id)
                      ? "favorite-button active"
                      : "favorite-button"
                  }
                  disabled={favoriteLoading}
                  onClick={toggleFavorite}
                >
                  {favoriteLoading
                    ? "Se procesează..."
                    : favoriteEventIds.has(selectedEvent.id)
                      ? "★ Elimină de la favorite"
                      : "☆ Adaugă la favorite"}
                </button>

                {favoriteMessage && (
                  <p className="favorite-message">{favoriteMessage}</p>
                )}
              </div>
              <button
                type="button"
                className="modal-close"
                onClick={closeDetails}
              >
                ×
              </button>
            </div>

            <div className="modal-description-block">
              <span className="modal-section-label">Descriere</span>
              <p className="modal-description">{selectedEvent.description}</p>
            </div>

            <div className="modal-sections">
              <section className="modal-card modal-card--wide">
                <div className="modal-card-head">
                  <div>
                    <span className="modal-card-kicker">Perioadă</span>
                    <h3>Intervalul evenimentului</h3>
                  </div>
                  <span className="modal-card-note">Când are loc</span>
                </div>
                <div className="modal-card-grid modal-card-grid--two">
                  <div className="modal-field">
                    <span>Începe</span>
                    <strong>{formatDateTime(selectedEvent.start_date)}</strong>
                  </div>
                  <div className="modal-field">
                    <span>Se termină</span>
                    <strong>{formatDateTime(selectedEvent.end_date)}</strong>
                  </div>
                  <div className="modal-field">
                    <span>Termen înscriere</span>
                    <strong>
                      {formatOptionalDateTime(
                        selectedEvent.registration_deadline,
                      )}
                    </strong>
                  </div>
                </div>
                <div className="event-registration">
                  <div className="event-registration-info">
                    <strong>
                      {selectedEvent.registered_count ?? 0}
                      {selectedEvent.capacity
                        ? ` / ${selectedEvent.capacity}`
                        : ""}{" "}
                      participanți
                    </strong>

                    {isRegistered && (
                      <span className="registration-status confirmed">
                        Înscris
                      </span>
                    )}

                    {isWaiting && (
                      <span className="registration-status waiting">
                        Lista de așteptare
                      </span>
                    )}
                  </div>

                  {registrationMessage && (
                    <p className="registration-message">
                      {registrationMessage}
                    </p>
                  )}

                  {isRegistered || isWaiting ? (
                    <button
                      type="button"
                      className="registration-button cancel"
                      disabled={registrationLoading}
                      onClick={cancelRegistration}
                    >
                      {registrationLoading
                        ? "Se procesează..."
                        : "Renunță la înscriere"}
                    </button>
                  ) : (
                    <button
                      type="button"
                      className="registration-button"
                      disabled={registrationLoading}
                      onClick={registerToEvent}
                    >
                      {registrationLoading ? "Se procesează..." : "Înscrie-te"}
                    </button>
                  )}
                </div>
              </section>

              <section className="modal-card">
                <div className="modal-card-head">
                  <div>
                    <span className="modal-card-kicker">Unde</span>
                    <h3>Locație și organizator</h3>
                  </div>
                </div>
                <div className="modal-card-grid">
                  <div
                    className="modal-field"
                    {...withDescriptionTitle(selectedEvent.location)}
                  >
                    <span>Locație</span>
                    <strong>
                      {selectedEvent.location.name}
                      {selectedEvent.location.room &&
                        `, Sala ${selectedEvent.location.room}`}
                    </strong>
                  </div>
                  <div
                    className="modal-field"
                    {...withDescriptionTitle(selectedEvent.organizer)}
                  >
                    <span>Organizator</span>
                    <strong>{selectedEvent.organizer.name}</strong>
                  </div>
                </div>
              </section>

              <section className="modal-card">
                <div className="modal-card-head">
                  <div>
                    <span className="modal-card-kicker">Participare</span>
                    <h3>Acces și tip eveniment</h3>
                  </div>
                </div>
                <div className="modal-card-grid">
                  <div
                    className="modal-field"
                    {...withDescriptionTitle(selectedEvent.category)}
                  >
                    <span>Categorie</span>
                    <strong>{selectedEvent.category.name}</strong>
                  </div>
                  <div
                    className="modal-field"
                    {...withDescriptionTitle(selectedEvent.participation_type)}
                  >
                    <span>Tip participare</span>
                    <strong>{selectedEvent.participation_type.name}</strong>
                  </div>
                  <div
                    className="modal-field"
                    {...withDescriptionTitle(selectedEvent.status)}
                  >
                    <span>Stare eveniment</span>
                    <strong>{selectedEvent.status.name}</strong>
                  </div>
                  <div className="modal-field">
                    <span>Capacitate</span>
                    <strong>{selectedEvent.capacity ?? "N/A"}</strong>
                  </div>
                  <div className="modal-field">
                    <span>Tip intrare</span>
                    <strong>
                      {formatPricingType(selectedEvent.pricing_type)}
                    </strong>
                  </div>
                  <div className="modal-field">
                    <span>Mod acces</span>
                    <strong>
                      {formatAccessPolicy(selectedEvent.access_policy)}
                    </strong>
                  </div>
                  <div className="modal-field modal-field--qr">
                    <span>Cod QR</span>
                    {selectedEvent.qr_code ? (
                      <>
                        {console.log("QR RAW:", selectedEvent.qr_code)}
                        {console.log(
                          "QR URL:",
                          getMediaUrl(selectedEvent.qr_code),
                        )}

                        <a
                          href={getMediaUrl(selectedEvent.qr_code)}
                          target="_blank"
                          rel="noreferrer"
                        >
                          <img
                            className="event-qr-code"
                            src={getMediaUrl(selectedEvent.qr_code)}
                            alt={`QR ${selectedEvent.name}`}
                          />
                        </a>
                      </>
                    ) : (
                      <strong>N/A</strong>
                    )}
                  </div>
                </div>
              </section>

              <section className="modal-card">
                <div className="modal-card-head">
                  <div>
                    <span className="modal-card-kicker">Linkuri</span>
                    <h3>Acces rapid</h3>
                  </div>
                </div>
                <div className="modal-card-grid">
                  <div className="modal-field">
                    <span>Înscriere</span>
                    <strong>
                      {selectedEvent.registration_link ? (
                        <a
                          className="modal-link"
                          href={selectedEvent.registration_link}
                          target="_blank"
                          rel="noreferrer"
                        >
                          {formatLinkText(selectedEvent.registration_link)}
                        </a>
                      ) : (
                        "N/A"
                      )}
                    </strong>
                  </div>
                  <div className="modal-field">
                    <span>Online</span>
                    <strong>
                      {selectedEvent.online_link ? (
                        <a
                          className="modal-link"
                          href={selectedEvent.online_link}
                          target="_blank"
                          rel="noreferrer"
                        >
                          {formatLinkText(selectedEvent.online_link)}
                        </a>
                      ) : (
                        "N/A"
                      )}
                    </strong>
                  </div>
                </div>
              </section>

              <section className="modal-card feedback-card">
                <div className="modal-card-head">
                  <div>
                    <span className="modal-card-kicker">Feedback</span>
                    <h3>Rating și comentarii</h3>
                  </div>

                  <span className="modal-card-note">
                    {feedbacks.length > 0
                      ? `${averageRating.toFixed(1)} / 5 din ${feedbacks.length} review-uri`
                      : "Fără review-uri"}
                  </span>
                </div>

                {canLeaveFeedback ? (
                  <div className="feedback-form">
                    <div className="feedback-stars">
                      {[1, 2, 3, 4, 5].map((star) => (
                        <button
                          key={star}
                          type="button"
                          className={
                            star <= feedbackRating
                              ? "feedback-star active"
                              : "feedback-star"
                          }
                          onClick={() => setFeedbackRating(star)}
                        >
                          ★
                        </button>
                      ))}
                    </div>

                    <textarea
                      className="feedback-textarea"
                      value={feedbackComment}
                      onChange={(event) =>
                        setFeedbackComment(event.target.value)
                      }
                      placeholder="Scrie părerea ta despre eveniment..."
                      rows={4}
                    />

                    {feedbackMessage && (
                      <p className="feedback-message">{feedbackMessage}</p>
                    )}

                    <button
                      type="button"
                      className="feedback-submit"
                      onClick={submitFeedback}
                      disabled={feedbackLoading}
                    >
                      {feedbackLoading ? "Se trimite..." : "Trimite feedback"}
                    </button>
                  </div>
                ) : (
                  <p className="feedback-unavailable">
                    Feedback-ul poate fi oferit doar după finalizarea
                    evenimentului.
                  </p>
                )}

                <div className="feedback-list">
                  {feedbacks.length > 0 ? (
                    feedbacks.map((feedback) => (
                      <article key={feedback.id} className="feedback-item">
                        <div className="feedback-item-header">
                          <strong>{feedback.username || "Utilizator"}</strong>
                          <span>{"★".repeat(feedback.rating)}</span>
                        </div>

                        {feedback.comment && <p>{feedback.comment}</p>}

                        {feedback.created_at && (
                          <small>
                            {new Intl.DateTimeFormat("ro-RO", {
                              dateStyle: "medium",
                              timeStyle: "short",
                            }).format(new Date(feedback.created_at))}
                          </small>
                        )}
                      </article>
                    ))
                  ) : (
                    <p className="feedback-empty">
                      Nu există feedback pentru acest eveniment încă.
                    </p>
                  )}
                </div>
              </section>

              <section className="modal-card modal-card--subtle">
                <div className="modal-card-head">
                  <div>
                    <span className="modal-card-kicker">Istoric</span>
                    <h3>Metadate</h3>
                  </div>
                </div>
                <div className="modal-card-grid modal-card-grid--two">
                  <div className="modal-field">
                    <span>Creat la</span>
                    <strong>
                      {formatOptionalDateTime(selectedEvent.created_at)}
                    </strong>
                  </div>
                  <div className="modal-field">
                    <span>Actualizat la</span>
                    <strong>
                      {formatOptionalDateTime(selectedEvent.updated_at)}
                    </strong>
                  </div>
                </div>
              </section>
            </div>

            <div className="modal-actions">
              {selectedEvent.registration_link && (
                <a
                  className="modal-primary"
                  href={selectedEvent.registration_link}
                  target="_blank"
                  rel="noreferrer"
                >
                  Website eveniment
                </a>
              )}
              <a
                className="modal-secondary"
                href={`https://calendar.google.com/calendar/render?action=TEMPLATE&text=${encodeURIComponent(selectedEvent.name)}&dates=${moment(selectedEvent.start_date).format("YYYYMMDDTHHmmss")}/${moment(selectedEvent.end_date).format("YYYYMMDDTHHmmss")}&details=${encodeURIComponent(selectedEvent.description)}&location=${encodeURIComponent(selectedEvent.location.name)}`}
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
          </div>
        </div>
      )}
    </main>
  );
};
