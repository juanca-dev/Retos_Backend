const express = require('express');
const router = express.Router();

const mysqlConnection  = require('../database');

// GET todos los empleados
router.get('/', (req, res) => {
  mysqlConnection.query('SELECT * FROM empleado', (err, rows, fields) => {
    if(!err) {
      res.json(rows);
    } else {
      console.log(err);
    }
  });  
});

// GET un empleado
router.get('/:id', (req, res) => {
  const { id } = req.params; 
  mysqlConnection.query('SELECT * FROM empleado WHERE id = ?', [id], (err, rows, fields) => {
    if (!err) {
      res.json(rows[0]);
    } else {
      console.log(err);
    }
  });
});

// DELETE un empleado
router.delete('/:id', (req, res) => {
  const { id } = req.params;
  mysqlConnection.query('DELETE FROM empleado WHERE id = ?', [id], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Empleado Borrado'});
    } else {
      console.log(err);
    }
  });
});

// INSERT un Empleado
router.post('/', (req, res) => {
  const {id, name, salario} = req.body;
  console.log(id, name, salario);
  const query = `CALL empleadoAddOrEdit(?, ?, ?);
  `;
  mysqlConnection.query(query, [id, name, salario], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Guardar Empleado'});
    } else {
      console.log(err);
    }
  });

});

router.put('/:id', (req, res) => {
  const { name, salario } = req.body;
  const { id } = req.params;
  const query = `CALL empleadoAddOrEdit(?, ?, ?);
  `;
  mysqlConnection.query(query, [id, name, salario], (err, rows, fields) => {
    if(!err) {
      res.json({status: 'Empleado Actualizado'});
    } else {
      console.log(err);
    }
  });
});

module.exports = router;