import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext";
import { useTheme } from "../context/ThemeContext";
import CartModal from "./CartModal";

export default function NavBar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [cartOpen, setCartOpen] = useState(false);
  const { itemCount } = useCart();
  const { theme } = useTheme();

  return (
    <>
      <CartModal isOpen={cartOpen} onClose={() => setCartOpen(false)} />
      <nav className="bg-white/90 backdrop-blur-md shadow-lg sticky top-0 z-50">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link
            to="/"
            className="text-xl sm:text-2xl font-bold bg-clip-text text-transparent transition-all"
            style={{
              backgroundImage: `linear-gradient(to right, ${theme.colors.primary}, ${theme.colors.secondary})`
            }}
          >
            Mi Ecommerce
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-6">
            <Link
              to="/"
              className="transition-colors font-medium"
              style={{ color: theme.colors.text }}
              onMouseEnter={(e) => e.currentTarget.style.color = theme.colors.primary}
              onMouseLeave={(e) => e.currentTarget.style.color = theme.colors.text}
            >
              Inicio
            </Link>
            <Link
              to="/catalog"
              className="transition-colors font-medium"
              style={{ color: theme.colors.text }}
              onMouseEnter={(e) => e.currentTarget.style.color = theme.colors.primary}
              onMouseLeave={(e) => e.currentTarget.style.color = theme.colors.text}
            >
              Catálogo
            </Link>
            <Link
              to="/admin"
              className="transition-colors font-semibold"
              style={{ color: theme.colors.primary }}
              onMouseEnter={(e) => e.currentTarget.style.opacity = '0.8'}
              onMouseLeave={(e) => e.currentTarget.style.opacity = '1'}
            >
              Admin
            </Link>
            <button
              onClick={() => setCartOpen(true)}
              className="relative text-white px-4 py-2 rounded-lg transition-all transform hover:scale-105 shadow-md"
              style={{
                backgroundImage: `linear-gradient(to right, ${theme.colors.primary}, ${theme.colors.secondary})`
              }}
            >
              <span className="flex items-center gap-2">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
                Carrito
              </span>
              {itemCount > 0 && (
                <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs font-bold rounded-full w-6 h-6 flex items-center justify-center animate-bounce">
                  {itemCount}
                </span>
              )}
            </button>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="md:hidden p-2 rounded-lg hover:bg-gray-100 transition-colors"
            aria-label="Toggle menu"
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              {mobileMenuOpen ? (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              ) : (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              )}
            </svg>
          </button>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden py-4 border-t border-gray-200">
            <div className="flex flex-col gap-3">
              <Link
                to="/"
                onClick={() => setMobileMenuOpen(false)}
                className="transition-colors font-medium py-2"
                style={{ color: theme.colors.text }}
                onMouseEnter={(e) => e.currentTarget.style.color = theme.colors.primary}
                onMouseLeave={(e) => e.currentTarget.style.color = theme.colors.text}
              >
                Inicio
              </Link>
              <Link
                to="/catalog"
                onClick={() => setMobileMenuOpen(false)}
                className="transition-colors font-medium py-2"
                style={{ color: theme.colors.text }}
                onMouseEnter={(e) => e.currentTarget.style.color = theme.colors.primary}
                onMouseLeave={(e) => e.currentTarget.style.color = theme.colors.text}
              >
                Catálogo
              </Link>
              <Link
                to="/admin"
                onClick={() => setMobileMenuOpen(false)}
                className="transition-colors font-semibold py-2"
                style={{ color: theme.colors.primary }}
                onMouseEnter={(e) => e.currentTarget.style.opacity = '0.8'}
                onMouseLeave={(e) => e.currentTarget.style.opacity = '1'}
              >
                Admin
              </Link>
              <button
                onClick={() => {
                  setCartOpen(true);
                  setMobileMenuOpen(false);
                }}
                className="relative text-white px-4 py-2 rounded-lg transition-all shadow-md text-left flex items-center gap-2"
                style={{
                  backgroundImage: `linear-gradient(to right, ${theme.colors.primary}, ${theme.colors.secondary})`
                }}
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
                Carrito
                {itemCount > 0 && (
                  <span className="ml-auto bg-red-500 text-white text-xs font-bold rounded-full w-6 h-6 flex items-center justify-center">
                    {itemCount}
                  </span>
                )}
              </button>
            </div>
          </div>
        )}
      </div>
    </nav>
    </>
  );
}
