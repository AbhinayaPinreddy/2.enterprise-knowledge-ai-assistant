import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import {
    getDocuments,
    deleteDocument,
    downloadDocument,
} from "../api/documents";

import toast, { Toaster } from "react-hot-toast";

function Documents() {

    const [documents, setDocuments] = useState([]);

    const loadDocuments = async () => {

        try {

            const data = await getDocuments();

            setDocuments(data);

        }
        catch {

            toast.error("Failed to load documents");

        }
    };

    useEffect(() => {

        loadDocuments();

    }, []);

    const handleDelete = async (id) => {

        if (!window.confirm("Delete this document?"))
            return;

        try {

            await deleteDocument(id);

            toast.success("Document Deleted");

            loadDocuments();

        }
        catch {

            toast.error("Delete Failed");

        }

    };

    return (

        <Layout>

            <Toaster position="top-right" />

            <h1>Documents</h1>

            <table className="doc-table">

                <thead>

                    <tr>

                        <th>Title</th>

                        <th>Category</th>

                        <th>Actions</th>

                    </tr>

                </thead>

                <tbody>

                    {documents.map((doc) => (

                        <tr key={doc.id}>

                            <td>{doc.title}</td>

                            <td>{doc.category}</td>

                            <td>

                                <button
                                    className="download-btn"
                                    onClick={() =>
                                        downloadDocument(doc.id)
                                    }
                                >
                                    Download
                                </button>

                                <button
                                    className="delete-btn"
                                    onClick={() =>
                                        handleDelete(doc.id)
                                    }
                                >
                                    Delete
                                </button>

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </Layout>

    );
}

export default Documents;