import React, { useEffect, useRef } from "react";
import { useTheme } from "../context/ThemeContext";

// Helper function to convert hex color to RGB
const hexToRgb = (hex) => {
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : { r: 59, g: 130, b: 246 }; // Default to blue if parsing fails
};

export default function AnimatedBackground() {
  const { theme } = useTheme();
  const canvasRef = useRef(null);
  const mousePos = useRef({ x: 0, y: 0 });
  const particles = useRef([]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    let animationFrameId;
    let time = 0;

    // Set canvas size
    const resizeCanvas = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };
    resizeCanvas();
    window.addEventListener("resize", resizeCanvas);

    // Track mouse position
    const handleMouseMove = (e) => {
      mousePos.current = {
        x: e.clientX,
        y: e.clientY,
      };
    };
    window.addEventListener("mousemove", handleMouseMove);

    // Initialize particles
    const particleCount = Math.min(80, Math.floor(window.innerWidth / 15));
    particles.current = Array.from({ length: particleCount }, () => ({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      radius: Math.random() * 2 + 1,
    }));

    // Get theme colors and convert to RGB
    const primaryRgb = hexToRgb(theme.colors.primary);
    const secondaryRgb = hexToRgb(theme.colors.secondary);

    // Animation loop
    const animate = () => {
      time += 0.005;

      // Create breathing gradient background using theme colors
      const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      const breathe = Math.sin(time) * 0.5 + 0.5; // Oscillates between 0 and 1

      // Darken the primary color for background
      const darkPrimaryR = Math.max(0, primaryRgb.r * 0.2);
      const darkPrimaryG = Math.max(0, primaryRgb.g * 0.2);
      const darkPrimaryB = Math.max(0, primaryRgb.b * 0.2);

      // Use secondary color for middle with some variation
      const midSecondaryR = secondaryRgb.r * (0.3 + breathe * 0.2);
      const midSecondaryG = secondaryRgb.g * (0.3 + breathe * 0.2);
      const midSecondaryB = secondaryRgb.b * (0.3 + breathe * 0.2);

      gradient.addColorStop(0, `rgba(${darkPrimaryR + breathe * 20}, ${darkPrimaryG + breathe * 20}, ${darkPrimaryB + breathe * 30}, 1)`);
      gradient.addColorStop(0.5, `rgba(${midSecondaryR}, ${midSecondaryG}, ${midSecondaryB}, 1)`);
      gradient.addColorStop(1, `rgba(${darkPrimaryR + breathe * 20}, ${darkPrimaryG + breathe * 20}, ${darkPrimaryB + breathe * 30}, 1)`);

      ctx.fillStyle = gradient;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Update and draw particles
      particles.current.forEach((particle, i) => {
        // Move particle
        particle.x += particle.vx;
        particle.y += particle.vy;

        // Bounce off edges
        if (particle.x < 0 || particle.x > canvas.width) particle.vx *= -1;
        if (particle.y < 0 || particle.y > canvas.height) particle.vy *= -1;

        // Mouse attraction
        const dx = mousePos.current.x - particle.x;
        const dy = mousePos.current.y - particle.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < 150) {
          const force = (150 - distance) / 150;
          particle.vx += (dx / distance) * force * 0.05;
          particle.vy += (dy / distance) * force * 0.05;
        }

        // Limit velocity
        const maxSpeed = 2;
        const speed = Math.sqrt(particle.vx * particle.vx + particle.vy * particle.vy);
        if (speed > maxSpeed) {
          particle.vx = (particle.vx / speed) * maxSpeed;
          particle.vy = (particle.vy / speed) * maxSpeed;
        }

        // Draw particle
        ctx.beginPath();
        ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
        ctx.fill();

        // Draw connections
        particles.current.slice(i + 1).forEach((otherParticle) => {
          const dx = particle.x - otherParticle.x;
          const dy = particle.y - otherParticle.y;
          const distance = Math.sqrt(dx * dx + dy * dy);

          if (distance < 120) {
            ctx.beginPath();
            ctx.moveTo(particle.x, particle.y);
            ctx.lineTo(otherParticle.x, otherParticle.y);
            const opacity = (1 - distance / 120) * 0.3;
            ctx.strokeStyle = `rgba(255, 255, 255, ${opacity})`;
            ctx.lineWidth = 0.5;
            ctx.stroke();
          }
        });
      });

      animationFrameId = requestAnimationFrame(animate);
    };

    animate();

    // Cleanup
    return () => {
      window.removeEventListener("resize", resizeCanvas);
      window.removeEventListener("mousemove", handleMouseMove);
      cancelAnimationFrame(animationFrameId);
    };
  }, [theme]); // Re-run effect when theme changes

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        width: "100vw",
        height: "100vh",
        zIndex: -1,
        pointerEvents: "none"
      }}
    />
  );
}
