import { useState, useEffect } from "react";
import "./CompleteProfileForm.css";

type Faculty = {
  id: number;
  name: string;
};

type Specialization = {
  id: number;
  name: string;
  faculty: number;
};

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
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
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
        setFaculties(data.faculties ?? []);
        setSpecializations(data.specializations ?? []);
      })
      .catch((err) => console.error(err));
  }, [token]);

  const filteredSpecializations = facultyId
    ? specializations.filter(
        (specialization) => specialization.faculty === facultyId,
      )
    : specializations;

  const handleFacultyChange = (value: string) => {
    const newFacultyId = value ? Number(value) : null;

    setFacultyId(newFacultyId);
    setSpecializationId(null);
  };

  const handleSpecializationChange = (value: string) => {
    const newSpecializationId = value ? Number(value) : null;

    setSpecializationId(newSpecializationId);

    const selectedSpecialization = specializations.find(
      (specialization) => specialization.id === newSpecializationId,
    );

    if (selectedSpecialization) {
      setFacultyId(selectedSpecialization.faculty);
    }
  };

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
            first_name: firstName,
            last_name: lastName,
            faculty: facultyId,
            specialization: specializationId,
            study_year: anStudiu ? Number(anStudiu) : null,
            group: grupa ? Number(grupa) : null,
            semi_group: semiGrupa || null,
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
          text:
            data.detail ||
            data.error ||
            JSON.stringify(data) ||
            "Eroare la completare",
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

      <label className="complete-profile-label">Prenume</label>
      <input
        type="text"
        className="complete-profile-input"
        value={firstName}
        onChange={(e) => setFirstName(e.target.value)}
      />

      <label className="complete-profile-label">Nume</label>
      <input
        type="text"
        className="complete-profile-input"
        value={lastName}
        onChange={(e) => setLastName(e.target.value)}
      />

      <label className="complete-profile-label">Facultate</label>
      <select
        className="complete-profile-input"
        value={facultyId ?? ""}
        onChange={(e) => handleFacultyChange(e.target.value)}
      >
        <option value="">Selectează facultate</option>
        {faculties.map((faculty) => (
          <option key={faculty.id} value={faculty.id}>
            {faculty.name}
          </option>
        ))}
      </select>

      <label className="complete-profile-label">Specializare</label>
      <select
        className="complete-profile-input"
        value={specializationId ?? ""}
        onChange={(e) => handleSpecializationChange(e.target.value)}
      >
        <option value="">Selectează specializare</option>
        {filteredSpecializations.map((specialization) => (
          <option key={specialization.id} value={specialization.id}>
            {specialization.name}
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
