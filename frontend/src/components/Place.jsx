import { Link } from "react-router-dom";
function PlaceComponent({ place }) {
  return (
    <div className="place-container">
      {/*<p className="place-name"><a href={`/places/${place.id}/`}>{place.name}</a></p>*/}
      <Link to={`/places/${place.id}`}>
        <p className="place-name">{place.name}</p>
      </Link>
    </div>
  );
}

export default PlaceComponent
