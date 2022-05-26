import playbackInfo from "../types/playbackInfo";

class API {
	#url = "http://192.168.132.102";
	#port = "23450";
	#fullUrl = this.#url + ":" + this.#port;

	#getCooke(name: string): string {
		const cookie = document.cookie
			.split(";")
			.find((c) => c.trim().startsWith(name));
		if (!cookie) {
			return "";
		}
		return cookie.split("=")[1];
	}

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
		fetch(this.#fullUrl + "/spotify/start_playback", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				// "X-CSRFToken": this.#getCooke("csrftoken"),
			},
			body: JSON.stringify({
				device_name: content.deviceName,
				play_type: content.playType,
				name: content.name,
			}),
		});
	};
}

export default API;
