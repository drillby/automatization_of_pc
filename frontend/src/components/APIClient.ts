class API {
	fetchCurrentSong = async () => {
		const data = await fetch(
			"http://192.168.132.102:23450/spotify/current_song",
			{
				method: "GET",
			}
		);
		const json = await data.json();
		console.log(json);

		return json;
	};
}

export default API;
