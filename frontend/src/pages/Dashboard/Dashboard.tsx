import { Navigate } from "react-router-dom";
import { Header } from "../../components/Header/Header";
import { OrganizerDashboard } from "../../components/OrganizerDashboard/OrganizerDashboard";
import { AdminDashboard } from "../../components/AdminDashboard/AdminDashboard";

const Dashboard = () => {
  const user = JSON.parse(localStorage.getItem("user") || "{}");
  const roleName = user?.profile?.role?.name;

  if (roleName === "Organizatie") {
    return (
      <div style={{ background: "var(--bg)", minHeight: "100svh" }}>
        <Header
          title="Dashboard Organizator"
          showBack
          showDropdown={false}
          onBack={() => history.back()}
        />
        <OrganizerDashboard />
      </div>
    );
  }

  if (roleName === "Administrator") {
    return (
      <div style={{ background: "var(--bg)", minHeight: "100svh" }}>
        <Header
          title="Dashboard Administrator"
          showBack
          showDropdown={false}
          onBack={() => history.back()}
        />
        <AdminDashboard />
        <main style={{ paddingTop: 120, color: "var(--text-h)" }}>
          Dashboard administrator încă neimplementat.
        </main>
      </div>
    );
  }

  return <Navigate to="/home" replace />;
};

export default Dashboard;
