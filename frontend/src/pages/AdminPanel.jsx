import React, { useState } from "react";
import PostManager from "../components/admin/PostManager";
import DesignEditor from "../components/admin/DesignEditor";

export default function AdminPanel() {
  const [activeTab, setActiveTab] = useState("posts");

  return (
    <div className="min-h-screen pb-12">
      {/* Header */}
      <div className="bg-white/90 backdrop-blur-md shadow-lg mb-6">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">
          <h1 className="text-3xl sm:text-4xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
            Admin Panel
          </h1>
          <p className="text-gray-600 mt-2 text-sm sm:text-base">Gestiona tu contenido y diseño</p>
        </div>
      </div>

      {/* Tabs */}
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-white/95 backdrop-blur-sm rounded-2xl shadow-xl overflow-hidden">
          <div className="border-b border-gray-200">
            <nav className="flex flex-wrap -mb-px">
              <button
                onClick={() => setActiveTab("posts")}
                className={`px-4 sm:px-6 py-3 font-medium text-sm sm:text-base border-b-2 transition-all ${
                  activeTab === "posts"
                    ? "border-purple-500 text-purple-600 bg-purple-50/50"
                    : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
                }`}
              >
                Posts & Content
              </button>
              <button
                onClick={() => setActiveTab("design")}
                className={`px-4 sm:px-6 py-3 font-medium text-sm sm:text-base border-b-2 transition-all ${
                  activeTab === "design"
                    ? "border-purple-500 text-purple-600 bg-purple-50/50"
                    : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
                }`}
              >
                Visual Design
              </button>
            </nav>
          </div>

          {/* Tab Content */}
          <div className="p-4 sm:p-6 lg:p-8 min-h-[500px]">
            {activeTab === "posts" && <PostManager />}
            {activeTab === "design" && <DesignEditor />}
          </div>
        </div>
      </div>
    </div>
  );
}
