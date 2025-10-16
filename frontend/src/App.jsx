import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { ThemeProvider } from "./context/ThemeContext";
import { CartProvider } from "./context/CartContext";
import AnimatedBackground from "./components/AnimatedBackground";
import NavBar from "./components/NavBar";
import Home from "./pages/Home";
import AdminPanel from "./pages/AdminPanel";

export default function App(){
  return (
    <ThemeProvider>
      <CartProvider>
        <BrowserRouter>
          <div className="min-h-screen relative">
            <AnimatedBackground />
            <NavBar />
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/catalog" element={
                <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-8">
                  <h2 className="text-2xl sm:text-3xl lg:text-4xl font-bold text-white">Catálogo (próximamente)</h2>
                </div>
              } />
              <Route path="/admin" element={<AdminPanel />} />
            </Routes>
          </div>
        </BrowserRouter>
      </CartProvider>
    </ThemeProvider>
  )
}
