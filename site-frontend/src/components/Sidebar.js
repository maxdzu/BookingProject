import { useState } from "react";
import { Link } from "react-router-dom";
import { motion } from "framer-motion";
import { Menu, X } from "lucide-react";
import "../style/Sidebar.css";

function Sidebar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <button className="menu-button" onClick={() => setIsOpen(true)}>
        <Menu size={24} />
      </button>

      {isOpen && <div className="overlay" onClick={() => setIsOpen(false)} />}

      <motion.div
        initial={{ x: "-100%" }}
        animate={{ x: isOpen ? "0%" : "-100%" }}
        transition={{ duration: 0.3, ease: "easeOut" }}
        className="sidebar"
      >
        <button className="close-button" onClick={() => setIsOpen(false)}>
          <X size={24} />
        </button>

        <h2 className="sidebar-title">Menu</h2>

        <nav>
          <ul className="sidebar-list">
            <li className="sidebar-item">
              <Link to="/" className="sidebar-link" onClick={() => setIsOpen(false)}>
                📂 Catalog
              </Link>
            </li>
            <li className="sidebar-item">
              <Link to="/profile" className="sidebar-link" onClick={() => setIsOpen(false)}>
                👤 Profile
              </Link>
            </li>
          </ul>
        </nav>
      </motion.div>
    </>
  );
}

export default Sidebar;
