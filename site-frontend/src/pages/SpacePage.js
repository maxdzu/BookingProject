import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "../style/SpacePage.css";

function SpacePage() {
  const { accomodationId } = useParams();
  const [spaces, setSpaces] = useState([]);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/a/bookings/accomodations/${accomodationId}/spaces/`)
      .then((response) => setSpaces(response.data))
      .catch((error) => console.error("Loading error:", error));
  }, [accomodationId]);

  return (
    <div className="spaces-container">
      <h1 className="spaces-title">Rooms in this Coworking</h1>
      <div className="spaces-grid">
        {spaces.map((space) => (
          <div key={space.id} className="space-card">
            <h2 className="space-title">{space.name}</h2>
            <p className="space-description">{space.description}</p>
            <p className="space-capacity">Capacity: {space.capacity} people</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SpacePage;
