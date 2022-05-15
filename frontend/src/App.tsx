import "./index.css";
import TrackInfo from "./components/TrackInfo";
import { useEffect, useState, useMemo } from "react";
import API from "./functions/APIClient";
import changingInfoType from "./types/changingInfo";
import changeHeadInfo from "./functions/changeHead";
import ActiveDevice from "./components/ActiveDevice";
import loadingIcon from "./svgs/loading.svg";

function App(): JSX.Element {
	// wrap API in useMemo to avoid unnecessary re-renders
	const api = useMemo(() => new API(), []);

	const [changingInfo, setChangingInfo] = useState<changingInfoType[]>([
		{
			current_track: {
				name: "",
				artist: "",
				cover:
					"https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/768px-Spotify_logo_without_text.svg.png",
			},
			active_device: {
				name: "None",
				volume: "0",
			},
		},
	]);

	const [loading, setLoading] = useState(true);

	useEffect(() => {
		const id = setInterval(() => {
			const getChangingSong = () => {
				api.fetchChangingInfo().then((data) => {
					setChangingInfo(data.results);
					setLoading(false);
				});
			};
			getChangingSong();
			changeHeadInfo(
				changingInfo[0].current_track.name,
				changingInfo[0].current_track.cover
			);
		}, 5000);
		return () => clearInterval(id);
	}, [api, changingInfo]);

	return (
		<>
			{loading ? (
				<img
					className="animate-spin m-auto mt-40"
					width={500}
					src={loadingIcon}
					alt=""
				/>
			) : (
				<div className="w-4/5 m-auto text-center">
					<TrackInfo song={changingInfo[0].current_track} loading={loading} />
					<ActiveDevice device={changingInfo[0].active_device} />
				</div>
			)}
		</>
	);
}

export default App;
