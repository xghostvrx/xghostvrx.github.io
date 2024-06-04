import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Sacred Spirituality",
  description: "Unlock transformation. Book an appointment at Sacred Spirituality to unveil Reiki's healing power, seek energy work, and experience quality spiritual guidance.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
