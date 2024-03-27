import './App.css';
import React from 'react';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Title from './component/Title';
import Content from './component/layoutSidenav_content';
import Sidenav from './component/layoutSidenav_nav';
import Row from './component/content_row';
import DataTable from './component/Datatable';
import data from './component/data';
// import './css/DataTable.css'

import SuccessIPPage from './pages/SuccessIPPage';


function App() {
  return (
    <Router>
      <div className='App'>
        <Title />
        <div id='layoutSidenav'>
            <Sidenav />
            <div id='layoutSidenav_content'>
                <main>
                    <Routes>
                        <Route path="/" element={
                          <>
                            <Content />
                            <Row />
                            <DataTable data={data} />
                          </>
                        } />
                    </Routes>
                </main>  
            </div>
        </div>
      </div>
    </Router>
  );
}

export default App;