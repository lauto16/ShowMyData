import { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const API = "http://localhost:5000";

import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import {
  FaFileAlt,
  FaFileCode,
  FaGlobe,
  FaFileImage,
  FaFileVideo,
  FaFileAudio,
  FaFilePdf,
  FaFileArchive,
  FaCog,
  FaDatabase,
  FaCogs,
} from "react-icons/fa";

const TYPE_ICON_MAP = {
  text: <FaFileAlt color="#6c757d" />,
  code: <FaFileCode color="#0d6efd" />,
  web: <FaGlobe color="#20c997" />,
  image: <FaFileImage color="#198754" />,
  video: <FaFileVideo color="#dc3545" />,
  audio: <FaFileAudio color="#fd7e14" />,
  document: <FaFilePdf color="#dc3545" />,
  archive: <FaFileArchive color="#6f42c1" />,
  executable: <FaCogs color="#212529" />,
  database: <FaDatabase color="#0dcaf0" />,
  config: <FaCog color="#adb5bd" />,
  default: <FaFileAlt />,
};

const TYPES_SP = {
  "text": "Texto",
  "code": "Código",
  "web": "Web",
  "image": "Imagen",
  "video": "Video",
  "audio": "Audio",
  "document": "Documento",
  "archive": "Archivo",
  "executable": "Ejecutable",
  "database": "Base de datos",
  "config": "Configuracion",
  "default": "Default"
}

const getFileIcon = (type) => {
  return TYPE_ICON_MAP[type] || TYPE_ICON_MAP.default;
};

function App() {

  const [authenticated, setAuthenticated] = useState(false);
  const [password, setPassword] = useState("");

  const [files, setFiles] = useState([]);
  const [selectedFiles, setSelectedFiles] = useState(new Set());
  const [search, setSearch] = useState("");

  const fetchFiles = async () => {
    try {
      const res = await fetch(`${API}/files`);
      const data = await res.json();
      setFiles(data.files || []);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    if (authenticated) {
      fetchFiles();
    }
  }, [authenticated]);

  const handleLogin = async () => {
    if (!password) {
      toast.error("Ingrese contraseña");
      return;
    }

    try {
      const res = await fetch(`${API}/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ password })
      });

      if (!res.ok) {
        toast.error("Contraseña incorrecta");
        return;
      }

      setAuthenticated(true);

    } catch (err) {
      console.error(err);
      toast.error("Error de conexión");
    }
  };

  const handleUpload = async (e) => {

    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {

      await fetch(`${API}/upload`, {
        method: "POST",
        body: formData
      });

      fetchFiles();

    } catch (err) {
      console.error(err);
    }
  };

  const toggleSelect = (path) => {

    const newSet = new Set(selectedFiles);

    if (newSet.has(path)) {
      newSet.delete(path);
    } else {
      newSet.add(path);
    }

    setSelectedFiles(newSet);
  };

  const deleteSelected = async () => {

    if (selectedFiles.size === 0) return;

    try {

      await fetch(`${API}/files`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          files: Array.from(selectedFiles)
        })
      });

      setSelectedFiles(new Set());
      fetchFiles();

    } catch (err) {
      console.error(err);
    }
  };

  const filteredFiles = files.filter((file) =>
    file.path.toLowerCase().includes(search.toLowerCase())
  );

  if (!authenticated) {

    return (


      <div className="container vh-100 d-flex justify-content-center align-items-center">
        <ToastContainer />

        <div className="card p-4 shadow" style={{ width: "350px" }}>

          <h2 className="text-center mb-3">ShowMyData</h2>

          <input
            type="password"
            className="form-control mb-3"
            placeholder="Contraseña"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button
            className="btn btn-primary w-100"
            onClick={handleLogin}
          >
            Entrar
          </button>

        </div>

      </div>
    );
  }

  return (

      <div className="container mt-4">
      <ToastContainer />

        <h1 className="text-center mb-4">ShowMyData</h1>

        <div className="row mb-3">

          <div className="col-md-4">
            <input
              type="file"
              className="form-control"
              onChange={handleUpload}
            />
          </div>

          <div className="col-md-4">
            <input
              type="text"
              className="form-control"
              placeholder="Buscar archivo..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
          </div>

          <div className="col-md-4">
            <button
              className="btn btn-danger w-100"
              onClick={deleteSelected}
            >
              Borrar seleccionados
            </button>
          </div>

        </div>

        <div className="card shadow">

          <div className="card-body">

            <table className="table table-hover">

              <thead>
                <tr>
                  <th></th>
                  <th></th>
                  <th>Archivo</th>
                  <th>Tipo</th>
                </tr>
              </thead>

              <tbody>
                {filteredFiles.map((file) => (
                  <tr key={file.hash}>
                    <td>
                      <input
                        type="checkbox"
                        checked={selectedFiles.has(file.path)}
                        onChange={() => toggleSelect(file.path)}
                      />
                    </td>

                    <td style={{ fontSize: "1.2rem" }}>
                      {getFileIcon(file.type)}
                    </td>

                    <td>{file.path}</td>
                    <td>{TYPES_SP[file.type]}</td>
                  </tr>
                ))}

              </tbody>

            </table>

          </div>

        </div>

      </div>
  );
}

export default App;