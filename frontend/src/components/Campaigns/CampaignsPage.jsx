import React, { useState } from 'react';
import axios from 'axios';

function CampaignsPage() {
  const [paciente, setPaciente] = useState('');
  const [medico, setMedico] = useState('');
  const [laboratorio, setLaboratorio] = useState('');
  const [clinica, setClinica] = useState('');
  const [diagnostico, setDiagnostico] = useState('');
  const [fecha, setFecha] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = {
      datos_personales: {
        diagnostico,
        medico: parseInt(medico),
        laboratorio,
        paciente: parseInt(paciente),
        fecha,
        clinica: parseInt(clinica),
      },
    };

    try {
      const response = await axios.post('http://192.168.100.47:8000/insert_triaje', formData);

      if (response.data.success) {
        console.log('Data sent successfully!');
        // Reset form fields
        setPaciente('');
        setMedico('');
        setLaboratorio('');
        setClinica('');
        setDiagnostico('');
        setFecha('');
      } else {
        console.error('Error:', response.data.error);
      }
    } catch (error) {
      console.error('Error:', error.message);
    }
  };

  return (
    <div className="dashboard-container">
      <div className="content-2">
        <h1>Registrar Paciente</h1>
        <div className="form-container">
          <div className="form-column">
            <form onSubmit={handleSubmit} className='form'>
              {/* Columna 1 */}
              <label>Paciente CI:</label>
              <input type="text" className="input-field" required value={paciente} onChange={(e) => setPaciente(e.target.value)} />

              <label>Analisis:</label>
              <input type="text" className="input-field" required value={laboratorio} onChange={(e) => setLaboratorio(e.target.value)} />

              <label>Diagnostico:</label>
              <input type="text" className="input-field" required value={diagnostico} onChange={(e) => setDiagnostico(e.target.value)} />
              <button type="submit">Agregar</button>
            </form>
          </div>

          <div className="form-column">
            {/* Columna 2 */}
            <form onSubmit={handleSubmit} className='form'>
              <label>Matricula Doctor:</label>
              <input type="text" className="input-field" required value={medico} onChange={(e) => setMedico(e.target.value)} />
              <label>Fecha:</label>
              <input type="text" className="input-field" required value={fecha} onChange={(e) => setFecha(e.target.value)} />
              <label>Clinica:</label>
              <input type="text" className="input-field" required value={clinica} onChange={(e) => setClinica(e.target.value)} />
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default CampaignsPage;
