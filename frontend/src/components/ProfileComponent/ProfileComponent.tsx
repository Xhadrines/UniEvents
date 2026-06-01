import { useEffect, useMemo, useState } from "react";

import "./ProfileComponent.css";

type NamedEntity = {
  id: number;
  name: string;
  faculty?: number;
};

type FavoriteItem = {
  id: number;
  event: {
    id: number;
    name: string;
    description?: string;
    start_date?: string;
    location?: {
      name?: string;
    };
  };
};

type NotificationItem = {
  id: number;
  title: string;
  message: string;
  is_read: boolean;
  created_at?: string;
};

type UserDetails = {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  date_joined: string;
};

export const ProfileComponent = () => {
  const [favorites, setFavorites] = useState<FavoriteItem[]>([]);
  const [notifications, setNotifications] = useState<NotificationItem[]>([]);

  const [roles, setRoles] = useState<NamedEntity[]>([]);
  const [statuses, setStatuses] = useState<NamedEntity[]>([]);
  const [faculties, setFaculties] = useState<NamedEntity[]>([]);
  const [specializations, setSpecializations] = useState<NamedEntity[]>([]);

  const [user, setUser] = useState(() => {
    const storedUser = localStorage.getItem("user");
    return storedUser ? JSON.parse(storedUser) : {};
  });

  const [userDetails, setUserDetails] = useState<UserDetails | null>(null);

  const profile = user.profile || {};

  const [editOpen, setEditOpen] = useState(false);
  const [editUsername, setEditUsername] = useState("");
  const [editFirstName, setEditFirstName] = useState("");
  const [editLastName, setEditLastName] = useState("");
  const [editFacultyId, setEditFacultyId] = useState<number | null>(null);
  const [editSpecializationId, setEditSpecializationId] = useState<
    number | null
  >(null);
  const [editStudyYear, setEditStudyYear] = useState("");
  const [editGroup, setEditGroup] = useState("");
  const [editSemiGroup, setEditSemiGroup] = useState("");
  const [editMessage, setEditMessage] = useState("");
  const [editLoading, setEditLoading] = useState(false);

  const [passwordResetLoading, setPasswordResetLoading] = useState(false);

  const [adminMessage, setAdminMessage] = useState("");
  const [adminRequestMessage, setAdminRequestMessage] = useState("");
  const [adminRequestLoading, setAdminRequestLoading] = useState(false);

  const [feedbackPopup, setFeedbackPopup] = useState<{
    type: "success" | "error";
    title: string;
    message: string;
  } | null>(null);

  const getEntityName = (value: unknown, list: NamedEntity[]) => {
    if (!value) return "";

    if (typeof value === "object" && "name" in value) {
      return String((value as { name?: string }).name || "");
    }

    const id = Number(value);
    return list.find((item) => item.id === id)?.name || "";
  };

  const getEntityId = (value: unknown) => {
    if (!value) return null;

    if (typeof value === "object" && "id" in value) {
      return Number((value as { id?: number }).id);
    }

    return Number(value);
  };

  const roleName = useMemo(
    () => getEntityName(profile.role, roles),
    [profile.role, roles],
  );

  const statusName = useMemo(
    () => getEntityName(profile.status, statuses),
    [profile.status, statuses],
  );

  const facultyName = useMemo(
    () => getEntityName(profile.faculty, faculties),
    [profile.faculty, faculties],
  );

  const specializationName = useMemo(
    () => getEntityName(profile.specialization, specializations),
    [profile.specialization, specializations],
  );

  const isStudent = roleName.toLowerCase() === "student";
  const isAdministrator = roleName.toLowerCase() === "administrator";

  const filteredSpecializations = editFacultyId
    ? specializations.filter(
        (specialization) => specialization.faculty === editFacultyId,
      )
    : specializations;

  const authHeaders = (token?: string | null): Record<string, string> =>
    token ? { Authorization: `Bearer ${token}` } : {};

  useEffect(() => {
    const token = localStorage.getItem("access");

    const loadProfileData = async () => {
      const headers = authHeaders(token);

      const [
        favoritesRes,
        notificationsRes,
        rolesRes,
        statusesRes,
        facultiesRes,
        specializationsRes,
        userRes,
      ] = await Promise.all([
        fetch(`${import.meta.env.VITE_API}/api/my-favorite-events/`, {
          headers,
        }),
        fetch(`${import.meta.env.VITE_API}/api/my-notifications/`, { headers }),
        fetch(`${import.meta.env.VITE_API}/api/roles/`, { headers }),
        fetch(`${import.meta.env.VITE_API}/api/statuses/`, { headers }),
        fetch(`${import.meta.env.VITE_API}/api/faculties/`, { headers }),
        fetch(`${import.meta.env.VITE_API}/api/specializations/`, { headers }),
        fetch(`${import.meta.env.VITE_API}/api/users/${user.user_id}/`, {
          headers,
        }),
      ]);

      if (favoritesRes.ok) setFavorites(await favoritesRes.json());
      if (notificationsRes.ok) setNotifications(await notificationsRes.json());
      if (rolesRes.ok) setRoles(await rolesRes.json());
      if (statusesRes.ok) setStatuses(await statusesRes.json());
      if (facultiesRes.ok) setFaculties(await facultiesRes.json());
      if (specializationsRes.ok)
        setSpecializations(await specializationsRes.json());
      if (userRes.ok) {
        setUserDetails(await userRes.json());
      }
    };

    loadProfileData().catch(console.error);
  }, []);

  const openEditProfile = () => {
    setEditUsername(user.username || "");
    setEditFirstName(userDetails?.first_name || user.first_name || "");
    setEditLastName(userDetails?.last_name || user.last_name || "");

    setEditFacultyId(getEntityId(profile.faculty));
    setEditSpecializationId(getEntityId(profile.specialization));
    setEditStudyYear(profile.study_year ? String(profile.study_year) : "");
    setEditGroup(profile.group ? String(profile.group) : "");
    setEditSemiGroup(profile.semi_group || "");

    setEditMessage("");
    setEditOpen(true);
  };

  const handleFacultyChange = (value: string) => {
    const newFacultyId = value ? Number(value) : null;

    setEditFacultyId(newFacultyId);
    setEditSpecializationId(null);
  };

  const handleSpecializationChange = (value: string) => {
    const newSpecializationId = value ? Number(value) : null;

    setEditSpecializationId(newSpecializationId);

    const selectedSpecialization = specializations.find(
      (specialization) => specialization.id === newSpecializationId,
    );

    if (selectedSpecialization?.faculty) {
      setEditFacultyId(selectedSpecialization.faculty);
    }
  };

  const saveProfile = async () => {
    setEditLoading(true);
    setEditMessage("");

    try {
      const token = localStorage.getItem("access");

      const body: Record<string, unknown> = {
        username: editUsername.trim(),
        first_name: editFirstName.trim(),
        last_name: editLastName.trim(),
      };

      if (isStudent) {
        body.faculty = editFacultyId;
        body.specialization = editSpecializationId;
        body.study_year = editStudyYear ? Number(editStudyYear) : null;
        body.group = editGroup ? Number(editGroup) : null;
        body.semi_group = editSemiGroup || null;
      }

      const res = await fetch(
        `${import.meta.env.VITE_API}/api/my-profile/update/`,
        {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            ...authHeaders(token),
          },
          body: JSON.stringify(body),
        },
      );

      const data = await res.json();

      if (!res.ok) {
        setEditMessage(data.error || "Profilul nu a putut fi actualizat.");
        return;
      }

      localStorage.setItem("user", JSON.stringify(data));
      setUser(data);

      setUserDetails({
        id: Number(data.user_id),
        username: data.username,
        email: data.email,
        first_name: data.first_name,
        last_name: data.last_name,
        date_joined: data.date_joined,
      });

      setEditOpen(false);

      setFeedbackPopup({
        type: "success",
        title: "Profil actualizat",
        message: "Datele tale au fost salvate cu succes.",
      });
    } catch (err) {
      console.error(err);
      setEditMessage("A apărut o eroare.");
    } finally {
      setEditLoading(false);
    }
  };

  const requestPasswordReset = async () => {
    setEditMessage("");
    setPasswordResetLoading(true);

    try {
      const res = await fetch(
        `${import.meta.env.VITE_API}/api/password-reset/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: user.email,
          }),
        },
      );

      const data = await res.json();

      if (!res.ok) {
        setFeedbackPopup({
          type: "error",
          title: "Eroare",
          message: data.error || "Nu s-a putut trimite email-ul.",
        });

        return;
      }

      setEditOpen(false);

      setFeedbackPopup({
        type: "success",
        title: "Email trimis",
        message: data.message || "Emailul de resetare a parolei a fost trimis.",
      });
    } catch (err) {
      console.error(err);

      setFeedbackPopup({
        type: "error",
        title: "Eroare",
        message: "A apărut o eroare.",
      });
    } finally {
      setPasswordResetLoading(false);
    }
  };

  const sendAdminRequest = async () => {
    setAdminRequestLoading(true);
    setAdminRequestMessage("");

    try {
      const token = localStorage.getItem("access");

      const res = await fetch(
        `${import.meta.env.VITE_API}/api/admin-role-request/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            ...authHeaders(token),
          },
          body: JSON.stringify({
            message: adminMessage,
          }),
        },
      );

      const data = await res.json();

      if (!res.ok) {
        setAdminRequestMessage(data.error || "Cererea nu a putut fi trimisă.");
        return;
      }

      setAdminRequestMessage("Cererea a fost trimisă către administrator.");
      setAdminMessage("");
    } catch (err) {
      console.error(err);
      setAdminRequestMessage("A apărut o eroare.");
    } finally {
      setAdminRequestLoading(false);
    }
  };

  const markNotificationAsRead = async (notificationId: number) => {
    try {
      const token = localStorage.getItem("access");

      const res = await fetch(
        `${import.meta.env.VITE_API}/api/notifications/${notificationId}/read/`,
        {
          method: "POST",
          headers: authHeaders(token),
        },
      );

      if (!res.ok) {
        return;
      }

      setNotifications((previous) =>
        previous.map((notification) =>
          notification.id === notificationId
            ? {
                ...notification,
                is_read: true,
              }
            : notification,
        ),
      );
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <main className="profile-shell">
      <aside className="profile-sidebar">
        <section className="profile-section">
          <div className="profile-section-header">
            <h2>Profil</h2>

            <button
              type="button"
              className="profile-small-button"
              onClick={openEditProfile}
            >
              Editează
            </button>
          </div>

          <div className="profile-stack">
            <p>
              <strong>Nume:</strong>{" "}
              {userDetails?.last_name || user.last_name || "N/A"}
            </p>
            <p>
              <strong>Prenume:</strong>{" "}
              {userDetails?.first_name || user.first_name || "N/A"}
            </p>
            <p>
              <strong>Username:</strong> {user.username || "N/A"}
            </p>
            <p>
              <strong>Email:</strong> {user.email || "N/A"}
            </p>
            <p>
              <strong>Rol:</strong> {roleName || "N/A"}
            </p>
            <p>
              <strong>Status:</strong> {statusName || "N/A"}
            </p>
            <p>
              <strong>Alăturat la:</strong>{" "}
              {userDetails?.date_joined || user.date_joined
                ? new Date(
                    userDetails?.date_joined || user.date_joined,
                  ).toLocaleDateString("ro-RO")
                : "N/A"}
            </p>

            {isStudent && (
              <>
                <p>
                  <strong>Facultate:</strong> {facultyName || "N/A"}
                </p>
                <p>
                  <strong>Specializare:</strong> {specializationName || "N/A"}
                </p>
                <p>
                  <strong>An studiu:</strong> {profile.study_year || "N/A"}
                </p>
                <p>
                  <strong>Grupă:</strong> {profile.group || "N/A"}
                </p>
                <p>
                  <strong>Semigrupă:</strong> {profile.semi_group || "N/A"}
                </p>
              </>
            )}
          </div>
        </section>

        {!isStudent && !isAdministrator && (
          <section className="profile-section">
            <div className="profile-section-header">
              <h2>Cerere administrator</h2>
            </div>

            <div className="profile-stack">
              <textarea
                className="profile-textarea"
                rows={5}
                value={adminMessage}
                onChange={(event) => setAdminMessage(event.target.value)}
                placeholder="Scrie de ce vrei să devii sponsor sau organizator..."
              />

              {adminRequestMessage && (
                <p className="profile-message">{adminRequestMessage}</p>
              )}

              <button
                type="button"
                className="profile-button"
                disabled={adminRequestLoading || !adminMessage.trim()}
                onClick={sendAdminRequest}
              >
                {adminRequestLoading ? "Se trimite..." : "Trimite cererea"}
              </button>
            </div>
          </section>
        )}
      </aside>

      <section className="profile-main">
        <div className="profile-content">
          <section className="profile-card">
            <div className="profile-card-header">
              <div>
                <span className="profile-card-kicker">Favorite</span>
                <h3>Evenimente salvate</h3>
              </div>

              <span className="profile-card-note">
                {favorites.length} evenimente
              </span>
            </div>

            <div className="profile-list">
              {favorites.length > 0 ? (
                favorites.map((favorite) => (
                  <article key={favorite.id} className="profile-item">
                    <div className="profile-item-header">
                      <strong>{favorite.event.name}</strong>
                    </div>

                    <p>{favorite.event.description || "Fără descriere."}</p>

                    <small>
                      {favorite.event.start_date
                        ? new Date(favorite.event.start_date).toLocaleString(
                            "ro-RO",
                          )
                        : "Dată indisponibilă"}
                      {" · "}
                      {favorite.event.location?.name || "Locație indisponibilă"}
                    </small>
                  </article>
                ))
              ) : (
                <p className="profile-empty">Nu ai evenimente favorite încă.</p>
              )}
            </div>
          </section>

          <section className="profile-card">
            <div className="profile-card-header">
              <div>
                <span className="profile-card-kicker">Notificări</span>
                <h3>Remindere și mesaje</h3>
              </div>

              <span className="profile-card-note">
                {notifications.length} notificări
              </span>
            </div>

            <div className="profile-list">
              {notifications.length > 0 ? (
                notifications.map((notification) => (
                  <article
                    key={notification.id}
                    className={
                      notification.is_read
                        ? "profile-item notification-read"
                        : "profile-item notification-unread"
                    }
                    onClick={() => {
                      if (!notification.is_read) {
                        markNotificationAsRead(notification.id);
                      }
                    }}
                  >
                    <div className="profile-item-header">
                      <strong>{notification.title}</strong>

                      {!notification.is_read && (
                        <button
                          type="button"
                          className="notification-new-badge"
                          onClick={(event) => {
                            event.stopPropagation();
                            markNotificationAsRead(notification.id);
                          }}
                        >
                          Nou
                        </button>
                      )}
                    </div>

                    <p>{notification.message}</p>
                  </article>
                ))
              ) : (
                <p className="profile-empty">Nu ai notificări încă.</p>
              )}
            </div>
          </section>
        </div>
      </section>

      {editOpen && (
        <div
          className="profile-modal-backdrop"
          onClick={() => {
            if (!passwordResetLoading && !editLoading) {
              setEditOpen(false);
            }
          }}
        >
          <div
            className="profile-modal"
            onClick={(event) => event.stopPropagation()}
          >
            <div className="profile-modal-header">
              <div>
                <span className="profile-card-kicker">Editare</span>
                <h2>Modifică datele profilului</h2>
              </div>

              <button
                type="button"
                className="profile-modal-close"
                onClick={() => {
                  if (!passwordResetLoading && !editLoading) {
                    setEditOpen(false);
                  }
                }}
              >
                ×
              </button>
            </div>

            <div className="profile-form-grid">
              <label className="profile-form-field">
                <span>Prenume</span>
                <input
                  value={editFirstName}
                  onChange={(event) => setEditFirstName(event.target.value)}
                />
              </label>

              <label className="profile-form-field">
                <span>Nume</span>
                <input
                  value={editLastName}
                  onChange={(event) => setEditLastName(event.target.value)}
                />
              </label>

              <label className="profile-form-field">
                <span>Username</span>
                <input
                  value={editUsername}
                  onChange={(event) => setEditUsername(event.target.value)}
                />
              </label>

              <label className="profile-form-field">
                <span>Email</span>
                <input value={user.email || ""} disabled />
              </label>

              {isStudent && (
                <>
                  <label className="profile-form-field">
                    <span>Facultate</span>
                    <select
                      value={editFacultyId ?? ""}
                      onChange={(event) =>
                        handleFacultyChange(event.target.value)
                      }
                    >
                      <option value="">Selectează facultate</option>
                      {faculties.map((faculty) => (
                        <option key={faculty.id} value={faculty.id}>
                          {faculty.name}
                        </option>
                      ))}
                    </select>
                  </label>

                  <label className="profile-form-field">
                    <span>Specializare</span>
                    <select
                      value={editSpecializationId ?? ""}
                      onChange={(event) =>
                        handleSpecializationChange(event.target.value)
                      }
                    >
                      <option value="">Selectează specializare</option>
                      {filteredSpecializations.map((specialization) => (
                        <option
                          key={specialization.id}
                          value={specialization.id}
                        >
                          {specialization.name}
                        </option>
                      ))}
                    </select>
                  </label>

                  <label className="profile-form-field">
                    <span>An studiu</span>
                    <input
                      type="number"
                      value={editStudyYear}
                      onChange={(event) => setEditStudyYear(event.target.value)}
                    />
                  </label>

                  <label className="profile-form-field">
                    <span>Grupă</span>
                    <input
                      type="number"
                      value={editGroup}
                      onChange={(event) => setEditGroup(event.target.value)}
                    />
                  </label>

                  <label className="profile-form-field">
                    <span>Semigrupă</span>
                    <input
                      value={editSemiGroup}
                      onChange={(event) => setEditSemiGroup(event.target.value)}
                    />
                  </label>
                </>
              )}
            </div>

            {editMessage && <p className="profile-message">{editMessage}</p>}

            <div className="profile-modal-actions">
              <button
                type="button"
                className="profile-button"
                disabled={editLoading}
                onClick={saveProfile}
              >
                {editLoading ? "Se salvează..." : "Salvează modificările"}
              </button>

              <button
                type="button"
                className="profile-secondary-button"
                disabled={passwordResetLoading || editLoading}
                onClick={requestPasswordReset}
              >
                {passwordResetLoading
                  ? "Se trimite emailul..."
                  : "Trimite email resetare parolă"}
              </button>
            </div>
          </div>
        </div>
      )}

      {feedbackPopup && (
        <div
          className="profile-feedback-backdrop"
          onClick={() => setFeedbackPopup(null)}
        >
          <div
            className={`profile-feedback-modal ${feedbackPopup.type}`}
            onClick={(event) => event.stopPropagation()}
          >
            <div className="profile-feedback-icon">
              {feedbackPopup.type === "success" ? "✓" : "!"}
            </div>

            <h2>{feedbackPopup.title}</h2>
            <p>{feedbackPopup.message}</p>

            <button
              type="button"
              className="profile-button"
              onClick={() => setFeedbackPopup(null)}
            >
              Am înțeles
            </button>
          </div>
        </div>
      )}
    </main>
  );
};
