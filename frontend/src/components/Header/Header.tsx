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
  const dropdownOptions = [
    { icon: userIcon, label: "Profil", show: true },
    { icon: dashboardIcon, label: "Panou de control", show: showDashboard },
    { icon: logoutIcon, label: "Deconectare", show: true },
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
