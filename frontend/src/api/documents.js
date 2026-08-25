import api from "./api";

// Get Documents
export const getDocuments = async () => {
    const response = await api.get("/documents/");
    return response.data;
};

// Delete Document
export const deleteDocument = async (id) => {
    const response = await api.delete(`/documents/${id}`);
    return response.data;
};

// Download
export const downloadDocument = (id) => {
    window.open(
        `${import.meta.env.VITE_API_URL}/documents/download/${id}`,
        "_blank"
    );
};

// Upload Document
export const uploadDocument = async (formData) => {
    const response = await api.post(
        "/documents/upload",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};