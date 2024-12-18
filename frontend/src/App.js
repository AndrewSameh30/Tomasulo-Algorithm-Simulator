import * as React from 'react';
import Alert from '@mui/material/Alert';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

import Button from '@mui/material/Button';

import AluTable from './tables/aluTable';
import LoadTable from './tables/loadTable';
import StoreTable from './tables/storeTable';
import StatusTable from './tables/statusTable';
import MemoryTable from './tables/memory';
import RegisterTable from './tables/registersTable';

import Snackbar from '@mui/material/Snackbar';
import Configs from './configs';

import KeyboardDoubleArrowLeftIcon from '@mui/icons-material/KeyboardDoubleArrowLeft';
import KeyboardDoubleArrowRightIcon from '@mui/icons-material/KeyboardDoubleArrowRight';


import axios from 'axios';



function App() {
  const [value, setValue] = React.useState(0);
  const [configs, setConfigs] =  React.useState({});
  const [file, setFile] = React.useState("");
  const [succ, setSucc] = React.useState(-1);
  const [results, setResults] = React.useState(false);
  const [data, setData] = React.useState([]);
  const [cycle, setCycle] = React.useState(1);


  // -1 -> not ready
  // 0 -> failed
  // 1 -> success

  const handleFileSelect = (e)=>{
    setFile(e.target.files[0]);
  }
  const handleChange = (e)=>{
    if(e.target.value  >= 0){
      var curr = configs;
      curr[e.target.id]  = e.target.value;
      setConfigs(curr);
    }else{
      setSucc(52);
    }

  }



  const showFile = async (file) => {

    const reader = new FileReader()
    reader.onload = function (event) {
      console.log(event.target.result);
   }
    reader.readAsText(file)
  }

 
  const sendForm = async ()=>{
    setSucc(-1);


    const formData = new FormData();
    Object.keys(configs).forEach((key)=>{
          formData.append(key, configs[key])

    })
    formData.append('file', file);

    for (var [key, value] of formData.entries()) { 
      console.log(key, value);
     }
    
     try{
      const response = await axios({
        method: "POST",
        url: `http://127.0.0.1:5000/configs`,
        data: formData,
        headers: {
            "Access-Control-Allow-Origin": "*",
            'Content-Type': 'multipart/form-data',
  
        },
        transformRequest: (data, error) => {
            return formData;
        }
    });
    if(response.data.response !== 'error'){
      setResults(true);
      setData(response.data.response);
      setSucc(1);
    }

    console.log(response)
     }catch(e){
      setSucc(0);
      setResults(false);

     }    


  }

  const getTables = ()=>{
    return (
      <div className="tables">

      <div style={{display:'flex', flexDirection:'column', gridColumn:'1/-1'}}>
        <div style={{fontSize:'30px', fontWeight:'bolder'}}>Status Q</div>
        <StatusTable data={data} cycle={cycle-1} station="statusContent"/>
      </div>
        <div style={{display:'flex', flexDirection:'column',}}>
          <div style={{fontSize:'30px', fontWeight:'bolder'}}>Addition Reservation Station</div>
          <AluTable data={data} cycle={cycle-1} station="addStation"/>
        </div>
        

        <div style={{display:'flex', flexDirection:'column',}}>
          <div style={{fontSize:'30px', fontWeight:'bolder'}}>Store Reservation Station</div>
          <StoreTable data={data} cycle={cycle-1} station="storeStation"/>
        </div>

        <div style={{display:'flex', flexDirection:'column',}}>
          <div style={{fontSize:'30px', fontWeight:'bolder'}}>Multiplication Reservation Station</div>
          <AluTable data={data} cycle={cycle-1} station="mulStation"/>
        </div>

        <div style={{display:'flex', flexDirection:'column',}}>
          <div style={{fontSize:'30px', fontWeight:'bolder'}}>Load Reservation Station</div>
          <LoadTable data={data} cycle={cycle-1} station="loadStation"/>
        </div>



        <div style={{display:'flex', flexDirection:'column',}}>
          <div style={{fontSize:'30px', fontWeight:'bolder'}}>Memory</div>
          <MemoryTable data={data} cycle={cycle-1} station="memory"/>
        </div>

        <div style={{display:'flex', flexDirection:'column',}}>
          <div style={{fontSize:'30px', fontWeight:'bolder'}}>Registers</div>
          <RegisterTable data={data} cycle={cycle-1} station="regs"/>
        </div>
        

        


      </div>
    )
  }

  const getContent = ()=>{
    if(value === 0) return <Configs handleFileSelect={handleFileSelect} sendConfigs={sendForm} handleChange={handleChange}/>

  }
  return (
    <div className="app">
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              <span style={{color:'var(--primary-color)', fontWeight:'bolder'}}>Tomasulo</span> <span style={{color:'black', fontWeight:'lighter'}}>Simulator</span>
            </Typography>
          </Toolbar>
        </AppBar>
      </Box>
      <div className="flag">
      <div id="black"></div>
      <div id="red"></div>
      <div id="yellow"></div>
    </div>
    <div className='content'>
      {results&&<div className="controller">

        <h3>Current {cycle} Out of { data.length}</h3>
        <div style={{display:'flex',alignItems:'center'}}>
          <KeyboardDoubleArrowLeftIcon 
          onClick={()=>{setCycle(1)}}
          className="icon"/>
          <Button variant="outlined" onClick={()=>{if(cycle-1 >= 1)setCycle(cycle -1)}} >Prev</Button>
          <Button variant="contained" onClick={()=>{if(cycle+1 <= data.length)setCycle(cycle +1)}}>Next</Button>
          <KeyboardDoubleArrowRightIcon
          onClick={()=>{setCycle(data.length-1)}}
          className="icon"/>
        </div>


      </div>}
        {!results&&succ!==1&&getContent()}
        {results&&getTables()}
    </div>
    <Snackbar open={succ!== -1} autoHideDuration={6000} onClose={()=>{setSucc(-1)}}>
      <Alert variant="filled" severity={succ === 0 || succ === 52? 'error':'success'}>{succ === 1? 'Simulated your code successfully. Check your files':(succ === 52)? 'No negative values':'Error occurred'}</Alert>
    </Snackbar>





    </div>
  );
}

export default App;
