import "../index.css";
import TrackInfo from "../components/SpotifyApp/InformationComponents/TrackInfo";
import { useEffect, useState, useMemo } from "react";
import API from "../functions/SpotifyApp/APIClient";
import changingInfoType from "../types/SpotifyTypes/changingInfo";
import changeHeadInfo from "../functions/common/changeHead";
import ActiveDevice from "../components/SpotifyApp/InformationComponents/ActiveDevice";
import loadingIcon from "../svgs/find-magnifier-magnifying-glass-svgrepo-com.svg";
import Play from "../components/SpotifyApp/PlaybackComponents/Play";
import VolumeSlider from "../components/SpotifyApp/VolumeSliderComponents/VolumeSlider";
import QueueAdder from "../components/SpotifyApp/QueueAdderComponents/QueueAdder";

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
			changeHeadInfo(
				changingInfo[0].current_track.name,
				changingInfo[0].current_track.cover
			);
			getChangingSong();
		}, 5000);
		return () => clearInterval(id);
	}, [api, changingInfo]);

	return (
		<>
			{loading ? (
				<img
					className="sm:animation-loading-spotify m-auto mt-40 animate-pulse"
					width={200}
					src={loadingIcon}
					alt=""
				/>
			) : (
				<div className="w-3/4 m-auto text-center xl:w-1/4 mb-12">
					<TrackInfo song={changingInfo[0].current_track} loading={loading} />
					<ActiveDevice device={changingInfo[0].active_device} />
					<VolumeSlider
						api={api}
						volume={changingInfo[0].active_device.volume}
					/>
					<Play api={api} />
					<QueueAdder api={api} />
				</div>
			)}
		</>
	);
}

export default App;
