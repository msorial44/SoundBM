import React, {useState} from 'react';
import {Menu,} from 'antd';
import logo from './logo.svg';
import 'antd/dist/antd.css';
import './App.scss';

import Sidebar from './Components/Sidebar/sidebar';
import Options from './Components/Options/options';
import Saved from './Components/Saved Clips/saved';
import About from './Components/About/about';



function App() {
  const [selectedKey, setSelectedKey] = useState('Options');

  function changeFunction({ key }: { key: string }) {
    if (key === 'Options') {
      setSelectedKey('Options');
    } else if (key === 'Saved Clips') {
      setSelectedKey('Saved Clips');
    } else if (key === 'About') {
      setSelectedKey('About');
    }
    }

  return (
    <div className="App">
      <Sidebar changeFunc={changeFunction}/>
      <div className={`options ${selectedKey === 'Options' ? 'options-toggled' : ''}`}>
        <Options/>
      </div>
      <div className={`saved ${selectedKey === 'Saved Clips' ? 'saved-toggled' : ''}`}>
        <Saved/>
      </div>
      <div className={`about ${selectedKey === 'About' ? 'about-toggled' : ''}`}>
        <About/>
      </div>
    </div>
  );
}

export default App;
