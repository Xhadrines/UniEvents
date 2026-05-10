import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { MainLayout } from "../layouts/MainLayout";

import LogIn from "../pages/Login/LogIn";
import SignUp from "../pages/SignUp/SignUp";
import { ResetPassword } from "../pages/ResetPassword/ResetPassword";
import { ResetPasswordConfirm } from "../pages/ResetPasswordConfirm/ResetPasswordConfirm";
import CompleteProfilePage from "../pages/CompleteProfile/CompleteProfile";
import Home from "../pages/Home/Home";

const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const accessToken = localStorage.getItem("access");
  const user = localStorage.getItem("user");

  if (!accessToken || !user) {
    return <Navigate to="/log-in" replace />;
  }

  return children;
};

export const AppRouter = () => {
  return (
    <BrowserRouter>
      <MainLayout>
        <Routes>
          <Route path="/" element={<Navigate to="/log-in" replace />} />

          <Route path="/log-in" element={<LogIn />} />
          <Route path="/sign-up" element={<SignUp />} />
          <Route path="/reset-password" element={<ResetPassword />} />
          <Route
            path="/reset-password-confirm"
            element={<ResetPasswordConfirm />}
          />
          <Route path="/complete-profile" element={<CompleteProfilePage />} />

          <Route
            path="/home"
            element={
              <ProtectedRoute>
                <Home />
              </ProtectedRoute>
            }
          />
        </Routes>
      </MainLayout>
    </BrowserRouter>
  );
};
