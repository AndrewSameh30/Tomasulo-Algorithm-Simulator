import React, { useState }  from 'react'
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import axios from 'axios';

export default function Configs(props) {

// const [configs, setConfigs] = useState({});
//   const handleChange = (e)=>{
//     var curr = configs;
//     curr[e.target.id]  = e.target.value;
//     setConfigs(curr);
//     console.log(curr);
//   }

  // const sendConfigs = async ()=>{

  //   const formData = new FormData();

  //   Object.keys(configs).map((key, index) => ( 
  //     formData.append(key,configs[key])
  //   ))




  //   const res = await axios.post("http://127.0.0.1:5000/configs", formData);
  //   console.log(res);
  // }
  return (
    <div className='configs'>
        <div style={{marginBottom:'20px', fontWeight:'bolder'}}>Configurations</div>
        <div className='config__text'>

            <TextField 
            InputProps={{
              inputProps: { min: 0 }
            }}
            type="number" onChange={props.handleChange} className='config__text__input' id="mul" label="MUL Latency" variant="outlined" />
            <TextField
            InputProps={{
              inputProps: { min: 0 }
            }}
            type="number" onChange={props.handleChange} className='config__text__input' id="div" label="DIV Latency" variant="outlined" />
            <TextField
            InputProps={{
              inputProps: { min: 0 }
            }}
            type="number" onChange={props.handleChange} className='config__text__input' id="add" label="ADD Latency" variant="outlined" />
            <TextField
            InputProps={{
              inputProps: { min: 0 }
            }}
            type="number" onChange={props.handleChange} className='config__text__input' id="sub" label="SUB Latency" variant="outlined" />

            <TextField
            InputProps={{
              inputProps: { min: 0 }
            }}
            type="number" onChange={props.handleChange} className='config__text__input' id="load" label="LOAD Latency" variant="outlined" />
            <TextField
            InputProps={{
              inputProps: { min: 0 }
            }}
            type="number" onChange={props.handleChange} className='config__text__input' id="store" label="STORE Latency" variant="outlined" />
            <div className='config__text' style={{height:'100%',}}>


            <div className="file-upload" style={{paddingBottom:'20px',paddingTop:'20px',display:'flex', justifyContent:'flex-start'}}>
                <input id="input-file" type="file" onChange={props.handleFileSelect}/>
              </div>

            </div>
    
            <div style={{

                bottom:'30px',
                width:'100%',
                height:'8%',

                display:'flex', justifyContent:'center'}}>

                    <Button style={{background:"var(--primary-color)"}} onClick={props.sendConfigs} sx={{width:'50%'}} variant="contained">Upload Your Program</Button>

            </div>

        
        
        </div>

    
    </div>
  )
}
