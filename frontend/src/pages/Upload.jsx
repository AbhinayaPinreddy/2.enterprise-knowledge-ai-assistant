import { useRef, useState } from "react";
import Layout from "../components/Layout";
import { uploadDocument } from "../api/documents";
import toast, { Toaster } from "react-hot-toast";

function Upload() {

    const [title, setTitle] = useState("");
    const [category, setCategory] = useState("");
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);

    const fileInputRef = useRef(null);

    const handleUpload = async (e) => {

        e.preventDefault();

        if (!file) {
            toast.error("Please choose a PDF");
            return;
        }

        const formData = new FormData();

        formData.append("title", title);
        formData.append("category", category);
        formData.append("file", file);

        try {

            setLoading(true);

            await uploadDocument(formData);

            toast.success("Document Uploaded Successfully");

            setTitle("");
            setCategory("");
            setFile(null);

            if (fileInputRef.current) {
                fileInputRef.current.value = "";
            }

        } catch {

            toast.error("Upload Failed");

        } finally {

            setLoading(false);

        }

    };

    return (

        <Layout>

            <Toaster position="top-right" />

            <h1>Upload Document</h1>

            <form
                className="upload-form"
                onSubmit={handleUpload}
            >

                <input
                    type="text"
                    placeholder="Document Title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    disabled={loading}
                    required
                />

                <select
                    value={category}
                    onChange={(e) => setCategory(e.target.value)}
                    disabled={loading}
                    required
                >

                    <option value="">Select Category</option>

                    <option value="HR">HR</option>

                    <option value="Finance">Finance</option>

                    <option value="IT">IT</option>

                </select>

                <input
                    ref={fileInputRef}
                    type="file"
                    accept=".pdf"
                    disabled={loading}
                    onChange={(e) => setFile(e.target.files[0])}
                    required
                />

                {file && !loading && (
                    <p style={{ color: "#555" }}>
                        📄 Selected: <strong>{file.name}</strong>
                    </p>
                )}

                {loading && (
                    <p
                        style={{
                            color: "#2563eb",
                            fontWeight: "600"
                        }}
                    >
                        ⏳ Processing document...
                    </p>
                )}

                <button
                    type="submit"
                    disabled={loading}
                >
                    {loading ? "Uploading..." : "Upload"}
                </button>

            </form>

        </Layout>

    );
}

export default Upload;