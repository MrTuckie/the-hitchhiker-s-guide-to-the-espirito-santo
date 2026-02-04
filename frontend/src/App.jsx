import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"
import Place from "./pages/Place"
import PlaceDetail from "./pages/PlaceDetail"
import Post from "./pages/Post"
import Activity from "./pages/Activity"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}
// <Route path="/" element={<ProtectedRoute><Home /></ProtectedRoute>} />
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/places" element={<Place />}></Route>
        <Route path="/places/:id" element={<PlaceDetail />}></Route>
        <Route path="/activities" element={<Activity />}></Route>
        <Route path="/posts" element={<Post />}></Route>
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="*" element={<NotFound />}> </Route>

      </Routes>

    </BrowserRouter >
  )
}

export default App



