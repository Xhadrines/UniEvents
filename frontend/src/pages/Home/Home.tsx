import { Header } from "../../components/Header/Header";
import { HomeComponent } from "../../components/HomeComponent/HomeComponent";

const Home = () => {
  return (
    <div style={{ background: "var(--bg)", minHeight: "100svh" }}>
      <Header
        title="UniEvents"
        showBack={false}
        showDropdown={true}
        showDashboard={false}
      />

      <HomeComponent />
    </div>
  );
};

export default Home;
