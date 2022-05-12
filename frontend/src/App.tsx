import "./index.css";
import TrackInfo from "./components/TrackInfo";
import { useEffect, useState, useMemo } from "react";
import API from "./components/APIClient";
import currentSongType from "./components/types/currentSong";

function App(): JSX.Element {
	// wrap API in useMemo to avoid unnecessary re-renders
	const api = useMemo(() => new API(), []);

	const [currentSong, setCurrentSong] = useState<currentSongType[]>([]);
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		setInterval(() => {
			const getCurrentSong = () => {
				api.fetchCurrentSong().then((data) => {
					setLoading(false);
					setCurrentSong(data.results);
					console.log(data.results);
				});
			};
			getCurrentSong();
		}, 5000);
	}, [api]);

	return (
		<>
			<TrackInfo song={currentSong[0]} loading={loading} />
		</>
	);
}

export default App;
