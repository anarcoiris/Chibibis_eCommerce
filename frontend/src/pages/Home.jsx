import React, {useEffect, useState} from "react";
import axios from "axios";

export default function Home(){
  const [products, setProducts] = useState([]);

  useEffect(()=>{
    axios.get("/api/v1/products/").then(r=>setProducts(r.data)).catch(()=>{})
  },[]);

  return (
    <div style={{padding:20}}>
      <h2>Novedades</h2>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(220px,1fr))',gap:16}}>
        {products.map(p=>(
          <div key={p.id} style={{background:'#fff',borderRadius:12,padding:12,boxShadow:'0 6px 18px rgba(0,0,0,0.06)'}}>
            <img src={p.image} alt={p.title} style={{width:'100%',height:140,objectFit:'cover',borderRadius:8}}/>
            <h3>{p.title}</h3>
            <p style={{fontSize:13,color:'#555'}}>{p.description}</p>
            <strong>{p.price} €</strong>
          </div>
        ))}
      </div>
    </div>
  )
}
