import { useState } from 'react';
import { BsPerson } from 'react-icons/bs';
import { Link } from 'react-router-dom';
import './DashboardPage.css';

const MainPage = () => {
  const [nombres, setNombres] = useState('');
  const [apellidos, setApellidos] = useState('');
  const [fechaNacimiento, setFechaNacimiento] = useState('');
  const [ci, setCI] = useState('');
  const [genero, setGenero] = useState('');
  const [telefono, setTelefono] = useState('');
  const [email, setEmail] = useState('');
  const [tipoSanguineo, setTipoSanguineo] = useState('');
  const [direccionCompleta, setDireccionCompleta] = useState('');
  const [ciudad, setCiudad] = useState('');
  const [provincia, setProvincia] = useState('');
  const [pais, setPais] = useState('');

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const formData = {
      datos_personales: {
        nombres,
        apellidos,
        fecha_nacimiento: fechaNacimiento,
        ci: parseInt(ci),
        genero,
        telefono: parseInt(telefono),
        email,
        tipo_sanguineo: tipoSanguineo,
      },
      direccion: {
        direccion: direccionCompleta,
        ciudad,
        provincia,
        pais,
      },
      paciente:{
        paciente:true
      }
    };

    try {
      const response = await fetch('http://192.168.100.47:8000/insert_register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        console.log('Data sent successfully!');
        // Reset form fields
        setNombres('');
        setApellidos('');
        setFechaNacimiento('');
        setCI('');
        setGenero('');
        setTelefono('');
        setEmail('');
        setTipoSanguineo('');
        setDireccionCompleta('');
        setCiudad('');
        setProvincia('');
        setPais('');
      } else {
        console.error('Error:', response.statusText);
      }
    } catch (error) {
      console.error('Error:', error);
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
              <label>Nombre:</label>
              <input type="text" className="input-field" required value={nombres} onChange={(e) => setNombres(e.target.value)} />
  
              <label>Fecha de Nacimiento:</label>
              <input type="text" className="input-field" required value={fechaNacimiento} onChange={(e) => setFechaNacimiento(e.target.value)} />
  
              <label>Género:</label>
              <input type="text" className="input-field" required value={genero} onChange={(e) => setGenero(e.target.value)} />
  
              <label>Teléfono:</label>
              <input type="text" className="input-field" required value={telefono} onChange={(e) => setTelefono(e.target.value)} />
  
              <label>Dirección:</label>
              <input type="text" className="input-field" required value={direccionCompleta} onChange={(e) => setDireccionCompleta(e.target.value)} />
  
              <label>Ciudad:</label>
              <input type="text" className="input-field" required value={ciudad} onChange={(e) => setCiudad(e.target.value)} />
            </form>
          </div>
  
          <div className="form-column">
            {/* Columna 2 */}
            <form onSubmit={handleSubmit} className='form'>
              <label>Apellidos:</label>
              <input type="text" className="input-field" required value={apellidos} onChange={(e) => setApellidos(e.target.value)} />
  
              <label>Cédula de Identidad:</label>
              <input type="text" className="input-field" required value={ci} onChange={(e) => setCI(e.target.value)} />
  
              <label>Tipo de Sangre:</label>
              <input type="text" className="input-field" required value={tipoSanguineo} onChange={(e) => setTipoSanguineo(e.target.value)} />
  
              <label>Email:</label>
              <input type="text" className="input-field" required value={email} onChange={(e) => setEmail(e.target.value)} />
  
              <label>País:</label>
              <input type="text" className="input-field" required value={pais} onChange={(e) => setPais(e.target.value)} />
  
              <label>Provincia:</label>
              <input type="text" className="input-field" required value={provincia} onChange={(e) => setProvincia(e.target.value)} />
  
              <button type="submit">Agregar</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
  
};

export default MainPage;
