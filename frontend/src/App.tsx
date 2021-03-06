import React from "react";
import "./index.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Spotify from "./pages/Spotify";
import Tests from "./pages/Tests";
import Infotainment from "./pages/Infotainment";
function App() {
	return (
		<Router>
			<Routes>
				<Route path="/spotify" element={<Spotify />}></Route>
				<Route path="/dev" element={<Tests />}></Route>
				<Route path="/infotainment" element={<Infotainment />}></Route>
			</Routes>
		</Router>
	);
}

export default App;
