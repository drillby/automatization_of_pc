import React from "react";
import API from "../functions/APIClient";
import { useState, useEffect } from "react";

function PlayActive(props: {
	api: API;
	state: React.Dispatch<React.SetStateAction<boolean>>;
}) {
	const [playableDevices, setPlayableDevices] = useState<string[]>([]);

	useEffect(() => {
		const getPlayableDevices = () => {
			props.api.fetchPlayableDevices().then((data) => {
				setPlayableDevices(data.devices);
			});
		};
		getPlayableDevices();
	}, [props.api]);

	const onSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
		const form = event.target as HTMLFormElement;
		const formData = new FormData(form);
		const deviceName = formData.get("device") as string;
		const playType = formData.get("type_of_play") as string;
		const name = formData.get("name") as string;
		event.preventDefault();
		const call = props.api.startPlayback({ deviceName, playType, name });
		if (await call) {
			props.state(false);
		}
	};

	return (
		<div>
			<form action="" method="POST" onSubmit={onSubmit}>
				<div className="flex flex-row">
					<div className="w-1/2">
						<label
							className="block text-gray-700 text-sm font-bold mb-2"
							htmlFor="device"
						>
							Zařízení
						</label>
						<select name="device" id="device">
							<option value="">Vyberete zařízení</option>
							{playableDevices.map((device) => (
								<option key={device} value={device}>
									{device}
								</option>
							))}
						</select>
					</div>
					<div className="w-1/2">
						<label
							className="block text-gray-700 text-sm font-bold mb-2"
							htmlFor="type_of_play"
						>
							Typ
						</label>
						<select name="type_of_play" id="type_of_play">
							<option value="">Vyberte typ</option>
							<option value="song">Skladba</option>
							<option value="album">Album</option>
							<option value="playlist">Playlist</option>
							<option value="queue">Přidat do fronty</option>
						</select>
					</div>
				</div>
				<div className="mt-4">
					<div className="w-full">
						<label
							className="block text-gray-700 text-sm font-bold mb-2"
							htmlFor="name"
						>
							Název
						</label>
						<input
							className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
							type="text"
							placeholder="Název"
							id="name"
							name="name"
						/>
					</div>
					<div className="w-full">
						<input
							type="submit"
							name="submit"
							id="submit"
							value="Zpracovat"
							className="outline mt-4 w-8/12 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mb-4"
						/>
					</div>
				</div>
			</form>
		</div>
	);
}

export default PlayActive;
