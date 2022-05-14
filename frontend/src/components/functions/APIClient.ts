class API {
	fetchCurrentSong = async () => {
		const data = await fetch(
			"http://192.168.132.102:23450/spotify/current_song",
			{
				method: "GET",
			}
		);
		const json = await data.json();

		return json;
	};

	fetchActiveDevice = async () => {
		const data = await fetch(
			"http://192.168.132.102:23450/spotify/active_device",
			{
				method: "GET",
			}
		);
		const json = await data.json();

		return json;
	};

	fetchChangingInfo = async () => {
		const data = await fetch(
			"http://192.168.132.102:23450/spotify/current_info",
			{
				method: "GET",
			}
		);
		const json = await data.json();

		return json;
	};
}

export default API;
