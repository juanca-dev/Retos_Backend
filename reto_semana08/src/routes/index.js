const { Router } = require('express');
//const { database } = require('firebase-admin');
const router = Router();
const admin = require('firebase-admin');


var serviceAccount = require("../../reto24-b766c-firebase-adminsdk-npja6-1c35834bbc.json");


admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: 'https://reto24-b766c-default-rtdb.firebaseio.com/'
});

const db = admin.database();

router.get('/', (req, res) => {
  db.ref('contacts').once('value',(snapshot) => {
    const data = snapshot.val();
    res.render('index',{contacts: data});
  });
});


router.post('/nuevo-contacto', (req, res) => {
  const nuevocontacto = {
    nombre:req.body.nombre,
    npellido:req.body.apellido,
    email:req.body.email,
    telefono:req.body.telefono
    };
  db.ref('contacts').push(nuevocontacto);
  res.send('recivido');
});
module.exports = router;