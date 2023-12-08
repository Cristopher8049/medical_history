import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './NewCampaingPage.css';

function NewCampaignPage() {
  const [inputValue, setInputValue] = useState('');
  const [jsonData, setJSONData] = useState(null);

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.get(`http://192.168.100.47:8000/get_patient_info?card_id=${inputValue}`);
      setJSONData(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const renderData = () => {
    if (jsonData) {
      return (
        <div className="table-container">
          <table className="rendered-table">
            <tbody>
              {Object.keys(jsonData).map((key) => (
                <tr key={key}>
                  <td className="blue-text">{key}</td>
                  <td className="white-text">{jsonData[key]}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="dashboard-container">
      <div className="fondo">
        <h1>Consulta</h1>
        <form onSubmit={handleFormSubmit}>
          <input
            type="text"
            placeholder="ID Paciente"
            value={inputValue}
            onChange={handleInputChange}
            className = "new-campaing-name"
          />
          <button type="submit">Submit</button>
        </form>
        {renderData()}
      </div>
    </div>
  );
}

export default NewCampaignPage;