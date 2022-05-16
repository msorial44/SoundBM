import React, { useState, useEffect, useCallback } from 'react';
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

    const [recordButtonContent, setRecordButtonContent] = useState('Click to Record Keybind');
    const [deleteButtonContent, setDeleteButtonContent] = useState('Click to Record Keybind');
    const [specialButtonContent, setSpecialButtonContent] = useState('Click to Record Keybind');
    
    const handleRecordClick = useCallback((event: { key: React.SetStateAction<string>; }) => {
      if (canRecord) {
        setRecordKey(event.key);
        setCanRecord(false);
        setRecordButtonContent('Click to Record Keybind');
      } else if (canDelete) {
        setDeleteKey(event.key);
        setCanDelete(false);
        setDeleteButtonContent('Click to Record Keybind');
      } else if (canSpecial) {
        setSpecialKey(event.key);
        setCanSpecial(false);
        setSpecialButtonContent('Click to Record Keybind');
      }
      setCanRecord(false);
      setCanDelete(false);
      setCanSpecial(false);
    }, [canRecord, canDelete, canSpecial]);

    useEffect(() => {
      window.addEventListener('keydown', handleRecordClick);
      return () => window.removeEventListener('keydown', handleRecordClick);

    }, [handleRecordClick]);

    function handleRecord() {
      console.log('clicked record')
        setCanRecord(true);
        setRecordButtonContent('Recording...');
    }

    function handleDelete() {
        setCanDelete(true);
        setDeleteButtonContent('Recording...');
    }

    function handleSpecial() {
        setCanSpecial(true);
        setSpecialButtonContent('Recording...');
    }



    return (
        <div className="Options">

          <div className='record-options'>
            <div className='record-title'>
              <h2>Record Button</h2>
            </div>
            <div className='record-body'> 
              <Button type="default" onClick={() => {handleRecord()}}>{recordButtonContent}</Button>
              <div className='curr-record-key'> {recordKey} </div>
            </div>
          </div>

          <div className='delete-options'>
            <div className='delete-title'>
              <h2>Delete Button</h2>
            </div>
            <div className='delete-body'> 
              <Button type="default" onClick={() => {handleDelete()}}>{deleteButtonContent}</Button>
              <div className='curr-delete-key'> {deleteKey} </div>
            </div>
          </div>

          <div className='special-options'>
            <div className='special-title'>
              <h2>Special Button</h2>
            </div>
            <div className='special-body'> 
              <Button type="default" onClick={() => {handleSpecial()}}>{specialButtonContent}</Button>
              <div className='curr-special-key'> {specialKey} </div>
            </div>
          </div>

        </div>
      );

}