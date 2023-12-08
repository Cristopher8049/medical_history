import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import './CampaignCollectionPage.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSpinner } from '@fortawesome/free-solid-svg-icons';

function CampaignCollectionPage() {
  const { collectionName } = useParams();
  const [collectionData, setCollectionData] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isUploaded, setIsUploaded] = useState(false);

  useEffect(() => {
    fetchCollectionData();
  }, [collectionName]);

  const fetchCollectionData = async () => {
    try {
      const response = await axios.get(`http://localhost:5050/campaigns/${collectionName}`);
      setCollectionData(response.data.documents);
    } catch (error) {
      console.error('Error al obtener los datos de la colección:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        await axios.post(`http://localhost:5050/campaigns/${collectionName}/upload`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        // Actualizar los datos de la colección después de subir el archivo
        fetchCollectionData();
        setIsUploaded(true);
      } catch (error) {
        console.error('Error al subir el archivo:', error);
      }
    }
  };

  return (
    <div className="dashboard-container">
      <h1>{collectionName}</h1>

      <div className="table-container">
        {isLoading ? (
          <div className="loading-overlay">
            <FontAwesomeIcon icon={faSpinner} spin size="3x" className="spinner" />
          </div>
        ) : collectionData && collectionData.length > 0 ? (
          <table>
            <thead>
              <tr>
                {Object.keys(collectionData[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {collectionData.map((item, index) => (
                <tr key={index}>
                  {Object.entries(item).map(([key, value]) => (
                    <td key={key}>
                      {key === 'img' || key === 'pdf' ? (value !== 'null' ? 'yes' : 'no') : value}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <div>{collectionData ? 'La colección está vacía' : 'Cargando...'}</div>
        )}
      </div>
      {collectionData && (
        <div className="row-count">
          Filas: {collectionData.length}
        </div>
      )}
      <div className="input-container">
        <input type="file" onChange={handleFileChange} className="input-file" accept=".csv" />
        <button className="minimal-button" onClick={handleUpload}>Agregar</button>
        {isUploaded}
      </div>
      <div className="button-container">
        <button className="minimal-button">Eliminar</button>
      </div>
    </div>
  );
}

export default CampaignCollectionPage;
