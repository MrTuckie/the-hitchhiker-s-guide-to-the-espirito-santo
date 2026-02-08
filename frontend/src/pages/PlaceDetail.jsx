import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import api from "../api";
import AddPostForm from "../components/Form";
function PlantDetail() {
  const { id } = useParams()
  const [place, setPlace] = useState(null);
  const [posts, setPosts] = useState(null);

  useEffect(() => { getPlace(); }, [id]);
  useEffect(() => { getPosts(); }, [id]);
  const getPlace = () => {
    api.get(`/api/v1/places/${id}`).then((res) => res.data).then((data) => { setPlace(data); }).catch((err) => alert(err))
  }
  // TODO: evidentemente, eu preciso enviar o id do lugar
  // para poder pegar os posts dele, e não um id aleatório
  const getPosts = () => {
    api.get(`/api/v1/posts/?place=${id}`)
      .then((res) => res.data)
      .then((data) => { setPosts(data); console.log(data) })
      .catch((err) => alert(err))
  }
  // Endereço padrão
  let address = 'Onde os fracos não tem vez'

  if (!place) return <div>Place not found</div>;
  if (place.address) {
    address = `${place.address.street_name} - ${place.address.street_number}`
  }
  let default_post = 'Não tem posts aqui ainda, amigão. Seja o primeiro.'
  if (posts.length) {
    console.log('com posts')
    default_post = posts.map((post) => (<p> post do lugar: {post.description}</p>))
  }
  return (
    <div>
      <h1>{place.name}</h1>
      <p><b>Endereço do lugar: {address}</b></p>
      <p>id do lugar {id}</p>
      {default_post}
      <AddPostForm id={id}></AddPostForm>
    </div >

  )
}

export default PlantDetail
