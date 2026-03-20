import { useState, useEffect } from "react";
import "./CompleteProfileForm.css";

type Faculty = { id: number; name: string };
type Specialization = { id: number; name: string };

type Props = {
  token: string;
  onComplete?: () => void;
};

export const CompleteProfileForm = ({ token, onComplete }: Props) => {
  const [faculties, setFaculties] = useState<Faculty[]>([]);
  const [specializations, setSpecializations] = useState<Specialization[]>([]);
  const [facultyId, setFacultyId] = useState<number | null>(null);
  const [specializationId, setSpecializationId] = useState<number | null>(null);
  const [anStudiu, setAnStudiu] = useState("");
  const [grupa, setGrupa] = useState("");
  const [semiGrupa, setSemiGrupa] = useState("");
  const [message, setMessage] = useState<{
    text: string;
    type: "success" | "error";
  } | null>(null);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API}/api/complete-profile/`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        setFaculties(data.faculties);
        setSpecializations(data.specializations);
      })
      .catch((err) => console.error(err));
  }, [token]);

  const handleSubmit = async () => {
    try {
      const res = await fetch(
        `${import.meta.env.VITE_API}/api/complete-profile/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${token}`,
          },
          body: JSON.stringify({
            facultate: facultyId,
            specializare: specializationId,
            an_studiu: anStudiu,
            grupa,
            semi_grupa: semiGrupa,
            token,
          }),
        },
      );

      const data = await res.json();
      if (res.ok) {
        setMessage({ text: "Profil completat cu succes!", type: "success" });
        onComplete?.();
      } else {
        setMessage({
          text: data.detail || "Eroare la completare",
          type: "error",
        });
      }
    } catch (err) {
      console.error(err);
      setMessage({ text: "Eroare server", type: "error" });
    }
  };

  return (
    <div className="complete-profile-container">
      <h2 className="complete-profile-title">Completează Profilul</h2>

      <label className="complete-profile-label">Facultate</label>
      <select
        className="complete-profile-input"
        value={facultyId ?? ""}
        onChange={(e) => setFacultyId(Number(e.target.value))}
      >
        <option value="">Selectează facultate</option>
        {faculties.map((f) => (
          <option key={f.id} value={f.id}>
            {f.name}
          </option>
        ))}
      </select>

      <label className="complete-profile-label">Specializare</label>
      <select
        className="complete-profile-input"
        value={specializationId ?? ""}
        onChange={(e) => setSpecializationId(Number(e.target.value))}
      >
        <option value="">Selectează specializare</option>
        {specializations.map((s) => (
          <option key={s.id} value={s.id}>
            {s.name}
          </option>
        ))}
      </select>

      <label className="complete-profile-label">An studiu</label>
      <input
        type="number"
        className="complete-profile-input"
        value={anStudiu}
        onChange={(e) => setAnStudiu(e.target.value)}
      />

      <label className="complete-profile-label">Grupa</label>
      <input
        type="number"
        className="complete-profile-input"
        value={grupa}
        onChange={(e) => setGrupa(e.target.value)}
      />

      <label className="complete-profile-label">Semi-grupa</label>
      <input
        type="text"
        className="complete-profile-input"
        value={semiGrupa}
        onChange={(e) => setSemiGrupa(e.target.value)}
      />

      <button className="complete-profile-btn" onClick={handleSubmit}>
        Salvează
      </button>

      {message && (
        <p
          style={{
            color: message.type === "success" ? "green" : "red",
            textAlign: "center",
          }}
        >
          {message.text}
        </p>
      )}
    </div>
  );
};
