import "./SignUpForm.css";

type Props = {
  onRegister?: () => void;
  onGoogleRegister?: () => void;
};

export const SingUpForm = ({ onRegister, onGoogleRegister }: Props) => {
  return (
    <div className="singup-container">
      <h2 className="singup-title">Sign Up</h2>

      <label className="singup-label" htmlFor="username">
        Username
      </label>
      <input
        id="username"
        type="text"
        className="singup-input"
        placeholder="Introduceți username-ul"
      />

      <label className="singup-label" htmlFor="email">
        Email
      </label>
      <input
        id="email"
        type="email"
        className="singup-input"
        placeholder="Introduceți email-ul"
      />

      <label className="singup-label" htmlFor="password">
        Password
      </label>
      <input
        id="password"
        type="password"
        className="singup-input"
        placeholder="Introduceți parola"
      />

      <button className="singup-btn" onClick={onRegister}>
        Sign Up
      </button>

      <button className="google-btn" onClick={onGoogleRegister}>
        <img
          src="/src/assets/google.svg"
          alt="Google"
          className="google-icon"
        />
        Înregistrează-te cu Google
      </button>
    </div>
  );
};
