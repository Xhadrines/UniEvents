import { useState } from "react";
import { useSearchParams } from "react-router-dom";
import "./ResetPasswordConfirmForm.css";

type Props = {
  onSubmit?: () => void;
};

export const ResetPasswordConfirmForm = ({ onSubmit }: Props) => {
  const [searchParams] = useSearchParams();

  const uid = searchParams.get("uid");
  const token = searchParams.get("token");

  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [message, setMessage] = useState<{
    text: string;
    type: "success" | "error";
  } | null>(null);

  const handleSubmit = async () => {
    if (password !== confirmPassword) {
      setMessage({
        text: "Parolele nu coincid.",
        type: "error",
      });
      return;
    }

    try {
      const res = await fetch(
        `${import.meta.env.VITE_API}/api/password-reset-confirm/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            uid,
            token,
            password,
          }),
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
          text: data.error || "Link invalid sau expirat.",
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

      <label className="reset-password-label">Parolă nouă</label>
      <input
        type="password"
        className="reset-password-input"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <label className="reset-password-label">Confirmă parola</label>
      <input
        type="password"
        className="reset-password-input"
        value={confirmPassword}
        onChange={(e) => setConfirmPassword(e.target.value)}
      />

      <button className="reset-password-btn" onClick={handleSubmit}>
        Resetează parola
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
