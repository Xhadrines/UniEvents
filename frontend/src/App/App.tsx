import { AppRouter } from "../router/AppRouter";
import { GoogleOAuthProvider } from "@react-oauth/google";

import "./App.css";

function App() {
  return (
    <GoogleOAuthProvider clientId={import.meta.env.VITE_GOOGLE_CLIENT_ID}>
      <AppRouter />
    </GoogleOAuthProvider>
  );
}

export default App;
