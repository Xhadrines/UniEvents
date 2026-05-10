import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useGoogleLogin } from "@react-oauth/google";

import "./LogInForm.css";

type Props = {
  onLogin?: () => void;
  onGoogleLogin?: () => void;
};

type AuthResponse = {
  access: string;
  refresh: string;
  user_id: string | number;
  username: string;
  email: string;
  profile: unknown;
};

export const LogInForm = ({ onLogin, onGoogleLogin }: Props) => {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState<{
    text: string;
    type: "success" | "error";
  } | null>(null);

  const saveAuthData = (data: AuthResponse) => {
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
        saveAuthData(data);

        onLogin?.();

        setMessage({ text: "Autentificare reușită!", type: "success" });
        navigate("/home");
      } else {
        setMessage({
          text: data.error || data.detail || "Eroare la autentificare",
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
        console.log("Google login:", data);

        if (res.ok) {
          saveAuthData(data);

          onGoogleLogin?.();

          setMessage({ text: "Autentificare reușită!", type: "success" });
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
        Nu ai cont? <a href="/sign-up">Creează unul!</a>
      </p>
    </div>
  );
};
