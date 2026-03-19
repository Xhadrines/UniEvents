import { useState, useRef, useEffect } from "react";
import "./Dropdown.css";

type Option = {
  icon: string;
  label: string;
  show?: boolean;
};

type Props = {
  options: Option[];
  triggerIcon: string;
};

export const Dropdown = ({ options, triggerIcon }: Props) => {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (ref.current && !ref.current.contains(event.target as Node)) {
        setOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div className="dropdown" ref={ref}>
      <button className="dropdown-btn" onClick={() => setOpen(!open)}>
        <img src={triggerIcon} alt="more" className="dropdown-trigger-icon" />
      </button>
      {open && (
        <div className="dropdown-menu">
          {options
            .filter((opt) => opt.show !== false)
            .map((opt) => (
              <button key={opt.label} className="dropdown-item">
                <img src={opt.icon} alt={opt.label} />
                <span>{opt.label}</span>
              </button>
            ))}
        </div>
      )}
    </div>
  );
};
