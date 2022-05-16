import React from 'react';
import {Menu,} from 'antd';
import logo from './logo.svg';
import './sidebar.scss';


export default function Sidebar() {
    const items = [
        { label: 'Options', key: 'Options' }, // remember to pass the key prop
        { label: 'Saved Clips', key: 'Saved Clips' }, // which is required
        { label: 'About', key: 'About' },
    ];

    return (
        <div className="Sidebar">
            <Menu items={items} />
        </div>
      );

}