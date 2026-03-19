import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { MainLayout } from "../layouts/MainLayout";

import LogIn from "../pages/Login/LogIn";
import SignUp from "../pages/SignUp/SignUp";

export const AppRouter = () => {
  return (
    <BrowserRouter>
      <MainLayout>
        <Routes>
          <Route path="/" element={<Navigate to="/log-in" replace />} />

          <Route path="/log-in" element={<LogIn />} />
          <Route path="/sign-up" element={<SignUp />} />
        </Routes>
      </MainLayout>
    </BrowserRouter>
  );
};
