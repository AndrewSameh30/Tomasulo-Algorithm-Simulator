import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { createTheme, ThemeProvider } from '@mui/material/styles';


const theme = createTheme({
    
  palette: {
    primary: {
      main: 'rgb(176,0,4)',

      },
    secondary: {
      main: 'rgb(252, 113, 13)'
    },
  }
});
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <ThemeProvider theme={theme}>
    <App />
  </ThemeProvider>

    
);

