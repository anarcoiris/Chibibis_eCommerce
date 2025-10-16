import React, { useState, useEffect } from "react";
import axios from "axios";

export default function PostManager() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showEditor, setShowEditor] = useState(false);
  const [editingPost, setEditingPost] = useState(null);
  const [formData, setFormData] = useState({
    title: "",
    slug: "",
    content: "",
    excerpt: "",
    status: "draft",
    post_type: "post",
    is_published: false
  });

  useEffect(() => {
    loadPosts();
  }, []);

  const loadPosts = async () => {
    try {
      const response = await axios.get("/api/v1/posts/");
      setPosts(response.data);
    } catch (error) {
      console.error("Error loading posts:", error);
      setPosts([]);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingPost) {
        await axios.patch(`/api/v1/posts/${editingPost.id}`, formData);
      } else {
        await axios.post("/api/v1/posts/", formData);
      }
      loadPosts();
      resetForm();
    } catch (error) {
      alert("Error saving post: " + (error.response?.data?.detail || error.message));
    }
  };

  const handleDelete = async (id) => {
    if (!confirm("Are you sure you want to delete this post?")) return;
    try {
      await axios.delete(`/api/v1/posts/${id}`);
      loadPosts();
    } catch (error) {
      alert("Error deleting post: " + error.message);
    }
  };

  const handleEdit = (post) => {
    setEditingPost(post);
    setFormData({
      title: post.title,
      slug: post.slug,
      content: post.content,
      excerpt: post.excerpt || "",
      status: post.status,
      post_type: post.post_type,
      is_published: post.is_published
    });
    setShowEditor(true);
  };

  const resetForm = () => {
    setFormData({
      title: "",
      slug: "",
      content: "",
      excerpt: "",
      status: "draft",
      post_type: "post",
      is_published: false
    });
    setEditingPost(null);
    setShowEditor(false);
  };

  const generateSlug = (title) => {
    return title
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/(^-|-$)/g, "");
  };

  if (loading) {
    return (
      <div className="text-center py-12">
        <div className="inline-block animate-spin rounded-full h-10 w-10 border-4 border-purple-600 border-t-transparent mb-3"></div>
        <p className="text-gray-600 font-medium">Cargando posts...</p>
      </div>
    );
  }

  if (showEditor) {
    return (
      <div>
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-xl font-bold">
            {editingPost ? "Edit Post" : "Create New Post"}
          </h2>
          <button
            onClick={resetForm}
            className="px-4 py-2 text-gray-600 hover:text-purple-600 transition-colors font-medium"
          >
            ← Volver a la lista
          </button>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Title
            </label>
            <input
              type="text"
              value={formData.title}
              onChange={(e) => {
                setFormData({ ...formData, title: e.target.value });
                if (!editingPost) {
                  setFormData(prev => ({ ...prev, slug: generateSlug(e.target.value) }));
                }
              }}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Slug (URL)
            </label>
            <input
              type="text"
              value={formData.slug}
              onChange={(e) => setFormData({ ...formData, slug: e.target.value })}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Content (HTML supported)
            </label>
            <textarea
              value={formData.content}
              onChange={(e) => setFormData({ ...formData, content: e.target.value })}
              rows={10}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent font-mono text-sm"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Excerpt
            </label>
            <textarea
              value={formData.excerpt}
              onChange={(e) => setFormData({ ...formData, excerpt: e.target.value })}
              rows={3}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>

          <div className="grid grid-cols-3 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Type
              </label>
              <select
                value={formData.post_type}
                onChange={(e) => setFormData({ ...formData, post_type: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="post">Post</option>
                <option value="page">Page</option>
                <option value="banner">Banner</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Status
              </label>
              <select
                value={formData.status}
                onChange={(e) => setFormData({ ...formData, status: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="draft">Draft</option>
                <option value="published">Published</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Published
              </label>
              <label className="flex items-center h-[42px] px-3 py-2 border border-gray-300 rounded-lg cursor-pointer">
                <input
                  type="checkbox"
                  checked={formData.is_published}
                  onChange={(e) => setFormData({ ...formData, is_published: e.target.checked })}
                  className="mr-2"
                />
                <span className="text-sm">{formData.is_published ? "Yes" : "No"}</span>
              </label>
            </div>
          </div>

          <div className="flex gap-3 pt-4">
            <button
              type="submit"
              className="px-6 py-2 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg hover:from-blue-700 hover:to-purple-700 transition-all transform hover:scale-105 shadow-md font-medium"
            >
              {editingPost ? "Actualizar Post" : "Crear Post"}
            </button>
            <button
              type="button"
              onClick={resetForm}
              className="px-6 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-all font-medium"
            >
              Cancelar
            </button>
          </div>
        </form>
      </div>
    );
  }

  return (
    <div>
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-6">
        <h2 className="text-xl sm:text-2xl font-bold text-gray-800">Posts & Content</h2>
        <button
          onClick={() => setShowEditor(true)}
          className="px-6 py-2 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg hover:from-blue-700 hover:to-purple-700 transition-all transform hover:scale-105 shadow-md font-medium"
        >
          + Nuevo Post
        </button>
      </div>

      {posts.length === 0 ? (
        <div className="text-center py-16 bg-gradient-to-br from-purple-50 to-blue-50 rounded-2xl border-2 border-dashed border-purple-300">
          <svg className="w-16 h-16 mx-auto mb-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <p className="text-gray-600 mb-6 text-lg font-medium">No hay posts todavía</p>
          <button
            onClick={() => setShowEditor(true)}
            className="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg hover:from-blue-700 hover:to-purple-700 transition-all transform hover:scale-105 shadow-lg font-medium"
          >
            Crear tu primer Post
          </button>
        </div>
      ) : (
        <div className="space-y-3">
          {posts.map((post) => (
            <div
              key={post.id}
              className="flex flex-col sm:flex-row items-start sm:items-center justify-between p-4 sm:p-5 bg-gradient-to-r from-white to-gray-50 border border-gray-200 rounded-xl hover:shadow-lg hover:border-purple-300 transition-all gap-4"
            >
              <div className="flex-1 min-w-0">
                <h3 className="font-bold text-gray-900 text-lg mb-2 truncate">{post.title}</h3>
                <div className="flex flex-wrap items-center gap-2 text-sm">
                  <span className="px-3 py-1 bg-purple-100 text-purple-700 rounded-full font-medium">
                    {post.post_type}
                  </span>
                  <span className={`px-3 py-1 rounded-full font-medium ${
                    post.is_published
                      ? "bg-green-100 text-green-700"
                      : "bg-yellow-100 text-yellow-700"
                  }`}>
                    {post.is_published ? "Publicado" : "Borrador"}
                  </span>
                  <span className="text-gray-500 truncate">/{post.slug}</span>
                </div>
              </div>
              <div className="flex gap-2 w-full sm:w-auto">
                <button
                  onClick={() => handleEdit(post)}
                  className="flex-1 sm:flex-none px-4 py-2 text-blue-600 hover:bg-blue-50 rounded-lg transition-all font-medium border border-blue-200 hover:border-blue-400"
                >
                  Editar
                </button>
                <button
                  onClick={() => handleDelete(post.id)}
                  className="flex-1 sm:flex-none px-4 py-2 text-red-600 hover:bg-red-50 rounded-lg transition-all font-medium border border-red-200 hover:border-red-400"
                >
                  Eliminar
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
