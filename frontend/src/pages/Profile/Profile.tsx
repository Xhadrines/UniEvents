import { useNavigate } from "react-router-dom";

import { Header } from "../../components/Header/Header";
import { ProfileComponent } from "../../components/ProfileComponent/ProfileComponent";

const Profile = () => {
  const navigate = useNavigate();

  return (
    <div style={{ background: "var(--bg)", minHeight: "100svh" }}>
      <Header
        title="Profilul meu"
        showBack={true}
        showDropdown={false}
        showDashboard={false}
        onBack={() => navigate("/home")}
      />

      <ProfileComponent />
    </div>
  );
};

export default Profile;
