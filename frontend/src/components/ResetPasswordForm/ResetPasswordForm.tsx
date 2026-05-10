import { useState } from "react";
import "./ResetPasswordForm.css";

type Props = {
  onSubmit?: () => void;
};

export const ResetPasswordForm = ({ onSubmit }: Props) => {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState<{
    text: string;
    type: "success" | "error";
  } | null>(null);

  const handleSubmit = async () => {
    try {
      const res = await fetch(
        `${import.meta.env.VITE_API}/api/password-reset/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email }),
        },
      );

      const data = await res.json();

      if (res.ok) {
        setMessage({
          text: data.message,
          type: "success",
        });

        onSubmit?.();
      } else {
        setMessage({
          text: data.error || "Eroare la trimiterea email-ului.",
          type: "error",
        });
      }
    } catch (err) {
      console.error(err);
      setMessage({
        text: "Eroare server.",
        type: "error",
      });
    }
  };

  return (
    <div className="reset-password-container">
      <h2 className="reset-password-title">Resetare parolă</h2>

      <label className="reset-password-label">Email</label>
      <input
        type="email"
        className="reset-password-input"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Introdu email-ul contului"
      />

      <button className="reset-password-btn" onClick={handleSubmit}>
        Trimite email
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
