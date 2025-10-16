import React, { useState, useEffect } from "react";
import axios from "axios";
import { useTheme } from "../../context/ThemeContext";

export default function DesignEditor() {
  const { theme, designId, updateTheme, reloadTheme } = useTheme();
  const [design, setDesign] = useState(theme);
  const [preview, setPreview] = useState(true);

  // Update local state when theme context changes (on mount or reload)
  useEffect(() => {
    setDesign(theme);
  }, [theme]);

  const handleSave = async () => {
    try {
      if (designId) {
        await axios.patch(`/api/v1/design/${designId}`, {
          colors: design.colors,
          typography: design.typography,
          layout: design.layout,
          components: design.components,
          is_active: true
        });
      } else {
        await axios.post("/api/v1/design/", {
          name: "Custom Design " + new Date().toISOString(),
          colors: design.colors,
          typography: design.typography,
          layout: design.layout,
          components: design.components,
          is_active: true
        });
      }
      alert("Design saved successfully!");
      // Reload theme from API to update entire site
      reloadTheme();
    } catch (error) {
      alert("Error saving design: " + error.message);
    }
  };

  const updateColor = (key, value) => {
    const newDesign = {
      ...design,
      colors: { ...design.colors, [key]: value }
    };
    setDesign(newDesign);
    // Update theme context in real-time for live preview across site
    updateTheme(newDesign);
  };

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-xl font-bold" style={{ color: theme.colors.text }}>Visual Design Editor</h2>
        <div className="flex gap-2">
          <button
            onClick={() => setPreview(!preview)}
            className="px-4 py-2 rounded-lg transition-colors"
            style={{
              backgroundColor: `${theme.colors.primary}20`,
              color: theme.colors.text
            }}
          >
            {preview ? "Hide" : "Show"} Preview
          </button>
          <button
            onClick={handleSave}
            className="px-4 py-2 text-white rounded-lg transition-colors"
            style={{
              backgroundImage: `linear-gradient(to right, ${theme.colors.primary}, ${theme.colors.secondary})`
            }}
          >
            Save Design
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Design Controls */}
        <div className="space-y-6">
          {/* Colors Section */}
          <div className="bg-white p-4 rounded-lg border border-gray-200">
            <h3 className="font-semibold text-lg mb-4" style={{ color: theme.colors.text }}>Colors</h3>
            <div className="space-y-3">
              {Object.entries(design.colors).map(([key, value]) => (
                <div key={key} className="flex items-center gap-3">
                  <label className="w-32 text-sm font-medium capitalize" style={{ color: theme.colors.text }}>
                    {key.replace("_", " ")}
                  </label>
                  <input
                    type="color"
                    value={value}
                    onChange={(e) => updateColor(key, e.target.value)}
                    className="w-16 h-10 rounded border border-gray-300 cursor-pointer"
                  />
                  <input
                    type="text"
                    value={value}
                    onChange={(e) => updateColor(key, e.target.value)}
                    className="flex-1 px-3 py-2 border border-gray-300 rounded-lg text-sm font-mono"
                  />
                </div>
              ))}
            </div>
          </div>

          {/* Typography Section */}
          <div className="bg-white p-4 rounded-lg border border-gray-200">
            <h3 className="font-semibold text-lg mb-4" style={{ color: theme.colors.text }}>Typography</h3>
            <div className="space-y-3">
              <div>
                <label className="block text-sm font-medium mb-1" style={{ color: theme.colors.text }}>
                  Heading Font
                </label>
                <select
                  value={design.typography.heading_font}
                  onChange={(e) => {
                    const newDesign = {
                      ...design,
                      typography: { ...design.typography, heading_font: e.target.value }
                    };
                    setDesign(newDesign);
                    updateTheme(newDesign);
                  }}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                >
                  <option value="Inter">Inter</option>
                  <option value="Roboto">Roboto</option>
                  <option value="Open Sans">Open Sans</option>
                  <option value="Poppins">Poppins</option>
                  <option value="Montserrat">Montserrat</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium mb-1" style={{ color: theme.colors.text }}>
                  Body Font
                </label>
                <select
                  value={design.typography.body_font}
                  onChange={(e) => {
                    const newDesign = {
                      ...design,
                      typography: { ...design.typography, body_font: e.target.value }
                    };
                    setDesign(newDesign);
                    updateTheme(newDesign);
                  }}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                >
                  <option value="Inter">Inter</option>
                  <option value="Roboto">Roboto</option>
                  <option value="Open Sans">Open Sans</option>
                  <option value="Lato">Lato</option>
                  <option value="Source Sans Pro">Source Sans Pro</option>
                </select>
              </div>
            </div>
          </div>

          {/* Layout Section */}
          <div className="bg-white p-4 rounded-lg border border-gray-200">
            <h3 className="font-semibold text-lg mb-4" style={{ color: theme.colors.text }}>Layout</h3>
            <div className="space-y-3">
              <div>
                <label className="block text-sm font-medium mb-1" style={{ color: theme.colors.text }}>
                  Border Radius
                </label>
                <select
                  value={design.layout.border_radius}
                  onChange={(e) => {
                    const newDesign = {
                      ...design,
                      layout: { ...design.layout, border_radius: e.target.value }
                    };
                    setDesign(newDesign);
                    updateTheme(newDesign);
                  }}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                >
                  <option value="none">None</option>
                  <option value="sm">Small</option>
                  <option value="md">Medium</option>
                  <option value="lg">Large</option>
                  <option value="xl">Extra Large</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium mb-1" style={{ color: theme.colors.text }}>
                  Spacing
                </label>
                <select
                  value={design.layout.spacing}
                  onChange={(e) => {
                    const newDesign = {
                      ...design,
                      layout: { ...design.layout, spacing: e.target.value }
                    };
                    setDesign(newDesign);
                    updateTheme(newDesign);
                  }}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                >
                  <option value="compact">Compact</option>
                  <option value="normal">Normal</option>
                  <option value="relaxed">Relaxed</option>
                </select>
              </div>
            </div>
          </div>
        </div>

        {/* Preview Panel */}
        {preview && (
          <div className="bg-gray-50 p-6 rounded-lg border border-gray-200">
            <h3 className="font-semibold text-lg mb-4" style={{ color: theme.colors.text }}>Live Preview</h3>

            <div className="space-y-4" style={{
              backgroundColor: design.colors.background,
              color: design.colors.text,
              fontFamily: design.typography.body_font,
              padding: "1.5rem",
              borderRadius: design.layout.border_radius === "none" ? "0" :
                design.layout.border_radius === "sm" ? "0.25rem" :
                design.layout.border_radius === "lg" ? "1rem" :
                design.layout.border_radius === "xl" ? "1.5rem" : "0.5rem"
            }}>
              {/* Sample Heading */}
              <h1 style={{
                color: design.colors.primary,
                fontFamily: design.typography.heading_font,
                fontSize: "2rem",
                fontWeight: "bold"
              }}>
                Sample Heading
              </h1>

              {/* Sample Paragraph */}
              <p style={{ color: design.colors.text }}>
                This is how your body text will look. The quick brown fox jumps over the lazy dog.
              </p>

              {/* Sample Button */}
              <button style={{
                backgroundColor: design.colors.primary,
                color: "#FFFFFF",
                padding: "0.5rem 1.5rem",
                borderRadius: design.layout.border_radius === "none" ? "0" :
                  design.layout.border_radius === "sm" ? "0.25rem" :
                  design.layout.border_radius === "lg" ? "1rem" :
                  design.layout.border_radius === "xl" ? "1.5rem" : "0.5rem",
                border: "none",
                fontWeight: "500",
                cursor: "pointer"
              }}>
                Primary Button
              </button>

              {/* Sample Card */}
              <div style={{
                backgroundColor: "#FFFFFF",
                padding: "1rem",
                borderRadius: design.layout.border_radius === "none" ? "0" :
                  design.layout.border_radius === "sm" ? "0.25rem" :
                  design.layout.border_radius === "lg" ? "1rem" :
                  design.layout.border_radius === "xl" ? "1.5rem" : "0.5rem",
                boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
                border: `1px solid ${design.colors.secondary}20`
              }}>
                <h3 style={{
                  color: design.colors.secondary,
                  fontWeight: "600",
                  marginBottom: "0.5rem"
                }}>
                  Sample Card
                </h3>
                <p style={{
                  color: design.colors.text,
                  fontSize: "0.875rem"
                }}>
                  This is a preview card showing your design colors and typography.
                </p>
              </div>

              {/* Color Palette */}
              <div className="mt-6">
                <p className="text-sm font-medium mb-2" style={{ color: design.colors.text }}>
                  Color Palette:
                </p>
                <div className="flex gap-2">
                  {Object.entries(design.colors).map(([key, value]) => (
                    <div key={key} className="text-center">
                      <div
                        style={{
                          width: "50px",
                          height: "50px",
                          backgroundColor: value,
                          borderRadius: "0.5rem",
                          border: "2px solid #E5E7EB"
                        }}
                      />
                      <p className="text-xs mt-1" style={{ color: design.colors.text }}>
                        {key}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
