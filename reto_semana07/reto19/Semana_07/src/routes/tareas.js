import { Router } from 'express'
import * as tareaController from  '../controllers/tareas'
import { verificarUsuario } from '../middlewares/verificarUsuario'

const router = Router ()
router.get('/tareas/:userId',verificarUsuario,tareaController.obterTareas)
router.post('/tareas/:userId',verificarUsuario,tareaController.craerTarea)

export default router