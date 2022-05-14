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
					className="animate-spin m-auto"
					width={200}
				/>
			) : (
				<div>
					<h1>{props.song.name}</h1>
					<img className="m-auto" src={props.song.cover} width={300} alt="" />
					<h1>{props.song.artist}</h1>
				</div>
			)}
		</>
	);
}

export default TrackInfo;
