import activeDeviceType from "./activeDevice";
import currentSongType from "./currentSong";

type changingInfoType = {
	active_device: activeDeviceType;
	current_track: currentSongType;
};

export default changingInfoType;
