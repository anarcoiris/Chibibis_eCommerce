import React, { useState } from "react";
import { useCart } from "../context/CartContext";
import { useTheme } from "../context/ThemeContext";

export default function ProductCard({ product }) {
  const { addItem } = useCart();
  const { theme } = useTheme();
  const [adding, setAdding] = useState(false);

  const handleAddToCart = () => {
    setAdding(true);
    addItem(product);
    setTimeout(() => setAdding(false), 600);
  };

  return (
    <article className="group bg-white/95 backdrop-blur-sm rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden hover:-translate-y-2">
      {/* Image Container */}
      <div
        className="relative overflow-hidden h-48 sm:h-56"
        style={{
          background: `linear-gradient(to bottom right, ${theme.colors.primary}20, ${theme.colors.secondary}20)`
        }}
      >
        <img
          src={product.image}
          alt={product.title}
          className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-110"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
      </div>

      {/* Content */}
      <div className="p-4 sm:p-5">
        <h3
          className="text-lg sm:text-xl font-bold mb-2 line-clamp-2 transition-colors"
          style={{ color: theme.colors.text }}
          onMouseEnter={(e) => e.currentTarget.style.color = theme.colors.primary}
          onMouseLeave={(e) => e.currentTarget.style.color = theme.colors.text}
        >
          {product.title}
        </h3>
        <p className="text-sm mb-4 line-clamp-2" style={{ color: theme.colors.text, opacity: 0.7 }}>
          {product.description}
        </p>

        {/* Price and Button */}
        <div className="flex items-center justify-between mt-auto">
          <div className="flex flex-col">
            <span
              className="text-2xl font-bold bg-clip-text text-transparent"
              style={{
                backgroundImage: `linear-gradient(to right, ${theme.colors.primary}, ${theme.colors.secondary})`
              }}
            >
              €{product.price}
            </span>
          </div>
          <button
            onClick={handleAddToCart}
            disabled={adding}
            className={`px-4 py-2 text-white rounded-lg font-medium transition-all transform hover:scale-105 shadow-md hover:shadow-lg flex items-center gap-2 ${adding ? 'scale-110' : ''}`}
            style={{
              backgroundImage: `linear-gradient(to right, ${theme.colors.primary}, ${theme.colors.secondary})`
            }}
          >
            {adding ? (
              <>
                <svg className="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
                ¡Añadido!
              </>
            ) : (
              <>
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
                Añadir
              </>
            )}
          </button>
        </div>
      </div>
    </article>
  );
}
