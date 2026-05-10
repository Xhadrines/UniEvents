import { useNavigate } from "react-router-dom";

import { Header } from "../../components/Header/Header";
import { ResetPasswordForm } from "../../components/ResetPasswordForm/ResetPasswordForm";

export const ResetPassword = () => {
  const navigate = useNavigate();

  const handleBack = () => {
    console.log("Back clicked");
    navigate("/log-in");
  };

  const handleResetPassword = () => {
    console.log("Reset Password clicked");
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
        <ResetPasswordForm onSubmit={handleResetPassword} />
      </main>
    </div>
  );
};
