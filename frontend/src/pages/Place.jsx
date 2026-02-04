import { useState, useEffect } from "react"
import api from "../api"
import PlaceComponent from "../components/Place"

function Place() {
  const [places, setPlaces] = useState([]);
  useEffect(() => {
    getPlaces();
  }, []);
  const getPlaces = () => {
    api.get("/api/v1/places/").then((res) => res.data).then((data) => { setPlaces(data); console.log(data); }).catch((err) => alert(err));
  };
  return (

    <div>
      <h2>Places</h2>
      {places.map((place) => (
        <PlaceComponent place={place} key={place.id} />
      ))}
    </div>
  )
}

export default Place
