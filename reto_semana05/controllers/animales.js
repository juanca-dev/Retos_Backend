const animales = []

export const añadirAnimal = (req,res) => {
  animales.push(req.body)
  return res.json({
    content: animales[animales.length-1]
  })
}

export const listarAnimales = (req,res) =>{
  return res.json({
    content: animales
  })
}

export const listarAnimalPorId = (req,res) => {
  const id = req.params.id - 1
  if(animales[id]){
    return res.json({
      content: animales[id]
    })
  }
  return res.status(404).json({
    content: `El animal ${id} no existe`
  })
}

export const actualizarAnimal = (req,res) => {
  const id = req.params.id - 1
  if(animales[id]){
    animales[id] = req.body
    return res.json({
      content: animales[id]
    })
  }
  return res.status(404).json({
    content: `El animal ${id} no existe`
  })
}

export const eliminarAnimal = (req,res) => {
  const id = req.params.id - 1
  if(animales[id]){
    const animal_eliminado = animales.splice(id,1)
    return res.json({
      content: animal_eliminado
    })
  }
  return res.status(404).json({
    content: `El animal ${id} no existe`
  })
}