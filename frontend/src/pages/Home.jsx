import React, {useEffect, useState} from "react";
import axios from "axios";
import ProductCard from "../components/ProductCard";

export default function Home(){
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(()=>{
    axios.get("/api/v1/products/")
      .then(r => {
        setProducts(r.data);
        setLoading(false);
      })
      .catch(err => {
        setError("Error loading products");
        setLoading(false);
      });
  },[]);

  if (loading) {
    return (
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="flex items-center justify-center min-h-[50vh]">
          <div className="text-center">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-4 border-white border-t-transparent mb-4"></div>
            <p className="text-white text-lg font-medium">Cargando productos...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="bg-red-500/20 backdrop-blur-sm border border-red-500/50 rounded-2xl p-6 text-center">
          <p className="text-white text-lg">{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12">
      {/* Hero Section */}
      <div className="text-center mb-12 sm:mb-16">
        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-white mb-4 drop-shadow-lg">
          Bienvenido a Mi Ecommerce
        </h1>
        <p className="text-lg sm:text-xl text-white/90 max-w-2xl mx-auto drop-shadow-md">
          Descubre nuestra selección de productos exclusivos
        </p>
      </div>

      {/* Products Section */}
      <div className="mb-8">
        <h2 className="text-2xl sm:text-3xl lg:text-4xl font-bold text-white mb-6 sm:mb-8 drop-shadow-lg">
          Novedades
        </h2>
        {products.length === 0 ? (
          <div className="bg-white/10 backdrop-blur-sm border border-white/20 rounded-2xl p-12 text-center">
            <p className="text-white text-lg">No hay productos disponibles</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 sm:gap-6 lg:gap-8">
            {products.map(p => (
              <ProductCard key={p.id} product={p} />
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
