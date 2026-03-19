import { Header } from "../../components/Header/Header";
import { LogInForm } from "../../components/LogInForm/LogInForm";

const LogIn = () => {
  const handleBack = () => {
    console.log("Back clicked");
  };

  const handleLogin = () => {
    console.log("Login clicked");
  };

  const handleGoogleLogin = () => {
    console.log("Google Login clicked");
  };

  return (
    <div style={{ background: "var(--bg)", minHeight: "100svh" }}>
      <Header
        title="UniEvents"
        showBack={false}
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
        <LogInForm onLogin={handleLogin} onGoogleLogin={handleGoogleLogin} />
      </main>
    </div>
  );
};

export default LogIn;
