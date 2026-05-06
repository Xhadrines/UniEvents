import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useGoogleLogin } from "@react-oauth/google";

import "./SignUpForm.css";

type Props = {
  onRegister?: () => void;
  onGoogleRegister?: () => void;
};

export const SignUpForm = ({ onRegister, onGoogleRegister }: Props) => {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState<{
    text: string;
    type: "success" | "error";
  } | null>(null);

  const saveAuthData = (data: any) => {
    localStorage.setItem("access", data.access);
    localStorage.setItem("refresh", data.refresh);

    localStorage.setItem(
      "user",
      JSON.stringify({
        user_id: data.user_id,
        username: data.username,
        email: data.email,
        profile: data.profile,
      }),
    );
  };

  const handleRegister = async () => {
    try {
      const res = await fetch(`${import.meta.env.VITE_API}/api/register/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, email, password }),
      });

      const data = await res.json();
      console.log("Response from backend:", data);

      if (res.ok) {
        onRegister?.();

        setMessage({
          text: "Înregistrare reușită! Verifică email-ul pentru link-ul de completare profil.",
          type: "success",
        });

        setUsername("");
        setEmail("");
        setPassword("");
      } else {
        setMessage({
          text: data.error || data.detail || "Eroare la înregistrare",
          type: "error",
        });
      }
    } catch (err) {
      console.error(err);
      setMessage({ text: "Eroare server", type: "error" });
    }
  };

  const googleLogin = useGoogleLogin({
    onSuccess: async (tokenResponse) => {
      try {
        const res = await fetch(
          `${import.meta.env.VITE_API}/api/auth/google/`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({
              token: tokenResponse.access_token,
            }).toString(),
          },
        );

        const data = await res.json();
        console.log("Google register/login:", data);

        if (res.ok) {
          saveAuthData(data);

          onGoogleRegister?.();

          setMessage({
            text: data.created
              ? "Cont creat cu Google cu succes!"
              : "Autentificare cu Google reușită!",
            type: "success",
          });

          navigate("/home");
        } else {
          setMessage({
            text:
              data.error || data.detail || "Eroare la autentificare cu Google",
            type: "error",
          });
        }
      } catch (error) {
        console.error(error);
        setMessage({ text: "Eroare server Google", type: "error" });
      }
    },
    onError: () => {
      setMessage({
        text: "Autentificarea cu Google a eșuat",
        type: "error",
      });
    },
  });

  return (
    <div className="signup-container">
      <h2 className="signup-title">Sign Up</h2>

      <label className="signup-label" htmlFor="username">
        Username
      </label>
      <input
        id="username"
        type="text"
        className="signup-input"
        placeholder="Introduceți username-ul"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <label className="signup-label" htmlFor="email">
        Email
      </label>
      <input
        id="email"
        type="email"
        className="signup-input"
        placeholder="Introduceți email-ul"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <label className="signup-label" htmlFor="password">
        Password
      </label>
      <input
        id="password"
        type="password"
        className="signup-input"
        placeholder="Introduceți parola"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button className="signup-btn" onClick={handleRegister}>
        Sign Up
      </button>

      <button className="google-btn" onClick={() => googleLogin()}>
        <img
          src="/src/assets/google.svg"
          alt="Google"
          className="google-icon"
        />
        Înregistrează-te cu Google
      </button>

      {message && (
        <p
          style={{
            color: message.type === "success" ? "green" : "red",
            textAlign: "center",
            marginTop: "12px",
          }}
        >
          {message.text}
        </p>
      )}
    </div>
  );
};
