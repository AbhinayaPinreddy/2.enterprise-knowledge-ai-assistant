import api from "./api";

// Create new chat session
export const createSession = async (title) => {

    const response = await api.post("/chat-history/session", {
        title,
    });

    return response.data;
};

// Get all sessions
export const getSessions = async () => {

    const response = await api.get("/chat-history/sessions");

    return response.data;
};

// Get messages
export const getMessages = async (sessionId) => {

    const response = await api.get(
        `/chat-history/messages/${sessionId}`
    );

    return response.data;
};

// Ask AI
export const askQuestion = async (sessionId, question) => {

    try {

        const response = await api.post("/chat/", {
            session_id: sessionId,
            question: question,
        });

        return response.data;

    } catch (err) {

        console.log(err.response);

        throw err;
    }
};