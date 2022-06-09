import playbackInfo from "../types/playbackInfo";

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

	fetchPlayableDevices = async () => {
		const data = await fetch(this.#fullUrl + "/spotify/playable_devices", {
			method: "GET",
		});
		const json = await data.json();

		return json;
	};

	startPlayback = async (content: playbackInfo) => {
		const res = await fetch(this.#fullUrl + "/spotify/start_playback", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				device_name: content.deviceName,
				play_type: content.playType,
				name: content.name,
			}),
		});
		const json = await res.json();

		return json;
	};

	setVolume = async (volume: string) => {
		const res = await fetch(this.#fullUrl + "/spotify/set_volume", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				volume: volume,
			}),
		});
		const json = await res.json();

		return json;
	}

	addSongsToQueue = async (songs: string) => {
		const res = await fetch(this.#fullUrl + "/spotify/add_songs_to_queue", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				songs: songs,
			}),
		});
		const json = await res.json();

		return json;
	}
}

export default API;
