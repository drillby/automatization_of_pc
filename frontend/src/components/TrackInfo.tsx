import React from "react";
import currentSongType from "../types/currentSong";

function TrackInfo(props: {
	song: currentSongType;
	loading: boolean;
}): JSX.Element {
	return (
		<>
			<div className="mt-8">
				{props.song.artist !== "" ? (
					<h1 className="text-xl font-bold">
						Právě hraje "{props.song.name}" od {props.song.artist}
					</h1>
				) : (
					<h1 className="text-xl font-bold">Momentálně nic nehraje</h1>
				)}
				<img
					className="m-auto mt-4"
					src={props.song.cover}
					width={300}
					alt=""
				/>
			</div>
		</>
	);
}

export default TrackInfo;
