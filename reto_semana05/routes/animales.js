import {Router} from 'express'
import {añadirAnimal,listarAnimales,listarAnimalPorId,actualizarAnimal,eliminarAnimal} from '../controllers/animales'

export const animales_router = Router()

animales_router.route('/animales')
  .post(añadirAnimal)
  .get(listarAnimales)

animales_router.route('/animales/:id')
  .get(listarAnimalPorId)
  .put(actualizarAnimal)
  .delete(eliminarAnimal)