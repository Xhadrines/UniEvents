import { Header } from "../../components/Header/Header";
import { HomeComponent } from "../../components/HomeComponent/HomeComponent";

const Home = () => {
  const user = JSON.parse(localStorage.getItem("user") || "{}");
  const roleName = user?.profile?.role?.name;

  const canSeeDashboard =
    roleName === "Organizatie" || roleName === "Administrator";

  return (
    <div style={{ background: "var(--bg)", minHeight: "100svh" }}>
      <Header
        title="UniEvents"
        showBack={false}
        showDropdown={true}
        showDashboard={canSeeDashboard}
      />

      <HomeComponent />
    </div>
  );
};

export default Home;
