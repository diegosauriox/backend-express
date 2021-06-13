const { Router } = require('express');
const router = Router();

const {createData}
= require('../controllers/datos.controller');

router.route('/')
    .get(createData);

module.exports = router;