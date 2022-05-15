class API {
	#url = "http://192.168.132.102";
	#port = "23450";
	#fullUrl = this.#url + ":" + this.#port;

	fetchCurrentSong = async () => {
		const data = await fetch(this.#fullUrl + "/spotify/current_song", {
			method: "GET",
		});
		const json = await data.json();

		return json;
	};

	fetchActiveDevice = async () => {
		const data = await fetch(this.#fullUrl + "/spotify/active_device", {
			method: "GET",
		});
		const json = await data.json();

		return json;
	};

	fetchChangingInfo = async () => {
		const data = await fetch(this.#fullUrl + "/spotify/current_info", {
			method: "GET",
		});
		const json = await data.json();

		return json;
	};
}

export default API;
