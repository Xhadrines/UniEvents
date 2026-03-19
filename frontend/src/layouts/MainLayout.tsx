import { Header } from "../components/Header/Header";

type Props = {
  children: React.ReactNode;
};

export const MainLayout = ({ children }: Props) => {
  const role = "user";

  return (
    <>
      <Header role={role} />
      <main>{children}</main>
    </>
  );
};
