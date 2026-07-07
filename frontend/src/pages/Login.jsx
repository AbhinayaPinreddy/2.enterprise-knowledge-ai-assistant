import { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import { loginUser, getCurrentUser } from "../api/auth";
import toast, { Toaster } from "react-hot-toast";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  // If already logged in, go to dashboard
  useEffect(() => {
    const token = localStorage.getItem("token");

    if (token) {
      navigate("/dashboard");
    }
  }, [navigate]);

  const handleLogin = async (e) => {
    e.preventDefault();

    setLoading(true);

    try {
      const data = await loginUser(email, password);

// Save token
      localStorage.setItem("token", data.access_token);

// Get logged-in user details
      const user = await getCurrentUser();

      localStorage.setItem("name", user.name);
      localStorage.setItem("email", user.email);
      localStorage.setItem("role", user.role);

      toast.success("Login Successful");

      navigate("/dashboard");
    } catch (err) {
      toast.error("Invalid Email or Password");
    }

    setLoading(false);
  };

  return (
    <div className="login-container">
      <Toaster position="top-right" />

      <form className="login-card" onSubmit={handleLogin}>
        <h1>Enterprise Knowledge Assistant</h1>
        <p>AI Powered Enterprise Document Assistant</p>

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">
          {loading ? "Logging in..." : "Login"}
        </button>

        <p style={{ marginTop: "20px" }}>
          New User?{" "}
          <Link to="/register">
            Create Account
          </Link>
        </p>
      </form>
    </div>
  );
}

export default Login;