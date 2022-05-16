import React, { useState } from 'react';
import logo from './logo.svg';
import { Button } from 'antd';
import 'antd/dist/antd.css';
import './options.scss';


export default function Options(props: any) {
    const [canRecord, setCanRecord] = useState(false);
    const [canDelete, setCanDelete] = useState(false);
    const [canSpecial, setCanSpecial] = useState(false);
    const [recordKey, setRecordKey] = useState('N/A');
    const [deleteKey, setDeleteKey] = useState('N/A');
    const [specialKey, setSpecialKey] = useState('N/A');

    window.addEventListener('keydown', (event) => {
        if (canRecord) {
            setRecordKey(event.key);
            setCanRecord(false);
        } else if (canDelete) {
            setDeleteKey(event.key);
            setCanDelete(false);
        } else if (canSpecial) {
            setSpecialKey(event.key);
            setCanSpecial(false);
        }
    });

    function handleRecord() {
        setCanRecord(true);
    }

    function handleDelete() {
        setCanDelete(true);
    }

    function handleSpecial() {
        setCanSpecial(true);
    }



    return (
        <div className="Options">

          <div className='record-options'>
            <div className='record-title'>
              <h2>Record Button</h2>
            </div>
            <div className='record-body'> 
              <Button type="default" onClick={() => {handleRecord()}}>Click to Record Keybind</Button>
              <div className='curr-record-key'> {recordKey} </div>
            </div>
          </div>

          <div className='delete-options'>
            <div className='delete-title'>
              <h2>Delete Button</h2>
            </div>
            <div className='delete-body'> 
              <Button type="default" onClick={() => {handleDelete()}}>Click to Record Keybind</Button>
              <div className='curr-delete-key'> {deleteKey} </div>
            </div>
          </div>

          <div className='special-options'>
            <div className='special-title'>
              <h2>Special Button</h2>
            </div>
            <div className='special-body'> 
              <Button type="default" onClick={() => {handleSpecial()}}>Click to Record Keybind</Button>
              <div className='curr-special-key'> {specialKey} </div>
            </div>
          </div>

        </div>
      );

}