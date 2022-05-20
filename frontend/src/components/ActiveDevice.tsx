import React from "react";
import activeDeviceType from "../types/activeDevice";

function ActiveDevice(props: { device: activeDeviceType }) {
	return (
		<div className="mt-4">
			<h1 className="text-xl font-bold">
				Hudba hraje na zařízení "{props.device.name}"
			</h1>
			<h2 className="text-xl">Hlasitost: {props.device.volume}</h2>
		</div>
	);
}

export default ActiveDevice;
