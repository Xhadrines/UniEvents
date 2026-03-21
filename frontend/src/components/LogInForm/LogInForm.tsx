import React, { useState } from "react";
import { useGoogleLogin } from "@react-oauth/google";

import "./LogInForm.css";

type Props = {
  onLogin?: () => void;
  onGoogleLogin?: () => void;
};

export const LogInForm = ({ onLogin, onGoogleLogin }: Props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState<{
    text: string;
    type: "success" | "error";
  } | null>(null);

  const handleLogin = async () => {
    try {
      const res = await fetch(`${import.meta.env.VITE_API}/api/login/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username_or_email: username, password }),
      });

      const data = await res.json();
      console.log("Response from backend:", data);

      if (res.ok) {
        setMessage({ text: "Autentificare reușită!", type: "success" });
      } else {
        setMessage({
          text: data.detail || "Eroare la autentificare",
          type: "error",
        });
      }
    } catch (error) {
      console.error(error);
      setMessage({ text: "Eroare server", type: "error" });
    }
  };

  const googleLogin = useGoogleLogin({
    onSuccess: async (tokenResponse) => {
      const res = await fetch(`${import.meta.env.VITE_API}/api/auth/google/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          token: tokenResponse.access_token,
        }).toString(),
      });

      const data = await res.json();
      console.log("Google login:", data);
    },
    onError: () => console.log("Login Failed"),
  });

  return (
    <div className="login-container">
      <h2 className="login-title">Log In</h2>

      <label className="login-label" htmlFor="username">
        Username/Email
      </label>
      <input
        id="username"
        type="text"
        className="login-input"
        placeholder="Introduceți username sau email"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <label className="login-label" htmlFor="password">
        Password
      </label>
      <input
        id="password"
        type="password"
        className="login-input"
        placeholder="Introduceți parola"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button className="login-btn" onClick={handleLogin}>
        Log In
      </button>

      {message && (
        <p
          style={{
            color: message.type === "success" ? "green" : "red",
            marginTop: "12px",
            textAlign: "center",
          }}
        >
          {message.text}
        </p>
      )}

      <button className="google-btn" onClick={() => googleLogin()}>
        <img
          src="/src/assets/google.svg"
          alt="Google"
          className="google-icon"
        />
        Conectează-te cu Google
      </button>

      <p className="signup-text">
        Nu ai cont? <a href="/sign-up">Crează unul!</a>
      </p>
    </div>
  );
};
