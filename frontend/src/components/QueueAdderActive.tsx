import React from "react";
import API from "../functions/APIClient";

function QueueAdderActive(props: {
	api: API;
	state: React.Dispatch<React.SetStateAction<boolean>>;
}) {
	const onSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
		const form = event.target as HTMLFormElement;
		const formData = new FormData(form);
		const numberOfSongs = formData.get("num_of_songs") as string;
		event.preventDefault();
		const call = props.api.addSongsToQueue(numberOfSongs);
		if (await call) {
			props.state(false);
		}
	};

	return (
		<form action="" method="POST" onSubmit={onSubmit}>
			<label
				htmlFor="num_of_songs"
				className="block text-gray-700 text-sm font-bold mb-2"
			>
				Počet skladeb
			</label>

			<input
				type="number"
				name="num_of_songs"
				id="num_of_songs"
				min="1"
				max="50"
				step="1"
				defaultValue="1"
				className="shadow appearance-none border rounded w-11/12 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
			/>
			<br />
			<input
				type="submit"
				name="submit"
				id="submit"
				value="Přidat"
				className="outline mt-4 w-8/12 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mb-4"
			/>
		</form>
	);
}

export default QueueAdderActive;
