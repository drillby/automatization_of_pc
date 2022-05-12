import React from "react";
import currentSongType from "./types/currentSong";
import loadingIcon from "../svgs/loading.svg";

function TrackInfo(props: {
	song: currentSongType;
	loading: boolean;
}): JSX.Element {
	return (
		<>
			{props.loading ? (
				<img
					src={loadingIcon}
					alt=""
					className="animate-spin outline m-auto"
					width={200}
				/>
			) : (
				<div>
					<h1>{props.song.title}</h1>
					<img src={props.song.cover_of_track} alt="" />
				</div>
			)}
		</>
	);
}

export default TrackInfo;
