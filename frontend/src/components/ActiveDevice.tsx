import React from "react";
import activeDeviceType from "../types/activeDevice";

function ActiveDevice(props: { device: activeDeviceType }) {
	return (
		<div>
			<h1>{props.device.name}</h1>
			<h2>Volume: {props.device.volume}</h2>
		</div>
	);
}

export default ActiveDevice;
