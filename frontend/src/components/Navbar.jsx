function Navbar() {

  const name = localStorage.getItem("name");

  return (
    <div className="navbar">

      <h2>Enterprise Knowledge Assistant</h2>

      <p>Welcome, {name} 👋</p>

    </div>
  );
}

export default Navbar;