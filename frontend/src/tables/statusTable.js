import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(station) {

    var instruction = station[0];
    var fetch = station[1];
    var s_exec = station[2];
    var e_exec = station[3];
    var wb = station[4];


    return [ instruction, fetch, s_exec, e_exec, wb ];
  }
  


export default function StatusTable(props) {
    const [rows, setRows] = React.useState([]);
    React.useEffect(()=>{


        var res = []
        props.data[props.cycle][props.station]&&props.data[props.cycle][props.station].forEach((station)=>{
            res.push(createData(station))
        })
        setRows(res)
 
    },[props.cycle])
  return (

    <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
            <TableRow>
            <TableCell align="center">Instruction</TableCell>
            <TableCell align="center">Fetch</TableCell>
            <TableCell align="center">Started Exec.</TableCell>
            <TableCell align="center">Finished Exec.</TableCell>
            <TableCell align="center">Writeback</TableCell>
            </TableRow>
        </TableHead>
        <TableBody>
            {rows.map((row) => (
            <TableRow
                key={row.name}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
                <TableCell align="center">{row[0]}</TableCell>
                <TableCell align="center">{row[1]}</TableCell>
                <TableCell align="center">{row[2]}</TableCell>
                <TableCell align="center">{row[3]}</TableCell>
                <TableCell align="center">{row[4]}</TableCell>

            </TableRow>
            ))}
        </TableBody>
        </Table>
    </TableContainer>
  )
}
