import { Link, useNavigate } from "react-router-dom";
import {
  FaHome,
  FaFileAlt,
  FaUpload,
  FaComments,
  FaSignOutAlt,
} from "react-icons/fa";

function Sidebar() {

  const navigate = useNavigate();
  const handleLogout = () => {

    localStorage.removeItem("token");
    localStorage.removeItem("name");
    localStorage.removeItem("email");
    localStorage.removeItem("role");

    navigate("/");
  };

  return (
    <div className="sidebar">

      <h2>Enterprise AI</h2>

      <Link to="/dashboard">
        <FaHome /> Dashboard
      </Link>

      <Link to="/documents">
        <FaFileAlt /> Documents
      </Link>

      <Link to="/upload">
        <FaUpload /> Upload
      </Link>

      <Link to="/chat">
        <FaComments /> Chats
      </Link>

      <button
        className="logout-btn"
        onClick={handleLogout}
      >
        <FaSignOutAlt /> Logout
      </button>

    </div>
  );
}

export default Sidebar;