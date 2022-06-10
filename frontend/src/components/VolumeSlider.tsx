import React from "react";
import API from "../functions/APIClient";
import { useState, useEffect } from "react";

function VolumeSlider(props: { api: API; volume: string }) {
	const [volume, setVolume] = useState(props.volume);

	useEffect(() => {
		const getVolume = () => {
			if (parseInt(volume) > 100) {
				setVolume("100");
			}

			if (parseInt(volume) < 0) {
				setVolume("0");
			}

			console.log("Volume: " + volume);
		};
		getVolume();
	}, [volume]);

	return (
		<>
			<table className="m-auto w-full sm:w-1/4">
				<tbody>
					<tr>
						<td>
							<button
								className="outline rounded-sm w-6 h-6 bg-slate-300 hover:bg-slate-400 mr-2 duration-500"
								onClick={() => {
									setVolume((parseInt(volume) - 10).toString());
									props.api.setVolume(volume);
								}}
							>
								-
							</button>
						</td>
						<td>0</td>
						<td>
							<input
								type="range"
								name=""
								id="volume_slider"
								min="0"
								max="100"
								value={volume}
								onChange={(e) => {
									setVolume(e.target.value.toString());
								}}
								onMouseUp={() => {
									props.api.setVolume(volume);
								}}
								onTouchEnd={() => {
									props.api.setVolume(volume);
								}}
							/>
						</td>
						<td>100</td>
						<td>
							<button
								className="outline rounded-sm w-6 h-6 bg-slate-300 hover:bg-slate-400 ml-2 duration-500"
								onClick={() => {
									setVolume((parseInt(volume) + 10).toString());
									props.api.setVolume(volume);
								}}
							>
								+
							</button>
						</td>
					</tr>
				</tbody>
			</table>
		</>
	);
}

export default VolumeSlider;
