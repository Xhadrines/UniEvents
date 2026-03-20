import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { MainLayout } from "../layouts/MainLayout";

import LogIn from "../pages/Login/LogIn";
import SignUp from "../pages/SignUp/SignUp";
import CompleteProfilePage from "../pages/CompleteProfile/CompleteProfile";

export const AppRouter = () => {
  return (
    <BrowserRouter>
      <MainLayout>
        <Routes>
          <Route path="/" element={<Navigate to="/log-in" replace />} />

          <Route path="/log-in" element={<LogIn />} />
          <Route path="/sign-up" element={<SignUp />} />
          <Route path="/complete-profile" element={<CompleteProfilePage />} />
        </Routes>
      </MainLayout>
    </BrowserRouter>
  );
};
