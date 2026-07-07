import { useEffect, useState } from "react";
import Layout from "../components/Layout";

import {
  FaFileAlt,
  FaComments,
  FaLayerGroup,
  FaFolderOpen,
} from "react-icons/fa";

import { getDashboardStats } from "../api/dashboard";

function Dashboard() {

  const [stats, setStats] = useState({

    documents: 0,

    chat_sessions: 0,

    chunks: 0,

    categories: 0,

    recent_documents: []

  });

  useEffect(() => {

    fetchStats();

  }, []);

  const fetchStats = async () => {

    try {

      const data = await getDashboardStats();

      setStats(data);

    }

    catch (err) {

      console.log(err);

    }

  };

  return (

    <Layout>

      <h1>Dashboard</h1>

      <div className="cards">

        <div className="card">

          <FaFileAlt className="card-icon"/>

          <h2>{stats.documents}</h2>

          <p>Total Documents</p>

        </div>

        <div className="card">

          <FaComments className="card-icon"/>

          <h2>{stats.chat_sessions}</h2>

          <p>Chat Sessions</p>

        </div>

        <div className="card">

          <FaLayerGroup className="card-icon"/>

          <h2>{stats.chunks}</h2>

          <p>Total Chunks</p>

        </div>

        <div className="card">

          <FaFolderOpen className="card-icon"/>

          <h2>{stats.categories}</h2>

          <p>Categories</p>

        </div>

      </div>

      <div className="recent">

        <h2>Recent Documents</h2>

        <ul>

          {

            stats.recent_documents.length === 0 ?

            (

              <li>No Documents Uploaded</li>

            )

            :

            (

              stats.recent_documents.map((doc)=>(

                <li key={doc.id}>

                  {doc.filename}

                  {" "}

                  ({doc.category})

                </li>

              ))

            )

          }

        </ul>

      </div>

    </Layout>

  );

}

export default Dashboard;