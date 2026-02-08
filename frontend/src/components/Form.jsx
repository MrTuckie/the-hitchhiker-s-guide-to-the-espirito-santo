import { useState } from "react";
import api from "../api"
function AddPostForm({ id }) {
  /* Sobre formulários em react: você tem que fazer as
  * chamadas de api no formulário. E tem que chamar uma função
  * assíncrona em form action para chamar essa api
  */

  const [description, setDescription] = useState('');
  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('description', description)
    // lidando com o post na api
    try {
      const response = await api.post(`api/v1/places/${id}/add_post/`,
        formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
      });
      console.log('aoba:', response.data)

    } catch (error) {
      console.error('deu ruim:', error.message)
    }


  }
  return (
    // e = event .
    // ele contém várias informações importantes, como: target, target.value
    // 
    <form onSubmit={handleSubmit} >
      <input value={description}
        onChange={(e) => setDescription((e.target.value))}
        placeholder="description" />
      <button type="submit">Criar post</button>
    </form>
  )
}

export default AddPostForm
