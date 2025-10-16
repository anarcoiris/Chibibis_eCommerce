import React, { createContext, useContext, useState, useEffect } from "react";
import axios from "axios";

const ThemeContext = createContext();

// Default theme configuration
const defaultTheme = {
  colors: {
    primary: "#3B82F6",
    secondary: "#10B981",
    background: "#FFFFFF",
    text: "#1F2937",
    accent: "#F59E0B"
  },
  typography: {
    heading_font: "Inter",
    body_font: "Inter",
    heading_size: "2xl",
    body_size: "base"
  },
  layout: {
    container_width: "1280px",
    spacing: "normal",
    border_radius: "md"
  },
  components: {
    button_style: "rounded",
    card_shadow: "md",
    navbar_style: "sticky"
  }
};

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(defaultTheme);
  const [loading, setLoading] = useState(true);
  const [designId, setDesignId] = useState(null);

  // Load active design from API
  useEffect(() => {
    loadActiveDesign();
  }, []);

  const loadActiveDesign = async () => {
    try {
      const response = await axios.get("/api/v1/design/active");
      if (response.data) {
        const loadedTheme = {
          colors: response.data.colors || defaultTheme.colors,
          typography: response.data.typography || defaultTheme.typography,
          layout: response.data.layout || defaultTheme.layout,
          components: response.data.components || defaultTheme.components
        };
        setTheme(loadedTheme);
        setDesignId(response.data.id);
        console.log("Theme loaded:", loadedTheme);
      }
    } catch (error) {
      console.error("Error loading theme:", error);
      // Use default theme on error
    } finally {
      setLoading(false);
    }
  };

  // Update theme (called by DesignEditor)
  const updateTheme = (newTheme) => {
    setTheme(newTheme);
  };

  // Reload theme after save
  const reloadTheme = () => {
    loadActiveDesign();
  };

  const value = {
    theme,
    loading,
    designId,
    updateTheme,
    reloadTheme
  };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error("useTheme must be used within a ThemeProvider");
  }
  return context;
}
