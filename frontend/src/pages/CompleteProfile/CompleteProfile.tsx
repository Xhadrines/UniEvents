import { useNavigate, useSearchParams } from "react-router-dom";

import { Header } from "../../components/Header/Header";
import { CompleteProfileForm } from "../../components/CompleteProfileForm/CompleteProfileForm";

const CompleteProfilePage = () => {
  const [searchParams] = useSearchParams();
  const token = searchParams.get("token") || "";
  const navigate = useNavigate();

  const handleBack = () => {
    navigate("/log-in");
  };

  return (
    <div style={{ background: "var(--bg)", minHeight: "100svh" }}>
      <Header
        title="Completează Profilul"
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
        <CompleteProfileForm token={token} />
      </main>
    </div>
  );
};

export default CompleteProfilePage;
