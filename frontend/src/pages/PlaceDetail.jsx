import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import api from "../api";
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



  if (!place) return <div>Place not found</div>;
  return (
    <div>
      <h1>{place.name}</h1>
      <p>id do lugar {id}</p>
      {posts.map((post) => (<p> post do lugar: {post.description}</p>))}
    </div>
  )
}

export default PlantDetail
