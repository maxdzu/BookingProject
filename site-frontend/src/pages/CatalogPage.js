import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import "../style/CatalogPage.css";

function CatalogPage() {
  const [coworkings, setCoworkings] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/a/bookings/accomodations/")
      .then((response) => setCoworkings(response.data))
      .catch((error) => console.error("Loading error:", error));
  }, []);

  return (
    <div className="catalog-container">
      <h1 className="catalog-title">Coworking Directory</h1>
      <div className="catalog-grid">
        {coworkings.map((coworking) => (
          <Link 
            to={`/coworking/${coworking.id}`} 
            key={coworking.id} 
            className="coworking-card"
          >
            <h2 className="coworking-title">{coworking.title}</h2>
            <p className="coworking-description">{coworking.description}</p>
            <p className="coworking-rating">⭐ {coworking.rating}/5</p>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default CatalogPage;
