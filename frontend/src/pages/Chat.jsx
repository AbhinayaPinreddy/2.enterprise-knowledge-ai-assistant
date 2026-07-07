import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import {
  getSessions,
  createSession,
  getMessages,
  askQuestion,
} from "../api/chat";
import toast, { Toaster } from "react-hot-toast";

function Chat() {
  const [sessions, setSessions] = useState([]);
  const [selectedSession, setSelectedSession] = useState(null);
  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");

  const loadSessions = async () => {
    try {
      const data = await getSessions();
      setSessions(data);
    } catch {
      toast.error("Unable to load chats");
    }
  };

  useEffect(() => {
    loadSessions();
  }, []);

  const loadMessages = async (sessionId) => {
    try {
      const data = await getMessages(sessionId);

      setSelectedSession(sessionId);

      setMessages(data);
    } catch {
      toast.error("Unable to load messages");
    }
  };

  const handleNewChat = async () => {
    const title = prompt("Enter Chat Title");

    if (!title) return;

    await createSession(title);

    loadSessions();
  };

  const handleSend = async () => {
    if (!question.trim()) return;

    if (!selectedSession) {
      toast.error("Select a chat first");
      return;
    }

    const userMessage = {
      role: "user",
      message: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentQuestion = question;
    setQuestion("");

    try {
      const response = await askQuestion(
        selectedSession,
        currentQuestion
      );

      const aiMessage = {
        role: "assistant",
        message: response.answer,
        sources: response.sources,
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch {
      toast.error("Failed to get AI response");
    }
  };

  return (
    <Layout>
      <Toaster />

      <div className="chat-page">

        <div className="chat-sidebar">

          <button
            className="new-chat-btn"
            onClick={handleNewChat}
          >
            + New Chat
          </button>

          <br />
          <br />

          {sessions.map((chat) => (
            <div
              key={chat.id}
              className="chat-session"
              onClick={() => loadMessages(chat.id)}
            >
              {chat.title}
            </div>
          ))}

        </div>

        <div className="chat-window">

          <div className="messages">

            {messages.map((msg, index) => (

              <div
                key={index}
                className={
                  msg.role === "user"
                    ? "user-msg"
                    : "ai-msg"
                }
              >
                <strong>{msg.role}</strong>

                <p>{msg.message}</p>

              </div>

            ))}

          </div>

          <div className="chat-input">

            <input
              value={question}
              onChange={(e) =>
                setQuestion(e.target.value)
              }
              placeholder="Ask something..."
            />

            <button onClick={handleSend}>
              Send
            </button>

          </div>

        </div>

      </div>
    </Layout>
  );
}

export default Chat;