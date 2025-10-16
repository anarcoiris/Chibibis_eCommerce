import React from "react";
import { useCart } from "../context/CartContext";
import { useTheme } from "../context/ThemeContext";

export default function CartModal({ isOpen, onClose }) {
  const { items, itemCount, cartTotal, updateQuantity, removeItem, clearCart } = useCart();
  const { theme } = useTheme();

  if (!isOpen) return null;

  return (
    <>
      {/* Backdrop */}
      <div
        className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40 transition-opacity"
        onClick={onClose}
      />

      {/* Modal */}
      <div className="fixed right-0 top-0 h-full w-full sm:w-96 bg-white shadow-2xl z-50 transform transition-transform">
        <div className="flex flex-col h-full">
          {/* Header */}
          <div
            className="flex items-center justify-between p-6 border-b border-gray-200"
            style={{
              background: `linear-gradient(to right, ${theme.colors.primary}10, ${theme.colors.secondary}10)`
            }}
          >
            <h2
              className="text-2xl font-bold bg-clip-text text-transparent"
              style={{
                backgroundImage: `linear-gradient(to right, ${theme.colors.primary}, ${theme.colors.secondary})`
              }}
            >
              Carrito ({itemCount})
            </h2>
            <button
              onClick={onClose}
              className="p-2 hover:bg-gray-200 rounded-lg transition-colors"
              aria-label="Cerrar carrito"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          {/* Content */}
          <div className="flex-1 overflow-y-auto p-6">
            {items.length === 0 ? (
              <div className="flex flex-col items-center justify-center h-full text-center">
                <svg className="w-24 h-24 text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
                <p className="text-gray-500 text-lg font-medium mb-2">Tu carrito está vacío</p>
                <p className="text-gray-400 text-sm">Añade productos para comenzar tu compra</p>
              </div>
            ) : (
              <div className="space-y-4">
                {items.map((item) => (
                  <div
                    key={item.id}
                    className="flex gap-4 p-4 bg-gradient-to-r from-gray-50 to-white border border-gray-200 rounded-xl hover:shadow-md transition-shadow"
                  >
                    {/* Image */}
                    <div
                      className="w-20 h-20 flex-shrink-0 rounded-lg overflow-hidden"
                      style={{
                        background: `linear-gradient(to bottom right, ${theme.colors.primary}20, ${theme.colors.secondary}20)`
                      }}
                    >
                      <img
                        src={item.image}
                        alt={item.title}
                        className="w-full h-full object-cover"
                      />
                    </div>

                    {/* Details */}
                    <div className="flex-1 min-w-0">
                      <h3 className="font-semibold text-gray-900 truncate">{item.title}</h3>
                      <p className="text-sm text-gray-500 truncate">{item.description}</p>
                      <p className="mt-1 font-bold" style={{ color: theme.colors.primary }}>€{item.price}</p>

                      {/* Quantity Controls */}
                      <div className="flex items-center gap-2 mt-2">
                        <button
                          onClick={() => updateQuantity(item.id, item.quantity - 1)}
                          className="w-8 h-8 flex items-center justify-center bg-gray-200 hover:bg-gray-300 rounded-lg transition-colors"
                          aria-label="Disminuir cantidad"
                        >
                          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20 12H4" />
                          </svg>
                        </button>
                        <span className="w-8 text-center font-semibold">{item.quantity}</span>
                        <button
                          onClick={() => updateQuantity(item.id, item.quantity + 1)}
                          className="w-8 h-8 flex items-center justify-center bg-gray-200 hover:bg-gray-300 rounded-lg transition-colors"
                          aria-label="Aumentar cantidad"
                        >
                          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                          </svg>
                        </button>
                        <button
                          onClick={() => removeItem(item.id)}
                          className="ml-auto text-red-600 hover:text-red-700 p-2 hover:bg-red-50 rounded-lg transition-colors"
                          aria-label="Eliminar producto"
                        >
                          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                          </svg>
                        </button>
                      </div>
                    </div>
                  </div>
                ))}

                {/* Clear Cart Button */}
                {items.length > 1 && (
                  <button
                    onClick={clearCart}
                    className="w-full py-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors font-medium"
                  >
                    Vaciar carrito
                  </button>
                )}
              </div>
            )}
          </div>

          {/* Footer */}
          {items.length > 0 && (
            <div className="border-t border-gray-200 p-6 bg-gray-50">
              {/* Subtotal */}
              <div className="flex justify-between items-center mb-4">
                <span className="text-gray-600">Subtotal:</span>
                <span
                  className="text-2xl font-bold bg-clip-text text-transparent"
                  style={{
                    backgroundImage: `linear-gradient(to right, ${theme.colors.primary}, ${theme.colors.secondary})`
                  }}
                >
                  €{cartTotal.toFixed(2)}
                </span>
              </div>

              {/* Checkout Button */}
              <button
                className="w-full py-3 text-white rounded-lg font-semibold transition-all transform hover:scale-105 shadow-lg mb-3"
                style={{
                  backgroundImage: `linear-gradient(to right, ${theme.colors.primary}, ${theme.colors.secondary})`
                }}
              >
                Proceder al pago
              </button>

              {/* Continue Shopping */}
              <button
                onClick={onClose}
                className="w-full py-3 bg-gray-200 text-gray-700 rounded-lg font-medium hover:bg-gray-300 transition-colors"
              >
                Seguir comprando
              </button>
            </div>
          )}
        </div>
      </div>
    </>
  );
}
