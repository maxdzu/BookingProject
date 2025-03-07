import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import CatalogPage from "./pages/CatalogPage";
import ProfilePage from "./pages/ProfilePage";
import SpacePage from "./pages/SpacePage";

function App() {
  return (
    <Router>
      <div className="app-container">
        <Sidebar />
        <div className="content">
          <Routes>
            <Route path="/" element={<CatalogPage />} />
            <Route path="/profile" element={<ProfilePage />} />
            <Route path="/coworking/:accomodationId" element={<SpacePage />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
