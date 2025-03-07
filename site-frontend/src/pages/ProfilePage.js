import { useEffect, useState } from "react";
import axios from "axios";
import "../style/ProfilePage.css";

function ProfilePage() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [loginData, setLoginData] = useState({ username: "", password: "" });

  const token = localStorage.getItem("access_token");

  useEffect(() => {
    if (token) {
      axios
        .get("http://127.0.0.1:8000/a/users/profile/", {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((response) => {
          setUser(response.data);
          setLoading(false);
        })
        .catch((error) => {
          console.error("Profile loading error:", error);
          setLoading(false);
        });
    } else {
      setLoading(false);
    }
  }, [token]);

  const handleLogin = (e) => {
    e.preventDefault();
    axios
      .post("http://127.0.0.1:8000/a/users/login/", loginData)
      .then((response) => {
        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);
        window.location.reload();
      })
      .catch((error) => {
        console.error("Login error:", error);
        alert("Invalid credentials");
      });
  };

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    setUser(null);
  };

  if (loading) return <p>Loading...</p>;

  return (
    <div className="profile-container">
      {user ? (
        <div className="profile-info">
          <h1>Welcome, {user.username}!</h1>
          <p><strong>Age:</strong> {user.age || "Not provided"}</p>
          <p><strong>Phone:</strong> {user.phone}</p>
          <p><strong>Email:</strong> {user.email}</p>
          <p><strong>First name:</strong> {user.first_name}</p>
          <p><strong>Last name:</strong> {user.last_name}</p>
          <button className="logout-btn" onClick={handleLogout}>Logout</button>
        </div>
      ) : (
        <div className="login-form">
          <h1>Login</h1>
          <form onSubmit={handleLogin}>
            <input
              type="text"
              placeholder="Username"
              value={loginData.username}
              onChange={(e) => setLoginData({ ...loginData, username: e.target.value })}
              required
            />
            <input
              type="password"
              placeholder="Password"
              value={loginData.password}
              onChange={(e) => setLoginData({ ...loginData, password: e.target.value })}
              required
            />
            <button type="submit">Login</button>
          </form>
        </div>
      )}
    </div>
  );
}

export default ProfilePage;
