import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(station) {
    const {busy, id, op, Vj, Qj, Vk, Qk } = station;
    return { busy, id, op, Vj, Qj, Vk, Qk };
  }
  


export default function AluTable(props) {
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
            <TableCell align="center">Busy</TableCell>
            <TableCell align="center">ID</TableCell>
            <TableCell align="center">OP</TableCell>
            <TableCell align="center">Vj</TableCell>
            <TableCell align="center">Qj</TableCell>
            <TableCell align="center">Vk</TableCell>
            <TableCell align="center">Qk</TableCell>
            </TableRow>
        </TableHead>
        <TableBody>
            {rows.map((row) => (
            <TableRow
                key={row.name}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
                <TableCell align="center">{row.busy}</TableCell>
                <TableCell align="center">{row.id}</TableCell>
                <TableCell align="center">{row.op}</TableCell>
                <TableCell align="center">{row.Vj}</TableCell>
                <TableCell align="center">{row.Vk}</TableCell>
                <TableCell align="center">{row.Qj}</TableCell>
                <TableCell align="center">{row.Qk}</TableCell>
            </TableRow>
            ))}
        </TableBody>
        </Table>
    </TableContainer>
  )
}
