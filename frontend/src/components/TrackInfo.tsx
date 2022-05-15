import React from "react";
import currentSongType from "../types/currentSong";
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
			)}
		</>
	);
}

export default TrackInfo;
