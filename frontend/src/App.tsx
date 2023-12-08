import "./App.css";
import Sidebar from "./components/Sidebar/Sidebar";
import { BrowserRouter, Route, Routes} from "react-router-dom";
import DashboardPage from "./components/Dashboard/DashboardPage";
import CampanasPage from "./components/Campaigns/CampaignsPage";
import NewCampaingPage from "./components/NewCampaing/NewCampaingPage";
import CampaignCollectionPage from "./components/CampaignCollection/CampaignCollectionPage";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route
            path="*"
            element={<>NOT FOUND</>}
          />

          <Route
            path="/"
            element={
              <div>
                <div>
                  <Sidebar />
                  <div className="content">
                    <DashboardPage/>
                  </div>
                </div>
              </div>
            }
          />
           <Route
            path="/consultas"
            element={
              <div>
                <div>
                  <Sidebar />
                  <div className="content">
                    <NewCampaingPage/>
                  </div>
                </div>
              </div>
            }
          />

          <Route
            path="/campaigns"
            element={
              <div>
                <div>
                  <Sidebar />
                  <div className="content">
                    <CampanasPage/>
                  </div>
                </div>
              </div>
            }
          />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
