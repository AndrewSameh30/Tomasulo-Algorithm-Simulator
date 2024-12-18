import React, { useState }  from 'react'
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import PhotoCamera from '@mui/icons-material/PhotoCamera';

export default function Program(props) {


  return (
    <div className='configs' >
        <div style={{marginBottom:'20px'}}>Upload Your Program</div>
        <div className='config__text' style={{height:'100%',}}>


          <div className="file-upload">
            <input id="input-file" type="file" onChange={props.handleFileSelect}/>
          </div>
            <div style={{
                position:'absolute',
                bottom:'30px',
                width:'100%',
                height:'8%',
                left:'0',
                display:'flex', justifyContent:'center'}}>
                <Button onClick={props.sendConfigs} sx={{width:'50%'}} variant="contained">Upload Your Program</Button>
            </div>
        </div>

    
    </div>
  )
}
