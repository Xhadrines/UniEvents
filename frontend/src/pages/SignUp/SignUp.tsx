import { useNavigate } from "react-router-dom";

import { Header } from "../../components/Header/Header";
import { SingUpForm } from "../../components/SignUpForm/SignUpForm";

const SignUp = () => {
  const navigate = useNavigate();

  const handleBack = () => {
    console.log("Back clicked");
    navigate("/log-in");
  };

  const handleRegister = () => {
    console.log("Register clicked");
  };

  const handleGoogleRegister = () => {
    console.log("Google Register clicked");
  };

  return (
    <div style={{ background: "var(--bg)", minHeight: "100svh" }}>
      <Header
        title="UniEvents"
        showBack={true}
        showDropdown={false}
        showDashboard={false}
        onBack={handleBack}
      />
      <main
        style={{
          paddingTop: "100px",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <SingUpForm
          onRegister={handleRegister}
          onGoogleRegister={handleGoogleRegister}
        />
      </main>
    </div>
  );
};

export default SignUp;
