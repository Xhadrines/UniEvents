import { useNavigate } from "react-router-dom";

import { Header } from "../../components/Header/Header";
import { ResetPasswordConfirmForm } from "../../components/ResetPasswordConfirmForm/ResetPasswordConfirmForm";

export const ResetPasswordConfirm = () => {
  const navigate = useNavigate();

  const handleBack = () => {
    console.log("Back clicked");
    navigate("/log-in");
  };

  const handleConfirmPasswordReset = () => {
    console.log("Confirm Password Reset clicked");
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
        <ResetPasswordConfirmForm onSubmit={handleConfirmPasswordReset} />
      </main>
    </div>
  );
};
