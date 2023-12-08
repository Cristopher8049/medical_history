import React, { useState, useEffect } from 'react';
import { Link, useLocation} from 'react-router-dom';
import { AiFillHome, AiFillTags, } from "react-icons/ai";
import { HiOutlineLogout , HiDeviceMobile } from 'react-icons/hi';
import { IoPhonePortraitOutline } from 'react-icons/io5';
import { HiArchive } from "react-icons/hi";
import { FaFileSignature } from "react-icons/fa";
import { FaBriefcaseMedical } from "react-icons/fa";
import { CiMedicalCross } from "react-icons/ci";
import "./Sidebar.css";

function Sidebar() {
  const location = useLocation();
  const [activeLink, setActiveLink] = useState('/');

  useEffect(() => {
    setActiveLink(location.pathname);
  }, [location]);

  const isCampaignCollectionPage = activeLink.startsWith('/campaigns/');
  

  return (
    <div className="sidebar">
      <div className='container'>
        <h2 className='logo'> Health App</h2>
      </div>

      <ul>
        <li className={activeLink === '/' ? 'active' : ''}>
          <Link to="/">
            <div className="icon-container">
              <span><FaFileSignature /></span>
              <span>Registros</span>
            </div>
          </Link>
        </li>
        
        <li className={activeLink === '/campaigns' || activeLink === '/new-campaign' || isCampaignCollectionPage ? 'active' : ''}>
          <Link to="/campaigns">
            <div className="icon-container">
              <span><FaBriefcaseMedical /></span>
              <span>Informe</span>
            </div>
          </Link>
        </li>
        <li className={activeLink === '/consultas' || activeLink === '/new-campaign' || isCampaignCollectionPage ? 'active' : ''}>
          <Link to="/consultas">
            <div className="icon-container">
              <span><HiArchive /></span>
              <span>Consultas</span>
            </div>
          </Link>
        </li>

      </ul>

      <Link className="logout-text" to="/">
        Logout <span><HiOutlineLogout /></span>
      </Link>
    </div>
  );
}

export default Sidebar;
