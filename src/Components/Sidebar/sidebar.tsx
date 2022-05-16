import React from 'react';
import {Menu,} from 'antd';
import logo from './logo.svg';
import 'antd/dist/antd.css';
import './sidebar.scss';


export default function Sidebar(props: any) {
    const items = [
        { label: 'Options', key: 'Options' }, // remember to pass the key prop
        { label: 'Saved Clips', key: 'Saved Clips' }, // which is required
        { label: 'About', key: 'About' },
    ];

    return (
        <div className="Sidebar">
            <Menu defaultSelectedKeys={['Options']} mode="inline" style={{height: "100vh"}} items={items} theme='dark' onSelect={props.changeFunc}/>
        </div>
      );

}