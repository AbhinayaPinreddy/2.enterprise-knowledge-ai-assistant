import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { registerUser } from "../api/auth";
import toast, { Toaster } from "react-hot-toast";

function Register() {

  const navigate = useNavigate();

  const [loading, setLoading] = useState(false);

  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    role: "employee"
  });

  const handleRegister = async (e) => {

    e.preventDefault();

    setLoading(true);

    try {

      await registerUser(form);

      toast.success("Registration Successful");

      setTimeout(() => {

        navigate("/");

      }, 1000);

    } catch (err) {

      if (err.response?.data?.detail) {
        toast.error(err.response.data.detail);
      } else {
        toast.error("Registration Failed");
      }

    }

    setLoading(false);
  };

  return (

    <div className="login-container">

      <Toaster position="top-right" />

      <form
        className="login-card"
        onSubmit={handleRegister}
      >

        <h1>Create Account</h1>

        <p>Create your account to access the Enterprise Knowledge Assistant</p>

        <input
          type="text"
          placeholder="Full Name"
          value={form.name}
          onChange={(e) =>
            setForm({
              ...form,
              name: e.target.value
            })
          }
          required
        />

        <input
          type="email"
          placeholder="Email"
          value={form.email}
          onChange={(e) =>
            setForm({
              ...form,
              email: e.target.value
            })
          }
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={(e) =>
            setForm({
              ...form,
              password: e.target.value
            })
          }
          required
        />

        <button type="submit">
          {loading ? "Registering..." : "Register"}
        </button>

        <p style={{ marginTop: "20px" }}>
          Already have an account?{" "}
          <Link to="/">
            Login
          </Link>
        </p>

      </form>

    </div>

  );
}

export default Register;