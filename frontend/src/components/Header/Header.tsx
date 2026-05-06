import { useNavigate } from "react-router-dom";

import { Dropdown } from "../Dropdown/Dropdown";
import "./Header.css";

import backIcon from "../../assets/back.svg";
import moreIcon from "../../assets/more.svg";
import userIcon from "../../assets/user.svg";
import logoutIcon from "../../assets/logout.svg";
import dashboardIcon from "../../assets/dashboard.svg";

type Props = {
  title: string;
  showBack?: boolean;
  showDropdown?: boolean;
  showDashboard?: boolean;
  onBack?: () => void;
};

export const Header = ({
  title,
  showBack,
  showDropdown,
  showDashboard,
  onBack,
}: Props) => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    localStorage.removeItem("user");

    navigate("/log-in", { replace: true });
  };

  const dropdownOptions = [
    {
      icon: userIcon,
      label: "Profil",
      show: true,
      onClick: () => navigate("/profile"),
    },
    {
      icon: dashboardIcon,
      label: "Panou de control",
      show: showDashboard,
      onClick: () => navigate("/dashboard"),
    },
    {
      icon: logoutIcon,
      label: "Deconectare",
      show: true,
      onClick: handleLogout,
    },
  ];

  return (
    <header className="login-header">
      <div className="header-left">
        {showBack && (
          <button className="back-btn" onClick={onBack}>
            <img src={backIcon} alt="Back" />
          </button>
        )}
      </div>

      <div className="header-center">{title}</div>

      <div className="header-right">
        {showDropdown && (
          <Dropdown options={dropdownOptions} triggerIcon={moreIcon} />
        )}
      </div>
    </header>
  );
};
