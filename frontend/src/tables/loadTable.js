import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(station) {
    const {busy, id, address } = station;
    return {busy, id, address };
  }
  


export default function LoadTable(props) {
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
            <TableCell align="center">Address</TableCell>
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
                <TableCell align="center">{row.address}</TableCell>
            </TableRow>
            ))}
        </TableBody>
        </Table>
    </TableContainer>
  )
}
